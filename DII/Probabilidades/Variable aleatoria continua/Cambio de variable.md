
Sea $Y=g(X)$ una función de una [[Variable aleatoria continua|variable aleatoria continua]] y se sabe calcular $E[Y]$. 

Si $X$ es una [[Variable aleatoria continua|variable aleatoria continnua]] y $g:\mathbb{R}\rightarrow\mathbb{R}$ es una función estrictamente monótona y derivable, entonces $Y=g(X)$ tiene [[Función de Densidad de Probabilidad (PDF)|densidad]]: 

$$f_y(y) = f_x(g^{-1}(y))·\frac{1}{\bigg\vert g'(g^{-1}(y))\bigg\vert}$$

## Generalización 

El caso cuando el [[Cambio de variable|cambio de variable]] no es monótona y se tiene una partición de intervalo en los reales $\lbrace I_i\rbrace_{i=1}^{N}$ donde $g$ es estricamente monótona y derivable en el interior de cada uno de dichos intervalos. Entonces $Y = g(X)$ tiene densidad: 

$$f_Y(y)=\sum_{i=1}^{N}f_x(g_{i}^{-1}(y))·\bigg\vert\frac{d}{dy}g_{i}^{-1}(y)\bigg\vert$$ 
Donde $g_i(x) = g(x)$ para todo $x\in I_i$. 


### Ejemplo 

Sea $X$ una [[Variable aleatoria continua|variable aleatoria continua]] con una [[Función de Densidad de Probabilidad (PDF)|densidad]]: 

$$f_x(x)=\begin{cases}\frac{1}{2}&\;\text{si}\;x\in[-1,1]\\
0&\;\text{si}\;x\notin[-1,1]\end{cases}$$ 
¿Cuál es la densidad de $Y=5X$? 

Por definición de densidad, se busca la [[Derivada parcial|derivada parcial]] respecto a $y$: 

$$\frac{\partial}{\partial y}F_x(\frac{1}{5})=\frac{1}{5}f_x(\frac{y}{5})$$ 
Por lo tanto, la PDF se puede escribir como: 

$$\frac{1}{5}·\frac{1}{2}\mathbb{1}_{y\in[-5,5]}$$ 
Donde $\mathbb{1}$ es la función indicatriz. 

### Ejemplo 

Si $X$ es una [[Variable aleatoria continua|variable aleatoria continua]] con una [[Función de Densidad de Probabilidad (PDF)|densidad]]: 


$$f_x(x)=\begin{cases}\frac{1}{2}&\;\text{si}\;x\in[-1,1]\\
0&\;\text{si}\;x\notin[-1,1]\end{cases}$$

¿Cúal es la densidad de $Y=X^2$? 

Tenemos que $$\mathbb{P}(X^2\leq Y) = \mathbb{P}(-\sqrt{y}\leq X\leq\sqrt{X})$$ $$\iff\mathbb{P}(x\leq\sqrt{y})-\mathbb{P}(x\leq -\sqrt{y})$$ $$\iff F_x(\sqrt{y})-F_x(-\sqrt{y})$$ 
Ahora se [[Derivada parcial|deriva]] con respecto a $y$: 
 $$\frac{\partial}{\partial y}F_x(\sqrt{y}) = \frac{1}{2}\frac{1}{\sqrt{y}}f_x(\sqrt{y})-f_x(-\sqrt{y})(-1)·\frac{1}{2}\frac{1}{\sqrt{y}}$$


$$=\frac{1}{2\sqrt{y}}[\frac{1}{2}\mathbb{1}_{\sqrt{y}\in[-1,1]} + \frac{1}{2}\mathbb{1}_{-\sqrt{y}\in [-1,1]}]$$ 
Pero, se sabe que $-1\leq -\sqrt{y}\leq 1\implies y\in[0,1]$. Lo mismo cumple para el otro caso. Entonces, se puede simplificar a: 

$$\mathbb{1}_{y\in[0,1]}\frac{1}{2\sqrt{y}}$$ 
Ahora, si se quisiera encontrar la [[Esperanza de una variable continua|esperanza]] de $y$, entonces: 

$$\int_{-\infty}^{\infty}g(x)f_x(x)dx$$ $$=\int_{-\infty}^{\infty}x^2 · \frac{1}{2}\mathbb{1}_{x\in[-1,1]}dx = \frac{1}{2}\int_{-1}^{1}x^2dx = \frac{1}{3}$$  