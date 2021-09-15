# Garner Algorithm



# summary 
- calculate minimum $x$ such that $0\le x \lt \prod_{i=1}^{k}{m_i}, x \equiv r_i \mod {m_i}, m_i \bot m_j (i \lt j)$
- $O(k^2 + k\log{\max(m)})$
- be careful of that $\forall{i, j}, m_i \bot m_j$

# use cases
- operation on large numbers with garner instead of arbitrary-precision integer.
  - calculate $x \mod{m_1}, x \mod{m_2}, ..., x \mod{m_k}$
  - restore $x$
- calculate $x \mod ({\text{arbitral mod}})$.


# references 
- [qiita drken CRT](https://qiita.com/drken/items/ae02240cd1f8edfc86fd)
- [cp algorithms CRT](https://cp-algorithms.com/algebra/chinese-remainder-theorem.html)
- [kopricky blog](https://kopricky.github.io/code/Computation_Advanced/garner.html)
- [furuyan blog](https://www.creativ.xyz/ect-gcd-crt-garner-927/)
- [kirika_comp bloc](https://kirika-comp.hatenablog.com/entry/2017/12/18/143923)
- [wiki en arbitrary-precition arithmetic](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic)
- [wiki ja arbitrary-precition arithmetic](https://ja.wikipedia.org/wiki/%E4%BB%BB%E6%84%8F%E7%B2%BE%E5%BA%A6%E6%BC%94%E7%AE%97)



# problems 
- [AtCoder ABC186 E - Throne](https://atcoder.jp/contests/abc186/tasks/abc186_e)