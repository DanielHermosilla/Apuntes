
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
y = x

```

