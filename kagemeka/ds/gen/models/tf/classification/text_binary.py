from tensorflow.keras import (
  layers, activations, regularizers, 
  initializers, losses, optimizers, 
  metrics, callbacks)
from tensorflow.keras \
  .models import Model, Sequential 
from tensorflow.keras.layers.experimental \
  .preprocessing import TextVectorization
from typing import Union 
import pathlib
import tensorflow as tf 
tf.random.set_seed(0)

from enum import Enum
import dataclasses

from ..utils import LRSchedule


layers.InputLayer


class TextBinaryBase(Model):
  def __init__(
      self, vocab_size: int=1<<20, 
      embedding_dim: int=1<<7, **kwargs):
    super(TextBinaryBase, self).__init__(
      **kwargs)
    self.vectorization = TextVectorization(
      output_mode='int')
    self.embedding = layers.Embedding(
      input_dim=vocab_size, output_dim=embedding_dim,
      mask_zero=True)

    self.relu = activations.relu 
    self.l2 = regularizers.L2(l2=1e-3)
    self.fc0 = layers.Dense(
      units=1<<7, 
      activation=self.relu,
      kernel_regularizer=self.l2)
    self.fc1 = layers.Dense(
      units=1<<6, 
      activation=self.relu,
      kernel_regularizer=self.l2)
    self.dropout = layers.Dropout(rate=0.2)

    self.to_out = layers.Dense(
      units=1, 
      activation=activations.sigmoid)

    self.compile(
      loss=losses.BinaryCrossentropy(
        from_logits=False),
      optimizer=optimizers.Adam(
        learning_rate= \
          LRSchedule.inv_time_decay),
      metrics=[
        metrics.BinaryAccuracy(threshold=.5)]
    )


  def call(self, inputs):
    x = self.vectorization(inputs)
    x = self.embedding(x)
    return x


  def train_(
      self, x, y, 
      epochs: int=..., 
      batch_size: int=...,
      checkpoint_path: Union[
        str, pathlib.Path]=None,
      **kwargs) -> None:
    
    callbacks_ = [
      callbacks.EarlyStopping(patience=10)]
    if checkpoint_path: 
      callbacks_.append(
        callbacks.ModelCheckpoint(
          filepath=checkpoint_path,
          save_best_only=True, save_weights_only=True)
      )
    
    self.fit(
      x, y, 
      validation_split=0.1,
      epochs=epochs, 
      batch_size=batch_size,
      callbacks=callbacks_,
    )


class TextBinaryCNN(TextBinaryBase):
  def __init__(self, **kwargs):
    super(TextBinaryCNN, self).__init__(
      **kwargs)
    self.conv1 = layers.Conv1D(
      filters=1<<9, kernel_size=3, 
      activation=self.relu,
      kernel_regularizer=self.l2)
    self.pool1 = layers.GlobalMaxPooling1D()

  def call(self, inputs):
    x = super(TextBinaryCNN, self).call(inputs)
    x = self.pool1(self.conv1(x))
    x = self.dropout(x)
    x = self.dropout(self.fc0(x))
    x = self.dropout(self.fc1(x))
    return self.to_out(x)



class TextBinaryLSTM(TextBinaryBase):
  def __init__(self, **kwargs):
    super(TextBinaryLSTM, self) \
      .__init__(
        **kwargs)
    self.lstm = layers.LSTM(
      units=1<<7, 
      activation=self.relu,
      return_sequences=False, 
      dropout=0.2,
      kernel_regularizer=self.l2)

  def call(self, inputs):
    x = super(TextBinaryLSTM, self).call(inputs)
    x = self.lstm(x)
    x = self.dropout(self.fc0(x))
    x = self.dropout(self.fc1(x))
    return self.to_out(x)


class TextBinaryRNN(TextBinaryBase):
  def __init__(self, **kwargs):
    super(TextBinaryRNN, self).__init__(
      **kwargs)
    self.rnn = layers.SimpleRNN(
      units=1<<7, 
      activation=self.relu,
      return_sequences=False, 
      dropout=0.2,
      kernel_regularizer=self.l2)

  def call(self, inputs):
    x = super(TextBinaryRNN, self).call(inputs)
    x = self.rnn(x)
    x = self.dropout(self.fc0(x))
    x = self.dropout(self.fc1(x))
    return self.to_out(x)


class TextBinaryGRU(TextBinaryBase):
  def __init__(self, **kwargs):
    super(TextBinaryGRU, self).__init__(
        **kwargs)
    self.gru = layers.GRU(
      units=1<<7, 
      activation=activations.relu,
      return_sequences=False, 
      dropout=0.2,
      kernel_regularizer=self.l2)

  def call(self, inputs):
    x = super(TextBinaryGRU, self).call(inputs)
    x = self.gru(x)
    x = self.dropout(self.fc0(x))
    x = self.dropout(self.fc1(x))
    return self.to_out(x)



'''TODO
# prevent overfitting
- Regularize: add penalty in addition to loss.
  e.g., L1 or L2.
- Dropout: use randomely dropping out technique. 
- Data Augmentation: increase the diversity of data 
  available for training models, 
  without actually collecting new data.
- Batch normalization
'''





