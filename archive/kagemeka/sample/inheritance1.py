class A:
  def __init__(self):
    print('a')
  

class B(A):
  def __init__(self):
    print('b')
    super(B, self).__init__()


class C(A):
  def __init__(self):
    print('c')
    super(C, self).__init__()


class D(B, C):
  def __init__(self):
    print('d')
    super(D, self).__init__()


D()