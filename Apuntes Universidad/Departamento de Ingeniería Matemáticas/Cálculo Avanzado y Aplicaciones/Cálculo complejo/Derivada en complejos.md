
Sea $f:\Omega\subseteq\mathbb{C}\to\mathbb{C}$ una [[Función compleja|función compleja]]. Si $z=x+iy$, entonces: 

$$f(z)=u(x,y)+iv(x,y)$$

Sea $z_0=x_o+iy_0$, entonces $f$ es [[Departamento de Ingeniería Matemáticas/Cálculo Diferencial e Integral/Derivadas/Derivada|derivable]] en $z_0$ si y sólo si existe: 

$$f'(z_0)=\lim_{z\to z_0}\frac{f(z)-f(z_0)}{z-z_0}$$

Acordándonos, gráficamente, que el límite significa acercarse al punto dentro de todas las direcciones. 

![[IMG_D0992C4F659B-1.jpeg|center]]

Matemáticamente, si se aproxima únicamente en dirección horizontal: 

$$\begin{align}
f'(z_0)&=\lim_{h\to 0}\frac{f(z)-f(z_0)}{z-z_0}\\  \\
&=\lim_{h\to 0}\frac{u(x_0+h,y_0)+iv(x_0+h,y_0)-u(x_0,y_0)-iv(x_0,y_0)}{h}\\  \\
&=\lim_{h\to 0}\left(\frac{u(x_0+h,y_0)-u(x_0,y_0)}{h}+i\frac{v(x_0+h,y_0)-v(x_0,y_0)}{h}\right)\\  \\
&=\frac{\partial u}{\partial x}(x_0,y_0)+i\frac{\partial v}{\partial x}(x_0,y_0)\tag{1}
\end{align}$$

Ahora, de forma vertical: 

$$\begin{align}
f'(z_0)&=\lim_{h\to 0}\left(\frac{u(x_0,y_0+h)+v(x_0,y_0+h)-u(x_0,y_0)-iv(x_0,y_0)}{ih}\right)\\  \\
&=\lim_{h\to 0}\frac{u(x_0,y_0+h)-u(x_0,y_0)}{ih}+\frac{v(x_0,y_0+h)-v(x_0,y_0)}{h}\\  \\
&=\frac{1}{i}\frac{\partial u}{\partial y}(x_0,y_0)+\frac{\partial v}{\partial y}(x_0,y_0)\\  \\
&=\frac{\partial u}{\partial y}(x_0,y_0)-i\frac{\partial v}{\partial y}(x_0,y_0)\tag{2}
\end{align}$$

Así, si la función es derivable, se debe cumplir la **condición de Cauchy-Riemann**, es decir, que $(1)=(2)$

>[!example] Teorema: Condiciones de Cauchy-Riemann
>
>Sea $f:\Omega\subset\mathbb{C}\to\mathbb{C}$ una [[Función compleja|función compleja]], con
>
>$$f=u+iv$$
>
>Sea $z_0\in\Omega$ un [[Conjuntos abiertos y cerrados|conjunto abierto]]. 
>
>Si $f$ es derivable en $z_0$, entonces: 
>
>$$\begin{align} 
\frac{\partial u}{\partial x}(x_0,y_0)&=\frac{\partial v}{\partial y}(x_0,y_0)\\  \\
\frac{\partial v}{\partial x}(x_0,y_0)&=-\frac{\partial u}{\partial y}(x_0,y_0)
\end{align}$$

#### Ejemplo 

Sea la siguiente función compleja: 

$$f(z)=z^2=(x+iy)^2=(x^2-y^2)+2xyi$$

Por lo tanto: 

$$\begin{align}
\frac{\partial u}{\partial x}&=2x=\frac{\partial v}{\partial y}\\  \\
\frac{\partial v}{\partial x}&=2y=-\frac{\partial u}{\partial y}
\end{align}$$

Entonces verficia la condición de Cauchy-Riemann. 

#### Ejemplo 

Sea la siguiente función compleja: 

$$f(z)=\bar{z}=f(x+iy)=x-iy$$

Así, notar que: 

$$\begin{align}
\frac{\partial u}{\partial x}&=1\neq\frac{\partial v}{\partial y}=-1
\end{align}$$

Así, **los conjugados por lo general no son derivables**. 



Ahora, si se toman las condiciones de Cauchy-Riemann y se derivan por $x$ e $y$ respectivamente: 

$$\begin{align}
\frac{\partial^2 u}{\partial^2x}&=\frac{\partial v}{\partial x\partial y}\\  \\
-\frac{\partial^2 v}{\partial^2y}&=\frac{\partial v}{\partial x\partial y}
\end{align}$$

Si esto los sumamos entre sí, se llega que: 

$$\begin{align}
\frac{\partial^2 u}{\partial^2 x}+\frac{\partial^2 u}{\partial^2v }&=0\\  \\
\Delta u&=0
\end{align}$$

Análogamente, si se deriva en el otro sentido: 

$$\begin{align}
\Delta v&=0
\end{align}$$

Por ende, se puede concluir que si una [[Función compleja|función compleja]] es derivable, entonces el [[Laplaciano|laplaciano]] de $u$ y $v$ es $0$, es decir, son armónicas: 

$$\Delta u=\Delta v=0$$

Así, se llegan a las siguientes definiciones: 

- Se dice que si una función es derivable en $z_0$ se dirá que es **homolorfa** en tal punto. 

- Si la función es derivable en todos los complejos, se dice que $f$ **es entera**. 

- Si la función es derivable en todos los complejos salvo algunos puntos finitos, se dice que $f$ **es melomorfa**. 



## Función armónica conjugada 

Sea $z=x+iy$ y sea $f(z)=(x+iy)=(x^2-y^2)+iv(x,y)$

Notemos que $\nabla(x^2-y^2)=0$, vale decir, es candidata para poder ser [[Derivada en complejos|derivada en complejos]]. 

Queremos encontrar funciones $v(x,y)$ tal que la función $f(z)=(x^2-y^2)+iv(x,y)$ sea derivable en $\mathbb{C}$. Por lo tanto, se deben cumplir las condiciones de Cauchy-Riemann. Esto significa: 

$$\begin{align}
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}&\implies\frac{\partial v}{\partial y}=2x\\  \\
\frac{\partial u}{\partial y}=\frac{-\partial v}{\partial x}&\implies-\frac{\partial v}{\partial x}=-2y
\end{align}$$

Entonces, llegando a un proceso análogo para encontrar potenciales: 

$$\begin{align}
v(x,y)&=\int 2xdy\\  \\
&=2xy+c(x)\\  \\
\end{align}$$

Además: 

$$\begin{align}
\frac{\partial v}{\partial x}&=2y=2y+C'(x)\\  \\
C'(x)&=0\\  \\
\implies& C(x)=\text{Constante}
\end{align}$$

Así, 

$$v(x,y)=2xy+C$$ 
Por lo tanto, se puede decir que al tener la función $u$, se tiene una **única función** $v$ para ser diferenciable. Esto se llama **armónicas conjugadas** 