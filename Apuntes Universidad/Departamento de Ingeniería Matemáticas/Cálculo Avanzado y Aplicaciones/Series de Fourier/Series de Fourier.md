
Haciendo un ánalogo a las [[Series numéricas|series numéricas]], existen muchas funciones que pueden ser descompuestas como sumas infinitas: 

$$\begin{align}
e^x&=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\dots\\  \\
&=\sum^{\infty}_{n=0}\frac{x^n}{n!}
\end{align}$$

Análogamente para las trigonométricas: 

$$\begin{align}
\sin{x}&=\sum^{\infty}_{n=0}\frac{x^{2n+1}}{(2n+1)!}
\end{align}$$

Y así sucesivamente, de hecho, se puede decir que para escribir una función como [[Series de Potencias|serie de potencias]] deben existir **infinitas derivadas** para poder hacerlo, de hecho, son de la forma: 

$$\begin{align}
f(x)&=\sum^{\infty}_{n=0}\frac{1}{n!}\frac{d^nf}{dx^n}(x_0)(x-x_0)^n
\end{align}$$

Esta condición es muy fuerte y poco probable, por lo tanto, se trató de buscar otra forma para expresar las series geométricas. 

Lo que hizo Fourier fue ver como se deforman una *"cuerda"* ante un impulso y medir la distancia vertical en función del eje $x$: 


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

Se puede ver una especie de oscilación, que sigue cierta forma sinusoidal. En el fondo, lo que quería lograr era ver si al sobreponer funciones oscilatorias es posible generar una función $u(t,x)$, vale decir: 

$$u(t,x)=a_0+\sum(a_n\cos{nx}+b_n\sin{nx})$$

Acordándonos que el término $n$ hace variar la [[frecuencia]] de la función sinusoidal y el término multiplicativo $(a_n$ y $b_n$) hace variar la amplitud: 


```functionplot
---
title: Funciones sinusoidales
xLabel: 
yLabel: 
bounds: [0,10,2,-2]
disableZoom: true
grid: false
---
f(x)=sin(x)
g(x)=2sin(x)
h(x)=sin(4x)
```

Si nos fijamos en las [[Integral de Riemann|integrales]] sinusoidales: 

$$\begin{align}
\int^{\pi}_{-\pi}\cos(nx)dx&=\frac{\sin(nx)}{n}\bigg\vert^{\pi}_{-\pi}\\  \\
&=\frac{\sin(n\pi)}{n}-\frac{\sin(-n\pi)}{n}\\  \\
&=0 
\end{align}$$

Y ahora para la función $\sin$: 

$$\begin{align}\int^{\pi}_{-\pi}\sin(nx)dx&=\frac{-\cos (nx)}{n}\bigg\vert^{\pi}_{-\pi}\\ \\ 
&=-\frac{\cos(n\pi)}{n}+\frac{\cos(-n\pi)}{n}\\ \\ 
&= 0
\end{align}
$$

Por último, el producto de ambas: 

$$\begin{align}
\int^{\pi}_{-\pi}\cos(nx)\sin(nx)dx
\end{align}$$

Acordándonos de la integral del seno de la diferencia y suma: 

$$\begin{align}
\sin((n-m)x)&=\sin(nx)\cos(mx)-\sin(mx)\cos(nx)\\  \\
\sin((n+m)x)&=\sin(nx)\cos(mx)-\sin(mx)\cos(nx)\tag{1}
\end{align}$$

Si se suman ambas, es posible resolver la integral: 

$$\begin{align}
\int^{\pi}_{-\pi}\left(\frac{\sin((n+m)x)-\sin((n-m)x)}{x}\right)dx&=0
\end{align}$$

Ahora, analizando otra integtral: 

$$\begin{align}\int^{\pi}_{-\pi}\cos^2(nx)dx&=\int^{\pi}_{-\pi}\frac{1+\cos(2nx)}{2}dx\\  \\
&=\frac{1}{2}\int^{\pi}_{-\pi}dx+\cancelto{0}{\frac{1}{2}\int^{\pi}_{-\pi}\cos(2nx)}dx\\  \\
&=\pi
\end{align}$$

Otra más; 

$$\begin{align}
\int^{\pi}_{-\pi}\sin^2(nx)dx&=\int^{\pi}_{-\pi}\frac{1-\cos(2nx)}{2}dx\\  \\
&=\frac{1}{2}\int^{\pi}_{-\pi}dx+\cancelto{0}{\frac{1}{2}\int^{\pi}_{-\pi}\cos(2nx)dx}
\end{align}$$

