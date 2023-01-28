
Sea $A\subset\mathbb{R}^n$ [[Conjuntos abiertos y cerrados|abierto]] y $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^m$ definimos la **[[Diferenciabilidad|derivada]] parcial** de $f$ en $x_0 \in A$ con respecto a la $i-esima$ variable por: 

$$\frac{\partial f}{\partial x_i}(x_0) = \lim_{h\rightarrow 0}\frac{f(x_0 + hl_i) - f(x_0)}{h}$$ 
Donde $l_i = (0,0,0,0,0,1 \;(\text{posición}\;l_i\;\text{del vector}),0,)$ Es decir, corresponde a la posición de la [[coordenadas]] de un [[vectores|vector]]. 


### Ejemplo 

Sea $f(x,y) = \frac{(x-1)(y-1)}{y}$. Calcular la derivada parcial en $x$ y en $y$ en $(2,1)$. 

Por definición, tenemos: 

$$\frac{\partial f}{\partial x} (2,1) = \lim_{h\rightarrow 0}\frac{f((2,1) + h(1,0)) - f(2,1)}{h} $$

$$\iff \lim_{h\rightarrow 0} \frac{f(2 + h, 1) - f(2,1)}{h} = 0$$

Si $(x,y)\in\mathbb{R}^2$ es arbitrario, tenemos: 

$$\frac{\partial f}{\partial x}(x,y) = \lim_{h\rightarrow 0} \frac{f(x + hy) - f(x,y)}{h}$$ $$\iff \lim_{h\rightarrow 0}\frac{\frac{(x + h - 1)(y-1)}{y} - \frac{(x-1)(y-1)}{y}}{h} $$ $$\iff \lim_{h\rightarrow 0} \frac{\frac{h(y-1)}{y}}{h} = \frac{y-1}{y}$$ 
Luego, $\frac{\partial f}{\partial x} (2,1) = 0$. 

La observación si queremos calcular la derivada parcial de $f$ respecto a $y$, tratamos como constante todo lo que no tiene que ver con $y$. Es decir: 

$$\frac{\partial f}{\partial y} = (x-1)[\frac{y-(y-1)}{y^2}] = \frac{(x-1)}{y^2} $$ 
Y, para ver el caso de $y^2$ se puede ocupar la definición de derivada parcial por límites. 

## Teorema 
 
Sea $A\subset\mathbb{R}^n$ [[Conjuntos abiertos y cerrados|abierto]], y $a\in A$. Consideremos $F:A\rightarrow\mathbb{R}^n$ con $F = (f_1, f_2, f_3, \dots)$. 

La [[matriz]] de $DF(a)$ respecto la [[Base|base canónica]] en $\mathbb{R}^n$ y $\mathbb{R}^m$, llamada [[matriz Jacobiana]] y denotada por $F'(a)$ es aquella que tiene a $\frac{\partial f_i}{x_j}(a)$ como elemento $ij$. Es decir, las filas sería tomar la primera función *i-esima* y la columna las variables *j-esimas*. Si la función va de $\mathbb{R}^n \rightarrow\mathbb{R}^m$ la [[matriz]] sería de dimensiones $m\times n$. Es decir: 

$$F'(a) =  \begin{equation}
		\begin{bmatrix}
			\frac{\partial f_1}{\partial x_1} (a) & \frac{\partial f_1}{\partial x_2} (a) & \frac{\partial f_1}{\partial x_3}(a) & \dots & \frac{\partial f_1}{\partial x_n}(a)\\ 
			 \frac{\partial f_2}{\partial x_1}(a) & \frac{\partial f_2}{\partial x_2}(a) & \frac{\partial f_2}{\partial x_3} (a)& \dots & \frac{\partial f_2}{\partial x_n}(a) \\ 
			 \vdots & \vdots & \vdots & \vdots & \vdots \\ 
			 \frac{\partial f_m}{\partial x_1} (a) & \frac{\partial f_m}{\partial x_2} (a) & \frac{\partial f_m}{\partial x_3}(a) & \dots & \frac{\partial f_m}{\partial x_n} (a)
		\end{bmatrix}
\end{equation}
		$$


El teorema anterior nos dice que si una función es [[Diferenciabilidad|diferenciable]], entonces todas sus [[Derivadas parciales|derivadas parciales]] existen. El recíproco **no es cierto**. 

$$ \text{Función diferenciable}\;\;\implies\;\;\text{Todas las derivadas parciales existen}$$ 

### Ejemplo 

Sea $f: \mathbb{R}^2\rightarrow\mathbb{R}$ la siguiente función divida por tramos: 

$$ f(x,y) = \frac{xy^2}{x^2 + 2y^4}\;\;\text{si}\;(x,y)\neq(0,0) $$ $$f(x,y) = 0\;\text{si}\;(x,y) = (0,0)$$ 
Notemos que no es [[Continuidad en varias variables|continua]] en $(0,0)$. 

Notemos que para el camino $\gamma (t) = (t^2,t)$ tenemos que $\lim_{t\rightarrow 0}\gamma(t)\rightarrow(0,0)$ 
Entonces: 
$$\lim_{t\rightarrow 0}\frac{t^4}{t^4 + 2t^4}$$ $$ \iff \frac{1}{3}\neq f(0,0) = 0$$ 
Y al no ser [[Continuidad en varias variables|continua]] en $(0,0)$ no sería [[Diferenciabilidad|diferenciable]], pero existen las [[Derivadas parciales|derivadas parciales]] de $f$ en ese punto: 


$$\frac{\partial f}{\partial x} (0,0) = \lim_{h\rightarrow 0}\frac{f(0+h,0) - f(0,0)}{h} = 0 $$

$$\frac{\partial f}{\partial y}(0,0) = \lim_{h\rightarrow 0} \frac{f(0,0+h)-f(0,0)}{h} = 0$$ 