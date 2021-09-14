# Euler's Totient function (Phi function)



# summary
- count of $\gcd(n, N) = 1, (1 \le n \le N)$
- let $N = {p_0}^{c_0}{p_1}^{c_1}...{p_k}^{c_k}$
- $\varphi(N) = N\prod_{i=0}^{k}{1 - \frac{1}{p_i}}$
- $O(\sqrt{N})$ (naive prime factorization)
- $O(\log{N})$ (prime factorization with LPF table)


# feature 
- $\varphi(p) = p - 1$ if $p$ is a prime number.
- $\sum_{d|n}\varphi(d) = n$
- $\varphi(nm) = \varphi(n)\varphi(m) \ (\text{ if } m \bot n)$
- $a^\varphi(m) \equiv 1 \mod{m}$ if $a \bot m$
  - especially, $a^{p - 1} \equiv 1 \mod{p}$ if $p$ is prime.



# references 
- [wiki en](https://en.wikipedia.org/wiki/Euler%27s_totient_function)
- [wiki ja](https://ja.wikipedia.org/wiki/%E3%82%AA%E3%82%A4%E3%83%A9%E3%83%BC%E3%81%AE%CF%86%E9%96%A2%E6%95%B0)