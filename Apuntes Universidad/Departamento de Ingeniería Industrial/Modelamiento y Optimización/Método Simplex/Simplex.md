
Primero, se escoge una [[Geometría lineal|esquina]], vale decir, una solución básica factible. Si no existe una esquina *mejor*, se queda ahi. 

La formalización es la siguiente: 

- Se tiene un punto $x$ que corresponde a un vértice. Por lo tanto, hacemos [[Producto punto|producto punto]] con la función objetivo con respecto a $(x+\theta d)$ (dirección de la línea respecto a sus vértices adyacentes), y si el producto punto es negativo, entonces el otro vértice es mejor y se *"mueve"* hacia allá. 

### Motivación

Sea el siguiente problema: 

$$\begin{align}
\min 3x_1-x_2+2x_3&\\  \\
s.a\;\;3x_1-x_3&\leq 4\\  \\
x_1+x_2+5x_3&\geq 1\\  \\
x_1&\geq 0\\ \\
x_3&\leq 0
\end{align}$$

Escribir el problema en formulación estándar y encontrar las soluciones básicas factibles. 

Invente $2$ poliedros $P_1, P_2\subseteq\mathbb{R}^2$ distintos tales que: 

- Cada uno tenga al menos $3$ vértices 
- $(-2,-1)$ sea el único óptimo para cada uno de los siguientes problemas de optimización: 

$$\begin{align}
\min x_2&\\  \\
s.a\;\;(x_1,x_2)&\in P_1
\end{align}$$$$\begin{align}
\min x_2&\\  \\
s.a\;\;(x_1,x_2)&\in P_2
\end{align}$$

- $(1,4)$ sea el único óptimo para cada uno de los siguientes problemas de optimización: 

$$\begin{align}
\min -x_1-x_2&\\  \\
s.a\;\;(x_1,x_2)&\in P_1
\end{align}$$
$$\begin{align}
\min -x_1-x_2&\\  \\
s.a\;\;(x_1,x_2)&\in P_2
\end{align}$$

Debe describir ambos poliedros con desigualdades y graficarlos. 