# Greatest Common Divisor



# keyword
- euclidean algorithm
- monoid


# summary
- $\gcd{(0, 0)} = 0$ (definition)
- $\gcd{(a, b)} = 
  \begin{cases}
    a & \text{if } b = 0 \\
    \gcd{(b, a\mod{b})} & \text{otherwise} \\
  \end{cases}
  $