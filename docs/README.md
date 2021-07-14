### build pkg 
```sh
python3 setup.py \
  sdist \
  bdist_wheel
```


### pload pkg 
```sh
twine upload dist/* 
```


## shap
```py3
import tensorflow as tf 

tf.compat.v1.enable_eager_execution()


#  AttributeError: 'TFDeep' object has no attribute 'between_tensors'
tf.compat.v1.disable_v2_behavior() 


``` 




## rm all __pycahe__ 
```sh
$ find . -name __pycache__ -type d -print0 | xargs -0 rm -r 
```