
Sean $X$ e $Y$ dos [[Variable aleatoria continua|variables aleatorias]], se define la covarianza como: 

$$\text{Cov}(X,Y)=E[(X-E[X])\cdot (Y-E[Y])]$$ 
La covarianza está asociada a una asociación lineal de las variables. Sería equivalente a la relación lineal entre dos variables aleatorias. 

Si se desarrolla la expresión: 

$$=E[(X-E[X])\cdot (Y-E[Y])]$$ $$=E[XY-XE[Y]-E[X]\cdot Y+E[X]E[Y]]$$ $$=E[XY]-E[XE[Y]]-E[E[X]\cdot Y]+E[E[X]E[Y]]$$ $$=E[XY]-E[X]E[Y]-E[X]E[Y]+E[X]E[Y]$$
$$=E[XY]-E[X]E[Y]$$ 
## Propiedades 

1. La covarianza es conmutativa: 
$$\text{Cov}(X,Y)=\text{Cov}(Y,X)$$ 
2. Linealidad en la multiplicación 

$$\text{Cov}(aX,Y)=a\cdot\text{Cov}(X,Y)$$ 
3. Covarianza en la suma: 

$$\text{Cov}(X+c,Y)=\text{Cov}(X,Y)$$ 
4. Covarianza de sumas de variables aleatorias: 

$$\text{Cov}(X+Y,Z)=\text{Cov}(X,Z)+\text{Cov}(Y,Z)$$ 
5. Covarianza de sumas ponderadas: 

$$\text{Cov}(\sum_{i=1}^{m}a_iX_i,\sum_{j=1}^{n}b_jY_j)=\sum_{i=1}^{m}\sum_{j=1}^{n}a_ib_j\text{Cov}(X_i,Y_j)$$ 
### Ejemplo 

Supongamos que tenemos $X$ con [[Distribución Normal]] e $Y$ con [[Distribución Exponencial]]. 

$$\text{Cov}(X,Y)=E[XY]-E[X]E[Y]$$ 
Sabemos que la densidades respectivas: 

- $f_X(x)=\mathbb{1}_{x\in\lbrace 1,2\rbrace}$ 
- $f_{y\vert x}(y\vert x)$ 

Entonces, para calcular la [[Esperanza de función de Múltiples Variables Aleatorias]], se hace lo siguiente:

$$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xyf_{x y}(x,y)dxdy$$

Por [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Diferenciabilidad/Regla de la cadena|regla de la cadena]] se tiene lo siguiente: 

$$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}xyf_{Y\vert X}(y\vert x)f_x(x)dxdy$$ 
Por lo tanto, ahora se puede integrar: 

$$\int_{0}^{\infty}\int_{1}^{2}x\cdot y\cdot x\cdot e^{-yx}\mathbb{1}_{\lbrace x\in(1,2)\rbrace} dxdy$$ 
Por fubini: 

$$=\int_{1}^{2}x\int_{0}^{\infty}xy\cdot e^{-yx}$$ $$=1$$ 
La [[Esperanza|esperanza]] de $X$ es conocida, pero para la esperanza de $Y$ se necesita la [[PDF marginal]], entonces: 

$$\int_{0}^{\infty}\int_{1}^{2}xe^{-yx}\cdot\mathbb{1}_{\lbrace (1,2)\rbrace}dxdy$$ 
$$\int_{1}^{2}\frac{1}{x}dx$$ $$=ln(2)$$ 
Por lo tanto, la covarianza, llegaría a ser: 

$$\text{Cov}(X,Y)=1-\frac{3}{2}\ln(2)$$ 