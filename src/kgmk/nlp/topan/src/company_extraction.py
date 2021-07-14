'''企業名マスタ(csv)を用意'''
from _base import * 
tbl_company_tws_path=f'{project_root}/data/tbl_company_tws.csv'

def load_company_tws():
    return pd.read_csv(tbl_company_tws_path)

def create_master():
    dic_path = f'{project_root}/data/jcl_dic.csv'
    data = open(dic_path)
    company_name, company_origin = [], []
    for line in data.readlines():
        line = line.split(',')
        company_name.append(line[0])
        company_origin.append(''.join(line[10:-2]))
    print('end extraction')

    company_id = dict()
    name_class = []
    company_code = []
    for name, origin in zip(company_name, company_origin):
        if not origin in company_id:
            company_id[origin] = len(company_id)+1
        company_code.append(company_id[origin])
        name_class.append(int(name==origin))
    company_master = pd.DataFrame({
        'company_id': range(1, len(company_code)+1),
        'company_code': company_code,
        'company_name': company_name,
        'name_class': name_class
    })
    for col in ['created_user_id', 'updated_user_id', 'created_at', 'updated_at', 'deleted_at']:
        company_master[col] = np.nan 
    print(company_master.head())

    company_master.to_csv(f'{project_root}/data/mst_companies.csv', index=False, na_rep='NULL')
    company_id = dict(zip(company_master['company_name'].values, company_master['company_code'].values))
    with open(f'{project_root}/data/company_id.pickle', 'wb') as f:
        pickle.dump(company_id, f)
    return

def extract(df):
    tp = TP(pos=['名詞'], dic_path=None, user_dic=f'{project_root}/data/jcl_slim_mecab.dic', origin=False)
    texts = df['all_text'].map(tp.to_terms).values
    tw_id = df['tw_id'].values
    relations = set()
    start = time.time()
    dba = clsDbAccessor()
    for i in range(len(texts)):
        text = '\',\''.join(texts[i])
        try:
            query = f"SELECT company_code FROM mst_companies WHERE deleted_at IS NULL AND company_name IN (\'{text}\')"
            res = dba.execQuery(query)
            company_codes = res['company_code']
            for company_code in company_codes:
                relations.add((company_code, tw_id[i]))
        except:
            continue
    
    # tw_idに紐づくレコード全削除
    for i in tw_id: 
        try:
            query = f'DELETE FROM `tbl_company_tws` WHERE tw_id={i}'
            dba.execNonQuery(query)
        except:
            continue
    
    for company_code, tw_id in relations:
        try:
            # query = f'SELECT company_tw_id FROM `tbl_company_tws` WHERE company_code={company_code} AND tw_id={tw_id};'
            # count = dba.execQuery(query)
            # if count.size > 0: continue
            query = f'INSERT IGNORE INTO `tbl_company_tws` (company_code, tw_id) VALUES ({company_code}, {tw_id})'
            dba.execNonQuery(query)
            
        except Exception as e:
            print(e)
            continue
    try:
        dba.commit()
        print('コミット')
    except Exception as e:
        raise e 

    dba.close()
    print(time.time() - start)


def update_past_all():
    s = time.time()
    dba = clsDbAccessor()
    df = dba.execQuery("SELECT `tw_id`, `text`, `text_long`, `og_description` FROM `tbl_twitters` WHERE proc_flag=1 AND deleted_at IS NULL;")
    dba.close()
    t = time.time()
    print(t - s)

    s = t
    for i in df.index:
        row = df.loc[i]
        for alter in ['text_long', 'og_description']:
            try:
                if len(row[alter]) > len(row['text']):
                    df.loc[i, 'text'] = row[alter]
            except:
                continue

    df['text'] = df['text'].map(TP.remove_whitespaces)
    t = time.time()
    print(t - s)

    extract(df)

if __name__ == '__main__':
    # create_master()
    update_past_all()