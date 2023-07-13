
La secuencia de variables aleatorias $X_1, X_2, X_3, \dots$ **converge en distribución** a la [[Variable aleatoria continua|variable aleatoria]] $X$, es decir, $X_n\to X$ si: 

$$\lim_{n\to +\infty}F_{X_n}(x)=F_X(x)$$ 
Para todo $x\in\mathbb{R}$ donde $F_X(x)$ es [[Continuidad|continua]]  

### Ejemplo 

Sea la secuencia de variables aleatorias $X_1,X_2,X_3,\dots$ tal que: 

$$F_{X_n}(x)=\begin{cases}1-\left(1-\frac{1}{n}\right)^{nx}&x>0\\\\
0&x\leq 0\end{cases}$$ 
Demostrar que la sería $X_n$ converge a una [[Distribución Exponencial|distribución exponencial]] de tasa 1. 

Primero notar que: 

$$\begin{align}
\lim_{n\to\infty}F_{X_n}(x)&=F_X(x)\\\\
\lim_{n\to\infty}1-\left(1-\frac{1}{n}\right)^{nx}&=1-\lim_{n\to\infty}\left(1-\frac{1}{n}\right)^{nx}\\\\
&=1-e^{-x}\end{align}$$ 
## Teorema 

Sea la secuencia de [[Variable aleatoria discreta|vriable aleatorias discretas]] $X_1,X_2,X_3,\dots$ no-negativas definidas en los enteros, es decir, 

$$\begin{align} 
R_X\subset\lbrace 0,1,2,\dots\rbrace\\\\
R_{X_n}\subset\lbrace 0,1,2,\dots\rbrace\end{align}$$ 
Para todo $n\in\mathbb{N}$, entonces $X_n\to X$ si y solo si: 

$$\lim_{n\to\infty}p_{x}=p_x(x)$$

Para $x\in\lbrace 0,1,2,3,\dots\rbrace$. 

## Teorema 2 

Si $\lim_{n\to\infty}M_{X_n}(s)=M_X(s)$ para todo $s\in[-c,c]$, entonces $X_n\to X$ 




$$\frac{0.875\cdot(0.875^{300}\cdot e^{-0.875\cdot 360\cdot 300})-300\cdot 0.875}{\sqrt{300}}$$