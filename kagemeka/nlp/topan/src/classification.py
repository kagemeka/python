from _base import *

config = config['classification']
tp = TP()
tokenizer_path = f'{project_root}/{config["tokenizer_path"]}'
tokenizer_gen_path = f'{project_root}/{config["tokenizer_gen_path"]}'

def load_category_master():
    try:
        dba = clsDbAccessor()
        category_master = dba.execQuery("SELECT category_id, category_name FROM mst_categories;")
        dba.close()
        return category_master
    except Exception as e:
        print('failed: SELECT mst_categories')
        raise e

def load_keyword_master():
    try:
        dba = clsDbAccessor()
        keyword_master = dba.execQuery("SELECT category_id, keyword FROM mst_keywords;")
        dba.close()
        return keyword_master
    except Exception as e:
        print('failed: SELECT mst_keywords')
        raise e
    

def load_gen_category_master():
    try:
        dba = clsDbAccessor()
        gen_category_master = dba.execQuery("SELECT category_id, category_name FROM mst_gen_categories;")
        dba.close()
        return gen_category_master
    except Exception as e:
        print('failed: SELECT mst_categories')
        raise e
    # return pd.read_csv(f'{project_root}/data/mst_gen_categories.csv')

def load_gen_keyword_master(): # localで学習時に使用
    return pd.read_csv(f'{project_root}/data/mst_gen_keywords.csv')


category_master = load_category_master()
categories = list(category_master['category_name'].values)
gen_category_master = load_gen_category_master()
gen_categories = list(gen_category_master['category_name'].values)


