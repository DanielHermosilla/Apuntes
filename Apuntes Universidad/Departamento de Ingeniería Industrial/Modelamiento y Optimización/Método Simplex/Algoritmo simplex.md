
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

