# Modular Inverse Fermat's Little Theorem



# summary
- $a^{p - 1} \equiv 1 \mod{p}$ ($p$ is a prime number)
- $O(\log{N})$



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
