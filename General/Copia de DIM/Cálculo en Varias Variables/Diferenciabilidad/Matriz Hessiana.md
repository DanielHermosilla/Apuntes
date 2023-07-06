
Supongamos que $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ donde $f$ es dos veces [[Diferenciabilidad|diferenciable]] en $x_0\in A$ con $A$ [[Conjuntos abiertos y cerrados|abierto]]. Definimos su [[matriz]] Hessiana en $x_0$, denotada por $f''(x_0)$. como la matriz de segundas [[Derivadas parciales|derivadas parciales]] de $f$ en $x_0$, de tamaño $n\times n$ dada como: 


$$ f''(x_0)=\begin{equation}
		\begin{bmatrix}
			\frac{\partial^2 f}{\partial x_{1}^2} & \frac{\partial^2 f}{\partial x_{1}\partial x_2} & \frac{\partial^2 f}{\partial x_{1}\partial x_3} &\dots&\frac{\partial f}{\partial x_1 \partial x_n}\\ 
			\frac{\partial^2 f}{\partial x_{2}\partial x_1} & \frac{\partial^2 f}{\partial x_{2}^2} & \frac{\partial^2 f}{\partial x_{2} \partial x_3} &\dots&\frac{\partial f}{\partial x_2 \partial x_n} \\
			\vdots&\vdots&\vdots&\vdots&\vdots\\ 
			\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \frac{\partial^2 f}{\partial x_n \partial x_3} &\dots &\frac{\partial^2 f}{\partial x_{n}^2}
		\end{bmatrix}
\end{equation}
		$$

Gracias al teorema de Schwartz ([[Derivadas de orden superior|la de derivadas de orden superior]]), si $f$ es de clase $C^2(A)$ se sigue que la matriz $f''(x_0)$ es una [[matriz]] simétrica. 

Supongamos que $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ es una función de clase $C^2(A)$ y sea $x_0\in A\;\land\;h\in\mathbb{R}^n$ pequeño.  Entonces el desarrollo de Taylor de orden dos para $f$ en torno a $x_0$ viene dado por: 

$$f(x_0 + h) = f(x_0) + f'(x_0)h + \frac{1}{2}\sum^{n}_{i,j=1}\frac{\partial^2f}{\partial x_i\partial x_j}(x_0 + sh)h_i h_j$$ 
Para cierto $s\in(0,1)$. 

Lo anterior lo podemos escribir como: 

$$f(x_0 + h) = f(x_0) +\nabla f(x_0)\;·\;h+\frac{1}{2}h^Tf''(x_0 + sh)h$$ 
Donde $h^T$ es $h$ traspuesta y $f''(x_0)$ es la [[Matriz Hessiana|matriz Hessiana]]. 