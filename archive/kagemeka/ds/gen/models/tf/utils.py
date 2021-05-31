from enum import Enum 
from tensorflow.keras import (
  layers,
  initializers, 
  optimizers,
)
import tensorflow as tf 

class LRSchedule(Enum):
  polynomial_decay = optimizers \
    .schedules.PolynomialDecay(
      initial_learning_rate=1e-3,
      decay_steps=1<<18,
      power=1<<6,
      end_learning_rate=1e-5,
    )

  inv_time_decay = optimizers \
    .schedules.InverseTimeDecay(
      initial_learning_rate=1e-3,
      decay_steps=1,
      decay_rate=1e-3, 
      staircase=False,
    )




# create user defined layer.
# https://www.tensorflow.org/guide/keras/custom_layers_and_models

class Linear(layers.Layer):
  def __init__(self, units=1<<5):
    super(Linear, self).__init__()
    self.units = units 
  
  def build(self, input_shape):
    self.w = self.add_weight(
      shape=(
        input_shape[-1], 
        self.units),
      initializer= \
        initializers.RandomNormal(),
      trainable=True,
    )
    
    self.b = self.add_weight(
      shape=(self.units, ),
      initializer= \
        initializers.RandomNormal(),
      trainable=True,
    )
    
  
  def call(self, inputs):
    return \
      tf.matmul(inputs, self.w) \
      + self.b


'''Test'''

class Base1:
  def call(self):
    print(1)


class Base2:
  def call(self):
    print(2)


class Model(Base2, Base1):
  ...


model = Model()
model.call()
print(type(model))