Ahora, viendo para un $n,m\in\mathbb{N}$, con $n\neq m$: 

$$\begin{align}
\int^{\pi}_{-\pi}\sin(nx)\sin(mx)dx&=\frac{1}{2}\int^{\pi}_{-\pi}\left(\cos((n-m)x))-\cos((n+m)x)\right)dx\tag{1}\\\\
&=0
\end{align}$$


Por último: 

$$\begin{align}
\int^{\pi}_{-\pi}\cos(nx)\cos(mx)dx&=\frac{1}{2}\int^{\pi}_{-\pi}\left(\cos((n+m)x)+\cos((n-m)x)\right)dx\tag{1}\\  \\
&=0
\end{align}$$

Posterior a esto, nos definimos un conjunto para luego definir un **producto interno**: 

$$L^2(-\pi,\pi)=\left\lbrace f:[-\pi,\pi]\to\mathbb{R}\;\bigg/\;\int^{\pi}_{-\pi}\vert f(x)\vert^2dx<\infty\right\rbrace$$

Notemos que cumple con ser un [[Espacios vectoriales|espacio vectorial]], y sobre este espacio se puede definir el producto interno: 

$$\langle f,g\rangle=\int^{\pi}_{-\pi}f(x)g(x)dx$$

Además, notemos que se tiene que $\lbrace 1,\cos nx,\sin nx\rbrace_{n\in\mathbb{N}}$ es un **[[Conjuntos|conjunto]] [[conjuntos ortogonales y ortonormales|ortogonal]]**. Vale decir, si hago el [[Producto punto|producto punto]] entre ellos da cero. 

Por lo tanto, volviendo al tema central, la pregunta a hacer es si dado $f:[-\pi,\pi]\to\mathbb{R}_C$ existen números reales tal que es posible escribirlo como: 

$$f(x)=\frac{a_0}{2}+\sum^{\infty}_{n=1}\left(a_n\cos(nx)+b_n\sin(nx)\right)\;\;a_0,b_0\in\mathbb{R}$$

Asumamos que esto [[Convergencia absoluta|converge]], es posible reescribir como: 

$$\begin{align}
\int^{\pi}_{-\pi}f(x)dx&=\int^{\pi}_{-\pi}\frac{a_0}{2}dx+\sum^{\infty}_{n=1}a_n\int^{\pi}_{-\pi}\cos(nx)dx+b_n\int^{\pi}_{-\pi}\sin(nx)dx\\  \\
a_0&=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)
\end{align}$$

Nuevamente, volviendo a la ecuación original, multiplicando por $\cos(x)$: 

$$\begin{align}
\int^{\pi}_{-\pi}\cos(x)f(x)dx&=\int^{\pi}_{-\pi}\frac{a_0}{2}\cos(x)dx+\sum^{\infty}_{n=1}a_n\int^{\pi}_{-\pi}\cos(x)\cos(nx)dx+b_n\int^{\pi}_{-\pi}\cos(x)\sin(nx)dx\\  \\
a_1&=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\cos(x)dx
\end{align}$$

Notemos que todas las integrales sinusoidales se cancelan por los cálculos anteriores. 

## Teorema 

Sea $f:[-\pi,\pi]\to\mathbb{R}$ una función tal que $f\in L^2[-\pi,\pi]$, es decir: 

$$\int^{\pi}_{-\pi}\vert f(x)\vert^2\;dx<\infty$$ 
Y, además, que sea **acotada**. Entonces, existen constantes: 

$$a_0,a_1,a_2,\dots,b_1,b_2,\dots,\in\mathbb{R}$$

Tal que la siguiente [[Series numéricas|serie]] converge: 

$$S(f)=\frac{a_0}{2}+\sum^{\infty}_{n=1}(a_n\cos{nx}+b_n\sin{nx})$$ 
En el caso que $f$ es [[Continuidad|continua]], entonces: 

$$S(f)(x)=f(x)$$

Y si $f$ no es continua en $x$, entonces la serie converge a: 

$$S(f)(x)=\frac{f(x^+)+f(x^-)}{2}$$ 
Donde: 

$$\begin{align}
f(x^+)&=\lim_{y\to x^+}f(y)\\  \\
f(x^-)&=\lim_{y\to x^-}f(y)
\end{align}$$


### Demostración 

Veamos si es posible calcular los valores de las constantes. Sea $x\in X$ tal que: 

