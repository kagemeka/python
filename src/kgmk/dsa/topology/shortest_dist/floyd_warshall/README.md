# floyd warshall shotest dist 


# note 
- from dense graph 
- all source shortest path


# complexity
- $O(V^3)$



# proof
- let $dp_{i, j, k} :=$ shortest dist $i$ to $j$ by using any of vertices from {1, 2, ... k} as halfway points.
- $dp_{i, j, k} = \min{(dp_{i, j, k - 1}, dp_{i, k, k - 1} + dp_{k, j, k - 1})}$
- if $\forall{i, j}, dp_{i, j, k - 1}$ is calculated precisely, $\forall{i, j}, dp_{i, j, k}$ can be calculated precisely.
- $dp_{i, j, 0} := 
  \begin{cases} 
  0 & \text{if } i = j \\
  \text{cost}_{i, j} & \text{if } \exist{\text{edge}_{i, j}} \\
  \inf & \text{otherwise} \\
  \end{cases}$


# references 
- [wiki en](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [wiki ja](https://ja.wikipedia.org/wiki/%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E2%80%93%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95)


# problems 
- [AtCoder ABC208 D - Shortest Path Queries 2](https://atcoder.jp/contests/abc208/tasks/abc208_d)
- [AtCoder ABC012 D - バスと避けられない運命](https://atcoder.jp/contests/abc012/tasks/abc012_4)