import requests
import json 
import time
# from memory_profiler import profile

'''stop words (全カテゴリ共通)'''
stop_words = ['好評発売中']

try:
    from _base import * 
    import company_extraction
    import classification
    import similarity
    import keyword_extraction
except:
    requests.post(slack_url, data = json.dumps({
        'text': f'<!channel> error: AI(import)'
    }))
    '''slack通知 メンション'''
    exit()


def load_dfs():
    try:
        dba = clsDbAccessor()
        df = dba.execQuery("SELECT `tw_id`, `text`, `text_long`, `og_description`, `similar1`, `proc_flag`, `og_title`, `deleted_at` FROM `tbl_twitters` WHERE deleted_at IS NULL ORDER BY `tw_date` DESC LIMIT 50000;")
        dba.close()
    except:
        logging.critical('failed: SELECT tbl_twitters')
        print('failed: SELECT tbl_twitters')   
    
    # ここでtextを文字数最大に変更
    all_texts = []
    for i in df.index:
        t = ''
        for col in ['text', 'text_long', 'og_description', 'og_title']:
            try:
                t += df.loc[i, col] + ' '
            except:
                continue
        all_texts.append(TP.remove_whitespaces(t))
    df['all_text'] = all_texts

    for i in df.index:
        row = df.loc[i]
        for alter in ['text_long', 'og_description']:
            try:
                if len(row[alter]) > len(row['text']):
                    df.loc[i, 'text'] = row[alter]
            except:
                continue
    df['text'] = df['text'].map(TP.remove_whitespaces)

    drop_df = df[(df.duplicated(subset='text', keep='last')) | (df['og_title'].notna() & df.duplicated(subset='og_title', keep='last')) | df['text'].str.contains('|'.join(stop_words), regex=True)]
    df.drop(drop_df.index, inplace=True)
    print(df)
    drop_df.set_index('tw_id', drop=False, inplace=True)
    drop_df['deleted_at'] = date
    drop_df['proc_flag'] = 9
    drop_df['updated_at'] = date
    print(drop_df[['proc_flag', 'deleted_at', 'updated_at']])
    update_tbl_twitter(drop_df, ['proc_flag', 'deleted_at', 'updated_at'])

    new_df = df[df['proc_flag']==0]
    df = df[df['proc_flag']==1]
    return df, new_df

def update_local_df(df, new_df, local_df):
    new_local_df = pd.concat([df, new_df])[['tw_id', 'text']].merge(local_df, on='tw_id', how='left')
    new_local_df = new_local_df[new_local_df['norm'].isna()]
    if new_local_df.empty:
        return local_df
    tp = TP(dic_path=None)
    new_local_df['wakati_text'] = new_local_df['text'].map(tp.norm_wakati)
    tp = TP(pos=config['similarity']['pos'])
    text_vector = similarity.vectorize(new_local_df['text'].map(tp.norm_wakati))
    new_local_df['text_vector'] = text_vector
    new_local_df['norm'] = np.linalg.norm(text_vector, axis=1)
    new_local_df.drop('text', axis=1, inplace=True)
    local_df = pd.concat([local_df, new_local_df], ignore_index=True)
    local_df.drop_duplicates(subset='tw_id', inplace=True)
    return local_df

