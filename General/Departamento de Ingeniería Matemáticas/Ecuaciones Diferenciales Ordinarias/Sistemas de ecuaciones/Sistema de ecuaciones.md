
Normalmente cuando se tiene un sistema de ecuaciones lineal se puede escribir en función de una [[matriz]]. Aún así, se podría describir una EDO en función de matrices, donde: 

$$X' = A(t)X + B$$ 
Donde: 

$$X=\begin{bmatrix}x_1(t)\\x_2(t)\\\vdots\\\vdots\\x_n(t)\end{bmatrix}\in\mathbb{R}^n = \text{Vector de estado}$$ 
$$A\begin{bmatrix}a_{ij}\end{bmatrix}=\text{Matriz de la dinámica del sistema}$$ 
$$B =\begin{bmatrix}f_{1}(t)\\f_2(t)\\\vdots\\\vdots\\f_n(t)\end{bmatrix}=\text{Forzante}$$ 
Sabemos que una EDO de orden n lineal se puede reescribir en un sistema: 

$$y^n + \bar{a_{n+1}}(x)y^{(n-1)}+\dots+\bar{a_1}(x)y'+\bar{a_0}y=\bar{Q}$$ 
Donde: 

$$X=\begin{bmatrix}y\\y'\\\vdots\\\vdots\\y^{(n+1)}\end{bmatrix}\in\mathbb{R}^n$$
$$X' = \begin{bmatrix}0 & 1 & 0 &\dots & 0 \\0&0&1&\dots&0\\\vdots&\vdots&\vdots&\vdots&\vdots\\0&0&0&\dots&1\\-\bar{a_{0}}&-\bar{a_1}&-\bar{a_2}&\dots&-\bar{a_{n-1}}\end{bmatrix}X + \begin{bmatrix}0\\0\\0\\0\\\bar{Q(t)}\end{bmatrix}$$ 
Con $\bar{Q(t)}$ siendo la EDO. 

# Sistema homogéneo 

Sistema de la forma: 

$$X' = A(t)X$$ 
En el caso de coeficientes constantes: 

$$X'=AX$$ 
Para resolver aquellos sistemas se ocupa la [[matriz diagonalizable|diagonalización]], donde $A\in\mathbb{R}^{n\times n}$

$$Ax=PDP_{x}^{-1}x$$ 
Donde $D$ consiste en los [[valores y vectores propios|valores propios]] y $P$ los [[vector propio|vectores propios]]. Entonces, se define $e^{At}$, donde: 

$$e^{At}=P\begin{bmatrix}e^{\lambda_1t}&0&0&\dots&0\\0&e^{\lambda_2t}&0&0&0\\\vdots&\vdots&\vdots&\vdots&\vdots\\0&0&0&0&e^{\lambda_5t}\end{bmatrix}P^{-1}$$ 
Por ejemplo, si $t=0$ se llega que cumple la condición: 

$$e^0 = P\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}P^{-1} = PIP = I$$

Esto también cumple con las derivadas, es decir, con $Ae^{At}$. 