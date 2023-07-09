
Ante un [[Problema de Cauchy de Sistema Lineales]], con $B=0$ homogéneo y $X_0$ [[vectores]] de la [[Base|base canónica]] $\mathbb{R}^n$. Se define lo siguiente: 

$$\begin{cases}\phi_1'=A(t)\phi_1\\\\\phi_1(t_0)=e_1\end{cases}\;\;e_1=\begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix}$$ 
Se podría tener también 

$$\begin{cases}\phi_2'=A(t)\phi_2\\\\\phi_1(t_0)=e_2\end{cases}\;\;e_2=\begin{pmatrix}0\\1\\\vdots\\0\end{pmatrix}$$
$$\begin{cases}\phi_n'=A(t)\phi_n\\\\\phi_n(t_0)=e_n\end{cases}\;\;e_n=\begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix}$$

Y, por último, se llega a la siguiente matriz: 

$$\phi=\begin{bmatrix}\bigg\vert&\bigg\vert&\dots&\bigg\vert\\
\phi_1&\phi_2&\dots&\phi_n\\
\bigg\vert&\bigg\vert&\dots&\bigg\vert\end{bmatrix}$$ 
Esto se llama la matriz fundamental. 

# Propiedades 

1. Para $t_0=0$, es decir, evaluado en el momento inicial se tiene la identidad: 

$$\phi(t_0,t_0)=\begin{bmatrix}\bigg\vert&\bigg\vert&\dots&\bigg\vert\\
\phi_1&\phi_2&\dots&\phi_n\\
\bigg\vert&\bigg\vert&\dots&\bigg\vert\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix} = I$$ 
2. La derivada es la siguiente: 


$$\phi'(t_0,t_0)=\begin{bmatrix}\bigg\vert&\bigg\vert&\dots&\bigg\vert\\
\phi_1'&\phi_2'&\dots&\phi_n'\\
\bigg\vert&\bigg\vert&\dots&\bigg\vert\end{bmatrix}=\begin{bmatrix}\bigg\vert&\bigg\vert&\dots&\bigg\vert\\
A(t)\phi_1&A(t)\phi_2&\dots&A(t)\phi_n\\
\bigg\vert&\bigg\vert&\dots&\bigg\vert\end{bmatrix}= A(t)\phi$$

El [[Problema de Cauchy de Sistema Lineales]] llegaría a ser: 

$$PC=\begin{cases}\phi'=A(t)\phi\\\\\phi(t_0)=I\end{cases}$$ 
Por [[Teoría de Existencia y Unicidad|TEU]] se concluye que $\exists!\phi\in C^1(I)^{n\times n}$.

# Solución homogénea 

Se plantea lo siguiente: $X=\phi(t,t_0)X_0$ donde reemplazando por $X'=A(t)X,\;X(t_0)=X_0$ se llega que: 

$$X_h'=\phi'(t,t_0)X_0 = A(t)\phi(t,t_0)X_0=A(t)X_h$$ 
Donde $X_h(t_0)=\phi(t_0,t_0)X_0 = X_0$ 

# Solución particular 

Donde $B\neq 0$ se busca de la siguiente forma: 

$$X_p = \phi(t,t_0)C(t)$$  
Reemplazando en la ecuación no homogénea: 

$$X_p'=A(t)X_p + B(t)$$ 
$$\phi'(t,t_0)C+\phi(t,t_0)C'(t)=A(t)\phi(t,t_0)C + B(t)$$ $$\iff\phi(t,t_0)C'(t)=B(t)$$ $$\implies X_p=\phi(t,t_0)\int_{t_0}^{t}\phi^{-1}(s,t_0)B(s)ds$$ 
# Solución general 

Por lo tanto, la solución general está determinado por: 

$$X(t)=\phi(t,t_0)X_0 + \int^{t}_{t_0}\phi(t,t_0)\phi^{-1}(s,t_0)B(s)ds$$ 
Notemos que el [[Matriz Wronskiana|wronskiano]] es equivalente al [[determinante]] de $\phi$. Además, $\phi$ es invertible.  

## Ejemplo 

Se tiene la siguiente ecuación lineal: 

$$\theta_1^{''} + \theta_{1}^{'} + \theta_1 + k(\theta_1-\theta_2)=f_1$$ $$\theta_2'' + \theta_2' + \theta_2 -k(\theta_1 - \theta_2)=f_2$$
Definimos las variables de estado como: 

$$X=\begin{bmatrix}\theta_1\\\theta_2\\\theta_{1}'\\\theta_2'\end{bmatrix}$$ 
Por lo tanto, se define la siguiente matriz: 

$$PC=\begin{cases}\begin{bmatrix}\theta_1'\\\theta_2'\\\theta_1''\\\theta_2''\end{bmatrix}=\begin{bmatrix}0&0&1&0\\0&0&0&1\\-(1+k)&k&-1&0\\k&-(1+k)&0&-1\end{bmatrix}\begin{bmatrix}\theta_1\\\theta_2\\\theta_1'\\\theta_2'\end{bmatrix}+\begin{bmatrix}0\\0\\f_1\\f_2\end{bmatrix}\\\\\begin{bmatrix}\theta_1\\\theta_2\\\theta_1'\\\theta_2'\end{bmatrix}=\begin{bmatrix}\text{Ángulo inicial}\;1\\\text{Ángulo inicial}\;2\\\text{Velocidad inicial}\;1\\\text{Velocidad inicial}\;2\end{bmatrix}\end{cases}$$ 

Entonces, para construir $\phi$ se va a usar las condiciones iniciales como base canónica. 

