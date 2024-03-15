
Conocido como el *knapsack problem*: existen $n$ ítems: 

- $b_i$: el beneficio de llevar el item $i$

- $w_i$: el peso del ítem $i$

- $W$ es la capacidad de la mochila 

*¿Qué items se deben llevar de forma de maximizar el beneficio sin superar la capacidad de la mochila?* 

### Solución 

Nos definimos la variable **binaria** $x_i$ que representa la acción de escojer $i$ o no. 

$$x_i=\begin{cases}
1&\text{Escogo el item}\;i\\ \\
0&\text{No escogo el item}\; i\end{cases}$$

Además, el beneficio escogido se puede representar como la siguiente sumatoria: 

$$\begin{align}
\sum^{n}_{i=1}b_ix_i&=\sum^{n}_{i=1,\;x_i=1}b_i
\end{align}$$

Y el **peso total escodigo** se puede representar como: 

$$\begin{align}
\sum^{n}_{i=1}w_ix_i
\end{align}$$

Por lo tanto, el problema se puede escribir como: 

$$\begin{align}
\text{Max}\;\sum^{n}_{i=1}b_ix_i&\\  \\
\sum^{n}_{i=1}w_ix_i&\leq W\\  \\
x_i&\in\lbrace 0,1\rbrace,\; i\in\lbrace 1,\dots,n\rbrace\\  \\

\end{align}$$

Notar que en el caso que $x_i\in\mathbb{R}$, la idea es ordenar los ítems por *pedazos*: 

$$\frac{b_1}{w_1}\geq\frac{b_2}{w_2}\geq\dots\geq\frac{b_n}{w_n}$$

De hecho, el problema **con la variable $x_i$ no tiene solución** 