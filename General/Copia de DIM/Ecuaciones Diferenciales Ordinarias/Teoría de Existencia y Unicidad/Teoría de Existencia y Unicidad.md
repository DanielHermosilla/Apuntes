
Supongamos lo siguiente en $I$, siendo un intervalo real no reducido a un punto, donde 

$$x_0\in I,\ y_0\in\mathbb{R}\ \land\ f:I\times \mathbb{R}\rightarrow\mathbb{R}$$ 
Se define el **problema de Cauchy**. 

$$ 
\text{Problema de Cauchy}=\begin{cases} 
       y'(x) = f(x,y(x)) \\
      y(x_0) = y  
   \end{cases}
$$

Por lo tanto, el Teorema de Existencia y Unicidad dice que existe una única curva solución al problema de Cauchy que pasa por $(x_0,y_0)$. 

![[ExistenciaYUnicidad.jpeg|center]]


Donde $\exists ! y\in C^1(I)$, es decir, existe una única función continua con derivada continua en $I$ 

Las condiciones para que esto se cumpla es lo siguiente; sea la función 

$$f: I\times\mathbb{R}\rightarrow\mathbb{R}$$ 
Donde $f(x,y)$ tiene que ser [[Función continua|continua]] en $x$ e $y$ ser [[Lipschitz]]. Se dirá que tal solución sera el [[Teorema del punto fijo de Banach|punto fijo]] de la integral de la función.

Si la hipótesis no se llegará a cumplir, se podría acotar para que se cumpla la condición de [[Lipschitz|lipschitz localmente]]. 

### Ejemplo funciones objetivo

Sea $y': x + y$, por lo tanto, $f(x,y) = x + y$. Es [[Función continua|continua]] respecta a $x$ y si se [[Derivadas parciale|deriva en función de y]] se tiene que es acotado en función de $y$. Entonces cumple las condiciones para la Teoría de Existencia y Unicidad. 

Sea $f(x,y) = x + y^2$, acá también se verifica que es [[Función continua|continua]] respecto a $x$ pero la [[Derivadas parciales|derivada parcial]] en función de $y$ es $2y$. Esto no es acotado, ya que $y\in\mathbb{R}$., 

### Ejemplo 

$$ 
\text{Ejemplo}=\begin{cases} 
       y'(x) = cos^2(x) \\
      y(x_0) = y_0 
   \end{cases}
$$


Si vemos el gráfico de $\cos^2(x)$: 

```functionplot
---
title: Función coseno al cuadrado
xLabel: x
yLabel: y
bounds: [0,7,0,1]
disableZoom: true
grid: true
---
y = (cos(x))^2

```

Se plantea que la función solución en el punto específico es **única y existe**, sea lineal o no lineal. Es decir, dado un punto en el plano, se puede trazar una solución. 

Además, la derivada llegaría a ser $-2\sin(x)$, que verifica ser [[Lipschitz]] donde $L=2$.  

```functionplot
---
title: Función coseno al cuadrado y su derivada
xLabel: x
yLabel: y
bounds: [0,7,-5,5]
disableZoom: true
grid: true
---
y = (cos(x))^2
h = -2sin(x)
```


### Ejemplo 

Se tiene la siguiente función: 

$$f(x,y) = xy$$ 
Donde: 

$$\frac{\partial f}{\partial y} = x$$ 
Entonces, la constante de Lipschitz será: 

$$\max_{x\in I\;\land\;y\in\mathbb{R}}|\frac{\partial f}{\partial y}| = \max_{x\in I\;\land\;y\in\mathbb{R}}|x|\leq L$$ 
Si $I$ es un intervalo acotado. Y se puede aplicar el [[Teoría de Existencia y Unicidad|TEU]], es decir $\exists !y\in\mathbb{C}^1(I)$ 


### Ejemplo 

Se tiene la siguiente función: 

$$y' = \frac{xy}{1 + x^2}\ x\in I$$ $$\implies f(x,y) = \frac{xy}{1 + x^2}$$ 
La [[Derivadas parciales|derivada parcial]] en función de $y$ sería: 

$$\frac{\partial f}{\partial y} = \frac{x}{1 + x^2}$$ 

Entonces, el máximo de la función llegaría a ser: 

$$\max_{x\in I}|\frac{x}{1 + x^2}|\leq L$$ 
[[Derivada|Derivando]] en función de $x$, se encuentra el máximo que es $\frac{1}{2}$. 



## Demostración 

Si $\phi: E\rightarrow E$ es una función de [[Lipschitz]], es decir, $|\phi(y)-\phi(z)| \leq L|y-z|, L<1$, entonces existe un único $y$ tal que $y* = \phi(y*)$. 

Primero, demostrando el [[Teorema del punto fijo de Banach]], se puede definir una **iteración de Picard**: 

```functionplot
---
title: Teorema punto fijo
xLabel: x
yLabel: y
bounds: [0,3,0,5]
disableZoom: true
grid: true
---
y = x
h = x/0.5 - 1.5


```

Es decir, $y_{n+1} = \phi (y_n)$, $h\leq 0$, $y_0$ dado en $E$. La idea es que si $y_n\rightarrow y_{\infty}$ entonces $y_{n+1}\rightarrow y_{\infty}$ y además $\phi(y_n)\rightarrow\phi(y_{\infty})$ entonces $y_{n+1}\rightarrow y_{\infty}$ y además $\phi (y_n)\rightarrow\phi (y_{\infty})$ porque $\phi$ es continua. 

Entonces $y_{\infty} = \phi (y_{\infty}) \implies y_{\infty}$. 

