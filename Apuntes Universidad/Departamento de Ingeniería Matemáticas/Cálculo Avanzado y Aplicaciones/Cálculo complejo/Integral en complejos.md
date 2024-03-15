
Si nos damos cuenta, las [[Función compleja|funciones complejas]] están en el plano $R^2$ de los reales e imaginarios. Entonces en realidad se estaría haciendo una [[Integral de línea|integral de línea]]. 

![[IMG_61012850F90D-1.jpeg|center]]

Si se tiene una función cualquiera: 

$$z(t)=x(t)+iy(t)$$

Entonces, en realidad se llegaría que: 

$$\begin{align}
\int^{z_1}_{z_0}f(z)dz&=\int^{a}_{b}(u+iv)(dx+idy)\\  \\
&=\int^{b}_{a}(udx-vdy)+i\int^{b}_{a}(vdx+udy)
\end{align}$$

La integral de una función compleja llegaría a ser dos integrales. 

Ahora, si se llegase a tener una trayectoria cerrada, se puede ocupar el [[Teorema de Green]]: 

$$\begin{align}
\int^{z_1}_{z_0}f(z)dz&=\iint\left(-\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}\right)dA+\iint\left(\frac{\partial u}{\partial x}-\frac{\partial v}{\partial y}\right)dA
\end{align}$$

Pero, si nos fijamos en las condiciones de Cauchy-Riemann, es posible decir que si **la función no es cerrada, entonces es [[Derivada en complejos|derivable en complejos]]**. 

Por lo tanto, las integrales complejas se pueden entender como **integrales de línea**. 

#### Ejemplo 

Sea $C$ el arco de circumferencia $\vert Z\vert=1$ desde $1$ a $i$. Calcular: 

$$\int_Cz^2\;dz$$

La parametrización que se ocupa es la siguiente: 

$$z(t)=\cos t+i\sin t$$

Como $z^2$ está definida únicamente en el primer cuadrante: $0\leq t\leq\frac{\pi}{4}$. 

Por lo tanto, 

$$\begin{align}
\int_Cz^2\;dz&=\int^{\frac{\pi}{2}}_{0}\left(\cos t+i\sin t\right)^2(-\sin t+\cos t)\;dt\\  \\
&=\int^{\frac{\pi}{2}}_{0}(\cos^2t-\sin^2t+2i\sin t\cos t)(-\sin t+i\cos t)\;dt\\  \\
&=\int^{\frac{\pi}{2}}_{0}(-\sin t(\cos^2t-\sin^2t)-2(\sin t\cos^2t))\;dt\tag{Parte real}\\  \\
&+\int^{\frac{\pi}{2}}_{0}i\left[(\cos^2 t-\sin^2t)\cos t-2\sin t\cos t\right]\;dt\tag{Parte im}\\  \\
&=\int^{\frac{\pi}{2}}_{0}(-3\sin t\cos^2 t+\sin^3t)dt\tag{Parte real}\\ \\
&+i\int^{\frac{\pi}{2}}_{0}(\cos^3t-3\sin^2+\cos t)dt\tag{Parte im}
\end{align}$$

Notar la siguiente propiedad: 

$$\begin{align}
\sin^3 t&=\sin t\sin^2 t\\  \\
&=\sin t(1-\cos^2 t)\\  \\
&=\sin t -\sin t\cos^2 t
\end{align}$$

También se puede reescribir para coseno: 

$$\begin{align}
\cos^3t&=\cos t\cos^2 t\\  \\
&=\cos t(1-\sin^2)\\  \\
&=\cos t-\cos t\sin^2 t
\end{align}$$

Por lo tanto, reescribiendo: 

