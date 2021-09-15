# Garner Algorithm



# summary 
- calculate minimum $x$ such that $0\le x \lt \prod_{i=1}^{k}{m_i}, x \equiv r_i \mod {m_i}, m_i \bot m_j (i \lt j)$
- algorithm flow
  - let $x = t_1 + t_2m_1 + t_3m_1m_2 + ... + t_km_1m_2..m_{k - 1} \equiv r_k \mod{m_k}$
    - calculate $t_1, t_2, ..., t_k$ and restore $x$
  - $x \equiv t_1 \equiv r_1 \mod{m_1}$
  - $x \equiv t_1 + t_2m_1 \equiv r_2 \mod{m_2} \leftrightarrow t2 \equiv (r_2 - t_1)m_{1, 2}^{-1} \mod{m_2}$
  - $x \equiv t_1 + t_2m_1 + t_3m_1m_2 \equiv r_3 \mod{m_3} \leftrightarrow t3 \equiv (r_3 - (t_1 + t_2m_1))m_{1, 3}^{-1}m_{2, 3}^{-1} \mod{m_3}$
  - ...
  - $x \equiv t_1 + t_2m_1 + t_3m_1m_2 + ... + t_km_1m_2..m_{k - 1} \equiv r_k \mod{m_k} \\$
    $\leftrightarrow t_k \equiv (r_k - (t_1 + t_2m_1 + t_3m_1m_2 + ... + t_{k - 1}m_1m_2..m_{k - 2}))m_{1, k}^{-1}m_{2, k}..m_{k - 1, k}^{-1}$

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