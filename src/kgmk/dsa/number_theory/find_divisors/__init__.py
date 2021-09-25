import typing



class FindDivisors():
  def __call__(self, n: int) -> typing.List[int]:
    divs = []
    i = 1
    while i * i < n:
      if n % i: 
        i += 1
        continue
      divs.append(i)
      divs.append(n // i)
      i += 1
    if i * i == n: divs.append(i)
    return sorted(divs)