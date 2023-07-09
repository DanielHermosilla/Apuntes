
Sea $A\subset\mathbb{R}^n$ y $B\subset\mathbb{R}^m$ [[Conjuntos abiertos y cerrados|conjuntos abiertos]]. Definimos $f:A\rightarrow\mathbb{R}^m$ y consideramos $g:B\rightarrow\mathbb{R}^k$. Consideremos $x_0\in A$ tal que $f(x_0)\in B$. Si $f$ es diferenciable en $x_0$ y $g$ es [[Diferenciabilidad|diferenciable]] en $f(x_0)$ entonces $g\; o\; f$ es diferenciable en $x_0$ y se verifica: 

$$ D(g\;o\;f)(x_0) = Dg(f(x_0))\;o\; Df(x_0)$$

Como estamos trabajando con funciones, en vez de multiplicar con [[escalares]], estamos haciendo la composición. Esto hará más sentido [[matriz|matricialmente]] ya que la composición de [[matriz|matrices]] es la multiplicación de matrices. 

### Ejemplo 

Note que una función $f:\mathbb{R}^2\rightarrow\mathbb{R}^2$ dada por $f(x,y)=(e^x + \sin(xy), x + 3y)$ es [[Diferenciabilidad|diferenciable]] ya que está compuesta por funciones con componentes: 

$$f_1(x,y) = e^x + \sin(xy)$$ $$f_2(x,y) = x + 3y$$ 
Ambas [[Diferenciabilidad|diferenciables]]. 

Entonces, se va a aplicar la [[matriz representante]] para poder trabajar con composición de funciones.  

## Teorema 

Sea $f: A\subset\mathbb{R}^d\rightarrow\mathbb{R}^p$ y $g:\mathbb{R}^p\rightarrow\mathbb{R}^q$ con $f$ diferenciable en $x_0$ y $g$ diferenciable en $f(x_0)$. Sea $F = g\;o\;f:\;A\rightarrow\mathbb{R}^q$  diferenciable en $x_0$. Entonces para $l\in\lbrace 1, \dots, q\rbrace$ y $m\in\lbrace 1,\dots,d\rbrace$ tenemos: 

$$\frac{\partial F_l}{\partial x_m}(x_0) = \sum^{p}_{k = 1}\frac{\partial g_l}{\partial y_k}f(x_0)\frac{\partial f_k}{\partial x_m} (x_0)\;\;\text{(Producto matricial)} $$ 
Donde escribimos $g = g(y_1, \dots, y_p)$ con $y_k$ las variables de $g$. Basicamente se está definiendo la [[Diferenciabilidad|derivada]] de una función como el [[matriz|producto matricial]].

### ejemplo 

Sean $f:\mathbb{R}^2\rightarrow\mathbb{R}^3$ y $g:\mathbb{R}^3\rightarrow\mathbb{R}^2$ dadas por: 

$$ f(x,y) = (x^2, xy^2, x-y) $$ $$ g(u,v,w) = (w^2, u +1) $$ 
Tenemos que: 

$$f'(x,y) = \begin{equation}
		\begin{bmatrix}
			2x & 0 \\ 
			y^2 & 2xy\\ 
			1 & -1
		\end{bmatrix}_{3\times 2}
\end{equation} $$ 
Análogamente: 

$$ g'(u,v,w) = \begin{equation}
		\begin{bmatrix}
			0 & 0 & 2w\\ 
			1 & 0 & 0
		\end{bmatrix}_{2\times 3}
\end{equation} $$ 
Luego, $(g\;o\;f)(x,y) = g'(f(x,y)) * f'(x,y)$ 

Notar que $f'(x,y) = (x^2, xy^2, x-y)$. Entonces: 

$$ (g\;o\;f)(x,y) = \begin{equation}
		\begin{bmatrix}
			0 & 0 & 2(x-y)\\ 
			1 & 0 & 0
		\end{bmatrix}_{2\times 3}
\times
		\begin{bmatrix}
			2x & 0 \\ 
			y^2 & 2xy\\ 
			1 & -1
		\end{bmatrix}_{3\times 2}
\end{equation} = \begin{bmatrix}
			2(x-y) & -2(x-y) \\ 
			2x & 0
		\end{bmatrix}_{2\times 2} $$

## Ejemplo 

Sea $z = f(u,v)$ una función tal que $f$ y sus [[Derivadas parciales|derivadas parciales]] de primer orden son [[Continuidad en varias variables|continuas]]. Ahora, sea $u(x,y) = x^3 - y^3\;;\;v(x,y) = \frac{2y}{x}$ y $\frac{\partial z}{\partial u} (0,2) = 1\;;\;\frac{\partial z}{\partial v}(0,2) = -1$.

**Calcular $\frac{\partial z}{\partial x} (1,1)$.**  

Note que cuando $(1,1) = (x,y)$ entonces $u(1,1) = 0\;\land\;v(1,1)=2$. 

Tengo el siguiente esquema: 

![[Captura de Pantalla 2022-12-27 a la(s) 13.10.41.png|center]]

Equivalente a decir:

$$\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u} \times\frac{\partial u}{\partial x} +\frac{\partial z}{\partial v} \times\frac{\partial v}{\partial x} $$ 
Luego, 

$$\frac{\partial z}{\partial x}(1,1) = \frac{\partial z}{\partial u} (0,2)\times\frac{\partial u}{\partial x}(1,1) + \frac{\partial z}{\partial v} (0,2)\times\frac{\partial v}{\partial x}(1,1) $$ 
$$\implies (1)(3) + (-1)(-2) = 5$$ 