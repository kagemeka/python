# Extended Euclidean Algorithm


# summary
- compute a pair of $x, y$ which is a solution for $ax + by = \gcd(a, b)$

- argument
  - $a$: int
  - $b$: int

- return
  - $\gcd(a, b)$: int
  - $x$: int
  - $y$: int


# proof $\exists{x, y}, ax + by = c\ (a, b, c, x, y \in \mathbb{N}) \leftrightarrow \gcd(a, b) | c$
## $\exists{x, y}, ax + by = c\ (a, b, c, x, y \in \mathbb{N}) \rightarrow \gcd(a, b) | c$
- let $d := \gcd(a, b)$, $d|a, d|b, \rightarrow d|(ax + by) \therefore d|c$

## $\exists{x, y}, ax + by = c\ (a, b, c, x, y \in \mathbb{N}) \leftarrow \gcd(a, b) | c$
- $let d := \gcd(a, b)$. 
- suppose $\exists{x, y}, ax + by = d\ (a, b, x, y \in \mathbb{N})$
- let $k := \displaystyle{\frac{c}{d}}$ $x := xk, y := yk$
- $\therefore\exists{x, y}, ax + by = c\ (a, b, c, x, y \in \mathbb{N})$

## $\exists{x, y}, ax + by = \gcd(a, b)\ (a, b, x, y \in \mathbb{N})$
### proof 1 simulate Extended Euclidean algorithm 
- $a = qb + r$, $d = \gcd(a, b)$
- $(qb + r)x + by = d$
- $b(qx + y) + rx = d$
- $x\prime = qx + y, y\prime = x$
- $bx\prime + ry\prime = d$
- ... (recursively)
- $ds + 0t = d \because r \text{ should become 0}$
- $\exist x\prime, y\prime \rightarrow x = y\prime, y = x\prime - qy\prime$
- here, $s = 1, t = 0$ is a solution.
- $\therefore \exist x, y, ax + by = \gcd(a, b)$

### proof 2
1. define $d_0$ is a smallest natural number expressed as $ax + by = k$.
2. $d_0 = ax_0 + by_0$
3. $k = qd_0 + r (0 \le r \lt d_0)$
4. $r = k - qd_0 = (ax + by) - q(ax_0 + by_0) = a(x - qx_0) + b(y - qy_0)$
    - $r$ is also expressed as $ax + by$
5. if $0 \lt r \lt d_0, $ this is conflict to 1 $\therefore r = 0$
6. $\therefore k = ax + by = qd_0$
7. let $d := \gcd(a, b)$
8. $d | d_0 \because d | (ax + by)$
9. $d_0 | a \because{a = a\times{1} + b\times{0} = qd_0}$. similarly, $d_0 | b$
10. $d_0$ is a common divisor of $a, b$ $\rightarrow d_0 | d$
11. $d_0 = d \because 8, 10$
12. $\therefore \exists{x, y}, ax + by = \gcd(a, b)\ (a, b, x, y \in \mathbb{N})$

### proof 3 use a feature of quotient ring.
- $\exists{x, y}, ax + by = \gcd(a, b) \leftrightarrow \exists{x, y}, ax + by = 1 (a \bot b)$
#### proof 3-1 $\exists{x, y}, ax + by = 1 (a \bot b)$
1. let $ia \equiv r_i \mod{b}, (0 \le i \lt b)$
2. suppose $\exist{i, j, i \lt j}, r_i = r_j$
3. $(j - i)a \equiv 0 \mod{b} \leftrightarrow j - i \equiv 0 \mod{b}$
4. this is conflict to 2 $\because 1 \le j - i \lt b$
5. $\therefore r_i$ are pairwise distinct. $\rightarrow \exist{j}, r_i = 1$
6. $\therefore \exist{i, n},  ai + bn \equiv 1 \mod{b} \leftrightarrow ax + by = 1$



# feature
- $\exists{x, y}, ax + by = 1 \leftrightarrow \gcd(a, b) = 1 \leftrightarrow a \bot b$


# references 
- [wiki en](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
- [manabitimes ax + by = c](https://manabitimes.jp/math/674)
- [mabanitimes euclidean algorithm](https://manabitimes.jp/math/672)
- [qiita drken](https://qiita.com/drken/items/b97ff231e43bce50199a)



# problems 
- [AtCoder ABC186 E - Throne](https://atcoder.jp/contests/abc186/tasks/abc186_e)