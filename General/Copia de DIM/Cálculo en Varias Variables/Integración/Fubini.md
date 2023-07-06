
El resultado del teorema de Fubini es el equivalente al primer y segundo [[Teorema Fundamental del Cálculo]], en el sentido que permite abordar de forma abstracta la integral, a partir de los teoremas generados por las funciones [[Extensión|extensión]]. Esto mismo hace simplificar la integral y reducir el problema al cálculo de [[Integral de Riemann|integrales de Riemann]] de solo una dimensión. 

### Motivación 

Supongamos que queremos integral la función $f(x,y) = x^2y^3$ sobre el cuadrado cerrado $R=[0,1]^2$ en $\mathbb{R}^2$. Es decir, la siguiente función: 

![[Captura de Pantalla 2023-01-09 a la(s) 17.20.54.png]]

Se puede ver que al realizar [[Particiones en varias variables|particiones]] y tratar de conseguir [[Suma superior e inferior|sumas inferiores y superiores]] no se llegará muy lejos, pues no es una función *"suave"*.  Por lo tanto, el primer paso intuitivo para calcular esta integral de $f$ sobre $R$ es una integral a dos variables independiente entre sí: 

$$\int^{}_{R}f=\int^{}_{[0,1]^2}f(x,y)dxdy$$ 
Para entender lo que se está haciendo es necesario entender como funciona la integración de $f$ sobre $R$, donde se recorre al cuadrado $R$ a través de pequeños *"parches"* para luego evaluar en $f$ un punto de tal parche, y para finalmente, ponderar tal resultado por el área del parche: 

![[Captura de Pantalla 2023-01-09 a la(s) 17.30.07.png|center]]

Luego, para integrar $f$ sobre $R$ se pueden tomar dos posibilidades para recorrer el *"dominio de integración"* (el cuadrado $R=[0,1]^2$). Se pueden tomar parches verticales para luego tomar las columnas sobre el rango horizontal o tomar parches horizontales para sumar las filas sobre el rango vertical. 

Ambos mecanismos corresponden al cálculo de [[Integral de Riemann|integrales de una dimensión]] de forma iterada. El mecanismo de la izquierda  corresponde a la integral iterada que integra primero en $y$ ("vertical") para luego integrar en el eje $x$ ("horizontal"), mientras que el de la derecha integra en $x$ para luego integrar en $y$.

![[Captura de Pantalla 2023-01-09 a la(s) 17.34.53.png|600|center]]

##### Integrando en y primero 

$$\int^{x=1}_{x=1}[\int^{y=1}_{y=0}x^2y^3dy]dx = \int^{x=0}_{x=0}x^2dx\int^{y=1}_{y=0}y^3dy$$
$$\iff\frac{1}{3}\times\frac{1}{4}=\frac{1}{12}$$ 
##### Integrando en x primero 

$$\int^{y=1}_{y=0}[\int^{x=1}_{x=0}x^2y^3dy]dx = \int^{y=1}_{y=0}y^3dy\int^{x=1}_{x=0}x^2dx$$ $$\iff\frac{1}{12}$$ 
Notemos que ambos resultandos coinciden numéricamente. 


## Teorema de Fubini 

Sea $R_1\subseteq\mathbb{R}^d$ y $R_2\subseteq\mathbb{R}^p$ dos rectángulos [[Conjuntos abiertos y cerrados|cerrados]] y sea $f:R_1\times R_2\rightarrow\mathbb{R}$ una función [[Integral en varias variables|integrable]]. Podemos introducir las funciones de una variable: 

$$L(x) = L\int^{}_{R_2}f(x,y)dy,\;\;x\in R_1$$ $$U(x)=U\int^{}_{R_2}f(x,y)dy,\;\;x\in R_1$$ 
Que están bien definidas, pues $f(x, ·)$ es acotada. Entonces $L$ y $U$ son integrables sobre $R_1$ y se tienen las igualdades: 

$$\int^{}_{R_1\times R_2}f=\int^{}_{R_1}L(x)dx=\int^{}_{R_1}(L\int^{}_{R_2}f(x,y)dy)dx$$ 
$$\iff\int^{}_{R_1\times R_2}f=\int^{}_{R_1}U(x)dx=\int^{}_{R_1}(U\int^{}_{R_2}f(x,y)dy)dx$$ 
Por lo tanto, el teorema de forma simple se puede escribir de la siguiente forma: 

Sea $R_1\subseteq\mathbb{R}^d$ y $R_2\subseteq\mathbb{R}^p$  dos [[Integral sobre rectángulos|rectángulos]] [[Conjuntos abiertos y cerrados|cerrados]] y sea $f:R_1\times R_2\rightarrow\mathbb{R}$ una función [[Funciones escalares|escalar]] y [[Continuidad en varias variables|continua]]. Entonces se tienen las igualdades: 

