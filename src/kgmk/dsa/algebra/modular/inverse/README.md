# Modular Multipricative Inverse 



# Fermat's Little Theorem
- $a^{p - 1} \equiv 1 \mod{p}$ ($p$ is a prime number)
## proof 1 
- consider $a, 2a, ... (p - 1)a$
- these are pairwise distinct $\mod{p}$
- $\therefore a^{p - 1}(p - 1)! \equiv (p - 1)! \mod{p} \leftrightarrow a^{p - 1} \equiv 1 \mod{p}$

## proof 2 
- suppose $(m + 1)^p \equiv m^p + 1$
- suppose $a^p \equiv a$
- $(a + 1)^p \equiv a^p + 1\equiv a + 1$
- when $m = 1$, $2^p = (1 + 1)^p \equiv 1^p + 1 = 2$
- when $a = 0, 1$ $a^p \equiv a$ is clear.
- $\therefore a^{p - 1} \equiv 1$
### proof 2-1 $(m + 1)^p \equiv m^p + 1$
- $(m + 1)^p = m^p + pC1m^{p - 1} + ... + pCp-1m + 1 \equiv m^p + 1$
- $\because pC1m^{p - 1} + ... + pCp-1m \equiv 0$



# references
- [wiki en fermat little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
- [wiki ja fermat little theorem](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A7%E3%83%AB%E3%83%9E%E3%83%BC%E3%81%AE%E5%B0%8F%E5%AE%9A%E7%90%86)


# tips 
- euler's theorem
  - $a^{\varphi(N)} \equiv 1 \mod{N} (a \bot N)$
  - references 
    - [wiki ja](https://ja.wikipedia.org/wiki/%E3%82%AA%E3%82%A4%E3%83%A9%E3%83%BC%E3%81%AE%E5%AE%9A%E7%90%86_(%E6%95%B0%E8%AB%96))
    - [wiki en](https://en.wikipedia.org/wiki/Euler%27s_theorem)
  ## proof
  - $A = \{b_1, b_2, ..., b_{\varphi(N)} \}$
    - $\forall{i}, b_i \bot N$
  - $B = \{ab_1, ab_2, ..., ab_{\varphi(N)} \}$
  - $\prod{A} \equiv \prod{B} \leftrightarrow a^{\varphi(N)} \equiv 1$