$$\begin{align}
\int^{\frac{\pi}{2}}_{0}z^2\;dz&=\int^{\frac{\pi}{2}}_{0}(\sin t-4\sin^3t\cos t)dt\tag{Parte real}\\  \\
&+i\int^{\frac{\pi}{2}}_{0}(\cos t-4\sin^2 t\cos t)dt\tag{Parte im}\\  \\
&=(-\cos t-4\frac{\cos^3 t}{3})\bigg\vert^{\frac{\pi}{2}}_0\tag{Parte real}\\  \\
&+i(\sin t-4\frac{\sin^3t}{3})\bigg\vert^{\frac{\pi}{2}}_0\tag{Parte im}\\  \\
&=-\frac{1}{3}-\frac{i}{3}
\end{align}$$

De igual forma, el cálculo se pudo haber hecho de una forma mucho más fácil. Notemos que: 

$$\begin{align}
z(t)&=\cos t+i\sin t=e^{it}\tag{Formula de Euler}
\end{align}$$

Así, $z'(t)=ie^{it}$. Por lo tanto: 

$$\begin{align}
\int_Cz^2\;dz&=\int^{\frac{\pi}{2}}_{0}\left(e^{it}\right)^2ie^{it}\;dt\\  \\
&=\int^{\frac{\pi}{2}}_{0}ie^{3it}\;dt\\  \\
&=\frac{\cancel{i}e^{3it}}{3\cancel{i}}\bigg\vert^{\frac{\pi}{2}}_0\\  \\
&=\frac{1}{3}(e^{3i\pi 2/t}-1)
\end{align}$$

## Parametrización 

En general, la siguiente ecuación es una circumferencia de radio $r$ y centro $z_0$: 

$$\vert z-z_0\vert =r$$

Esta circumferencia se parametriza como: 

$$z(t)=z_0+re^{it}$$

#### Ejemplo 

Calcular la siguiente integral: 

$$\int(z^3+i)\;dz$$

Con $\vert z\vert=1$. Primero, notemos que:

$$\begin{align}
\int z^n\;dz&=\int^{2\pi}_{0}(e^{it})^n(ie^{it})\;dt\;\;\;\;\;\;n\in\mathbb{Z}\\  \\
&=\int^{2\pi}_{0}ie^{i(n+1)t}\;dt\\  \\
&=ie^{i(n+1)t}/i(n+1)\bigg\vert^{2\pi}_{0}\\  \\
&=0
\end{align}$$

Es nula para todo $n\neq 1$, dado que la función exponencial está en términos de senos y cosenos. 

Luego; 

$$\int_{\vert Z\vert =r}z^n\;dz=0\;\;\;\;\;\forall n\in\mathbb{Z}\;,\;n\neq 1$$

Ahora, viéndolo para el caso $n=-1$ para una circumferencia unitaria: 

$$\begin{align}
\int\frac{dz}{z}&=\int^{2\pi}_{0}\frac{ie^{it}}{e^{it}}dt\\  \\
&=\int^{2\pi}_{0}i\;dt\\  \\
&=2\pi i
\end{align}$$

Así, se llega que el caso más general: 

$$\int_{\vert z\vert =r}z^n\;dz=\begin{cases}2\pi i&n=-1\\  \\
0&n\neq -1\end{cases}$$

## Teorema de Cauchy-Goursat 

Sea $f:\Omega\subset\mathbb{C}\to\mathbb{C}$ una [[Función compleja|función compleja]]. Vamos a decir que $\Omega$ es un [[Conjuntos abiertos y cerrados|conjunto abierto]] no vacio. Sea $C$ una [[Curva cerrada|curva cerrada]], [[Curva simple|simple]] y seccionalmente suave, $C\subseteq\Omega$

Supongamos que $f$ es holomorfa, vale decir, [[Derivada en complejos|derivable]] en $\mathbb{C}$, en la curva $C$ y en el interior de la curva cerrada. Así, se postula que: 

$$\int_Cf(z)\;dz=0$$

De hecho, al cumplir las condiciones de Cauchy-Riemann nos dice que la integral siempre va a valer cero por el [[Teorema de Green|teorema de Green]]. 

#### Ejemplo 

