  def factorial(
    self, 
  ):
    n = self.value
    fact = [
      self.__class__(i)
      for i in range(n)
    ]
    fact = np.array(fact)
    e = self.mul_identity()
    fact[0] = e
    fact.cumprod(out=fact)
    return fact
  

  def inv_factorial(
    self,
  ): 
    fact = self.factorial()
    n = self.value
    ifact = np.arange(
      1, 
      n + 1,
    ).astype(object)
    ifact[-1] = fact[-1].inv()
    ifact[::-1].cumprod(
      out=ifact[::-1],
    )
    return ifact