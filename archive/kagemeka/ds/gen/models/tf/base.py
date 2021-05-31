import tensorflow as tf 
from tensorflow.keras.models \
  import (
    Model,
  )
tf.random.set_seed(0)

from tensorflow.keras import (
  layers, 
  activations, 
  regularizers,
  initializers,
  losses, 
  optimizers, 
  metrics,
  callbacks,
)

from typing import (
  Tuple, 
  List,
)



def define_callbacks(
    save_path: str=None,
    ) -> List[callbacks.Callback]:
  callbacks_ = [
    callbacks.EarlyStopping(
      monitor='val_loss',
      patience=10,
    )
  ]

  if save_path:
    callbacks_.append(
      callbacks.ModelCheckpoint(
        filepath=save_path,
        monitor='val_loss',
        save_best_only=True,
        save_weights_only=True,
      )
    )
  return callbacks_



class TFBase(Model):
  def __init__(
      self, 
      input_shape: Tuple[int]=...,
      output_shape: Tuple[int]=...,
      **kwargs):

    super(TFBase, self).__init__()

    self.input_layer = \
      layers.InputLayer(
        input_shape=input_shape,
      )


    self.dropout = layers.Dropout(
      rate=0.3, 
      seed=0,
    )
    
  def call(self, x):
    return self.input_layer(x)


  def train_(
      self,
      train_data=..., 
      validation_data=None,
      validation_split: int=0.2,
      save_path: str=None,
      epochs: int=...,
      batch_size: int=...):

    callbacks_ = define_callbacks(
      save_path=save_path,
    )
      
    common_kwargs = {
      'x': train_data[0],
      'y': train_data[1],
      'epochs': epochs,
      'batch_size': batch_size,
      'callbacks': callbacks_,
    }

    if validation_data:
      self.fit(
        **common_kwargs,
        validation_data= \
          validation_data,
      )
    else:
      self.fit(
        **common_kwargs,
        validation_split= \
          validation_split,
      )
    
    if save_path:
      self.load_weights(save_path)






def _fully_connected(n: int=6):
  return layers.Dense(
    units=1<<n,
    activation=activations.relu,
    kernel_regularizer= \
      regularizers.L2(l2=1e-3),
  )


def _simple_rnn(
    n: int=7, 
    return_sequences: bool=False):
  return layers.SimpleRNN(
    units=1<<n,
    activation=activations.relu,
    recurrent_dropout=0.3,
    dropout=0.3,
    kernel_regularizer= \
      regularizers.L2(l2=1e-3),
    return_sequences= \
      return_sequences,
  )


def _lstm(
    n: int=7, 
    return_sequences: bool=False): 
  return layers.LSTM(
    units=1<<n,
    activation=activations.tanh,
    recurrent_activation= \
      activations.sigmoid,
    unroll=False,
    use_bias=True,
    dropout=0.3,
    recurrent_dropout=.0,
    kernel_regularizer= \
      regularizers.L2(l2=1e-3),
    return_sequences= \
      return_sequences,
  )


def _gru(
    n: int=7, 
    return_sequences: bool=False):
  return layers.GRU(
    units=1<<n,
    recurrent_activation= \
      activations.relu, 
    activation=activations.relu,
    recurrent_dropout=0.3,
    dropout=0.3,
    kernel_regularizer= \
      regularizers.L2(l2=1e-3),
    return_sequences= \
      return_sequences,
  )



layers.LSTM 
layers.LSTMCell
layers.Conv1D
layers.Convolution1D
layers.Conv1DTranspose
layers.Convolution1DTranspose
layers.Conv2D 
layers.Conv2DTranspose
layers.Convolution2D
layers.Convolution2DTranspose
layers.Conv3D 
layers.ConvLSTM2D
layers.InputLayer
layers.Lambda 
layers.GlobalAveragePooling1D
layers.GlobalAvgPool1D
layers.GlobalMaxPool1D
layers.GlobalMaxPooling1D
layers.Activation
layers.Attention
layers.AlphaDropout
layers.Dropout
layers.ELU
layers.Embedding
layers.ReLU
layers.RNN
layers.SimpleRNN
layers.GRU
layers.ZeroPadding1D
layers.Reshape
layers.Softmax
layers.Bidirectional
layers.Dense 
layers.Concatenate


print(losses.Reduction.AUTO)
print(type(losses.Reduction.AUTO))