Calcular la siguiente integral: 

$$\int\frac{\sin^z}{z^2+1}dz$$

Con $\vert z\vert = 2$. 

Notemos que el término de abajo se puede escribir en **fracciones parciales**, es decir: 

$$\begin{align}
\frac{1}{z^2+1}&=\frac{1}{(z-i)(z+i)}\\  \\
&=\frac{a}{z-i}+\frac{b}{z+i}
\end{align}$$

## Fórmula integral de Cauchy 

Sea $f:\Omega\subset\mathbb{C}\to\mathbb{C}$ una [[Función compleja|función compleja]] homolorfa en $\Omega$. Sea $C$ una [[Curva cerrada|curva cerrada]], [[Curva simple|simple]] y seccionalmente suave, $C\subseteq\Omega$ y sea $z_0$ un punto al interior de $C$. Se postula que: 

$$\frac{1}{2\pi i}\int_C\frac{f(z)}{z-z_0}=f(z_0)$$


Por el otro lado, se puede extrapolar a la siguiente expresión: 

$$\int_C\frac{f(z)}{(z-z_0)^n}\;dz=\frac{2\pi i}{(n-1)!}\frac{d^{n-1}}{dz^{n-1}}f(z_0)$$

Cuando $n\geq 1$. 

Si la integral es holomorfa salvo una cantidad finita de puntos $z_0,z_1,z_2,\dots,z_n$, se les llamará **polos** a estos puntos.
### Demostración 

Como $f(z)$ es homolorfa entonces se puede hacer un desarrollo de Taylor: 

$$f(z)=f(z_0)+f'(z_0)(z-z_0)+\frac{1}{2!}f''(z_0)(z-z_0)^2$$

Así, 

