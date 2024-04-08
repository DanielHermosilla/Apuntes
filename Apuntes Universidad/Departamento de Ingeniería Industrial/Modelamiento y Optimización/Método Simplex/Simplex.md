
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

