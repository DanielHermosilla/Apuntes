
Para dos variable aleatorias $(X,Y)$, la pdf conjunta viene dada por: 

$$f(x,y)=P(X=x, Y=y)$$

En particular: 

- **Discreto**: $$P(a\leq x\leq b, c\leq y\leq d)=\sum_{a\leq x\leq b}\sum_{c\leq y\leq d}f(x,y)$$

- **Continuo**: $$P(a\leq x\leq b, c\leq y\leq d)=\int^{b}_{a}\int^{d}_{c}f(x,y)\cdot dy\;dx$$
También se cumple que $\sum_x\sum_yf(x,y)=1$ y $\iint f(x,y)=1$ 

Además, se va a definir la CDF como: 

- **Caso discreto**: 

$$F(x,y)=P(X\leq x, Y\leq y)=\sum_{X\leq x}\sum_{Y\leq y} f(x,y)$$
- **Caso continuo**: Análogo 

>[!example] Independencia en la distribución conjunta 
>
>Si para dos variables aleatorias $(X,Y)$ la pdf conjunta es $f(x,y)=f_X(x)\cdot f_Y(y)$, entonces $X$ e $Y$ son *estadísticamente independientes*. Las CDF también siguen el mismo principio: 
>
>$$F(x,y)=F_X(x)\cdot F_Y(y)$$



