
Sea la siguiente [[matriz]] no diagonalizable: 

$$A=\begin{bmatrix}1&1\\0&1\end{bmatrix}$$ 
Y, además. se tiene el siguiente sistema lineal: 

$$\begin{cases}
x_1'= x_1 + x_2\\\\x_2'=x_2\end{cases}$$ 
Es decir: 

$$\begin{bmatrix}x_1\\x_2\end{bmatrix}'=\begin{bmatrix}1&1\\0&1\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}$$ 
Si se intentara diagonalizar, se calcularían los [[valores y vectores propios|valores propios]], donde se llega que: 

$$\begin{bmatrix}1-\lambda&1\\0&1-\lambda\end{bmatrix}$$ 
Donde el [[polinomio característico]] sería: 

$$p(\lambda) = (1-\lambda)^2\implies\lambda_1=1,\;\;\lambda_2=1$$ 
Por ende, si buscamos los espacios propios: 

$$\begin{bmatrix}0&1\\0&0\end{bmatrix}v=\begin{bmatrix}0\\0\end{bmatrix}$$
$$v_1\in\langle\lbrace\begin{pmatrix}1\\0\end{pmatrix}\rbrace\rangle$$ 

Como solo hay un [[vector propio]], entonces no hay una base de los vectores propios. Entonces, cuando se llegan a estos casos se ocupa la **fórmula de Jordan**. 

Toda matriz se pude reducir (por un [[matriz cambio de base|cambio de base]]) a una forma de Jordan. Es decir, 

$$A\in\mathbb{R}^{n\times n},\;\exists P\;\;\text{invertible tal que}\;\; A=PJP^{-1}$$ 
Donde $J$ es su forma de Jordan. La forma de Jordan es diagonal por bloques, i.e, una matriz que tiene bloques asociados a su diagonal asociados a los [[valores y vectores propios|valores propios]] repetidos. Estos bloques, se van a llamar **bloques de Jordan**. 

Por lo tanto, se obtendría algo del estilo: 

$$J_k=\begin{bmatrix}\lambda_k&1&0&\dots&\dots&\\&\lambda_k&1&0&\dots&\\&&\lambda_k&1&0\\&&&\lambda_k&1\\&&&&\lambda_k\end{bmatrix}$$ 
Por ejemplo: 

$$J_k=\begin{bmatrix}2&0&0&\dots&\dots&\\&2&1&0&\dots&\\&&2&0&0\\&&&-1&1\\&&&&-1\end{bmatrix}$$

Donde $\lambda_1 = 2, m_1=3$ y hay 3 sub-bloques y $\lambda_2=1,m_2=2$ y hay solo un subloque. 

Entonces, la dimension del subespacio propio asociado a cada valor propio va a ser el número de sub-bloques que hay en cada bloque. ([[multiplicidad geométrica|Multiplicidad geométrica]]). 

Si se calculan los vectores propios por de la matriz: 

$$J_k(\lambda_1=2)=\begin{bmatrix}0&0&0&\dots&\dots&\\&0&1&0&\dots&\\&&0&0&0\\&&&-3&1\\&&&&-3\end{bmatrix}$$

Entonces, notemos que vectores propios que nos sirven serían: 

$$v\in\langle\lbrace\begin{pmatrix}1\\0\\0\\0\\0\end{pmatrix},\begin{pmatrix}0\\1\\0\\0\\0\end{pmatrix},\begin{pmatrix}0\\0\\1\\0\\0\end{pmatrix}\rbrace\rangle$$ 
Y para $\lambda_2$ se tiene que: 

$$v_2\in\langle\lbrace\begin{pmatrix}0\\0\\0\\1\\0\end{pmatrix}\rbrace\rangle$$ 
Entonces, 

$$P = \begin{bmatrix}1&0&0&0&\vdots&\vdots\\0&1&0&0&\vdots&\vdots\\0&0&1&0&\vdots&\vdots\\0&0&0&1&\vdots&\vdots\\0&0&0&0&\vdots&\vdots\end{bmatrix}$$ 

Entonces, para llenar la matriz con la columna faltante, se hace lo siguiente: 

$$(A-\lambda_1 I)v = v_1$$ 
Donde $v$ es el último vector que se encontró. Al final se llegaría a la matriz identidad.

