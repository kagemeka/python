
from tensorflow.keras.preprocessing.text \
  import Tokenizer, tokenizer_from_json 
import numpy as np


class MyTokenizer(Tokenizer):
  @classmethod 
  def from_texts(
      cls, texts: Iterable[str]=..., 
      save_path: \
        Union[str, pathlib.Path] =None,
      ) -> MyTokenizer:
    tokenizer = cls()
    tokenizer.fit_on_texts(texts)
    if save_path: 
      tokenizer.save(save_path)
    return tokenizer 

  def save(
      self, 
      path: Union[str, pathlib.Path]=...,
      ) -> None:
    dump: str = json.dumps(
      self.to_json(), ensure_ascii=False)
    with open(
        file=path, 
        mode='w', 
        encoding='utf-8') as f:
      f.write(dump)

  @classmethod 
  def from_json(
      cls, 
      path: Union[str, pathlib.Path]=...,
      ) -> MyTokenizer:
    with open(path, mode='r') as f:
      dump: str = json.load(f)
    tokenizer_cfg = json.loads(dump)
    config = tokenizer_cfg.get('config')

    word_counts = json.loads(
      config.pop('word_counts'))
    word_docs = json.loads(
      config.pop('word_docs'))
    index_docs = json.loads(
      config.pop('index_docs'))
    index_docs = {
      int(k): v 
      for k, v in index_docs.items()}
    index_word = json.loads(
      config.pop('index_word'))
    index_word = {
      int(k): v 
      for k, v in index_word.items()}
    word_index = json.loads(
      config.pop('word_index'))

    tokenizer = cls(**config)
    tokenizer.word_counts = word_counts
    tokenizer.word_docs = word_docs
    tokenizer.index_docs = index_docs
    tokenizer.word_index = word_index
    tokenizer.index_word = index_word
    return tokenizer 





import tensorflow as tf 
from tensorflow.keras.layers.experimental \
  .preprocessing import TextVectorization
class MyTextVectorization(TextVectorization):
  def adapt(self, *args, **kwargs):
    super(MyTextVectorization, self) \
      .adapt(*args, **kwargs)
    self._vocab = np.array(
      self.get_vocabulary())

  def to_text(
      self, 
      x: tf.Tensor) -> np.ndarray:
    return self._vocab[x]


from tensorflow.keras.preprocessing.sequence import pad_sequences
from typing import List 
import numpy as np 

def pad(
    x: List[List[int]]=..., 
    maxlen: int=...) -> np.ndarray:
  return pad_sequences(
    sequences=x, 
    maxlen=maxlen, 
    padding='post', 
    truncating='post', 
    dtype=np.int32, 
    value=0,
  )


