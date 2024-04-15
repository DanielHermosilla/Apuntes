
Para poder definir el algoritmo simplex, es necesario primero formular el problema con solución estándar. Para poder hacer esto, es necesario plantear el problema en forma estándar. 

Primero, se esbozará con un ejemplo: 

![[Pasted image 20240415102342.png|center|800]] 

Para el punto $(2,0,2)$ se tiene lo siguiente vector de puntos, donde $\lbrace x_4, x_5, x_6\rbrace$ son variables de holgura: 

$$(2,0,2,0,4,0,1)$$
Así, las variables **no básicas** (las que se vuelven cero en el punto) llegarían a ser $\lbrace x_2, x_4, x_6\rbrace$. 

Ahora, notemos que **la dirección de movimiento hacia un vértice** lo determina el siguiente vector: 

$$d^j=(-B^{-1}A_j, 010)$$

Donde los "1" corresponden a la posición $j$-ésima. Es decir, el $1$ llegaría a ser aquellos valores no básicos que "dejan" de ser básicos al trasladarse. Esto se deduce de lo siguiente: 

$$A(x+\theta d)=b$$

Como $Ax$ es solución básica factible, entonces esta se cancela con $b$: 

$$\begin{align}
Ax+\theta Ad&=b\\  \\
Ad&=0\\  \\
[BN]\begin{pmatrix}
d_b \\
\vdots \\
1 \\
0
\end{pmatrix}&=0
\end{align}$$

Esto, hace que quede algo de la forma: 

$$\begin{align}
Bd_B+A_j&=0\\  \\
d_b&=-B^{-1}A_j
\end{align}$$

Por ejemplo, en este caso, para desplazarnos al punto de abajo de $(2,0,2)$ se tiene lo siguiente: 

$$d_B=-B^{-1}A_j=\begin{pmatrix}
1 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 1
\end{pmatrix}^{-1}\begin{pmatrix}
1 \\
0 \\
0 \\
0
\end{pmatrix}$$

Donde $B$ representa las columnas $\lbrace x_1, x_3, x_5, x_7\rbrace$, vale decir, **las soluciones básicas factibles** (el complemento de las no básicas factibles). 

Un ejemplo aplicado de esto es volver a pararnos en el punto $(2,0,2)$. Para movernos, hay que analizar las variables no básicas. 