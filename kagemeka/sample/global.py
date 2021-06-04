import os 
cwd: str = os.path.dirname(os.path.abspath(__file__))

def hoge():
  global a
  a += 3
  print(a)


def bar():
  a = 10 # local
  # global a # error: assignment before global declaration
  print(a)
  hoge()


def foo():
  global a
  a = 1
  print(a)
  bar()
  ... 

foo()