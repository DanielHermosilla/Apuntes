Sabemos que un problema de optimización lineal es de la forma: 
$$
\begin{aligned}
& \min (o \max ) c^T x \\\\
& \text { s.a. } a_i^T x \leq b_i \quad i \in M_1 \\\\
& a_i^T x \geq b_i \quad i \in M_2 \\\\
& a_i^T x=b_i \quad i \in M_3 \\\\
&
\end{aligned}
$$

Donde se dice que se tiene un vector $x$ de $n$ variables con $\vert M_1\vert+ \vert M_2\vert + \vert M_3\vert=m$ restricciones. 

Una solución gráfica se vería de la siguiente forma: 

![[Pasted image 20240401102224.png|center|900]]


Por lo tanto, nos definimos la curva de nivel $\alpha$ como: 

$$\lbrace x\;\vert\; f(x)=\alpha\rbrace$$

Esto sale que cualquier problema se puede escribir como $\min c^Tx\;:\;Ax\geq b, x\geq 0$. Por lo tanto, $c^Tx=\alpha$, donde la curva de nivel es perpendicular a $c$. 

La curva de nivel en $\mathbb{R}^2$ sería una recta, en $\mathbb{R}^3$ es una cara, y así sucesivamente. 

### Ejemplo 

$$\begin{align}
3x+7y-2x&=4\\  \\
x-y+z&\geq 2\\  \\
-x+y-z&\geq -2\\  \\
x&\geq 0
\end{align}$$

Esto es lo mismo a escribir: 

$$\begin{pmatrix}
3 & 7 & -2 \\
-3 & -7 & 2 \\
-1 & 1 & -1 \\
1 & 0 & 0
\end{pmatrix}\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}\geq\begin{pmatrix}
4 \\
-4 \\
-2 \\
0
\end{pmatrix}$$

