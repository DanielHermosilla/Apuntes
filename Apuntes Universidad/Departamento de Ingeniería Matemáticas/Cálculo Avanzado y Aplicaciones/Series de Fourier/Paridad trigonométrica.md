
Notemos que la [[Series geométrica|serie geométrica]] de la función $\cos(x)$ y $\sin(x)$ se puede reescribir de la siguiente manera: 

$$\begin{align}
\cos{x}&=\sum^{\infty}_{k=0}\frac{(-1)^nx^{2n}}{(2n)!}\\  \\
\sin{x}&=\sum^{\infty}_{k=0}\frac{(-1)^nx^{2n+1}}{(2n+1)!}
\end{align}$$

Notemos que $\sin$, que es una función impar, está escrita en terminos impares. Análogo para $\cos$. Supongamos que $f$ es par, es decir: 

$$f(x)=f(-x)$$

Entonces, si lo llegamos a integrar por su multiplicación por $\sin(x)$

$$\begin{align}
\int^{\pi}_{-\pi}f(x)\sin(nx)dx&=\int^{0}_{-\pi}f(x)\sin(nx)\;dx+\int^{\pi}_{0}f(x)\sin(nx)dx\\  \\
&=-\int^{0}_{\pi}f(-u)\sin(-nu)\;du+\int^{\pi}_{0}f(x)\sin(nx)dx\\  \\
&=\int^{\pi}_{0}f(-u)\sin(-nu)du+\int^{\pi}_{0}f(x)\sin(nx)dx\\  \\
&=-\int^{\pi}_{0}f(u)\sin(nu)du+\int^{\pi}_{0}f(x)\sin(nx)dx\\  \\
&=0
\end{align}$$

Por lo tanto, **toda multiplicación de seno por una función par tiene integral nula en el intervalo de la [[Departamento de Ingeniería Matemáticas/Cálculo Avanzado y Aplicaciones/Series de Fourier/Series de Fourier|series de Fourier]]**. Este resultado es **análogo con el coseno y las funciones pares**. Por lo tanto, se puede plantear el siguiente lema: 

Sea $f:[-\pi,\pi]\to\mathbb{R}$, entonces si $f$ cumple la hipótesis: 

- Si $f$ es par, $f(x)=f(-x)$, entonces 

$$\begin{align}\int^{\pi}_{-\pi}f(x)\sin(nx)\;dx&=0\;\;\;\;\;\;\forall n\in\mathbb{N}\\  \\
\int^{\pi}_{-\pi}f(x)dx&=2\int^{\pi}_{0}f(x)\;dx\\  \\
\int^{\pi}_{-\pi}f(x)\cos(nx)\;dx&=2\int^{\pi}_{0}f(x)\cos(nx)\;dx
\end{align}$$

- Si $f$ es impar, $f(-x)=-f(x)$, entonces 

$$\begin{align}
\int^{\pi}_{-\pi}f(x)\cos(nx)dx&=0\;\;\;\;\;\;\;\forall n\in\mathbb{N}\\  \\
\int^{\pi}_{-\pi}f(x)dx&=0\\  \\
\int^{\pi}_{-\pi}f(x)\sin(nx)dx&=2\int^{\pi}_{0}f(x)\sin(nx)\;dx

\end{align}$$


```functionplot
---
title: Función impar
xLabel: x
yLabel: y
bounds: [-3.14,3.14,-10,10]
disableZoom: true
grid: false
---
f(x)=x^3
```

Esto simplifica muchos cálculos de [[Departamento de Ingeniería Matemáticas/Cálculo Avanzado y Aplicaciones/Series de Fourier/Series de Fourier|series de Fourier]].

Este concepto de paridad trigonométrica puede servir para calcular **series de Fourier en intervalos que no van de $[-\pi,\pi]$. 

>[!example] Extensión par 
>Sea $f:[0,\pi]\to\mathbb{R}$, podemos definir la extensión par de $f$ como: 
>
>$$f(x)=\begin{cases} f(x)&0\leq x\leq\pi\\ \\ f(-x)&-\pi\leq x\leq 0\end{cases}$$
>
>Esto implica, directamente, que la serie de Fourier va a estar únicamente en términos de coseno. 
>
>$$Sf_p(x)=\frac{a_0}{2}+\sum^{\infty}_{n=1}a_n\cos(nx)$$
>
>Donde: 
>
>$$\begin{align}
a_0&=\frac{2}{\pi}\int^{\pi}_{0}f(x)dx\\\\
a_n&=\frac{2}{\pi}\int^{\pi}_{0}f(x)\cos(nx)dx 
\end{align}$$


De forma análoga se puede definir la extensión impar: 

>[!example] Extensión impar 
>Sea $f:[0,\pi]\to\mathbb{R}$, podemos definir la extensión impar de $f$ como: 
>
>$$f(x)=\begin{cases} f(x)&0\leq x\leq\pi\\ \\ -f(-x)&-\pi\leq x\leq 0\end{cases}$$
>
>Esto implica, directamente, que la serie de Fourier va a estar únicamente en términos de seno. 
>
>$$Sf_p(x)=\sum^{\infty}_{n=1}b_n\sin(nx)$$
>
>Donde: 
>
>$$\begin{align}
b_n&=\frac{2}{\pi}\int^{\pi}_{0}f(x)\sin(nx)dx\\\\
\end{align}$$

#### Ejemplo: extensión par

Sea $f(x)=1+x$ definida en $x\in [0,\pi]$. El problema con esta función es que está definida en un intervalo distinto a $[-\pi,\pi]$. 

