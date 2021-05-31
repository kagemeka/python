

from typing import Union 
import pathlib 
import torch 
import tensorflow as tf 
import numpy as np 
from scipy.stats import spearmanr
import gensim
import fasttext


class WordEmbedding:
  def __init__(self, model): # embedding(model)を渡す。
    self.model = model
    self.emb_dim = self.get_vector_size()

  
  @classmethod
  def from_model_path(cls, path):
    return cls(cls.load_model(path))

  @classmethod 
  def from_corpus(cls, path):
    ...

  
  @staticmethod
  def load_model(path: Union[str, pathlib.Path]) -> ...:
    templates = [
      f'gensim.models.Word2Vec.load({path})',
      f'gensim.models.Word2Vec.load_word2vec_format({path})',
      f'gensim.models.FastText.load_fasttext_format({path})',
      f'gensim.models.FastText.load({path})',
      f'gensim.models.FastText.load_binary_data({path})',
      f'gensim.models.KeyedVectors.load_word2vec_format({path}, binary=True)',
      f'gensim.models.KeyedVectors.load_word2vec_format({path}, binary=False)',
      f'gensim.models.KeyedVectors.load({path})',
      f'gensim.models.KeyedVectors.load({path}, mmap=\'r\')',
      f'fasttext.load_model({path})',

    ]

    for t in templates:
      try:
        return exec(compile(t, '<string>', 'eval'))
      except: pass 
    return None 
  
    # try: 
    #     return gensim.models.Word2Vec.load(path)
    #     return gensim.models.Word2Vec.load_word2vec_format(path)
    #     return gensim.models.FastText.load_fasttext_format(path)
    #     return gensim.models.FastText.load(path)
    #     return gensim.models.FastText.load_binary_data(path)
    #     return gensim.models.KeyedVectors.load_word2vec_format(path, binary=True)
    #     return gensim.models.KeyedVectors.load_word2vec_format(path, binary=False)
    #     return gensim.models.KeyedVectors.load(path)
    #     return gensim.models.KeyedVectors.load(path, mmap='r')
    #     return fasttext.load_model(path)
    # except: 
    #     return None 


  @staticmethod
  def glove_to_w2v(file_path):
    lines = open(file_path, 'r').readlines()
    print(lines)
    ...


  def get_vector_size(self):
    try: return self.model.vector_size
    except: pass

  
  def term2vec(self, term) -> Union[np.array, torch.Tensor, tf.Tensor]:
    try: return self.model[term]
    except: ... 
    try: return self.model.get_word_vector(term)
    except: ... 
    return np.full(self.emb_dim, np.nan)

  
  def text2vec(self, text):
      vector = np.zeros(self.emb_dim, dtype=np.float32)
      terms = text.split()
      cnt = 0
      for term in set(terms):
        try:
          vec = self.term2vec(term)
          if np.isnan(vec[0]): continue
          vector += self.term2vec(term)
          cnt += 1
        except:
          continue 
      return vector/cnt if cnt else np.full(self.emb_dim, np.nan)


  @staticmethod 
  def cos_similarity(a, b, norm_a=None, norm_b=None):
    norm_a = np.linalg.norm(a, axis=-1) if norm_a is None else norm_a
    norm_b = np.linalg.norm(b, axis=-1) if norm_b is None else norm_b
    similarities = np.dot(a, b.T) / norm_a.reshape(-1, 1) / norm_b
    return similarities


  def evaluate(self, data=None, **keywords):
    if not 'mode' in keywords:   
      '''
      dataはword1, word2, similarityの3カラムがあるdf
      '''
      a = np.stack(data.word1.map(self.term2vec).values) 
      b = np.stack(data.word2.map(self.term2vec).values)

      sim = (a*b).sum(axis=1) / np.linalg.norm(a, axis=1) / np.linalg.norm(b, axis=1)
      data['similarity2'] = sim 
      res = spearmanr(data[['similarity', 'similarity2']].dropna().values)[0]
      return res
    else:
      ...



  def additional_train(self, corpus):
    self.model.build_vocab(corpus, update=True)
    self.model.train(corpus, total_examples=self.model.corpus_count, epochs=self.model.epochs)

  
  def similar_words(self, word):
    return self.model.most_similar(word)

