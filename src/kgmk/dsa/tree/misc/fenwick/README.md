# Fenwick Tree (Binary Indexed Tree)
  

# summary
- answer for range query on an array fast.
- target array should have Commutative Monoid $(S, *, e)$ on it.

## use case
- point set, range get
- range set, point get
- range set, range get (using two fenwick trees)
- binary search (it's needed to be that $\sum_{j=0}^{i} A_i$ is `monotonic` on $i$. 
  - ($\sum$ means cumulative operation on the Commutative Monoid)

## note
- both get and set operation is $O(\log(N))$.
- $\text{set}(i, x)$: $A_i = A_i * x \ (0 \le i \lt N)$.
- $\text{get}(i)$: return $\sum_{j=0}^{i}A_j$.
  - ($\sum$ means cumulative operation on the Commutative Monoid)
- $\text{get}(l, r)$: return $\sum_{i=l}^{r - 1}A_i$.
  - ($\sum$ means cumulative operation on the `Abelian Group`)
  - Abelian Group $\rightarrow$ Commutative Monoid
  - Abelian Group $\not \leftarrow$ Commutative Monoid
- $\text{set}(l, r, x)$: $\forall{l \le i \lt r}\ A_i = A_i * x$
  - fenwick tree stores delta values, that is, $d_i = A_i * A_{i - 1}^{-1}$
  - $A_i^{-1}$ means inverse of $A_i$ on the Abelian Group.
  - in this use case, $\text{get}(i)$: return $A_i = \sum_{j=0}^{i}d_j$
  
- Any `Commutative Monoid` can be stored on FenwickTree.
  - but it's needed to be `Abelian Group` to implement get or set range $[l, r)$ value.

## Commutative Monoid Example 
- (integer, $\max{(a, b)}$, $-\inf$), (monotoinic)
- (integer, $\min{(a, b)}$, $\inf$), (monotonic)
- (square matrix, $a\cdot{b}$, identity matrix)
- (integer, $\gcd{(a, b)}$, 0), (monotonic)
- (integer, $\text{lcm}(a, b)$, 1), (monotonic)

## Abelian Group Example
- (integer, $a + b$)
- (integer, $a \oplus b$)
- (integer, $a \times b$)





# references 
- [wiki en Monoid](https://en.wikipedia.org/wiki/Monoid)
- [wiki en Abelian Group](https://en.wikipedia.org/wiki/Abelian_group)
- [wiki en Commutative](https://en.wikipedia.org/wiki/Commutative_property)
- [hos.ac](http://hos.ac/slides/20140319_bit.pdf)
- [algo-logic](https://algo-logic.info/binary-indexed-tree/)


# tips 
- bit operation
```py
'''
0 := 0...0000
1 := 0...0001
-1 := 1....1111 (inv(1) + 1)
2 := 0...0010
-2 := 1....1110 (inv(2) + 1)

Here, 'inv' means bits world inverse operation.
default is 1-indexed.
'''
```



# problems
- [AtCoder ALPC B - Fenwick Tree](https://atcoder.jp/contests/practice2/tasks/practice2_b)
- [AtCoder ABC185 F - Range Xor Query](https://atcoder.jp/contests/abc185/tasks/abc185_f)
  - point xor, get range xor 
- [AtCoder ABC153 F - Silver Fox vs Monster](https://atcoder.jp/contests/abc153/tasks/abc153_f)
  - range add, get point
- [AtCoder Typical Algorithm A - 二分探索の練習問題](https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a)
  - max, lower bound
- [AtCoder ABC218 G - Game on Tree 2](https://atcoder.jp/contests/abc218/tasks/abc218_g)
  - add, lower bound
- [AtCoder ABC174 F - Range Set Query](https://atcoder.jp/contests/abc174/tasks/abc174_f)
  - add
- [AtCoder ABC186 F - Rook on Grid](https://atcoder.jp/contests/abc186/tasks/abc186_f)
  - add
- [AtCoder Typical90 017 - Crossing Segments（★7）](https://atcoder.jp/contests/typical90/tasks/typical90_q)
  - add