import tensorflow as tf
from tensorflow.keras import Sequential, layers, losses, optimizers, callbacks
def create_model(emb_dim=10):
    model = Sequential([
        layers.Embedding(input_dim=10**6, output_dim=emb_dim),
        layers.Conv1D(256, 3, activation='relu'),
        layers.GlobalMaxPooling1D(),
        layers.Dense(128, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(
        loss=losses.BinaryCrossentropy(),
        optimizer=optimizers.Adam(),
        metrics=['accuracy']
    )
    return model

def regex_and(s):
    return ''.join([f'(?=.*{w})' for w in s.split()])

def create_dataset(texts, keywords):
    # bl = texts.str.contains('|'.join(category_keywords[category]), regex=True)
    bl = texts.str.contains(r'{}'.format('|'.join(map(regex_and, keywords))), regex=True)
    true_datas = texts[bl]
    n = len(true_datas)
    false_datas = texts.drop(true_datas.index).sample(n=n, random_state=10)
    x = pd.concat([true_datas, false_datas]).map(tp.norm_wakati)
    y = np.array([1]*n + [0]*n)
    return x, y

from tensorflow.keras.preprocessing.text import Tokenizer, tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
def pad(x, maxlen):
    return pad_sequences(x, maxlen=maxlen, padding='post', truncating='post')

def train(df):
    # texts = df['text'].drop_duplicates()
    # if not os.path.exists(tokenizer_path):
    #     tokenizer = Tokenizer()
    #     tokenizer.fit_on_texts(texts.map(tp.norm_wakati))
    #     with open(tokenizer_path, 'w', encoding='utf-8') as f:
    #         f.write(json.dumps(tokenizer.to_json(), ensure_ascii=False))
    # with open(tokenizer_path) as f:
    #     tokenizer = tokenizer_from_json(json.load(f))

    # keyword_master = load_keyword_master()
    # id2category = dict(zip(category_master['category_id'], category_master['category_name']))
    # category_keywords = dict()
    # for category_id, df in keyword_master.groupby(['category_id']):
    #     keywords = df['keyword'].values
    #     category_keywords[id2category[category_id]] = list(keywords)
    # categories = list(category_keywords.keys())

    # for category in categories:
    #     x, y = create_dataset(texts, category_keywords[category])
    #     x = pad(tokenizer.texts_to_sequences(x), maxlen=100)
    #     model = create_model(emb_dim=2)
    #     weights_save_path = f'{project_root}/model/classification_model/{category}.ckpt'
    #     model.fit(
    #         x, y,
    #         epochs=config['epochs'], batch_size=config['batch_size'],
    #         callbacks=[
    #             callbacks.EarlyStopping(patience=config['patience']),
    #             callbacks.ModelCheckpoint(weights_save_path, save_best_only=True, save_weights_only=True)
    #         ],
    #         validation_split=0.1
    #     )
    #     print(f'{category} end')


    texts = df['text'].drop_duplicates()
    if not os.path.exists(tokenizer_gen_path):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(texts.map(tp.norm_wakati))
        with open(tokenizer_gen_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(tokenizer.to_json(), ensure_ascii=False))
    with open(tokenizer_gen_path) as f:
        tokenizer = tokenizer_from_json(json.load(f))

    keyword_master = load_gen_keyword_master()
    id2category = dict(zip(gen_category_master['category_id'], gen_category_master['category_name']))
    category_keywords = dict()
    for category_id, df in keyword_master.groupby(['category_id']):
        keywords = df['keyword'].values
        category_keywords[id2category[category_id]] = list(keywords)
    gen_categories = list(category_keywords.keys())

    for category in gen_categories:
        x, y = create_dataset(texts, category_keywords[category])
        x = pad(tokenizer.texts_to_sequences(x), maxlen=40)
        model = create_model(emb_dim=10)
        weights_save_path = f'{project_root}/model/gen_classification_model/{category}.ckpt'
        model.fit(
            x, y,
            epochs=config['epochs'], batch_size=config['batch_size'],
            callbacks=[
                callbacks.EarlyStopping(patience=config['patience']),
                callbacks.ModelCheckpoint(weights_save_path, save_best_only=True, save_weights_only=True)
            ],
            validation_split=0.1
        )
        print(f'{category} end')


def infer(df, categories=categories, gen_categories=gen_categories):
    toppan = (df['tw_id'] >= 9*10**18).map(int).values
    texts = df['wakati_text']
    with open(tokenizer_path) as f:
        tokenizer = tokenizer_from_json(json.load(f))
    x = pad(tokenizer.texts_to_sequences(texts), maxlen=100)
    print('data prepared!')

    category2id = dict(zip(category_master['category_name'], category_master['category_id']))
    res = []
    n_categories = []
    for category in categories:
        model = create_model(emb_dim=2)
        try:
            model.load_weights(f'{project_root}/model/classification_model/{category}.ckpt')
            n_categories.append(category)
        except:
            continue 
        predicted = np.around(model.predict(x).ravel(), 4)# probability
        res.append(predicted)
        print(f'{category} end')
        del model
    categories = n_categories
    category_score = [json.dumps(dict([(str(category2id[categories[j]]), {"val": str(res[j][i])}) for j in range(len(categories))] + [('8', {'val': str(toppan[i])})]), ensure_ascii=False) for i in range(len(res[0]))]
    df['category'] = category_score


    '''
    記事カテゴリ
    '''
    with open(tokenizer_gen_path) as f:
        tokenizer = tokenizer_from_json(json.load(f))
    x = pad(tokenizer.texts_to_sequences(texts), maxlen=100)
    print('data prepared!')

    category2id = dict(zip(gen_category_master['category_name'], gen_category_master['category_id']))
    res = []
    n_categories = []
    for category in gen_categories:
        model = create_model(emb_dim=10)
        try:
            model.load_weights(f'{project_root}/model/gen_classification_model/{category}.ckpt')
            n_categories.append(category)
        except:
            continue
        predicted = np.around(model.predict(x).ravel(), 4)# probability
        res.append(predicted)
        print(f'{category} end')
        del model
    gen_categories = n_categories
    category_score = [json.dumps(dict([(str(category2id[gen_categories[j]]), {"val": str(res[j][i])}) for j in range(len(gen_categories))]), ensure_ascii=False) for i in range(len(res[0]))]
    df['gen_category'] = category_score


# from main import update_local_df
def update_past_all():

    dba = clsDbAccessor()
    df = dba.execQuery("SELECT `tw_id` FROM `tbl_twitters` WHERE proc_flag=1 AND deleted_at IS NULL;")
    dba.close()
    print(df)
    local_df = load_local_df().set_index('tw_id').reset_index()
    print(local_df.head())

    df = df.merge(local_df, how='left', on='tw_id').set_index('tw_id', drop=False).dropna()
    print(df)
    infer(df)
    print(df.head())
    update_tbl_twitter(df, ['category', 'gen_category'])
    pass 

if __name__ == '__main__':
    # df = pd.read_csv(f'{project_root}/data/tbl_twitter.csv', names=['text'])
    # train(df)
    update_past_all()
    pass