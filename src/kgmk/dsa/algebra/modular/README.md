# Modular



# tips 

## Fermat's littele theorem

### proof 1
- $n^p \equiv n$ -> $(n + 1)^p \equiv n + 1 \mod p$ where p is a prime number.
$$
n = 1 \implies 1^p = 1
$$
$$
(n + 1)^p = 1 + n^p + \sum_{k = 1}^{n - 1}{\displaystyle{{p}\choose{k}}n^k}
\equiv n^p + 1 \equiv n + 1
$$
- $\forall{n}n^p \equiv n$
- $\forall{n}\perp{p}\ n^{p - 1} \equiv{1}$ 



### proof 2
- $\forall{n}\perp{p}$ think of a sequence $A = {[n, 2n, 3n, ..., (p - 1)n]}$
- $x\in{A} \mod p$ are pair wise distinct.
  - if there exist $A_i \equiv A_j i, j(1 \le i \lt j \le p - 1)$, $\exist{i, j} A_j - A_i = (j - i)n \equiv 0$
  - but ${n}\perp{p}$ and $1 \le j - i \lt p - 1, (j - i)\perp{p}$.
  - thus there not exist $A_i \equiv A_j$
- therefore, $n\cdot2n\cdot3n\cdot...\cdot(p - 1)n \equiv (p - 1)!$
$\longleftrightarrow n^{p - 1} \equiv 1$
