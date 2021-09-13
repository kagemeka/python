# Euler's Totient function (Phi function)



# summary
- count of $\gcd(n, N) = 1, (1 \le n \le N)$
- let $N = {p_0}^{c_0}{p_1}^{c_1}...{p_k}^{c_k}$
- $phi(N) = N\prod_{i=0}^{k}{1 - \frac{1}{p_i}}$
- $O(\sqrt{N})$ (naive prime factorization)
- $O(\log{N})$ (prime factorization with LPF table)