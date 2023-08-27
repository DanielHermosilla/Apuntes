
Corresponde a un *"cascarón"* o [[Fronteras|frontera]] de un cuerpo $\mathbb{R}^3$ que es producido por una función en $\mathbb{R^2}$: 

![[Captura de pantalla 2023-08-27 a la(s) 11.39.11.png|center]]

Normalmente se define mediante una función $\mathbb{R}^2\to\mathbb{R}^3$. 

Una superficie $\Sigma$ de ecuación $\vec{X}=\vec{F}(u,v)$ con $(u,v)\in D$ es regular si $\vec{F}\in Dif(D)$ y el [[Producto vectorial|producto vectorial]] $\vec{F_u}\times\vec{F_v}\neq 0$ para todo punto en $D$. 

- Se dice que $\Sigma$ es una superficie suave cuando es regular y $\vec{F}\in C^1(D)$
- Se dice que $\Sigma$ es una superficie suave a trozos si es una unión finita de superficies. 

## Vectores tangentes 

Notemos que al recorrer la superficie por el dominio en $\mathbb{R}^2$ es posible modelar los [[Vector tangencial|vectores tangentes]] a la superficie al derivar parcialmente una variable por el dominio: 

![[Captura de pantalla 2023-08-27 a la(s) 11.42.24.png|center]]

## Plano tangente 

Ahora, si se quisiera obtener el **plano tangente** en cierto punto para la superficie, es necesario obtener un [[vectores|vector]] normal que se perpendicular a los vectores tangentes, vale decir, bajo el ejemplo de las imagenes, un vector tangencial a $\vec{d_2}$ y $\vec{d_1}$. Esto se obtiene al realizar el [[Producto vectorial|producto cruz]] entre $\vec{d_1}\times\vec{d_2}$. Si se quisiera resumir más aun, se podría definir como: 

$$\frac{\partial F}{\partial y}\times\frac{\partial F}{\partial x}$$