
El método de [[Método de separación de variables|separación de variables]] es análogo al separación de variables de las ecuaciones diferenciales ordinarias. Lo que se plantea es que una función lineal es posible descomponerla en dos funciones: 

$$u=u(t,x)=T(t)X(x)\tag{1}$$

Luego, la ecuación dice: 

$$\frac{\partial u}{\partial t}-\frac{\partial^2 u}{\partial x^2}=0$$

Es decir, aplicando $(1)$: 

$$T'(t)X(x)-T(t)X''(x)=0$$

Esto nos dice que: 

$$T'(t)X(x)=T(t)X''(x)$$

Asumiendo que $T$ y $X$ no son nulas, es posible pasar dividiendo por $T(t)$ y asímismo por $X(x)$: 

$$\frac{T'(t)}{T(t)}=\frac{X''(x)}{X(x)}$$

La única forma que una función que depende de $t$ y dependa de $x$ al mismo tiempo es que ambos sean una **constante**. Por lo tanto, existe un [[escalares|escalar]] $\lambda\in\mathbb{R}$ tal que: 

$$\frac{T'(t)}{T(t)}=\frac{X''(x)}{X(x)}=\lambda$$

Así, se tiene que: 

$$\begin{align}
T'(t)-\lambda T(t)&=0\\  \\
X''(x)-\lambda X(x)&=0
\end{align}$$

## Solución de la ecuación del calor 

Consideremos el siguiente problema: 

$$\frac{\partial u}{\partial t}-\frac{\partial^2 u}{\partial x^2}=0\;\;\,\;\;x\in(0,1)\\ 
$$

Si asumimos que se tienen las siguientes [[Condición inicial|condiciónes iniciales]]: 

$$\text{Condiciones iniciales}=\begin{cases}\frac{\partial u}{\partial x}(t,0)=0&t>0\\  \\
\frac{\partial u}{\partial x}(t,1)=0&t>0\\  \\
u(0,x)=x^2&x\in (0,1)\end{cases}$$

Entonces, se llega al problema de *Stum-Liouville*: 

$$\begin{align}
X''(x)-\lambda X(x)&=0\\  \\
X(0)=X'(1)&=0
\end{align}$$

Notemos que las condiciones iniciales son, en realidad, [[Departamento de Física/Electromagnetismo/Electrostática/Condiciones de borde|condiciones de borde]] sobre el dominio $x$. En tales límites la función se anula. 

El problema de *Stum-Liouville* es un sistema de EDO de [[Sistema de ecuaciones|términos homogeneos]]. Luego, $\lambda$ corresponde a los [[valores y vectores propios|valores propios]] del sistema. Entonces, analizando por casos: 

Cuando $\lambda=0$ se llega que: 

$$\begin{align}
X''(x)&=0\\  \\
X'(0)=X'(1)&=0
\end{align}$$

Luego, 

$$X(x)=ax+b$$

Así, 

$$X'(x)=a\;\;\;\;\;a\in\mathbb{R}$$

Pero, como $X'(x)=0$, se llega que: 

$$X(x)=b\;\;\;\;b\in\mathbb{R}$$

Básicamente, la solución es una constante cualquiera. 

Cuando $\lambda>0$, sea $\lambda=k^2$ con $k>0$. Entonces: 

$$\begin{align}
X''-k^2X&=0\\ \\
X'(0)=X'(1)&=0
\end{align}$$

Resolviendo el [[polinomio característico]], se llega que $X(x)=e^{\alpha x}$. Entonces, la solución general sería: 

$$X(x)=ae^{kx}+be^{-kx}$$

Notemos que $X'(x)=ake^{kx} - bke^{-kx}$. Así: 

$$\begin{align}
X'(0)&=ak-bk=0\\  \\
X'(1)&=ake^k-bke^k=0\
\end{align}$$

Luego, $a=b$ y $a=0$ ocupando la segunda ecuación. 

Por último, considerando un valor propio negativo, entonces, asumamos que $\lambda=-k^2$ con $k>0$. Luego, 

$$\begin{align}
X''+k^2X&=0\\  \\
X'(0)=X'(1)&=0
\end{align}$$

Así,

$$\begin{align}
X(x)&=a\cos(kx)+b\sin(kx)\\  \\
X'(x)&=-ak\sin(kx)+bk\cos(kx)\\  \\
X'(0)&=bk=0\implies b=0\tag{Condición inicial}\\  \\
X'(1)&=-ak\sin(k)=0\implies k=n\pi
\end{align}$$

Luego, 

$$\begin{align}
\lambda&=-(n\pi)^2\;\;\;\;\;\;\forall n\in\mathbb{N}\\  \\
X(x)&=a\cos(n\pi x)
\end{align}$$

Ahora falta considerar la ecuación en $T$. Notemos que $\forall n\in\mathbb{N}$ existen: 

$$\begin{align}
\lambda_n&=-(n\pi)^2\\  \\
X_n(x)&=a_n\cos(n\pi x)
\end{align}$$

Veamos las funciones $T_n(t)$ tales que: 

$$u_n(t,x)=T_n(t)X_n(x)$$

En $\lambda_0=0$ se cumple que $T_0'(t)=0$ y por ende, $T_0(t)=\alpha_0$. 

Ahora, para $\lambda_n=-(n\pi)^2$ se tiene que: 

$$\begin{align}
T_n'(t)+(n\pi)^2T_n&=0\\  \\
T_n(t)&=\alpha_ne^{-(n\pi)^2t}
\end{align}$$

Luego, 

$$\begin{align}
u_n(t,x)&=\alpha_ne^{-(n\pi^2)t}a_n\cos(n\pi x)\\  \\
&=c_ne^{-(n\pi)^2}\cos(n\pi x)
\end{align}$$

Así: 

$$u(t,x)=\frac{c_0}{2}+\sum^{\infty}_{n=1}c_ne^{-(n\pi)^2t}\cos(n\pi x)$$


Y, entonces: 

$$\begin{align}
u(0,x)&=x^2\;\;\;\;0<x<1\\  \\
u(0,x)&=\frac{c_0}{2}+\sum^{\infty}_{n=1}c_n\cos(n\pi x)
\end{align}$$

Se llega que la sumatoria es una [[Departamento de Ingeniería Matemáticas/Cálculo Avanzado y Aplicaciones/Series de Fourier/Series de Fourier|series de Fourier]] **que llegaría a ser la extensión [[Paridad trigonométrica|par]] de la función coseno**. Entonces, resolviendo: 

$$\begin{align}
c_0&=2\int^{1}_{0}x^2dx\\  \\
c_n&=2\int^{1}_{0}x^2\cos(n\pi x)dx
\end{align}$$

