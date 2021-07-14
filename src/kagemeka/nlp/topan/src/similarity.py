'''Cos類似度による類似記事抽出'''
from _base import *
config = config['similarity']

import gensim
import fasttext
class EmbedProcessor:
    def __init__(self, embedding):
        self.embedding = embedding
        self.emb_dim = len(self.term2vec('犬'))

    def term2vec(self, term):
        try:
            return self.embedding[term]
        except:
            return self.embedding.get_word_vector(term)
    
    def text2vec(self, text):
        vector = np.zeros(self.emb_dim, dtype=np.float32)
        terms = text.split()
        cnt = 0
        for term in set(terms):
            try:
                vector += self.term2vec(term)
                cnt += 1
            except:
                continue 
        return vector/cnt if cnt else np.full(self.emb_dim, np.nan)

model_path = f'{project_root}/model/emb_model/word2vec.gensim.model'
embedding = gensim.models.Word2Vec.load(model_path)
# model_path = f'{project_root}/model/emb_model/cc.ja.300.bin'
# embedding = fasttext.load_model(model_path)
ep = EmbedProcessor(embedding)


def remove_company(texts): # 数値以外を正規化して分かち書きしたものを渡す
    company_master = load_company_master()
    company_name = set(company_master['company_name'].values)
    for i in range(len(texts)):
        texts[i] = ' '.join([term for term in texts[i].split() if term not in company_name])
    return texts 


from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer
def vectorize(texts, method=1): # 正規化、分かち書きしたもの
    if method == 1: # word2vec, fasttext, etc...
        *vecs, = map(ep.text2vec, texts)
    elif method == 2: # LDA
        count_vectorizer = CountVectorizer()
        tf = count_vectorizer.fit_transform(texts)
        lda = LDA(n_components=50, random_state=0)
        lda.fit(tf)
        *vecs, = lda.transform(count_vectorizer.transform(texts))
    return vecs


def most_similar(df, row, topk=10, data=None):
    a = row['text_vector']
    b = np.vstack(df['text_vector'].values)
    similarities = np.dot(b, a) / row['norm'] / df['norm'].values
    try:
        old_scores = [(key, float(val['val'])) for key, val in json.loads(row['similar1']).items()]
    except:
        old_scores = []
    res = sorted(old_scores + list(zip(df.index, similarities)), key=lambda x: -x[1])[:topk]
    res = dict((str(res[i][0]), {'val': str(round(res[i][1], 3))}) for i in range(topk)) # to json
    return json.dumps(res, ensure_ascii=False)


def calculate(df, new_df, local_df, method=1, rm_company=False):
    tp = TP(pos=config['pos'])
    # df = df.merge(local_df, how='left', on='tw_id')
    # new_df = new_df.merge(local_df, how='left', on='tw_id')
    
    # df = df.merge()
    
    # df['text_vector'] = local_df.loc[df.index, 'text_vector']
    # df['norm'] = local_df.loc[df.index, 'norm']

    # texts = new_df['text'].map(tp.norm_wakati).values
    # if rm_company == True:
    #     texts = remove_company(texts)
    # text_vector = vectorize(texts, method=method)
    # new_df['text_vector'] = text_vector
    # local_df.loc[new_df.index, 'text_vector'] = new_df['text_vector']
    # new_df['norm'] = np.linalg.norm(text_vector, axis=1)
    # local_df.loc[new_df.index, 'norm'] = new_df['norm']

    # new_df['text_vector'] = local_df.loc[new_df.index, 'text_vector']
    # new_df['norm'] = local_df.loc[new_df.index, 'norm']

    df = df[df['text_vector'].notna() & df['deleted_at'].isna()]
    new_df = new_df[new_df['text_vector'].notna() & new_df['deleted_at'].isna()]
    all_df = pd.concat([df, new_df]).set_index('tw_id', drop=False)
    print(len(all_df))
    print(len(df))
    print(len(new_df))

    if not new_df.empty:
        j = 0
        for i in new_df.index:
            all_df.loc[i, 'similar1'] = most_similar(all_df.drop(i), new_df.loc[i])
            j += 1; print(j)
        j = 0
        for i in df.index:
            all_df.loc[i, 'similar1'] = most_similar(new_df, df.loc[i])
            j += 1
            if j % 50 == 0:
                print(j)

    return all_df.drop(['text_vector', 'norm'], axis=1)

def calculate_prepare(df, method=1, rm_company=False): # 最初だけ使う
    local_df = load_local_df()
    df['text_vector'] = local_df.loc[df.index, 'text_vector']
    df['norm'] = local_df.loc[df.index, 'norm']
    tmp = df[df['text_vector'].notna() & df['deleted_at'].isna()].set_index('tw_id', drop=False)
    df.drop(['text_vector', 'norm'], axis=1, inplace=True)
    df = tmp
    j = 0
    for i in df.index:
        df.loc[i, 'similar1'] = most_similar(df.drop(i), df.loc[i])
        j += 1; print(j)
    return df.drop(['text_vector', 'norm'], axis=1)