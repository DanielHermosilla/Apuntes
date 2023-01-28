
Podemos considerar $\frac{\partial f}{\partial x_j}\;;\;j=1,\dots,n$ donde $f:\mathbb{R}^n\rightarrow\mathbb{R}$ como una función $\frac{\partial f}{\partial x_j}:\mathbb{R}^n\rightarrow\mathbb{R}$. 

Luego podemos considerar: 

$$\frac{\partial}{\partial x_k}(\frac{\partial f}{\partial x_j})$$ 
#### Notación 

Si $f:\mathbb{R}^3\rightarrow\mathbb{R}$: 

$$\frac{\partial}{\partial z}(\frac{\partial}{\partial y}(\frac{\partial}{\partial z})) = \frac{\partial^3 f}{\partial z\partial y\partial z}$$ 
# Definición 

Si $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ posee sus segundas [[Derivadas parciales|derivadas parciales]]: 

$$\frac{\partial^2 f}{\partial x_k\partial x_j}\;\forall k,j=1,\dots,n$$  
Y son [[Continuidad en varias variables|continuas]] en A; entonces diremos que $f$ es una función de clase $C^2$ en $A$. ($C^2(A)$) 

## Teorema 

Sea $A\subset\mathbb{R}^n$ abierto y $f:A\rightarrow\mathbb{R}$. Si $f\in C^2(A)$; entonces: 

$$\frac{\partial^2 f}{\partial x_i\partial x_j} = \frac{\partial^2 f}{\partial x_j\partial x_i}\;\forall j,i = 1,\dots,n$$ 
Es decir, ocurre una permutación entre ambas [[Derivadas parciales|derivadas parciales]]. 

### Ejemplo 

Consideremos una función definida en tramos como: 

$$f(x,y) = \frac{xy(x^2-y^2)}{x^2 + y^2}\;(x,y)\neq (0,0)$$ $$f(x,y) = 0\;(x,y) = (0,0)$$ 
Construyamos la función $\frac{\partial f}{\partial x}$. Note que para que los $(x,y)\neq(0,0)$ tenemos que la [[Derivadas parciales|derivada parcial]] de $f$ tenemos que: 

$$\frac{\partial f}{\partial x}(x,y) =\frac{[y(x^2 - y^2) + xy(2x)](x^2 + y^2) - [2x(xy)(x^2-y^2 )]}{(x^2 + y^2)^2}$$ 
Para $(x,y) = (0,0)$ lo sacaremos por definición: 

$$\lim_{h\rightarrow 0}\frac{f(h,0)-f(0,0)}{h} = 0$$ 
Se cumple, ya que antes de evaluar el límite ya tenemos que es cero. 

Así, la función $\frac{\partial f}{\partial x}$ es: 

$$\frac{\partial f}{\partial x}(x,y) = \frac{[y(x^2 - y^2) + xy(2x)](x^2 + y^2) - [2x(xy)(x^2-y^2 )]}{(x^2 + y^2)^2}\neq (0,0)$$ 
$$\frac{\partial f}{\partial x}(x,y) = 0 = (0,0)$$ 
Análogamente hacemos el mismo procedimiento para la [[Derivadas parciales|derivada parcial]] de $y$: 

$$\frac{\partial f}{\partial y}(x,y) = \frac{(x^3 + 2xy)(x^2 + y^2) - 2y(x^3y - xy^3)}{(x^2 + y^2)^2}\;\neq (0,0)$$ $$\frac{\partial f}{\partial y}(x,y)= 0 = (0,0)$$ 
Y la representación matricial sería la [[matriz Jacobiana]] que equivaldría al [[vector gradiente]]: 

$$\nabla f(0,0) = (\frac{\partial f(0,0)}{\partial x}, \frac{\partial f(0,0)}{\partial y})$$ 
Si hipotéticamente quisiera estudiar la [[Diferenciabilidad|diferenciabilidad]] en el punto $(0,0)$ podríamos hacer lo siguiente: 

$$\lim_{h\rightarrow 0} \nabla f(0,0)h = (\frac{\partial f(0,0)}{\partial x}, \frac{\partial f(0,0)}{\partial y})h$$

Luego, 

$$\frac{\partial^2 f}{\partial y\partial x}(0,0) = \frac{\partial}{\partial y}(\frac{\partial f}{\partial x})(0,0)$$ $$\iff\lim_{h\rightarrow 0}\frac{\frac{\partial f}{\partial x}(0,h) -\frac{\partial f}{\partial y}(0,0)}{h}$$
$$\iff\lim_{h\rightarrow 0}\frac{-h}{h}=-1$$ 
Similarmente, 

$$\frac{\partial^2 f}{\partial x\partial y}(0,0) = 1$$ 
Así, tenemos que: 

$$\frac{\partial^2 f}{\partial x\partial y}\neq\frac{\partial^2 f}{\partial y\partial x}$$ 
Pero no sería de clase $C^2$. 