
El control 1 consiste principalmente en [[Topología|topología]], [[Continuidad en varias variables|funciones continuas]] y [[Coercividad|coercividad]]. 

## [[Topología]]

### [[Norma en varias variables|Normas]]

Son formas de medir [[Distancia|distancias]]. Existen varios tipos de normas, pero cada uno deben cumplir las siguientes propiedades: 

1) $||x|| > 0 \; \forall x\in E$

2) $||x|| = 0\iff x = \vec{0} \; \forall x \in E$

3) $||\alpha x|| = |\alpha| \;||x||\;\forall x\in E, \forall\alpha\in\mathbb{K}$ 

4) $||x + y|| \leq ||x|| + ||y|| \; \forall x,y\in E \;\;\enspace\enspace\text{(desigualdad triangular)}$

La propiedad más dificil de demostrar es la desigualdad triangular, que se demuestra muchas veces con desigualdades conocidas, como la de [[Desigualdad de Cauchy-Schwartz|Cauchy-Schwartz]] o [[desigualdad de Young]]. 

### [[Bolas]]

Se definen de la siguiente forma $B(x,r)$ donde $x$ es su centro y $r$ es su radio. 

#### Bola abierta

Se define una bola abierta centrada en $x_0$ y de radio $r$ de la siguiente forma: 

$$ B(x_0,r) = \lbrace x\in\mathbb{R}^n||x-x_0||<r\rbrace $$ $$\iff ||x_0 - x|| < r$$ 
#### Bola cerrada

Se define una bola cerrada centrada en $x_0$ y de radio $r$ de la siguiente forma: 
$$ \bar{B}(x_0,r) = \lbrace x\in\mathbb{R}^n||x-x_0||\leq r\rbrace $$$$\iff ||x_0 - x|| \leq r$$ 
### Conjuntos 

El lugar donde van a vivir los elementos en $\mathbb{R}^d$, normalmente siendo [[vectores]]. 

#### [[Conjuntos abiertos y cerrados|conjunto abierto]]

Un conjunto se dice abierto si para cualquier $x\in A$ existe un $r>0$ tal que la [[Bolas|bola]] abierta $B(x,r)$ está contenida en $A$: 

$$ \forall x\in A\;\;\exists B(x,r) \subset A$$ 
#### [[Conjuntos abiertos y cerrados|conjunto cerrado]]

Un conjunto se dice cerrado **si su complemento es abierto**. De forma equivalente, también podemos establecer que un conjunto es cerrado si está definida como la [[Preimagenes|preimagen]] de una [[Continuidad en varias variables|función continua]] cuyo recorrido es cerrado. Por último, por caracterización de conjuntos cerrados, se puede llegar a lo siguiente: 

$$ A\;\;\text{es cerrado}\;\;\iff\;\;\text{para cualquier sucesión}\;\;(x_n)\subset A\;\;\text{tal que}\;\;x_n\rightarrow x\;\;\text{se tiene que}\;\;x\in A$$

Por último, también se puede probar que un conjunto es cerrado si se cumple lo siguiente: 

$$ A\;\;\text{es cerrado}\;\;\iff\;\; Fr(A)\subset A$$
#### [[Fronteras|frontera]]

Sea $A\subset\mathbb{R}^n$. Se define como **frontera** de A, denotada por $Fr(A)$ a aquellos puntos $x\in\mathbb{R}^n$ que verifican lo siguiente: 

$$ B(x,r)\cap A\neq\emptyset\;\land\;B(x,r)\cap A^c\neq\emptyset$$ 
#### Interior 

Sea $A\subset\mathbb{R}^n$, se define al interior de un conjunto como: 

$$ Int(A) = \lbrace x\in\mathbb{R}^n:\;\exists r>0,\;B(x,r)\subset A\rbrace$$ 
#### [[Punto de adherencia|adherencia]]

Se define a la adherencia como: 

$$Adh(A) = \lbrace x\in\mathbb{R}^n:\;\exists (x_n)_n \in A, x_n\rightarrow x\rbrace$$ 
Equivalentemente se caracteriza por lo siguiente: 

$$ Adh(A) = Fr(A) \cup Int(A) $$ 
#### Punto de acumulación: 

Sea $A\subset\mathbb{R}^n$, decimos que $\bar{x}\in\mathbb{R}^n$ es **punto de acumulación** de $A$ si: 

$$\exists (x_k)_k\subset A,\;\forall k,\;x_k\neq \bar{x},\;\text{tal que}\;x_k\rightarrow\bar{x}$$ 
#### Acotamiento

Se dice que un conjunto es acotado si cumple que existe un $M > 0$ tal que: 

$$\forall k\in\mathbb{N},\;||x_k||\leq M$$

Si se llega a cumplir que un conjunto es **acotado y cerrado** se tiene un **[[Conjuntos compactos|conjunto compacto]]**. 

### [[Sucesiones en varias variables|Sucesiones]]

Se dice que una [[Sucesiones en varias variables|sucesión]] es de [[Sucesión de Cauchy|Cauchy]] si cumple que: 

$$\forall\epsilon > 0\;\exists N_0\in\mathbb{N}\;\text{tal que si}\;n,m\geq N_0\implies ||x_n - x_m||<\epsilon$$ 
Normalmente toda [[Sucesiones en varias variables|sucesión]] que converge en $\mathbb{R}^n$ es de [[Sucesión de Cauchy|Cauchy]]. Por lo tanto, a aquellas [[Sucesión de Cauchy|sucesiones]] se les llamara [[Espacio de Banach|espacio de Banach]]. 


## Funciones 

### [[Continuidad en varias variables|continuidad]] 

Se dice que una función es [[Continuidad en varias variables|continua]] en $x_0$ si $\forall x\in A$: 

$$\forall\epsilon>0,\;\exists\delta>0,\;||x - x_0||\leq\delta\implies||f(x)-f(x_0)||<\epsilon$$ 
O, equivalentemente: 

$$\forall\epsilon >0,\;\exists\delta >0,\;f(B(x_0,\delta)\cap A)\subset B(f(x_0),\epsilon)$$ 
Alternativamente, se puede probar que: 

$$\forall (x_k)\subset A,\;x_k\neq x_0\;\land\;x_k\rightarrow x_0\;\text{se cumple que}\;\lim_{k\rightarrow\infty}f(x_k) = f(x_0)$$

O por otra forma: 

$$f\;\text{continua en}\;C\;\text{abierto}\iff\forall A\;\text{abierto},\;f^{-1}(A)\;\text{es abierto}$$ 
### [[Preimagenes]]

Se define la preimagen de una función de la siguiente forma: 

$$ f^{-1}(C):=\lbrace x\in A\;:\; f(x)\in C\rbrace $$

Por lo tanto, por teorema, si una función $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^p$ es [[Continuidad en varias variables|continua]] en $A$, entonces la preimagen de todo [[Conjuntos abiertos y cerrados|conjunto cerrado]] en $\mathbb{R}^p$  es un [[Conjuntos abiertos y cerrados|conjunto cerrado]] incluido en A. 

## [[Coercividad]] 

Una función $f:\mathbb{R}^n\rightarrow\mathbb{R}$ se dice **[[Coercividad|coerciva]]** si: 

$$\lim_{||x||\rightarrow+\infty} = +\infty$$ 
Y por lo tanto, si una función es [[Coercividad|coerciva]] alcanza su [[Máximos y mínimos de funciones continuas|mínimo global.]]  