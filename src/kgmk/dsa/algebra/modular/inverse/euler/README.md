# Modular Inverse Euler's Theorem


# summary
- $a^{\varphi(N)} \equiv 1 \mod{N} (a \bot N)$
- $O(\sqrt{N})$ by calculating euler-totient function naively, or $O(\log{N})$ with preprocessing



## proof
- $A = \{b_1, b_2, ..., b_{\varphi(N)} \}$
  - $\forall{i}, b_i \bot N$
- $B = \{ab_1, ab_2, ..., ab_{\varphi(N)} \}$
- $\prod{A} \equiv \prod{B} \leftrightarrow a^{\varphi(N)} \equiv 1$



# references
- [wiki ja](https://ja.wikipedia.org/wiki/%E3%82%AA%E3%82%A4%E3%83%A9%E3%83%BC%E3%81%AE%E5%AE%9A%E7%90%86_(%E6%95%B0%E8%AB%96))
- [wiki en](https://en.wikipedia.org/wiki/Euler%27s_theorem)