def main():
    try:
        '''データ読み込み, 重複テキストの削除、local_dfの更新'''
        try:
            df, new_df = load_dfs()
            if new_df.size == 0:
                print('no latest data')
                return 'no latest data'
            print(df, new_df)
            '''pickle load error'''
            try:
                local_df = load_local_df() # pickle に保存されている。
            except Exception as e:
                requests.post(slack_url, data = json.dumps({
                    'text': f'error: failed to load pickle'
                }))
                logging.critical('failed to load pickle')
                raise e
            local_df = local_df.set_index('tw_id').reset_index()
            local_df = update_local_df(df, new_df, local_df)
            df = df.merge(local_df, how='left', on='tw_id').set_index('tw_id', drop=False)
            new_df = new_df.merge(local_df, how='left', on='tw_id').set_index('tw_id', drop=False)
            local_df = local_df.set_index('tw_id', drop=False)
        except Exception as e:
            raise e

        '''keyword extraction'''
        try:
            keyword_extraction.extract(new_df, local_df)
            new_df['updated_at'] = date
            update_tbl_twitter(new_df, ['word', 'updated_at']) 
            print('success: keyword extraction')
        except Exception as e:
            new_df['proc_flag'] = 90
            update_tbl_twitter(new_df, ['proc_flag'])
            print('failed: keyword extraction')
            logging.critical('failed: keyword extraction')
            raise e 

        '''category classification'''
        try:
            classification.infer(new_df)
            update_tbl_twitter(new_df, ['category', 'gen_category']) 
            # update_tbl_twitter(new_df, ['gen_category'])
            print('success: category classification')          
        except Exception as e:
            new_df['proc_flag'] = 91
            update_tbl_twitter(new_df, ['proc_flag'])
            print('failed: category classification') 
            logging.critical('failed: category classification')
            raise e
            
        '''company extraction'''
        try:
            company_extraction.extract(new_df[['tw_id', 'all_text']])
            company_extraction.extract(df[['tw_id', 'all_text']]) # 過去1ヶ月分は常時更新。
            print('success: company extraction')
        except Exception as e:
            new_df['proc_flag'] = 92
            update_tbl_twitter(new_df, ['proc_flag'])
            print('failed: company extraction')
            logging.critical('failed: company extraction')
            raise e

        '''similar text finding'''
        try:
            all_df = pd.concat([df, new_df]).set_index('tw_id', drop=False)
            tmp = similarity.calculate(df, new_df, local_df, method=1, rm_company=False)
            all_df.loc[tmp.index, 'similar1'] = tmp['similar1']
            all_df['updated_at'] = date
            update_tbl_twitter(all_df, ['similar1', 'updated_at'])
            print('success: similarity')
        except Exception as e:
            new_df['proc_flag']  = 93
            update_tbl_twitter(new_df, ['proc_flag'])
            print('failed: similarity')
            logging.critical('failed: similarity')
            raise e
        
        '''類似まで終わったらnew_dfのproc_flagを1にして更新。local_dfの保存'''
        try:
            new_df['proc_flag'] = 1
            update_tbl_twitter(new_df, ['proc_flag'])
            local_df.set_index('tw_id').reset_index(inplace=True)
            tmp_local_df_path = f'{project_root}/data/local_df_{date}.pickle'
            try:
                with open(tmp_local_df_path, 'wb') as f:
                    pickle.dump(local_df, f)
            except Exception as e:
                requests.post(slack_url, data = json.dumps({
                    'text': f'error: failed to dump pickle'
                }))
                logging.critical('error: failed to dump pickle')
                raise e
            logging.critical('success: dump pickle')
            try:
                os.remove(local_df_path)
                os.rename(tmp_local_df_path, local_df_path)
            except Exception as e:
                requests.post(slack_url, data = json.dumps({
                    'text': f'<!channel> error: failed to rename pickle\nbackupよりlocal_df.pickleを復元してください!'
                }))
                logging.critical('failed: rename pickle')
                raise e
        except Exception as e:
            raise e 
        
    except Exception as e:
        '''slackにエラーの通知'''
        print(e)
        requests.post(slack_url, data = json.dumps({
            'text': f'<!channel> error: AI(main)'
        }))
        exit()

if __name__ == '__main__':
    t = time.time()
    res = main()
    t = time.time() - t
    '''finish通知, 時間'''
    if res:
        message = f'AI finished! {res} 実行時間: {t}秒'
    else:
        message = f'AI finished! 実行時間: {t}秒'
    requests.post(slack_url, data = json.dumps({
        'text': message
    }))