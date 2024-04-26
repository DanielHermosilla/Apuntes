
Dado un problema de optimización de la forma estándar: 

$$\begin{align}
p^*&=\min c^Tx\\  \\
Ax&\geq b\\  \\
x&\geq 0
\end{align}$$

Existe un problema relacionado **con los mismos parámetros**: 

$$\begin{align}
d^*&=\max b^Ty\\  \\
A^Ty&\leq c\\  \\
y&\geq 0
\end{align}$$

El primer problema se llama **primal**, el segundo, **dual**. Notar que las restricciones $b$ del primal es el mismo $b$ de la función objetivo del primal. 

Se siguen ciertas reglas, por ejemplo, si la variable $x_i$ es libre, entonces la restricción $y_i$ irá con una **igualdad**. Si $x_j\geq 0$ entonces $y_j$ ira con un $\leq$ y viceversa. 