$$f(x)=\frac{a_0}{2}+\sum^{\infty}_{n=1}(a_n\cos{nx}+b_n\sin{nx})$$

Integremos: 

$$\begin{align}
\int^{\pi}_{-\pi}f(x)\;dx&=\int^{\pi}_{-\pi}\frac{a_0}{2}+\int^{\pi}_{-\pi}\left(\sum^{\infty}_{n=1}[a_n\cos(nx)+b_n\sin(nx)]\right)\\  \\
&=\frac{a_0}{2}2\pi+\cancelto{0}{\int^{\pi}_{-\pi}\left(\sum^{\infty}_{n=1}[a_n\cos(nx)+b_n\sin(nx)]\right)}\\  \\
a_0&=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\;dx
\end{align}$$

Ahora, si multiplico por $\cos{x}$ e integro, se obtiene lo siguiente: 

$$\begin{align}
\int^{\pi}_{-\pi}f(x)\cos(x)\;dx&=\frac{a_0}{2}\int^{\pi}_{-\pi}\cos(x)\;dx+\sum^{\infty}_{n=1}\left(a_n\int^{\pi}_{-\pi}\cos(nx)\cos(x)\;dx+b_n\int^{\pi}_{-\pi}\sin(nx)\cos(x)dx\right)\\  \\
&=\cancelto{0}{\frac{a_0}{2}\int^{\pi}_{-\pi}\cos(x)\;dx}+\sum^{\infty}_{n=1}\left(a_n\int^{\pi}_{-\pi}\cos(nx)\cos(x)\;dx+b_n\int^{\pi}_\cancelto{0}{{-\pi}\sin(nx)\cos(x)dx}\right)\\  \\
&=a_1\int^{\pi}_{-\pi}\cos^2(x)\;dx\\  \\
&=a_1\pi
\end{align}$$

Luego, 

$$\begin{align}
a_1&=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\cos(x)\;dx\\  \\
\end{align}$$

Notemos, que si se hubiese multiplicado por $\cos{2x}$, el término a sobrevivir hubiera sido $a_2\pi$. Por $\cos{3x}, a_3\pi$, y así análogamente. Vale decir: 

$$a_n=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\cos(nx)\;dx\;\;\;\;\forall n\geq 1,n\in\mathbb{N}$$

Ahora, si se multiplica por $\sin(kx)$, con $k\in\mathbb{N}$ y se integra, se llega a algo muy parecido a lo anterior: 

$$b_k=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\sin(kx)\;dx$$

Así, si $f$ cumple la hipótesis, se tiene la **serie de Fourier de $f$ en el intervalo $[-\pi,\pi]$**, de la forma: 


$$S(f)(x)=\frac{a_0}{2}+\sum^{\infty}_{n=1}(a_n\cos{nx}+b_n\sin{nx})$$

Con: 

$$\begin{align}
a_0&=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\;dx\\  \\
a_n&=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\cos(nx)\;dx\\  \\
b_n&=\frac{1}{\pi}\int^{\pi}_{-\pi}f(x)\sin(nx)\;dx
\end{align}$$

#### Ejemplo 

Sea $f(x)=x$ con $x\in[-\pi,\pi]$. Calcular la serie de Fourier de $f$. 

$$\begin{align}
a_0&=\frac{1}{\pi}\int^{\pi}_{-\pi}x\;dx\\  \\
a_n&=\frac{1}{\pi}\int^{\pi}_{-\pi}x\cos(nx)\;dx\\  \\
b_n&=\frac{1}{\pi}\int^{\pi}_{-\pi}x\sin(nx)\;dx
\end{align}$$

Por lo tanto, para $a_0$: 

$$\begin{align}
a_0&=\frac{1}{\pi}\int^{\pi}_{-\pi}x\;dx\\  \\
&=\frac{x^2}{2\pi}\bigg\vert^{\pi}_{-\pi}\\  \\
&=\left(\frac{\pi^2}{2}-\frac{(-\pi)^2}{2}\right)\frac{1}{\pi}\\  \\
&=0
\end{align}$$

Además, para $a_n$: 

$$\begin{align}
a_n&=\frac{1}{\pi}\int^{\pi}_{-\pi}x\cos(nx)\;dx
\end{align}$$

Integrando por partes 

$$\begin{align}
u=x & &du=dx\\  \\
dv=\cos(nx)dx& &v=\frac{\sin(nx)}{n}
\end{align}$$

Por lo tanto, 

