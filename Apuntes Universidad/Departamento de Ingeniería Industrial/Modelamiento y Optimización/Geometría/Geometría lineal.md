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

Como se quiere llegar a la formulación estándar: 

$$\begin{align}
\min c^Tx&\\ \\
Ax&=b\\  \\
x&\geq 0
\end{align}$$

Para poder llegar a la igualdad, se agrega una *variable de holgura*. En ese sentido, me defino $s\geq0$ y las ecuaciones llegarían a ser: 

$$\begin{align}
3x+7y-2x&=4\\  \\
x-y+z+s&=2\\  \\
x\geq0\;\land\;s\geq 0
\end{align}$$

O, por el otro lado, se pueden definir lo siguiente: 

$$\begin{align}
y&=y^+-y^-\;\;\;\;\;\;\;\;y^+, y^-\geq 0\\  \\
\vdots&=\vdots\\  \\
x&=x^+-x^-
\end{align}$$

Por lo tanto, 

$$\begin{align}
3x+7y^+-7y^--2z^++2z^-&=4\\  \\
x-y^++y^-+z^+-z^-+s&=2
\end{align}$$

Con todas las variables mayores o iguales a cero. En este caso, la matriz $A$ cambia a lo siguiente: 

$$\begin{pmatrix}
3 & 7 & -7 & -2 & 2 & 0 \\
1 & -1 & 1 & 1 & -1 & 1
\end{pmatrix}$$

## Definiciones 

Dado una función objetivo: 

$$\min c^Tx. Ax\geq b$$

- $x$ es **solución factible** si $Ax\geq b$. 

- $x$ es **solución óptima** si es factible y $c^Tx\leq c^Ty$ para todo y solución factible: 

- $P=\lbrace x\;\vert\; Ax\geq b\rbrace$ es la **región factible**. 

- **Hiperplano**: $\lbrace x\;\vert\; a^Tx=b\rbrace$

- **Semiespacio**: $\lbrace x\;\vert\;a^Tx\geq b\rbrace$

- **Polihedro**: Intersección finita de semiespacios: 

$$P=\lbrace x\;\vert\; Ax\geq b\rbrace = \bigcap_{i=\lbrace 1,\dots m\rbrace}\lbrace x\;\vert\;a^{T}_{i}x\geq b_i\rbrace$$ 
- $C$ es **conjunto acotado** si existe $K$ tal que $\vert x_i\vert\leq K$ para todo $x\in C$, todo $i$. (Básicamente, si existe una [[Norma en varias variables|norma]]) 

- **Politopo** es un polihedro acotado.

![[IMG_C8C1FF3E5564-1.jpeg|center|600]] 

- $C$ es un **conjunto conveso** si para todo $x,y \in C$ y $\lambda\in [0,1]$, se tiene que: 

$$\lambda x + (1-\lambda)y\;\;\in C$$

Básicamente, si no es posible formar dos puntos dentro de un conjunto tal que al formar una línea no sale del conjunto. En el mundo entero, siempre se tiene que son problemas no convexos. 

- Dado $x^1, \dots, x^k$ y $\lambda_1, \dots,\lambda_k\geq 0$ tal que $\sum^{k}_{i=1}\lambda_i=1$, la **combinación convexa** de $x^1,\dots x^k$ es $y=\sum^{k}_{i=1}\lambda_ix^i$. 

- Dado conjunto $S$, la **envoltura convexa** de $S$ es: 

$$\text{Conv}(S)=\text{ch}(S)=\left\lbrace\sum^{k}_{i=1}\lambda_i x^i\;\vert\; x^1,\dots,x^k\;\in S,\sum^{K}_{i=1}\lambda_i=1,\lambda_1,\dots,\lambda_k\geq 0\right\rbrace$$


