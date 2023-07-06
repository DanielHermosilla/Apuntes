Sea una [[Funciones escalares|función escalar]], es decir, una función $f:\mathbb{R}^d \rightarrow\mathbb{R}$. Se dice que una función es coerciva si: 

$$\lim_{||x||\rightarrow +\infty} f(x) = +\infty$$

Notemos que si $f$ es coerciva se sigue que para cualquier [[Sucesiones en varias variables|sucesión]] $(x_n)\subset\mathbb{R}^d$ con $||x_n||\rightarrow +\infty$ se tiene que $f(x_n)\rightarrow +\infty$. 

## Teorema 

Sea $f:\mathbb{R}^d\rightarrow\mathbb{R}$ una función [[Continuidad en varias variables|continua]] en $\mathbb{R}^d$ y coerciva. Entonces existe un punto $\bar{x}\in\mathbb{R}^d$ tal que: 

$$f(\bar{x}) \leq f(x)\;\;\forall x\in\mathbb{R}^d$$ 
Es decir, la función $f$ alcanza su [[Máximos y mínimos de funciones continuas|mínimo]] en $\bar{x}\in\mathbb{R}^d$. 