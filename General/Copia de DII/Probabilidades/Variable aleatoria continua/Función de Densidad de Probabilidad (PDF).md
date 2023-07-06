
Para una [[Variable aleatoria continua|variable aleatoria continua]] $X$ con [[Función de Distribución Acumulada|CDF]] $F_X$, su función de densidad de probabilidad es $f_x(·)$ tal que: 

$$F_x(x)=\int_{-\infty}^{x}f_x(x)dx$$ 
O de otra forma: 

$$f_x(x) = \frac{dF_x(x)}{dx}$$ 
En todos los $x\in\mathbb{R}$ donde $F_x(x)$ es diferenciable, es decir, la [[Derivada|derivada]] de la [[Función de Distribución Acumulada|acumulada]]. 

### Propiedades 

- La integral debe ser igual a $1$ entre $-\infty$ y $\infty$. 

- $f_x(x)\geq 0\;\;\forall x\in\mathbb{R}$ 

- $P(x<X\leq x + \Delta)=\int_{x}^{x+\Delta}f_x(x)dx \approx\Delta f_x(x)$ 

- $A\subset\mathbb{R}\;\;\mathbb{P}(X\in A) = \int_{A}f_x(x)dx$ 

- $\mathbb{P}(X=x)=\int_{x}^{x}f_x(x)=0$

