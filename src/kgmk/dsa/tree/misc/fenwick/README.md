# Fenwick Tree (Binary Indexed Tree)


# problems
- [AtCoder ALPC B - Fenwick Tree](https://atcoder.jp/contests/practice2/tasks/practice2_b)
- [AtCoder ABC185 F - Range Xor Query](https://atcoder.jp/contests/abc185/tasks/abc185_f)
  - point xor, get range xor 
- [AtCoder ABC153 F - Silver Fox vs Monster](https://atcoder.jp/contests/abc153/tasks/abc153_f)
  - range add, get point sum
- [AtCoder Typical Algorithm A - 二分探索の練習問題](https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a)
  - max, lower bound


# use case 
- point set, range get
- range set, point get
- range set, range get (using two fenwick trees)
- binary search (it's needed to be that $\sum_{j=0}^{i} A_i$ is `monotonic` on $i$)



# note
- both get and set operation is O(log(n)).
- set operation point to index i.
- get operation point closed range [1, i]
- Any `Commutative Monoid` can be stored on FenwickTree.
  - it's needed to be `Abelian Group` to implement get/set range [l, r] value.
- set range [l, r], get point i
  - fenwick tree stores delta values, that is, $d_i = v_i\ op\ v_{i - 1}^{-1}$
  - $v^{-1}$ means inverse of $v$ on the Abelian Group.
  - get point $v_i = \sum_{j=0}^{i}d_j$ ($\sum$ means cumulative operation on the Abelian Group)




# references 
- [wiki en Monoid](https://en.wikipedia.org/wiki/Monoid)
- [wiki en Abelian Group](https://en.wikipedia.org/wiki/Abelian_group)
- [wiki en Commutative](https://en.wikipedia.org/wiki/Commutative_property)
- [hos.ac](http://hos.ac/slides/20140319_bit.pdf)
- [algo-logic](https://algo-logic.info/binary-indexed-tree/)



# tips 
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