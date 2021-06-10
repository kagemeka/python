'''キーワード再抽出'''
from _base import *
config = config['keyword_extraction']
from sklearn.feature_extraction.text import TfidfVectorizer

def extract(df, local_df, n=5):
    corpus = local_df['wakati_text'].dropna().values
    vectorizer = TfidfVectorizer()
    vectorizer.fit(corpus)
    features = np.array(vectorizer.get_feature_names())
    tp = TP(pos=['名詞'], dic_path=None)
    tmp_df = df['text'].map(tp.to_terms).dropna()
    texts = tmp_df.values
    texts_2 = [tp.normalize(' '.join(text)) for text in texts]
    sm = vectorizer.transform(texts_2)
    res = []
    for i in range(sm.shape[0]):
        words = dict((tp.normalize(word), word) for word in texts[i]).values()
        x = sm[i].tocoo()
        val = dict(zip(features[x.col], np.round(x.data, 3)))
        tmp = []
        for word in words:
            try:
                tmp.append((word, val[tp.normalize(word)]))
            except:
                continue
        tmp = dict((word, {'val': str(val)}) for word, val in sorted(tmp, key=lambda x: -x[1])[:n])
        res.append(json.dumps(tmp, ensure_ascii=False))
    df['word'] = np.nan
    df.loc[tmp_df.index, 'word'] = res 
