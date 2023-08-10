
Una curva en $\mathbb{R}^n$ es una función: 

$$\begin{align}

r:[a,b]\to&\;\mathbb{R}^n \\ \\
t\to&\;r(t)=(x(t),x_2(t),\dots,x_n(t))

\end{align}$$

Esta función se va a llamar una paratrización de la curva $C$ con $C=\lbrace r(t)\;\vert\; t\in [a,b]\rbrace$.

### Ejemplo: ecuación de la recta

Sea la recta $x+y=1$, es una recta que pasa por los puntos $(0,1)$ y $(1,0)$

```functionplot
---
title: Ecuación de la recta
xLabel: x
yLabel: y
bounds: [-2, 2, -2, 2]
disableZoom: True
grid: True
---
y = 1-x
```


Ahora, su parametrización llegaría a ser: 

$$\begin{align}
r:\mathbb{R}\to&\;\mathbb{R}^2\\  \\
x\to&\;(x,1-x)
\end{align}$$

Notemos que esta recta tiene varias formas de parametrización, en realidad, tiene infinitas: 

- $r_2(t)=(2t,1-2t)$
- $r_3(t)=(3t,1-3t)$
- $\dots$

### Ejemplo 

Sea $C=\lbrace (x,y)\;\vert\;x^2 + y^2=1,\;y\geq0\rbrace$

Esto sería la parte arriba de una circumferencia. 

```functionplot
---
title: Semicírculo 
xLabel: x
yLabel: y
bounds: [-2, 2, -2, 2]
disableZoom: True
grid: True
---
y = sqrt(1 - x*x)

```


Esto se puede parametrizar también con [[Departamento de Ingeniería Matemáticas/Cálculo Diferencial e Integral/Aplicaciones de la integral/Coordenadas polares|coordenadas polares]]: 

$$r(\theta)=(\cos\theta,\sin\theta),\;\theta\in[0,\pi]$$

En las curvas debemos considerar el **sentido** en que se recorre la curva. Es decir, debemos conocer el **inicio** y **final** de la curva. 

Se dirá que se recorre en sentido positivo si es en sentido **antihorario**. 

### Ejemplo 

Parametrizar el segmento de recta de $(1,2)$ al punto $(-3,5)$. 