# kasai's LCP Array algorithm
- $O(N)$



# summary 
- IO
  - input: original string and its suffix array.
  - output: lcp array (height array)
- algorithm
  - prepare rank array := index of each suffix in the suffix array.
  - prepare height array, $h[i + 1] := lcp(sa[i], sa[i + 1])$, where sa := suffix array
  - calculate heights in order from long to short suffix.
    - let i := current suffix's index
    - look up the suffix index next to current suffix by using rank array and suffix array.
      - let j := its adjacent suffix's index.
    - check lcp(i, j)
      - let $l := lcp(i, j), h[i] := l$
    - here, if $lcp(i, j) = l$, ($sa[i] \lt sa[j]$).  
      there should exist $j\prime$ such that 
      $lcp(i + 1, j\prime)$ = l - 1, ($sa[i + 1] \lt sa[j\prime]$).
      one of $j\prime = j + 1$.  
    - then, if suffix array was calculated correctly,
      - let k := `i + 1`'s adjacent suffix's index.
      - $lcp(i + 1, k) \ge l - 1$
      - if not, the suffix array is not correct.
      - e.g. [see Example](#Example)
    - in summary, if $lcp(i, j) = l$, $lcp(i + 1, k) \ge l - 1$
      - where 
        - $j :=$ adjacent suffix's index of suffix $i$
        - $k :=$ adjacent suffix's index of suffix $i + 1$
    - therefore, if $lcp(i, j) = l$, 
      $lcp(i + 1, k)$ does not need to be calculated with brute-force.  
      it's enough to be calculated from $i + l$ and $k + l - 1$.  
      in other words, it's enough to calculate $lcp(i + l, k + l - 1)$.  
      $lcp(i + 1, k) = lcp(i, j) - 1 + lcp(i + l, k + l - 1)$  
    - be careful about index out of range.



# Example
consider the case of 'banana'

| suffix | saffix array | rank | lcp array |
| :-     | - | - | - |
| a      | 5 | 0 | 0 |
| ana    | 3 | 1 | 1 |
| anana  | 1 | 2 | 3 |
| banana | 0 | 3 | 0 |
| na     | 4 | 4 | 0 |
| nana   | 2 | 5 | 2 |
- lcp(ana, anana) $= lcp(3, 1) = 3$,   
  then lcp(na, nana) $= lcp(4, 2) = 2 \ge 3 - 1$  
  then lcp(a, ana) $= lcp(5, 3) = 1 \ge 2 - 1$




# references 
- [Algorithms with Python](http://www.nct9.ne.jp/m_hiroi/light/pyalgo60.html)
