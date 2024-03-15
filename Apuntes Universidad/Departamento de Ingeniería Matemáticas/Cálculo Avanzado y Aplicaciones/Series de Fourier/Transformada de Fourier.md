
Análogo a las [[Transformada de Laplace|transformada de Laplace]], existen las transformadas de Fourier para ver imagenes: 

$$\int^{\infty}_{-\infty}f(x)e^{ix\xi}dx=f(\xi)$$

Donde también existe la antitransformada de Laplace, para recuperar ciertas señales: 

$$f(x)=\int\hat{f(\xi)}e^{-i\xi x}d\xi$$

Nuevamente, análogo a la [[Transformada de Laplace|transformada de Laplace]] que se ocupa para resolver [[EDO lineal de orden n|ecuaciones diferenciales]], la transformada de Fourier se ocupa para resolver **ecuaciones de diferenciales parciales**. De hecho, volviendo al ejemplo sinusoidal de la [[Departamento de Ingeniería Matemáticas/Cálculo Avanzado y Aplicaciones/Series de Fourier/Series de Fourier|series de Fourier]]: 

```functionplot
---
title: Cuerda ante un impulso
xLabel: 
yLabel: 
bounds: [0,10,-1,1]
disableZoom: true
grid: false
---
f(x) = cos(x)
```

Su ecuación llega a ser una **ecuación diferencial parcial**, que es la [[onda|ecuación de onda]]:  

$$\frac{\partial^2 u}{\partial t^2}-c^2\frac{\partial^2u}{\partial x^2}=f(t,x)$$

### Motivación 

Sea $f:\mathbb{R}\to\mathbb{R}$ una función [[Continuidad|continua]] y $l>0$. Para todo valor $x\in (-l,l)$, se tiene que: 

$$S_f(x)=\sum^{\infty}_{k=-\infty}C_ke^{ik\pi x/l}$$

Donde se define $C_k$ como: 

$$C_k=\frac{1}{2l}\int^{l}_{-l}f(\xi)e^{-\frac{i\pi\xi}{l}}d\xi$$


Redefiniendo la función, es posible escribirla como: 

$$f(x)=\sum^{\infty}_{k=-\infty}\frac{1}{2l}\int^{l}_{-l}f(y)e^{ik\pi/l\;(x-y)}dy$$

Entonces, notar que se tiene una especie de [[Suma de Riemann|suma de Riemann]], por lo tanto, se puede reescribir como: 

$$g_{x,l}(s)=\int^{l}_{-l}f(y)e^{(x-y)s}$$

Haciendo el límite de $l$ al infinito, se llega a la siguiente integral impropia: 

$$g_x(s)=\int^{+\infty}_{-\infty}f(y)e^{i(x-y)s}ds$$

Entonces, *deshaciendo* la [[Integral de Riemann|integral de Riemann]]:

$$f(x)=\frac{1}{2l}\sum^{\infty}_{k=-\infty}g_{x,l}\left(\frac{k\pi}{l}\right)$$

Notemos que para completar la suma de Riemann faltaría el elemento diferencial: 

$$\begin{align}
f(x)&=\frac{1}{2\pi}\sum^{\infty}_{k=-\infty}g_{x,l}\left(\frac{k\pi}{l}\right)\frac{\pi}{l}\\\\ 
&=\frac{1}{2\pi}\sum^{\infty}_{k=-\infty}g_{x,l}\left(\frac{k\pi}{l}\right)\left[(k-l)\frac{\pi}{l}-k\frac{\pi}{l}\right]\\\\ 
\lim_{l\to\infty}&\frac{1}{2\pi}\int^{+\infty}_{-\infty}g_x(y)dy\\\\ 
f(x)&=\frac{1}{2\pi}\int^{+\infty}_{-\infty}\int^{+\infty}_{-\infty}f(y)e^{i(x-y)s}dy\;ds\;\;\;\;\;\forall x\in\mathbb{R}\end{align}
$$

Convenientemente, se puede escribir: 

$$f(x)=\frac{1}{\sqrt{2\pi}}\int^{+\infty}_{-\infty}e^{ixs}\left(\frac{1}{\sqrt{2\pi}}\int^{+\infty}_{-\infty}f(y)e^{-iys}dy\right)ds$$


>[!example] Transformada de Fourier 
>
>Sea $f:\mathbb{R}\to\mathbb{C}$ integrable $(\int^{+\infty}_{-\infty}\vert f(s)\vert ds<+\infty)$. Se define la transformada de Fourier de $f$ como: 
>
>$$\begin{align}
 f:\mathbb{R}&\to\mathbb{C}\\  \\
s&\to f(s)=\frac{1}{\sqrt{2\pi}}\int^{+\infty}_{-\infty}f(y)e^{-iys}dy\end{align}$$

>[!example] Antitransformada de Fourier 
>Sea $g:\mathbb{R}\to\mathbb{C}$ otra función integrable. Se define la antitransformada de Fourier como: 
>
>$$\begin{align} 
f:\mathbb{R}&\to\mathbb{C}\\  \\
x&\to g(x)=\frac{1}{\sqrt{2\pi}}\int^{+\infty}_{-\infty}g(s)e^{ixs}ds\end{align}$$

Sea $f:\mathbb{R}\to\mathbb{C}$ una función integrable entonces su transformada de Fourier $\mathbb{F}$ está bien definida y es una función [[Continuidad|continua]]. 

>[!error] Teorema de inversión 
>
>Sea $f:\mathbb{R}\to\mathbb{C}$ una función integrable y además que $\mathbb{F}:\mathbb{R}\to\mathbb{C}$ es integrable. Entonces, se tiene que: 
>
>$$f(x)=T^{-1}(T(f))x$$
>
>Vale decir, la función es la transformada compuesta con la antitransformada 

Sea $f:\mathbb{R}\to\mathbb{C}$ una función integrable con derivada $(f')$ integrable. Entonces $T(f')(s)=isT(f)(s)$ 