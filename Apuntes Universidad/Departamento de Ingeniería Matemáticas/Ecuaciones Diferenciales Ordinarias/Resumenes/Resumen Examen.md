
## Resolución de sistema lineales

Para solucionar un sistema de EDO's , se busca su **matriz fundamental**, que es, básicamente, la matriz que contiene la multiplicación de los vectores propios, con los valores propios en la diagonal y la inversa al final. 

#### Ejemplo 

La siguiente EDO tiene como matriz lo siguiente: 

$$\begin{align}
y'' - 9y &= 0\\\\
\binom{x_1}{x_2}'&=\begin{pmatrix}
0 & 1 \\
9 & 0
\end{pmatrix}\binom{x_1}{x_2}\\\\
e^{At}&=\begin{pmatrix}
1 & 1 \\
-3 & 3
\end{pmatrix}\begin{pmatrix}
e^{-3t} & 0 \\
0 & e^{3t}
\end{pmatrix}\frac{1}{6}\begin{pmatrix}
3 & -1 \\
3 & 1
\end{pmatrix}
\end{align}$$

Tiene las siguientes propiedades: 

1. $e^{A\cdot 0}=0$ 