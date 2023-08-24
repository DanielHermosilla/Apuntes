
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


Por el otro lado, se puede parametrizar la [[Curvas|curva]] como: 

$$C_2:\;r(t)=(\cos(t),\sin(t))\;\;t\in[0,\frac{\pi}{2}]$$

Entonces, considerando la función $F_1$ y viendo las [[Integral de línea|integrales de línea]] sobre ambas curvas: 

$$\begin{align}
\int^{}_{C_1}F_1\cdot dr&=\int^{1}_{0}\left(2t(1-t),(1-t)^2+2\right)\cdot\left(-1,1\right)\;dt\\  \\
&=\int^{1}_{0}(2t-2t^2,1-2t+t^2+2)\cdot(-1,1)\;dt\\\\
&=\int^{1}_{0}(2t-2t^2 t^2,t^2-2t+3)\cdot(-1,1)\;dt\\  \\
&=\int^{1}_{0}-(2t-t^2)+(t^2-2t+3)\;dt\\   \\
&=\int^{1}_{0}(3t^2-4t+3)\;dt\\  \\
&=\left(t^3-4\frac{t^2}{2}+3t\right)\bigg\vert^{1}_{0}\\  \\
&=2
\end{align}$$


Ahora, ocupando la segunda parametrización: 

$$\begin{align}
\int^{}_{C_2}F_1\cdot dr&=\int^{\pi/2}_{0}\left(2\cos t\sin t,\cos^2 t+2\right)\left(-\sin(t),\cos(t)\right)\;dt\\  \\
&=\int^{\frac{\pi}{2}}_{0}\left(-2\cos t\sin^2 t+\cos^3 t+ 2\cos t\right)\;dt
\end{align}$$