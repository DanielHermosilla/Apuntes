Para todo par de [[vectores]] $x$ e $y$ de $\mathbb{R}^n$, tenemos: 

$$ |\langle x,y \rangle| \leq ||x||_2 \; ||y||_2 $$

Donde hacemos alusión al [[producto punto]], es decir: 

$$\langle x,y\rangle = \sum_{i=1}^{n} x_i y_i$$ 
## Demostración 

Consideremos un [[escalares|escalar]] "$\alpha$" arbitrario. Luego: 

$$||x-\alpha y||^2 \geq 0$$ 
$$\iff \sum^{n}_{i=1} (x_i - \lambda y_i)^2 \geq 0$$ 
$$\iff \sum^{n}_{i=1} (x_i)^2 - 2\alpha x_i y_i + \alpha^2 (y_i)^2 \geq 0$$

Esto representa un polinomio de segundo orden, en otras palabras, es una parábola. Analizando al desigualdad nos dice que su discriminante debe ser no positivo, es decir: 

$$ \implies (-2xy)^2 - 4||x||^2 ||y||^2 \leq 0$$ $$\iff (xy)^2 \leq ||x||^2 \;||y||^2 $$ $$ \iff |xy| \leq ||x|| \; ||y|| $$ 