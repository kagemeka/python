# モデルについて

基本的に、モデルやweightsはgitにあげていない。
ほとんどはプログラムで自動的にネットからダウンロードするが、
object_trackingのdeep_sortのようにモデルを手動でダウンロードする必要がある場合もある。


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


### pkg 整理
- [x] cp
- [ ] ds
  - [ ] processing
  - [ ] ml
- [x] dsa
- [x] gen
- [x] rpa
- [x] samples 
- [x] txn


## shapについて
tensorflow2でエラーが出た時のtips
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