
Uno podría definirse una [[función]] no negativa cuyo valor es $0$ si se tiene la certeza absoluta y un valor máximo si son eventos equiprobables. Además, imponer que las funciones son aditivas, vale decir, la pérdida de información de cada objeto se puede sumar. Notamos que se tiene la función logarítmica: 

$$\begin{align}
f(x,y)&=f(x)+f(y)&\frac{\partial x}{\partial}\\  \\
f'(x,y)\cdot y&=f'(x)&\frac{\partial y}{\partial} \\  \\
f''(x,y)\cdot xy+f'(x,y)&=0\\  \\
u&=xy\\  \\
f''(u)u+f'(u)&=0\\  \\
\left[uf'(u)\right]'&=0\\  \\
uf'(u)&=k\\  \\
f'(u)&=\frac{k}{u}\\  \\
f(x)&=k\ln x + C
\end{align}$$

Si imponemos que la certeza se da en $x=1$, entonces la función debería ser: 

$$f(x)=-k\ln(\frac{1}{x})$$

Con $k> 0$.

Ahora, si notamos la función $\ln\left( \frac{1}{x} \right)$: 


```functionplot
---
title: Función de pérdida de información
xLabel: x
yLabel: y
bounds: [0,1,0,10]
disableZoom: true
grid: true
---
y = log(1/x)

```

Notar que si $x\to 0$ se sabe que el evento no ocurre.  Por lo tanto, se introduce el **factor de peso**. Por ejemplo, se podría tener la función $x\ln x$ 

```functionplot
---
title: Función de pérdida de información
xLabel: x
yLabel: y
bounds: [0,1,0,0.4]
disableZoom: true
grid: true
---
y = x*log(1/x)

```

Notemos que los factores de peso siempre suman uno. Es decir, se podría tener la siguiente función de información: 

$$I(x)=0.6\cdot xln(x) + 0.4\cdot yln(y)$$

Aca notamos que los distintos pesos suman $1$, es decir, $0.6 + 0.4 = 1$. Si uno optimizara la función, encontraría que se llega al máximo cuando todos los [[Departamento de Ingeniería Industrial/Probabilidades/Axiomas y propiedades/Evento|eventos]] son [[Teoría de probabilidades|equiprobables]], es decir: 

$$\begin{align}
I_{max}&=-K\sum^{N}_{i=1}\frac{1}{N}\ln\left(\frac{1}{N}\right)\\  \\
&=K'\ln(N)\end{align}$$


## Sobre la elección de K 

En $1947$, el ingeniero *Shannon* ocupo a conveniencia el número $K=\frac{1}{\ln(2)}$, de ahí que la información se mide en **bits**. Esto se llama la **medida de información de Shannon**.

Está demostrado que al ocupar la función de Shannon, es decir, ante $\Omega$ datos y una función $I_{2}=\sum x_{i}\log_2x_i$, se puede decir que la busqueda de un objeto es de orden $O(log_2(\Omega))$. Esto se basa en el algoritmo de [[Busqueda binaria|busqueda binaria]]. 

Notemos que para el caso físico, donde se tienen muchas partículas, el orden $O(\log_2(\Omega))$ sigue siendo un número significativamente grande. 

En física se ocupa la **constante de Boltzmann** $(k_b)$, que equivale a la **constante de los gases** dividido con **la constante de Avogadro**, donde $k_b=1,38\times10^{-23}$ . Notemos que la constante de Gibbs se relaciona a la constante de Boltzmann de la siguiente forma: 

$$S=k_b\sum^{}_{i=1}x_i\ln(\frac{1}{x_i})$$


