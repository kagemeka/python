'''error pattern'''

class A:
  def __init__(self, text):
    print('a')
    print(text)


class B(A):
  def __init__(self, text):
    print('b')
    super(B, self).__init__(text)



class C:
  def __init__(self, **kwargs):
    print('c')
    super(C, self).__init__()


class D(C, B):
  def __init__(self, text):
    print('d')
    super(D, self).__init__(text=text)


D('aaa')