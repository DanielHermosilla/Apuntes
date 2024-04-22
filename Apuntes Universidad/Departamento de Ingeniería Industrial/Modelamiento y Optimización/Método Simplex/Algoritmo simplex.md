
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

Un ejemplo aplicado de esto es volver a pararnos en el punto $(2,0,2)$. Para movernos, hay que analizar las variables no básicas. Nos podemos mover hacia $\lbrace x_2, x_4, x_6\rbrace$. Por lo tanto, en caso de movernos en $x_6$ entonces el vector tentativo quedaría de la forma:

$$d_{x_6}=\begin{pmatrix}
\vdots \\
\vdots \\
\vdots \\
\vdots \\
\vdots \\
1 \\
\vdots
\end{pmatrix}$$

Ahora, habría que resolver el sistema de ecuaciones donde $B$ corresponde a los coeficientes de las **variables básicas** y $A_j$ el de las variables **no básicas**. 

## Determinar cuanto poder moverse 

Para determinar cuanto podemos movernos, lo determinará el valor del escalar $\theta$. 

Así, bajo a misma fórmula anterior, se tiene lo siguiente: 

$$x+\theta d\geq 0$$

Para determinar el valor de $\theta$, hay que analizar para que valor de $\theta$ una variable básica factible se vuelve cero. Por ejemplo: 

$$\begin{pmatrix}
2 \\
0 \\
2 \\
0 \\
4 \\
0 \\
1
\end{pmatrix}+\theta\begin{pmatrix}
0 \\
0 \\
-1 \\
1 \\
1 \\
0 \\
1
\end{pmatrix}\geq 0$$

Donde $\theta$ se tiene que desplazar en dos espacios, pues en ese valor el vector de dirección hace que se vuelva $0$ una otra variable. 

## Método Simplex 

Por lo tanto, podemos decir que el método [[Simplex]] se mueve a una solución básica factible adjacente mejor que la actual: 

$$\begin{align}
\theta^* c^Td^j&=\theta^*(c_{B}^{T},c_{N}^{T})(-B^{-1}A_j, \dots 1\dots)\\  \\
&=\theta^*(c_j-c_{B}^{T}B^{-1}A_j)\\  \\
&=\theta^*\bar{c_j}
\end{align}$$

Donde $\bar{c_j}$ es el costo reducido de la variable $j$. 

De forma generalizada, se hace de la siguiente forma: 

1. Inicializar: sea $x=\left(x_B, x_N\right)=\left(A_B^{-1} b, 0\right)$ SBF con base $B$

2. Calcule costos reducidos $\overline{\mathrm{c}_{\mathrm{j}}}$ para todo $\mathrm{j} \in \mathrm{N}$
- . Si $\overline{c_j} \geq 0$ para todo $\mathrm{j} \rightarrow \mathrm{x}$ es optimo. STOP
-  Si no, escoja $j$ con $\overline{c_j}<0$

2. Calcule $d^j=\left(-B^{-1} A_j, \ldots 1 \ldots\right)$
- . Si $d^j \geq 0 \rightarrow$ problema es no acotado. STOP

3. Calcule $\theta^*=\min _i\left\{\left.\frac{\left(x_B\right)_i}{\left(B^{-1} A_j\right)_i} \right\rvert\,\left(B^{-1} A_j\right)_i>0\right\}=\frac{\left(x_B\right)_l}{\left(B^{-1} A_j\right)_l}$

4. Nueva SBF: $\mathrm{x} \leftarrow \mathrm{x}+\theta^* \mathrm{~d}^{\mathrm{j}}$ con base $\mathrm{B} \leftarrow \mathrm{B} \cup\left\{x_j\right\} \backslash\left\{x_l\right\}$

5. Volver a 1

#### Ejemplo: 

![[Pasted image 20240415113005.png|center|800]] 

Tenemos la SBF que corresponde al punto $(2,0,2,0,4,0,1)$ y donde la base $B$ de soluciones factibles está definida como: 

$$B=\begin{pmatrix}
1 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 1
\end{pmatrix}$$

Por lo tanto, hay que calcular los costos de moverse por $C_{x_2}, C_{x_4}, C_{x_6}$. 

Notar que la función objetivo llegaría a ser: 

$$c=(0,-1,-3,0,0,0,0)$$

Por lo tanto, aplicando la fórmula del costo: 

$$\bar{c_j}=c_j-c_{B}^{-1}B^{-1}A_j$$

Para probar moverse en $c_{x_2}$ tendríamos que $c_{x_2}=-1$ y $c_B=(0,-3,0,0)$. Por lo tanto: 

$$\begin{align}
\bar{c_{x_2}}&=-1-(0,-3,0,0)\begin{pmatrix}
0 \\
1 \\
2 \\
-1
\end{pmatrix}\\ \\  \\
&=-2 
\end{align}$$

## Encontrar la solución básica factible inicial 

Notar que al hacer el algoritmo, se sabía *a priori* que vértice era solución básica factible. Sin embargo, es necesario saber como llegar a una SBF. 

Antes que nada, es necesario dejar el problema en forma estándar, donde: 

$$\begin{align}
u^*&=\min e^Ty\\  \\
Ax+y&=b\\  \\
x,y&\geq 0
\end{align}$$

Donde $y$ son variables de holgura. Notemos que el problema **debe ser de minimizar**. 

Notemos, antes que nada, la siguiente propiedad: 

- Si $u^*>0$ el problema es infactible. 

Para demostrarlo, supongamos que $\min c^Tx$ es una solución básica factible, donde se tienen $m$ variables básicas y $n-m$ variables no básicas. Por lo tanto, bajo esta suposición, $\exists\hat{x}\;\text{SBF}$. Por lo tanto, si denominamos como $(P)$ a la función objetivo, entonces: 

- $P$ tiene $n+m$ variables y $m$ restricciones $\implies$ $m$ variables básicas y $n$ variables no básicas. 

Así, $(\hat{x},0)$ es solución básica factible, que puede ser descrito también como: 

$$(\hat{x},0)=(\hat{x_B},\hat{x_{NB},0})$$

Pero, notemos que la solución se tiene con $y=0$, haciendo que $\min e^Ty=0$. Por lo tanto, como $y$ debe ser $0$, entonces no es posible que el problema a minimizar tenga como valor números positivos.