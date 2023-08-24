
Dado un par de funciones, $F_1$ y $F_2$, nos preguntamos si el camino influye en la [[Integral de línea|integral de línea]]. 

```functionplot
---
title: Dos funciones con camino distintos
xLabel: y
yLabel: x
bounds: [0, 1.2, 0, 2]
disableZoom: true
grid: true
---
g(x)=-x+1
f(x)=-x+1+sin(3.14*x)
```



Entonces, llamaremos a nuestras dos funciones: 

$$\begin{align}
F_1(x,y)&=(2xy,\;x^2+2)\\  \\
F_2(x,y)&=(2xy,\;x+z)
\end{align}$$


Notemos que la recta se puede **parametrizar** de la siguiente forma: 

$$C_1:\;r(t)=(1-t)\begin{pmatrix}
1 \\
0
\end{pmatrix}+t\begin{pmatrix}
0 \\
1
\end{pmatrix}$$


Por el otro lado, se puede parametri