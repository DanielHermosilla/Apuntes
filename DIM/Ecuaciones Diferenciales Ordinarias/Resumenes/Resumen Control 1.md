
Una EDO es básicamente una ecuación que contiene como incógnita una función. Dado esto, la incógnita tiene una variable **independiente** y **dependiente**. En este caso, se trata de buscar las soluciones que dan la relación entre ambas variables. Existen formas elementales para la resolución de éstas: 

## Ecuaciones diferenciales elementales 

Consisten en, básicamente, las ecuaciones representadas por una [[Ecuación diferencial lineal de primer orden|derivada]], vale decir, de la siguiente forma: 

$$ a_1(x)y' + a_0(x)y = f(x)\ \ ,\;x\in I$$ 
La resolución de este tipo de ecuaciones se les llamara **resoluciones elementales**: 

### Integración directa 

Son las más fáciles, donde se tiene la siguiente forma: 

$$y'(x) = f(x)$$ 
Basta con únicamente [[Integral de Riemann|integrar]] en función de $x$ para obtener la ecuación deseada. 

### Separación de variables 

Son de la forma: 

$$y'(x) = f(x)g(y)$$ 
Vale decir, se tiene una multiplicación entre los componentes no derivados. Aquí basta con pasar dividiendo $g(y)$ (obviamente argumentando que $g(y)\neq 0$) y hacer una integral por [[Teorema Fundamental del Cálculo]]. 

$$\frac{y'(x)}{g(y)}=f(x)$$ 
Entonces se integra **en función de *x***: 

$$\int\frac{y'(x)}{g(y)}=\int f(x)$$ 
Y aplicando el cambio de variable $u=y(x)\implies du=y'(x)$ se llega a lo siguiente: 

$$\int\frac{1}{g(y)}dy = \int f(x)dx$$

### Factor integrante 

Sea una EDO de la siguiente forma: 

$$a_1(x)y' + a_0(x)y = f(x)$$ 
Entonces el método de factor integrante consiste en **integrar $a_0$ en función de x**. Luego, multiplicar ambos lados por el resultado de la integral elevado a la función exponencial, es decir: 

$$e^{\int a_0}(a_1(x)y' + a_0(x)y) = f(x)e^{\int a_0}$$ 
Si nos fijamos, esto es equivalente a tener: 

$$\iff(a_1(x)y(x)e^{\int a_0})' = f(x)e^{\int a_0}$$ 
Entonces aplicando [[Teorema Fundamental del Cálculo]] se llega que: 

$$a_1(x)y(x)e^{\int a_0} = \int (f(x)e^{\int a_0})$$ 
Bastaría con despejar $y(x)$. 

Por lo tanto, principalmente los métodos de resolución **elementales** llegarían a ser separación de variables y factor integrante. 

## Ecuaciones reductibles  

Son aquellas que a partir de ciertos cambios de variables se pueden llegar a comportar como una ecuación elemental: 

