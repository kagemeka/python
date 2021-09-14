# Chinese Remainder Theorem





# references 
- [wiki en](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
- [wiki ja](https://ja.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E3%81%AE%E5%89%B0%E4%BD%99%E5%AE%9A%E7%90%86)
- [qiita drken](https://qiita.com/drken/items/ae02240cd1f8edfc86fd)
- [cp algorithms](cp-algorithms.com/algebra/chinese-remainder-theorem.html)



# proof case $m_1 \bot m_2$
## proof of uniqueness
1. suppose two solution $\exist{x, y}, 0 \le x, y \lt m_1m_2$
2. $x \equiv y \mod{m_1} \because x \equiv b_1 , y \equiv b_1 \mod{m_1}$
3. $x \equiv y \mod{m_2} \because x \equiv b_2 , y \equiv b_2 \mod{m_2}$
4. $x \equiv y \mod{m_1m_2}$ 
5. $x = y \because 0 \le x, y \lt m_1m_2$


## proof of existence 
- $x \equiv b_1 \mod{m_1}$, $x \equiv b_2 \mod{m_2}$
1. $\exist{p, q}, m_1p + m_2q = 1 \because m_1 \bot m_2$
2. $m_1p \equiv 1 \mod{m_2}$, $m_2q \equiv 1 \mod{m_1} \because 1$
3. let $x = b_2m_1p + b_1m_2q$
4. $x \equiv b_1m_2q \equiv b_1 \mod{m_1}$
4. $x \equiv b_2m_1p \equiv b_2 \mod{m_2}$
5. $\therefore x \equiv b_2m_1p + b_1m_2q \mod{m_1m_2}$


# proof case $\neg m_1 \bot m_2$ $\cup$ case $m_1 \bot m_2$
- $\exist{x}, x \equiv b_1 \mod{m_1}, x \equiv b_1 \mod{m_2}, 0 \le x \lt \text{lcm}(m_1, m_2) (\text{ x is unique})
  \leftrightarrow b_1 \equiv b_2 \mod{\gcd(m_1, m_2)}
  $
## proof of existence 
1. $d := \gcd(m_1, m_2)$
2. $x \equiv b_1 \mod{d} \because d|m_1 \land x \equiv b_1 \mod{m_1}$
3. $x \equiv b_2 \mod{d} \because d|m_2 \land x \equiv b_2 \mod{m_2}$
4. $b_1 \equiv b_2 \mod{d} \because 2\land 3$
5. here, $\exist{p, q}, m_1p + m_2q = d \because \text{extended euclidean algorithm}$ 
6. $d|(b2 - b1) \land 5 \leftrightarrow sm_1p + sm_2q = b2 - b1 \ (s = (b_2 - b_1)/d)$
7. let $x = b_1 + sm_1p = b_2 - sm_2q$
8. $x \equiv b_1 \mod{m_1}, x \equiv b_2 \mod{m_2}$
9. $\therefore x \equiv b_1 + sm_1p = b_2 - sm_2q \mod{\text{lcm}(m_1, m_2)}$