$$\int^{}_{R_1\times R_2}f=\int^{}_{R_1}(\int^{}_{R_2}f(x,y)dy)dx=\int^{}_{R_2}(\int^{}_{R_1}f(x,y)dx)dy$$ 
Esta expresión se puede usar recursivamente sobre dimensiones $n-esimas$. Por lo tanto, el orden de integración **puede ser cualquiera** siempre cuando se respeten los límites de integración. 

En casos donde la frontera tenga [[Medida nula|medida nula]] se va a integrar con la función [[Extensión|extensión]] ya que es equivalente. 

En particular, si $R=[a,b]\times[c,d]\subset\mathbb{R}^2$ entonces: 

$$\int^{}_{R}f=\int^{b}_{a}(\int^{d}_{c}f\;dy)\;dx=\int^{d}_{c}(\int^{b}_{a}f\;dx)\;dy$$ 
Si $R = I_1\times I_2\times\dots I_n$ es un rectángulo [[Conjuntos abiertos y cerrados|cerrado]] y $f$ es [[Continuidad en varias variables|continua]] en $R$, entonces: 

$$\int^{}_{R}f=\int^{}_{I_1}\int^{}_{I_2}\dots\int^{}_{I_n}f(x_1,x_2,\dots,x_n)\; dx_n\dots dx_2\; dx$$ 
### Ejemplo: 

Sea $R=[1,2]\times[0,1]$ un rectángulo en $\mathbb{R}^2$ y $f(x,y)=xy^2$. Es decir: 

![[Captura de Pantalla 2023-01-09 a la(s) 23.58.31.png|center|550]]

Calcular la integral $\int^{}_{R}f$. Claramente se tiene [[Continuidad en varias variables|continuidad]] sobre $R$, por lo que se tiene que $f$ es [[Integral en varias variables|integrable]] y bien definido. Por lo tanto, se aplica el teorema de Fubini donde: 

$$\int^{}_{R}f=\int^{1}_{2}(\int^{1}_{0}xy^2dy)dx$$ $$=\int^{2}_{1}xdx\int^{1}_{0}y^2dy$$ $$=\frac{1}{2}x^2\bigg\vert_{1}^{2}\times\frac{1}{3}y^3\bigg\vert_{0}^{1}$$
$$=\frac{3}{2}\times\frac{1}{3}=\frac{1}{2}$$ 
### ejemplo 

Calcular la integral de $f(x,y)=e^{x^2}$ sobre $A=\lbrace (x,y)\in [0,1]^2\; |\; y\leq x\rbrace$ 

![[Captura de Pantalla 2023-01-10 a la(s) 12.03.41.png|center]]

Notar que $A$ está limitado por $0\leq x\leq 1$ y $0\leq y\leq x$. Por lo tanto, la integral a calcular sería: 

$$\int^{}_{A}f(x,y) =\int^{1}_{0}\int^{x}_{0}e^{x^2}dydx$$ 
Así, la integral quedaría como: 

$$\int^{}_{A}f(x,y)=\int^{1}_{0}(\int^{1}_{y}e^{x^2}dx)\;dy$$ 
Conviene integrar primero en función de $y$, pues la otra no tiene primitiva: 

$$\int^{1}_{0}\int^{x}_{0}e^{x^2}dy\;dx=\int^{1}_{0}e^{x^2}y\bigg\lvert_{0}^{x}dx$$
$$\iff\int^{1}_{0}e^{x^2}x\;dx$$
$$\iff\frac{1}{2}e^{x^2}\bigg\lvert_{0}^{1}=\frac{1}{2}[e-1]$$ 
### Ejemplo 

Calcular el área de la elipse $\frac{(x)^2}{a^2} + \frac{(y)^2}{b^2}=1$

![[IMG_663D1DE46598-1.jpeg|center]]


Tenemos que lo siguiente define a $R$: 

$$-a\leq x\leq a$$ $$-b\sqrt{1-\frac{x^2}{a^2}}\leq y\leq b\sqrt{1-\frac{x^2}{a^2}}$$ 
Luego el área de nuestra región está dada por: 

$$\int^{}_{R}1 =\int^{a}_{-a}(\int^{b\sqrt{1-\frac{x^2}{a^2}}}_{-b\sqrt{1-\frac{x^2}{a^2}}}dy)\; dx = \int^{a}_{-a}2b\sqrt{1-\frac{x^2}{a^2}}dx$$ 
Esta integral se complica mucho, por lo tanto, se postula el [[Cambio de variable|teorema de cambio de variable]].