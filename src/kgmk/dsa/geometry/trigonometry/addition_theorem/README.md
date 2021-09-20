# Addition Theorem (Trigonometry)


# summary
- $\sin{(\alpha \pm \beta)} = \sin{\alpha}\cos{\beta} \pm \cos{\alpha}\sin{\beta}$
- $\cos{(\alpha \pm \beta)} = \cos{\alpha}\cos{\beta} \mp \cos{\alpha}\sin{\beta}$
- $\tan{(\alpha \pm \beta)} = \displaystyle{\frac{\tan{\alpha} \pm \tan{\beta}}{1 \mp \tan{\alpha}\tan{\beta}}} \ (\cos{\alpha}, \cos{\beta}, \cos{(\alpha \pm \beta)} \neq 0)$ 



# proof
## 1. $\cos{(\alpha - \beta)} = \cos{\alpha}\cos{\beta} + \sin{\alpha}\sin{\beta}$
1. $|AB|$
$$
|AB|^2 =
(\cos{\beta} - \cos{\alpha})^2 + (\sin{\beta} - \sin{\alpha})^2 \\
2 - 2\cos{\alpha}\cos{\beta} - 2\sin{\alpha}\cos{\beta}
$$
2. Law of cosines
$$
|AB|^2 = 1^2 + 1^2 - 2 \cdot 1 \cdot 1 \cos{\theta}
$$
3. $\cos{\theta} = \cos{(\alpha - \beta)}$ or $\cos{\theta} = \cos{(\beta - \alpha)}$, $\cos{(-\alpha)} = \cos{\alpha}$, $\therefore \cos{\theta} = \cos{(\alpha - \beta)} \ \forall{\alpha, \beta}$
4. $\cos{(\alpha - \beta)} = \cos{\alpha}\cos{\beta} + \sin{\alpha}\cos{\beta}\cos \because{1, 2, 3}$

## 2. $\cos{(\alpha + \beta)} = \cos{\alpha}\cos{\beta} - \sin{\alpha}\sin{\beta}$
$$
\cos{(\alpha + \beta)} = \cos{(\alpha - (-\beta))} =
\cos{\alpha}\cos{(-\beta)} + \sin{\alpha}\sin{(-\beta)} \\
= \cos{\alpha}\cos{\beta} - \sin{\alpha}\sin{\beta}
$$


## 3. $\sin{(\alpha \pm \beta)} = \sin{\alpha}\cos{\beta} \pm \cos{\alpha}\sin{\beta}$
$$
\sin{(\alpha \pm \beta)} = \\
\cos{(\alpha \pm \beta - \frac{\pi}{2})} = \\
\cos{(\alpha \pm (\beta \mp \frac{\pi}{2}))} = \\
\cos{\alpha}\cos{(\beta \mp \frac{\pi}{2})} \mp \sin{\alpha}\sin{(\beta \mp \frac{\pi}{2})} \\
= \pm \cos{\alpha}\sin{\beta} + \sin{\alpha}\cos{\beta} \\
= \sin{\alpha}\cos{\beta} \pm \cos{\alpha}\sin{\beta}
$$




# references
- [wiki en list of trigonometric identities - angle sum and difference identities](https://en.wikipedia.org/wiki/List_of_trigonometric_identities#Angle_sum_and_difference_identities)
- [manabitimes](https://manabitimes.jp/math/1021)