$$\begin{align}
\frac{f(z)}{z-z_0}&=\frac{f(z_0)}{z-z_0}+f'(z_0)+\frac{f''(z_0)}{z!}(z-z_0)+\dots\\  \\
\int\frac{f(z)}{z-z_0}&=\int\left(\frac{f(z_0)}{z-z_0}+f'(z_0)+\frac{f''(z_0)}{z!}(z-z_0)+\dots\right)\\  \\
&=f(z_0)\int\frac{dz}{z-z_0}+\cancelto{0}{f'(z_0)\int dz}+\cancelto{0}{\frac{f''(z_0)}{2}\int dz}+\cancelto{0}{\dots}\\  \\
&=2\pi i
\end{align}$$

#### Ejemplo 

Se quiere calcular: 

$$\int_{\vert Z\vert=1}\frac{e^z}{z}dz\;\land\;\int_{\vert Z\vert=1}\frac{e^z}{z^4}\;dz$$

Sabemos que: 

$$e^z=\sum^{\infty}_{k=0}\frac{z^k}{k!}$$

Luego, 

$$\frac{e^z}{k!}=\sum^{\infty}_{k=0}\frac{z^{k-1}}{k!}$$

Además: 

$$\int_{\vert Z\vert =1}z\;dz=\begin{cases}2\pi i&n=1\\  \\
0&n\neq 1\end{cases}$$

Así; 

$$\begin{align}
\int\frac{e^z}{z}\;dz&=\int\sum^\infty\frac{z^{k-1}}{k!}\;dz\\  \\
&=\sum^\infty\frac{1}{k!}\int z^{k-1}\;dz
\end{align}$$


El único caso que el valor de la integral es distinto de cero es cuando $k=0$. Así, se tiene que: 

$$\int\frac{e^z}{z}\;dz=2\pi i$$

Ahora, análogamente para el otro caso: 

$$\begin{align}
\int_{\vert Z\vert = 1}\frac{e^z}{z^4}\;dz&=\sum^\infty\frac{1}{k!}\int z^{k-4}\;dz
\end{align}$$

El único caso cuando no da $0$ es cuando $k=3$. Así: 

$$\int\frac{e^z}{z^4}\;dz=\frac{2\pi i}{3!}$$

#### Ejemplo 

Calcular la siguiente integral: 

$$\int_{\vert Z\vert=1/2}\frac{z^2+1}{z^2-z}\;dz$$

Notemos que $z$ tiene dos singularidades en $z=0$ y $z=1$. Pero sólo $z=0$ está al interior de la circumferencia. Notemos lo siguiente: 

$$\begin{align}
f(z)&=\frac{z^2+1}{z^2-z}\\  \\
&=\frac{z^2+1}{z(z-1)}\\  \\
&=\frac{(z^2+1)/(z-1)}{z}
\end{align}$$

Así, si llamamos: 

$$g(z)=\frac{z^2+1}{z-1}$$

Se tiene que: 

$$f(z)=\frac{g(z)}{z}$$

Así, **de la fórmula integral de Cauchy**: 

$$\begin{align}
\int_{\vert z\vert=1}f(z)\;dz&=\int_{\vert z\vert = 1/2}\frac{g(z)}{z}\;dz\\\\
&=2\pi i ig(0)\\  \\
&=2\pi i(\frac{1}{-1})\end{align}$$

#### Ejemplo 

Calcular la siguiente integral: 

$$\int_{\vert Z\vert = 2}\frac{z+1}{z^2-z}\;dz$$

Nuevamente, la función tiene dos singularidades en $z=0\land z=1$. Además, ambos están dentro de la circumferencia. Factorizando: 

$$\begin{align}
f(z)&=\frac{z+1}{z^2-z}\\  \\
&=\frac{z+1}{z(z-1)}\\  \\
&=\frac{a}{z}+\frac{b}{z+1}
\end{align}$$

Al poder reescribirlo con fracciones parciales: 

$$\begin{align}
\frac{z+1}{z(z-1)}&=\frac{a(z-1)+bz}{z(z-1)}\\  \\
&=\frac{z(a+b)-a}{z(z-1)}
\end{align}$$

Luego: 

$$\begin{align}
a&=-1\\  \\
b&=2
\end{align}$$


Así: 

$$\begin{align}
\int\frac{z+1}{z^2-z}\;dz&=\int\left(\frac{-1}{z}+\frac{2}{z-1}\right)\;dz\\  \\
&=\int\frac{-1}{z}\;dz+\int\frac{2}{z-1}\;dz\\  \\
&=-2\pi i + 2\cdot 2\pi i\tag{Integral Cauchy}
\end{align}$$

#### Ejemplo 

Calcular: 

$$\int_{\vert z\vert=2}\frac{e^{z^2}}{z^2+1}\;dz$$

La función tiene problemas en $z\pm i$. Así, ocupando fracciones parciales: 

$$\begin{align}
\frac{1}{z^2+1}&=\frac{a}{z+i}+\frac{b}{z-i}\\  \\
&=\frac{a(z-i)+b(z+i)}{(z-i)(z+i)}
\end{align}$$

Así: 

$$\begin{align}
a+b&=0\\  \\
i(b-a)&=1
\end{align}$$

Por lo tanto: 

$$\begin{align}
b&=-\frac{i}{2}\\  \\
a&=\frac{i}{2}
\end{align}$$


Por ende: 

$$\begin{align}
\frac{e^{z^2}}{z^2+1}&=\frac{i}{2}\frac{e^{z^2}}{z(z+i)}-\frac{i}{2}\frac{e^{z^2}}{z(z-i)}
\end{align}$$


Así: 

$$\begin{align}
\int\frac{e^{z^2}}{z^2+1}&=\frac{i}{2}\int\frac{e^{z^2}}{z+i}-\frac{i}{2}\int\frac{e^{z^2}}{z-i}\\ \\
&=\frac{i}{2}2\pi ie^{(-i)^2}-\frac{i}{2}2\pi ie^{i^2}\\  \\
&=-\pi e^{-1}+\pi e^{-1}=0\end{align}$$

