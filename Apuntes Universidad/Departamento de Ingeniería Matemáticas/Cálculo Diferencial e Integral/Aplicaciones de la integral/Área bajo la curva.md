
Consideremos la función $f(x) = 2x$. Claramente, si calculamos su [[Integral de Riemann|integral]] entre -4 y 4 no obtendremos su área bajo la curva, si no más bien, el resultado del *área negativa* mas la *positiva*.

$$ \int^{4}_{-4} 2x \space dx = 0 $$

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: true
grid: true
---
y = 2x

```

Para calcular el área de una función que tiene intervalos negativos se puede definir, por lo tanto, de la siguiente forma: 
$$ \int^{b}_{a} |f(x)| \space dx = 0 $$

Simultaneamente, volviendo al ejemplo anterior, se podría trabajar la función por intervalos considerando el valor absoluto solo en los fragmentos negativos: 

$$ - \int^{0}_{-4}2x \space dx + \int^{4}_{0} 2x \space dx $$

Para esto, basta hacer un análisis de signos de la función. 

### Ejemplo 

El área entre medio de las funciones $f(x) = \sqrt{x}  \text{ y } g(x) = \frac{1}{2} (x-1)$ . 

Claramente hay que analizar entre intervalos, entonces nos podemos percatar que los intervalos importantes están en $x = 1$ (cambio de signo) y $x = 6$ (intersección).

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [0,10,-4,6]
disableZoom: true
grid: true
---
y = x^(1/2)
g = 1/2 * (x-1)
```

Entonces, para calcular el **área entre las funciones** calculamos lo siguiente: 

$$ - \int^{1}_{0} g(x) \space dx + \int^{6}_{0} f(x) \space dx - \int^{1}_{6} g(x) \space dx $$

Por mera casualidad, la podemos simplificar como: 

$$ \int^{6}_{0} f(x) \space dx - \int^{0}_{6} g(x)\space dx = \text{área entre las funciones}$$ 
#Aplicación 