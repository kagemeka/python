def a():
  n = 1
  def f():
    nonlocal n
    n += 1
    return n
  return f 


f = a()
for _ in range(10):
  print(f())
