
Notemos la siguiente intuición; sea $f(x,y)$ una **función en varias variables**, vale decir, una función que depende implícitamente de otra variable $t$: 

$$\begin{align}
t&\to f\left(x(t),y(t)\right)
\end{align}$$

Si nos acordamos de la definición de [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Diferenciabilidad/Regla de la cadena|regla de la cadena]], podemos notar que al derivar $t$, se debe llegar a lo siguiente: 

$$\frac{d}{dt}\left[f\left(x(t),y(t)\right)\right]=\frac{\partial f}{\partial x}\cdot x'(t)+\frac{\partial f}{\partial y}\cdot y'(t)$$

Esto puede ser reescrito de otra forma como un [[Producto punto|producto punto]] entre las [[Derivada parcial|derivadas parciales]], llegando a: 


$$\frac{d}{dt}\left[f\left(x(t),y(t)\right)\right]=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)\cdot\left(x'(t),y'(t)\right)$$

Notemos que esto es algo **muy parecido** a la [[Integral de línea|integral de línea]], donde se multiplica la derivada de la parametrización por una función. Ahora, notemos que el [[vectores|vector]] de la izquierda, en realidad es el [[Gradiente y plano tangente|vector gradiente]]. Podríamos de hecho, intentar hacer la integral de línea de ésta. Sea $F(x,y)=\nabla f(x,y)$, entonces: 

$$\begin{align}
\int^{}_{C}F\cdot dr&=\int^{b}_{a}F(x(t),y(t))\cdot (x'(t),y'(t))\;dt\\  \\
&=\int^{b}_{a}\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)\cdot\left(x'(t),y'(t)\right)\; dt\\  \\
&=\int^{b}_{a}\frac{d}{dt}\left[f\left(x(t),y(t)\right)\right]\;dt\\  \\
&=f(x(b)),y(b))-f(x(a),y(a))\tag{TFC}
\end{align}$$

Notemos que esto **no depende de la parametrización de la [[Curvas|curva]]**, vale decir, hay una [[Independencia del camino|independencia del camino]]. 

# Definición 

Sea $F:\Omega\subseteq\mathbb{R}^n\to\mathbb{R}^n$, un [[Campos escalares y vectoriales|campo vectorial]] regular, $\Omega\subseteq\mathbb{R}^n$ un [[Conjuntos abiertos y cerrados|conjunto abierto]] y $C\subseteq\Omega$ una [[Curvas|curva regular a trozos]]. 

Supongamos que $\rho_0$ es el punto inicial de $C$ y $\rho_1$ es el punto final de $C$. Si existe $f:\Omega\subset\mathbb{R}^n\to\mathbb{R}$ tal que $F=\nabla f$, entonces: 

$$\int^{}_{C}F\cdot dr=f(\rho_1)-f(\rho_0)$$

A la función $f$ se le llamará el **potencial**. 

## Identificación del campo conservativo 

A partir de esta definición, la pregunta que surge es si a partir de una función $F$ es posible saber si es conservativo, vale decir, existe un $f$ tal que $F=\nabla f$. 

Sea $F=(F_1,F_2)$, entonces si $F$ es conservativo, entonces: 

$$F_1=\frac{\partial f}{\partial x}\;\land\; F_2=\frac{\partial f}{\partial y}$$

Además: 

$$\frac{\partial F_1}{\partial y}=\frac{\partial^2 f}{\partial y\partial x}\iff\frac{\partial F_2}{\partial x}=\frac{\partial^2 f}{\partial x\partial y}$$ 

Si la función $F$ es regular, entonces se cumple la igualdad por el **teorema de Schwartz**. Por lo tanto: 

Sea $F(x,y)=(F_1,F_2)=(2xy,x^2+y)$. Entonces, nos definimos lo siguiente: 

$$F_1=\frac{\partial f}{\partial x}\;\land\; F_2=\frac{\partial f}{\partial y}$$

Por ende, calculamos: 

$$\frac{\partial F_1}{\partial y}=\frac{\partial}{\partial y}(2xy)=2x\;\land\;\frac{\partial F_2}{\partial x}=\frac{\partial}{\partial x}(x^2+y )$$

Si $\frac{\partial F_1}{\partial y}=\frac{\partial F_2}{\partial x}\implies F=\nabla f$. Luego, $F=(F_1,F_2)$ es conservativo. 

## Calcular el campo conservativo

Cuando ya identificamos que $F$ cumple ser una función conservativa, vale decir, $F=\nabla f$, entonces ahora la pregunta es *¿Quién es $f$?*. Si $f$ existe, entonces debería ser la [[Integral en varias variables|integral]] respecto a la variable. 

#### Ejemplo 

Tenemos que $F=\nabla f=(2xy,x^2+y)=(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y})$, entonces, calculando primero la integral respecto a $x$: 

$$\int2xy\;dx=x^2y+C(y)\tag{1}$$

Donde la constante depende de $y$, ya que su derivada también es constante. No obstante, también se debe cumplir que: 

$$\frac{(1)}{\partial y}=\frac{\partial f}{\partial y}=x^2 + y$$

Equivalente a tener, al derivar $(1)$: 

$$x^2+C'(y)=\frac{\partial f}{\partial y}=x^2 + y$$

Esto nos dice que: 

$$C'(y)=y\implies C(y)=\frac{y^2}{2}+\text{cte}$$ 

Por lo tanto, de esta manera, $f(x,y)=x^2y+\frac{y^2}{2}+C$ 

Notemos que si tenemos un recorrido cerrado, vale decir, un circumferencia cerrada o cualquier otra cosa, al ser un campo conservativo, el punto de llegada será el punto de partida, por lo tanto, la integral valdrá cero. 

$$\oint F\cdot dr=0$$


#### Ejemplo 

Sea $F:\mathbb{R}^2\to\mathbb{R}^2$ tal que $F(x,y)=(2xy+3,x^2-1)$. Calcular: 

$$\int^{}_{C}F\cdot dr$$