Ocupando la condición de Lipschitz se llega que: 

$$|y_{\infty} - y_\star | = |\phi(y_\infty) - \phi(y*)|\leq |y_\infty - y*| \implies y_\infty = y*$$ 
Ahora, para probar que $y_n$ es de Cauchy, $|y_{n+1}-y_n|\rightarrow 0$. 

Entonces, se puede reescribir como: 

$$|y_{n+k}-y_n|\leq |y_{n+k} - y_{n+k-1}| + |y_{n+k-1}-y_{n+k-2}| + \dots + |y_{n+1}-y_n|$$ 
$$|y_{n+k}-y_n|\leq |\phi(y_{n+k-1}) - \phi(y_{n+k-2}| + \dots + |\phi(y_n)-\phi(y_{n-1}))$$ 
$$|y_{n+k}-y_n|\leq L|y_{n+k-1}-y_{n+k-2}| + L|y_{n+k-2} - y_{n+k-3}| + \dots + L|y_n - y_{n+1}|$$ 
Se podría seguir recursivamente hasta llegar a: 

$$|y_{n+k}-y_n|\leq L^{n+k}|y_1 - y_0| + L^{n+k-2}|y_1-y_0| + \dots + L^n|y_1 - y_0|$$ 
Y se tiene una **suma geométrica**: 

$$|y_{n+k}-y_n| = L^n\ |y_1 - y_0|\ \sum^{k-1}_{j=0}L^j = \frac{L^n}{1-L}(1-L^k)\ |y_1 - y_0|\rightarrow 0$$ 
Entonces, como $L<1$, por lo tanto es convergente, por lo tanto, es una [[Sucesión de Cauchy|sucesión de Cauchy]] y por conclusión es un [[Espacio de Banach|espacio de Banach]]. 

Dado que se demostró el punto fijo, ahora, volviendo al problema de Cauchy se define lo siguiente: 

$$ 
\text{Problema de Cauchy}=\begin{cases} 
       y'(x) = f(x,y(x)) \\
      y(x_0) = y  
   \end{cases}
$$

Equivalente a: 

$$\int_{x_0}^{x}y' = \int^{x}_{x_0}f(s,y(s))ds$$ $$y(x)-y(x_0) = \int^{x}_{x_0}f(s,y(s))ds$$ $$y(x) = y_0 + \int^{x}_{x_0}f(s,y(s))ds = \phi(y)$$ $$y(x) = \phi(y(x))^{x_0}\ \ \ \text{Teorema del Punto Fijo}$$ 
Entonces, basta mostrar que $\phi(y(x))$ menor a una constante. Sea $\phi$ la siguiente función: 

$$\phi:\mathbb{C}^0(I)\rightarrow\mathbb{C}^0(I)\ \ x\in I$$
$$y(x)\rightarrow \phi(y(x)) = y_0 + \int^{x}_{x_0}f(s,y(s))ds$$ 
Vale decir que, gracías la hipótesis del TEU, $f(s,y(s))$ es continua. 

Para que cumpla que las [[Sucesión de Cauchy|sucesiones de Cauchy]] convergan se debe establecer una [[Norma en varias variables|norma]], que en este caso será la norma infinito y que el intervalo sea cerrado y acotado, vale decir: 

$$||y||_\infty = \max_{x\in I}|y(x)|$$ 
Entonces, todas las sucesiones de Cauchy son convergentes, $E=\mathbb{C}^0(I)$ es [[Espacio de Banach|Banach]]. 

$$\phi(y(x))-\phi(z(x))=\int^{x}_{x_0}f(s,y(s)) - f(s,z(s))dx$$ 
Y aquí se podría ocupar la condición de [[Lipschitz]]. 

$$|\phi(y(x))-\phi(z(x))|\leq \int^{x}_{x_0}|f(s,y(s))-f(s,z(s))|ds\ \ \ \text{Hipótesis del TEU}$$$$|\phi(y(x))-\phi(z(x))|\leq L\int^{x}_{x_0}|y(s)-z(s)|ds\leq L\max|x-x_0|\ ||y-z||_\infty$$ 
Pero $L\ \max|x-x_0|$ no siempre es menor que uno. Entonces, se cambia la [[Norma en varias variables|norma]] que dependa de la constante de [[Lipschitz]]. 

$$||y||_{\infty , L} = \max_{x\in I}|y(x)|e^{-2L(x-x_0)}$$ 
Donde la exponencial decrece pero siempre es positiva. Por lo tanto, el espacio de las funciones [[Continuidad en varias variables|continuas]] sigue siendo de [[Espacio de Banach|Banach]] en la [[Norma en varias variables|norma]] definida. Entonces, redefiniendo: 

$$|\phi(y(x))-\phi(z(x))|\leq L\int^{x}_{x_0}|y(s)-z(s)|ds \ e^{-2L(s-x_0)}\ e^{2L(s-x_0)}$$
Al multiplicar por 1 al por $e^{-2L(s-x_0)}\ e^{2L(s-x_0)}$ entonces se puede llegar que: 

$$|\phi(y(x))-\phi(z(x))|\leq L ||y-z||_{\infty, L} \int^{x}_{x_0}e^{2L(s-x_0)}ds$$

Resolviendo la integral, siguiendo la desigualdad y multplicando por la el resultado de ésta se llega que: 

$$e^{-2L(x-x_0)}|\phi(y(x))-\phi(z(x))|\leq \frac{1}{2} ||y-z||_{\infty, L} $$

Y por lo tanto es de [[Lipschitz]] con $L=\frac{1}{2}$ 