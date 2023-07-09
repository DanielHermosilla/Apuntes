Acordándonos de la [[Integral de Riemann|integral de Riemann]] se definían dos condiciones básicas: 
1. La función **debe** estar definida en el intervalo [a,b]
2. La función **debe** ser acotada 

Por lo tanto, queremos estudiar los casos donde estos criterios no se cumplen, donde podemos tener un gráfico con **asíntotas vérticales** o funciones que tienden al infinito. 

```functionplot
---
title: Función no Riemann - Integrable
xLabel: 
yLabel: 
bounds: [0,5,0,10]
disableZoom: true
grid: true
---
y = 1/x

```

Por lo tanto, nos podemos poner en dos casos: 
1. Cuando la función tiende a infiníto 
2. Cuando la función no es acotada 

### [[Integrales de primera especie]]

Esta se refiere a las integrales que tienden al infiníto horizontalmente, como lo es en el siguiente caso: 

```functionplot
---
title: Función de primera especie
xLabel: 
yLabel: 
bounds: [2,10,0,4]
disableZoom: true
grid: true
---
y = 1/(0.2x)

```

Podemos ver que la imagen está acotada entre $[0, 2.5]$ pero la función va avanzando infinitamente. Si quisieramos obtener la integral la definiriamos de la siguiente forma: 

$$ \int^{\infty}_{2} f(x) \space dx $$

Lo que se hace, al no saber integrar con límites infinítos, es definir un "x" cualquiera en el intervalo en cuestión y hacerlo tender al infínito, es decir: 

$$ \lim_{x \rightarrow \infty} \int^{x}_{2} f(t) \space dt \space \space \space \space \space \space x \in [2, \infty) $$

##### Ejemplo 

Sea la función 
$$ f(x) = \frac{1}{x^{\alpha}} \space , \space \alpha \in \mathbb{R} \space , \space x \in [1, +\infty) $$
Por la forma en que está definida x, no tendremos **asíntotas verticales**. Entonces, reescribiendo: 

$$ \lim_{m \rightarrow \infty} \int^{m}_{1} \frac{1}{x^\alpha} \space dx = \frac{1}{1-\alpha} * \frac{1}{x^{\alpha -1}} \bigg\rvert^{m}_{1} $$

Si $\alpha > 1$ obtenemos lo siguiente al evaluar el límite, posterior a evaluar los límites inferiores y superiores (m y 1): 
$$ \frac{1}{\alpha - 1} $$ Pero, si $\alpha \leq 1$  el límite no existe. 

Por lo tanto, la función **tiene integral** cuando $\alpha > 1$, ya que su límite si existe. 

### [[Integrales de segunda especie]]

Es cuando la imagen no está acotada, es decir, existen **asíntotas verticales**. Análogo a lo anterior, hacemos tender el límite: 
$$ f(x) = \frac{1}{(x-3)^2} \space \space x \in (0,1]$$

```functionplot
---
title: Función de segunda especie
xLabel: 
yLabel: 
bounds: [0,3,0,100]
disableZoom: true
grid: true
---
y = 1/(x-3)^2

```

Normalmente la integral sería: 
$$\int^{3}_{0} f(x) \space dx$$

Bajo este concepto, se haría el siguiente cambio: 

$$\lim_{x \rightarrow 3^{-}} \int^{x}_{0} f(t) \space dt $$ #concepto