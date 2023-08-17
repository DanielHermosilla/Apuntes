
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

Es la integral de línea de $F$ a lo largo de la curva $C$. 

Observemos que dada una curva $C$, se podría llamar $-C$ a la curva $C$ recorrida en sentido opuesto: 

$$\int^{}_{-C}F\cdot dr=-\int^{}_{C}F\cdot dr$$

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
r:[0,2\pi]&\to\mathbb{R}^2\\  \\
\theta&\to (\cos\theta,\sin\theta)
\end{align}$$

Luego, 

$$\begin{align}

\oint_CF\cdot dr&=\int^{2\pi}_{0}F(\cos\theta,\sin\theta)\cdot r'(\theta)d\theta\\  \\
&=\int^{2\pi}_{0}(\cos\theta\sin\theta,\cos\theta+\sin\theta)\cdot(-\sin\theta,\cos\theta)d\theta\\ \\
&=\int^{2\pi}_{0}\left(\cos\theta\sin^2\theta+\cos^2\theta+\sin\theta\cos\theta\right)d\theta  
\end{align}$$

#### Ejemplo 

Considere la curva que se obtiene al intersectar el cono $z^2=x^2+y^2$ y la parábola $z=x^2+y^2$, con $z>0$ y recorrida en sentido antihorario. 

Calcular $\int^{}_{C}F\cdot dr$ donde la función es $F(x,y,z)=(2x,3y,x+y+z)$

Entonces, para parametrizar la curva ocupamos [[Coordenadas cilíndricas|coordenadas cilíndricas]]. Entonces, 

- $x=r\cos\theta$
- $y=r\sin\theta$
- $z=z$

Notemos que intersectando se llega que $z=1$. Ahora que sabemos que $z=1$, se puede deducir de la ecuación del cono que $r=1$. Por lo tanto, se llegan a las siguientes coordenadas: 

- $x=\cos\theta$
- $y=\sin\theta$
- $z=1$

Y la parametrización sería: 

$$\begin{align}
r:[0,2\pi]&\to\mathbb{R}^3\\  \\
r(\theta)&\to (\cos\theta,\sin\theta,1)
\end{align}$$


#### Ejemplo 

Consideremos las funciones siguientes: 

$$\begin{align}  \\
F:\mathbb{R}^2&\to\mathbb{R}^2 \\  \\
F_1(x,y)&=(4x+y,x)\\  \\
F_2(x,y)&=(4x+y,-x)
\end{align}$$

Consideramos las curvas: 

- $C_1$: el segmento de la recta de $(0,1)$ a $(0,1)$
- $C_2$: el arco de la circumferencia de $(1,0)$ a $(0,1)$

Luego, 

$$\begin{align}
C_1:\;&r_1(t)=(1-t)(1,0)+t(0,1)\;\; t\in[0,1]\\  \\
C_2:\;&r_2(t)=(\cos t,\sin t)\;\; t\in[0,\frac{\pi}{2}]
\end{align}$$

Por lo tanto, 

$$\begin{align}
\int^{}_{C_1}F_2dr &= \int^{1}_{0}F_2(1-t,t)\cdot(-1,1)dt\\  \\
&=\int^{1}_{0}\left(4(1-t)+t,-(1-t)\right)\cdot (-1,1)dt\\ \\
&=\int^{1}_{0}\left(4-3t,t-1\right)\cdot(-1,1)dt\\  \\
&=\int^{1}_{0}(3t-4+t-1)dt\\  \\
 
\end{align}$$