$$a_n=\frac{1}{\pi}\cancelto{0}{\left(\frac{x\sin(nx)}{n}\bigg\vert^{\pi}_{-\pi}-\int^{\pi}_{-\pi}\frac{\sin(nx)}{n}\;dx\right)}$$

Por último, para $b_n$: 

$$\begin{align}
b_n&=\frac{1}{\pi}\int^{\pi}_{-\pi}x\sin(nx)\;dx\\  \\
&=\frac{1}{\pi}\left(\frac{-x\cos(nx)}{n}\bigg\vert^{\pi}_{-\pi}+\cancelto{0}{\int^{\pi}_{-\pi}\frac{\cos(nx)}{n}\;dx}\right)\\  \\
&=\frac{1}{\pi}\left(-\frac{\pi\cos(n\pi)}{n}+\frac{(-\pi)\cos(-n\pi)}{n}\right)\\  \\
&=\frac{1}{\pi}\left(\frac{-2\pi\cos(n\pi)}{n}\right)\\  \\
&=-\frac{2}{n}(-1)^n\\  \\
&=(-1)^{n+1}\frac{2}{n}
\end{align}$$

Luego, 

$$f(x)=x=\sum^{\infty}_{n=1}(-1)^{n+1}\frac{2}{n}\sin(nx)$$


![[Fourier2.png|center]]






## Serie de Fourier para cualquier intervalo 

La serie de Fourier puede ser definida entre un intervalo $[-L,L]\to\mathbb{R}$ y con $y\in[-\pi,\pi]$ al hacer un cambio de variable $y=\pi x/L$. 

Sea $g(y)$ la función con el cambio de variable, entonces se llegaría a: 

$$\begin{align}
g(y)&=\frac{a_0}{2}+\sum^{\infty}_{n=1}a_n\cos(ny)+b_n\sin(ny)\\  \\
&=\frac{a_0}{2}+\sum^{\infty}_{n=1}a_n\cos(\frac{n\pi x}{L})+b_n\sin(\frac{n\pi x}{L})
\end{align}$$

Notemos que el término $a_0$ llegaría a ser: 

$$\begin{align}
a_0&=\frac{1}{\pi}\int^{\pi}_{-\pi}g(y)dy\\  \\
&=\frac{1}{\pi}\int^{L}_{-L}f(x)\frac{\pi}{L}dx\\  \\
&=\frac{1}{L}\int^{L}_{-L}f(x)dx
\end{align}$$

Para el término $a_n$ y $b_n$, haciendo el mismo desarrollo: 

$$\begin{align}
a_n&=\frac{1}{L}\int^{L}_{-L}f(x)\cos(\frac{n\pi x}{L})dx\\  \\
b_n&=\frac{1}{L}\int^{L}_{-L}f(x)\sin(\frac{n\pi x}{L})dx
\end{align}$$

#### Ejemplo: 

Sea la siguiente función: 

$$f(x)=\begin{cases}
1&0<x<1\\  \\
2&-1<x\leq 0
\end{cases}$$

Calculamos su serie de Fourier, tomando como $L=1$. Entonces, 

$$\begin{align}  
a_0&=\int^{1}_{-1}f(x)dx\\  \\
&=\int^{0}_{-1}2dx+\int^{1}_{0}dx\\  \\
&=3
\end{align}$$

Para el $a_n$: 

$$\begin{align}
a_n&=\int^{1}_{-1}f(x)\cos(n\pi x)dx\\  \\
&=\int^{0}_{-1}2\cos(n\pi x)dx+\int^{1}_{0}\cos(n\pi x)dx\\  \\
&=\frac{2\sin(n\pi x)}{n\pi}\bigg\vert^0_{-1}+\frac{\sin(n\pi x)}{n\pi}\bigg\vert^1_0\\  \\
&=0
\end{align}$$

Para $b_n$: 

$$\begin{align}
b_n&=\int^{0}_{-1}2\sin(n\pi x)dx+\int^{1}_{0}\sin(n\pi x)dx\\  \\
&=-2\frac{\cos(n\pi x)}{n\pi}\bigg\vert^0_{-1}-\frac{\cos(n\pi x)}{n\pi}\bigg\vert^1_0\\  \\
&=\frac{-1}{n\pi}+\frac{(-1)^n}{n\pi}
\end{align}$$

Entonces, la serie llegaría a ser: 

$$Sf(x)=\frac{3}{2}+\sum^{\infty}_{n=1}\frac{1}{n\pi}((-1)^n)\sin(n\pi x)$$

