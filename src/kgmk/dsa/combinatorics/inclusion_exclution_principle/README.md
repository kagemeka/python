# Inclusion-Exclusion Principle


# summary
- $|A \cup B| = |A|+ |B| - |A \cap B|$
- $|A \cup B| = |A| + |B| + |C| - |A\cap B| - |B\cap C| - |C\cap A| + |A\cap B\cap C|$
- $|\cup_{i=1}^{n}A_i| = \sum_{j=1}^{n}{((-1)^{j - 1}\sum_{S\prime \subseteq{S}, |S\prime| = j}{|\cap_{i\in S\prime}{A_i}|})} = \sum_i{|A_i|} - \sum_{i\lt j}{|A_i \cap A_j|} + \sum_{i\lt j\lt k}{|A_i \cap A_j \cap A_k|} + ... + (-1)^{n - 1}|A_1 \cap A_2 \cap ... \cap A_n|$



# related
- fast mobius transform



# references
- [wiki en](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle)
- [wiki ja](https://ja.wikipedia.org/wiki/%E5%8C%85%E9%99%A4%E5%8E%9F%E7%90%86)
- [mathworld](https://mathworld.wolfram.com/Inclusion-ExclusionPrinciple.html)


# problems 
- [AtCoder ABC003 D - AtCoder社の冬](https://atcoder.jp/contests/abc003/tasks/abc003_4)