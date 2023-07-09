
Sea $X$ una [[Variable aleatoria discreta|variable aleatoria discreta]] con rango $R_x$, entonces la **función de distribución acumulada** de $X$ se define como la función: 

$$F_x(x) = P(X\leq x)$$

Para todo $x\in\mathbb{R}$ 

Es decir, 

$$F_x(x)=\sum_{y\in R_x\ \bigg\vert\ y\leq x}P_x(y)$$ 
## Propiedades 

- $F_x(·)$ es creciente en $x$ 

- $\lim_{x\rightarrow +\infty} F_x(x) = 1$

- $\lim_{x\rightarrow -\infty} F_x(x) = 0$

- Para todo $x\in R_x$ se tiene que $F_x(x) - F_x(x-\epsilon) = p_x(x)$ para algun $\epsilon > 0$ suficientemente pequeño. 

## Ejemplo 

Se tiene un dado que se tira 3 veces, se define $X$ la cantidad de caras, donde $P_x(0) = \frac{1}{4}$, $P_x(1) = \frac{1}{2}$, $P_x(2)=\frac{1}{4}$. 

Entonces, la función de distribución acumulada en: 

1. $x< 0 \implies F_x(X\leq x) = 0$ 
2. $0<x<1\implies F_x (X\leq x) = \frac{1}{4}$ 
3. $1 \leq x < 2 \implies F_x(X \leq 1) = \frac{1}{4} + \frac{1}{2}$
4. $2\leq x \implies F_x(X \leq 2) = 1$ 