class A:
  def __init__(self):
    print('a')
    super(A, self).__init__()
  

class B(A):
  def __init__(self):
    print('b')
    super(B, self).__init__()


class C:
  def __init__(self):
    print('c')


class D(B, C):
  def __init__(self):
    print('d')
    super(D, self).__init__()


D()