Originalmente se tendría la siguiente función: 


```functionplot
---
title: Función de ejemplo
xLabel: x
yLabel: y
bounds: [-3.14,3.14,0,10]
disableZoom: true
grid: true
---
f(x) = 1+x
```


Su extensión par llegaría a ser: 

```functionplot
---
title: Extensión par
xLabel: x
yLabel: y
bounds: [-3.14,3.14,0,10]
disableZoom: true
grid: true
---
f(x) = 1+x
g(x) = 1-x
```

#### Ejemplo 

Calcular la serie de cosenos de la función $f(x)=e^x$ definida en el intervalo $x\in[0,\pi]$. 

Por lo tanto: 

$$Sf_p(x)=\frac{a_0}{2}+\sum^{\infty}_{n=1}a_n\cos(nx)$$

En este caso, 

$$\begin{align}
a_0&=\frac{2}{\pi}
\int^{\pi}_{0}f(x)dx\\  \\
&=\frac{2}{\pi}\int^{\pi}_{0}e^xdx\\  \\
&=\frac{2}{\pi}e^x\bigg\vert^{\pi}_{0}\\  \\
&=\frac{2}{\pi}(e^\pi-e^0)\\  \\
&=\frac{2}{\pi}(e^\pi-1)\end{align}$$

Para el caso de $a_n$: 

$$\begin{align}
a_n&=\frac{2}{\pi}\int^{\pi}_{0}f(x)\cos(nx)dx\\  \\
&=\frac{2}{\pi}\int^{\pi}_{0}e^x\cos(nx)dx
\end{align}$$

Sea $u=e^x$ y $dv=\cos(nx)$: 

$$\begin{align}
a_n&=\frac{2}{\pi}\left(\cancelto{0}{\frac{e^x\sin(nx)}{n}\bigg\vert^\pi_0}-\int^{\pi}_{0}\frac{e^x\sin(nx)}{n}\right)\\  \\
&=\frac{-2}{n\pi}\int^{\pi}_{0}e^x\sin(nx)dx
\end{align}$$

Nuevamente, con el mismo cambio de variable pero con $dv=\sin(nx)$: 

$$\begin{align}
a_n&=\frac{-2}{n\pi}\left(-\frac{e^x\cos(nx)}{n}\bigg\vert^\pi_0+\frac{1}{n}\int^{\pi}_{0}e^x\cos(nx)dx\right)\\  \\
&=-\frac{2}{n\pi}\left(-\frac{e^\pi(-1)^n}{n}+\frac{1}{n}+\frac{1}{n}\int^{\pi}_{0}e^x\cos(nx)dx\right)\\  \\
&=\frac{2}{\pi}\int^{\pi}_{0}e^x\cos(nx)dx\\  \\
&=\frac{2}{n\pi}\left(\frac{(-1)^ne^\pi}{n}-\frac{1}{n}\right)-\frac{2}{n^2\pi}\int^{\pi}_{0}e^x\cos(nx)dx\\  \\
&=\frac{2}{\pi}\left(1+\frac{1}{n^2}\right)\int^{\pi}_{0}e^x\cos(nx)dx\\   \\
&=\frac{2}{n\pi}\left(\frac{(-1)^ne^\pi}{n}-\frac{1}{n}\right)\\  \\
&=\frac{2}{\pi}\int^{\pi}_{0}e^x\cos(nx)dx\\  \\
&=\frac{n^2}{(n^2+1)}\frac{2}{n^2\pi}\left((-1)^ne^\pi-1\right)\\  \\
&=\frac{2}{(n^2+1)\pi}\left((-1)^ne^\pi-1\right)
\end{align}$$

Por lo tanto, la serie de Fourier llegaría a ser: 

$$\begin{align}
Sf_p(x)&=\frac{a_0}{2}+\sum^{\infty}_{n=1}a_n\cos(nx)\\  \\
&=\frac{1}{\pi}(e^\pi-1)+\sum^{\infty}_{n=1}\frac{2}{(n^2+1)\pi}\left((-1)^ne^\pi-1\right)\cos(nx)
\end{align}$$

![[Fourier3 1.png|center]]

La extensión impar llegaría a ser: 

$$b_n=\frac{2}{\pi}\int^{\pi}_{0}f(x)\sin(nx)dx$$

Reemplazando para $-f(-x)$: 

$$\begin{align}
b_n&=\frac{2}{\pi}\int^{\pi}_{0}-e^{-x}\sin(nx)dx
\end{align}$$

Calculando con doble cambio de variable, se llega que: 

$$\begin{align}
b_n&=\frac{2}{\pi}\int^{\pi}_{0}e^x\sin(nx)dx\\  \\
&=\frac{2}{n\pi}\left(\frac{n^2}{n^2+1}\right)\left(1-e^\pi(-1^n)\right)
\end{align}$$

Entonces, la [[Departamento de Ingeniería Matemáticas/Cálculo Avanzado y Aplicaciones/Series de Fourier/Series de Fourier|serie de Fourier]] llegaría a ser: 

$$Sf_1=\sum^{\infty}_{n=1}\left(\frac{2n}{n^2+1}\right)\frac{(1-e^\pi(-1)^n)}{\pi}\sin(x)$$

![[Fourier4.png|center]]

Notar que la función **es periódica en $2\pi$**.

![[Fourier5.png|center]]

Para el caso de la serie en función del coseno se tendría lo siguiente: 

![[Fourier6.png|center]]

