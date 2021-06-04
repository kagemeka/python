def make_counter():
  i = -1
  def counter():
    nonlocal i 
    i += 1
    return i 
  return counter 


import time

def main():
  counter = make_counter()
  s = time.time()
  while True:
    if time.time() - s > 3:
      break 
    i = counter()
    print(i)


if __name__ == '__main__':
  main()
  