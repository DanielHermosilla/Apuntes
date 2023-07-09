

**Problema**: Resolver el siguiente sistema no homogéneo:

$$X'(t)=\begin{pmatrix}-1&1&1\\0&2&1\\0&0&1\end{pmatrix}X(t) + \begin{pmatrix}0\\e^{2t}\\-e^{2t}\end{pmatrix}$$ 
## Solución homogenea 

Primero, buscando la solución homogénea, sabemos que las soluciones homogéneas son de la forma: 

$$x(t)=e^{\lambda t}V_\lambda$$ 
Por lo tanto, busco los valores característicos y sus vectores propios: 

$$\begin{align}
P(\lambda)&=-\left[1+\lambda\right]\left((2-\lambda)(1-\lambda)\right)\\\\
\lambda_1 &=-1\\
\lambda_2 &=2\\
\lambda_3 &= 1
\end{align}$$ 
Entonces, cuando se hacen los cálculos de los vectores propios, se llegan a los siguientes vectores: 

$$\begin{align}

\lambda_1 &= \begin{pmatrix}1\\0\\0\end{pmatrix}\\\\ \lambda_2&=\begin{pmatrix}3\\1\\0\end{pmatrix}\\\\\lambda_3&=\begin{pmatrix}0\\-1\\0\end{pmatrix}\end{align}$$

Entonces, la **solución homogénea** es la siguiente: 

$$x(t) = A\begin{pmatrix}1\\0\\0\end{pmatrix}e^{-t} + B\begin{pmatrix}3\\1\\0\end{pmatrix}e^{2t} + C\begin{pmatrix}0\\-1\\0\end{pmatrix}e^t$$ 
## Solución particular 


Ahora, dado que se tiene la matriz $\begin{pmatrix}0\\e^{2t}\\-e^{2t}\end{pmatrix}$ como el "*lado derecho*", entonces, se podría deducir por variación de parámetros que la solución será de la forma: 

$$X_p = \begin{pmatrix}a_1\\b_1\\c_1\end{pmatrix} + \begin{pmatrix}a_2\\b_2\\c_2\end{pmatrix}e^{2t}$$  
Entonces, la EDO a resolver sería la siguiente (notar que voy a derivar $X_p$):

$$2e^{2t}\begin{pmatrix}a_2\\b_2\\c_2\end{pmatrix}=\begin{pmatrix}-1&1&1\\0&2&1\\0&0&1\end{pmatrix}\left[\begin{pmatrix}a_1\\b_1\\c_1\end{pmatrix}+\begin{pmatrix}a_2\\b_2\\c_2\end{pmatrix}e^{2t}\right] + e^{2t}\begin{pmatrix}0\\1\\-1\end{pmatrix}$$ 
Aca, entonces, puedo resolver para los valores asociados a $e^{2t}$ primero: 

$$2e^{2t}\begin{pmatrix}a_2\\b_2\\c_2\end{pmatrix}=\begin{pmatrix}-1&1&1\\0&2&1\\0&0&1\end{pmatrix}\begin{pmatrix}a_2\\b_2\\c_2\end{pmatrix}e^{2t} + e^{2t}\begin{pmatrix}0\\1\\-1\end{pmatrix}$$

Simplificando $e^{2t}$: 

$$\begin{align}\begin{pmatrix}2\\1\\3\end{pmatrix}&=\begin{pmatrix}-1&1&1\\0&2&1\\0&0&1\end{pmatrix}\begin{pmatrix}a_2\\b_2\\c_2\end{pmatrix}\\\\a_2 &= 0\\b_2&=-1\\c_2 &=3 \end{align}$$

Ahora, buscando para los valores asociados a ninguna constante: 

$$\begin{align}\begin{pmatrix}0\\0\\0\end{pmatrix}&=\begin{pmatrix}-1&1&1\\0&2&1\\0&0&1\end{pmatrix}\begin{pmatrix}a_1\\b_1\\c_1\end{pmatrix}\\\\a_1 &= 0\\b_2 &= 0\\c_2 &=0\end{align}$$ 
Entonces, la solución particular es: 

$$X_p = \begin{pmatrix}0\\-1\\3\end{pmatrix}e^{2t}$$ 
La suma de ambas soluciones sería: 

$$X_t = A\begin{pmatrix}1\\0\\0\end{pmatrix}e^{-t} + \begin{pmatrix}3B\\B-1\\3\end{pmatrix}e^{2t} + C\begin{pmatrix}0\\-1\\0\end{pmatrix}e^t$$ 






