
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



