# Fenwick Tree (Binary Indexed Tree)


# problems
- [AtCoder ALPC B - Fenwick Tree](https://atcoder.jp/contests/practice2/tasks/practice2_b)
- [AtCoder ABC185 F - Range Xor Query](https://atcoder.jp/contests/abc185/tasks/abc185_f)




# use case 
- point set, range get
- range set, range get


# note
- both get and set operation is O(log(n)).
- set operation point to index i.
- get operation point closed range [1, i]
- Any `Commutative Monoid` can be stored on FenwickTree.
  - it's needed to be `Abelian Group` to use get range [l, r] value.



# references 
- [wiki en Monoid](https://en.wikipedia.org/wiki/Monoid)
- [wiki en Abelian Group](https://en.wikipedia.org/wiki/Abelian_group)
- [wiki en Commutative](https://en.wikipedia.org/wiki/Commutative_property)



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