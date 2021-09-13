# Greatest Common Divisor



# keyword
- euclidean algorithm
- monoid


# summary
- $\gcd{(0, 0)} = 0, \gcd(n, 0) = n$ (definition)
- $\gcd{(a, b)} = 
  \begin{cases}
    a & \text{if } b = 0 \\
    \gcd{(b, a\mod{b})} & \text{otherwise} \\
  \end{cases}
  $



# proof (GCD can be calculated by Euclidean algorithm)
- caluculate $\gcd{(a, b)}$
- let $a = bq + r (a, b, q, r \in \mathbb{N})$
1. let $d := \gcd{(a, b)}$
2. here, $d|(a - qb)$ because $d|a \land d|b$. 
3. that is, $\gcd(a, b) | \gcd(b, a - qb)$
4. on the other hand, let $a\prime := a - qb, d\prime := \gcd(b, a\prime)$
5. similarly, $d\prime |(a\prime + qb) \rightarrow \gcd(b, a\prime) | \gcd(a\prime + qb, b) \leftrightarrow \gcd(b, a - qb) | \gcd(a, b)$ 
6. from 3 and 5, $\gcd(a, b) = \gcd(b, a - qb) = \gcd(b, r)$

# references 
- [wiki en GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor)
- [wiki en Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
- [qiita drken](https://qiita.com/drken/items/b97ff231e43bce50199a)