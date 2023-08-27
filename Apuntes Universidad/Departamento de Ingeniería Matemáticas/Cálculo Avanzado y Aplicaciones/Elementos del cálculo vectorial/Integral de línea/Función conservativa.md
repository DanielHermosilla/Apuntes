
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
&=f((x(b)),y(b))-f(x(a),y(a))\tag{TFC}
\end{align}$$