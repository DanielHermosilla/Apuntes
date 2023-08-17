
Podríamos tener una función que nos determine una curva, es decir, una trayectoria. Por ejemplo, se podría tener la siguiente función en $\mathbb{R}^2$ que nos dictamine la siguiente trayectoria: 

![[IMG_D21BCBBEBBE4-1.jpeg|center|500]]

En este caso, se tendría una función $f:[a,b]\to\mathbb{R}^2$, pero se podría generalizar para una trayectoria en $n$ dimensiones. 

## Definición 

El trabajo realizado por una fuerza $F$ a lo largo de la [[Curvas|curva]] $C$, donde: 

$$\begin{align}
C:r[a,b]&\to\mathbb{R}^n\\  \\
t&\to r(t)
\end{align}$$

Está dado por: 

$$W=\int^{b}_{a}F(r(t))r'(t)dt$$

Que es equivalente a tener: 

$$W=\int^{}_{C}F\cdot dr$$

Es la integral de línea de $F$ a lo largo de la curva $C$

#### Ejemplo 

$F(x,y)=(2xy,2x-3y)$ y $C$ una recta desde $(1,1)$ a $(2,3)$. 

Se tiene que para la curva $C$, 

$$\begin{align}
r:[0,1]&\to\mathbb{R}\\ \\
r(t)&\to (1-t)(1,1) + t(2,3)\\  \\
&\to(1+t,1+2t)
\end{align}$$

Entonces, la integral de línea en este caso se vería de la siguiente forma: 

![[IMG_A8D0FB4079C8-1.jpeg|center|450]]


Entonces, la integral sería:

$$\begin{align}
\int^{}_{C}F\cdot dr&=\int^{1}_{0}F(1+t,1+2t)\cdot(1,2)dt\\  \\
&=\int^{1}_{0}\left(2(1+t)(1+2t),2(1+t)-3(1+2t)\right)\cdot (1,2)dt\\  \\
&=\int^{1}_{0}(-2t+4t^2)dt\\  \\
&=\left(-t^2+\frac{4}{3}t^3\right)\bigg\vert^{1}_{0}\\  \\
&=\frac{1}{3}
\end{align}$$


Notar que los límites de la integral tiene que ver principalmente por los valores de la variable $t$ cuando se define la parametrización. El [[Producto punto|producto punto]] que se obtiene es equivalente a la [[Distancia entre dos puntos|distancia entre dos puntos]]. 

#### Ejemplo 

Sea la siguiente función: 

$$\begin{align}
F:\mathbb{R}^2&\to\mathbb{R}^2\\  \\
(x,y)&\to F(x,y)=(xy, x+y)
\end{align}$$

Calcular el trabajo realizado por $F$ a lo largo de la circumferencia unitaria $x^2+y^2=1$ en sentido antihorario.

Esto se puede parametrizar fácilmente con [[Departamento de Ingeniería Matemáticas/Cálculo Diferencial e Integral/Aplicaciones de la integral/Coordenadas polares|coordenadas polares]], donde trivialmente el radio es $1$. Ahora, para establecer el sentido, sabemos que el ángulo va de $[0,2\pi]$. Entonces, la parametrización sería: 

$$\begin{align}
r:[0,2\pi]&\to\mathbb{R}
\end{align}$$

