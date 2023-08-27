
Dada la [[Superficie|superficie]] $\Sigma$ de ecuación $\vec{X}=\vec{F}(u,v)$ con $(u,v)\in D$, si $\Sigma$ es suave y simple, el área de la misma se puede calcular mediante: 

$$A(\Sigma)=\int\int_D\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv$$

Con $D\subset\mathbb{R}^2$ acotado y de [[Fronteras|frontera]] de área nula, vale decir, un [[Conjuntos abiertos y cerrados|conjunto abierto]].

![[Captura de pantalla 2023-08-27 a la(s) 11.50.18.png|center]]

Acordándonos que el plano tangente se devine como $\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)$, entonces lo que se está haciendo es recorrer la superficie mediante el plano tangente a través todo el dominio. 

Ahora, notemos que al hacer el cálculo $\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv$ lo que se está haciendo, en realidad, es obtener la [[Norma en varias variables|norma]] del vector normal a la superficie. Y justamente esta norma representa el área del pequeño paralelógramo que se forma en el producto cruz. 

Un ejemplo trivial es el [[Producto vectorial|producto cruz]] de los vectores $\vec{v_1}=(1,0,0)$ y $\vec{v_2}=(0,0,1)$. Esto claramente forman un cuadrado de área $1$ entre ellos, y al hacer el producto $\vec{v_1}\times\vec{v_2}$ se obtiene el vector $\vec{v_3}=(0,1,0)$, que casualmente es perpendicular a $\vec{v_1}$ y $\vec{v_2}$ y además $\vert\vert\vec{v_3}\vert\vert=1=\text{Área}$. 

Por ende, definimos el término **diferencial de área** como $\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv=d\sigma$. 

#### Ejemplo 

Calcular el área de superficie de la ecuación $z=xy$ con $(x,y)\in D=\lbrace(x,y)\in\mathbb{R}^2:x^2+y^2\leq 9\rbrace$ . 

En este caso, una ecuación [[vectores|vectorial]] para la superficie al parametrizar es: 

$$\vec{X}=\vec{F}(x,y)=(x,y,xy)\;\;\;(x,y)\in D$$

De aquí, se deduce que: 

$$\frac{\partial F}{\partial x}\times\frac{\partial F}{\partial y}= \begin{bmatrix}
\hat{i} & \hat{j} & \hat{k} \\
1 & 0 & y \\
0 & 1 & x
\end{bmatrix}=(-y,-x,1)$$ 
Vale decir, el [[Vector tangencial|vector tangencial]] que define el planto tangencial a la curva está definido por $(-y,-x,1)$. Ahora, si se calcula la [[Norma en varias variables|norma]] se obtiene: 

$$\vert\vert\frac{\partial F}{\partial x}\times\frac{\partial F}{\partial y}\vert\vert=\sqrt{1+x^2+y^2}$$ 

Entonces, para obtener el área de la superficie, se debe **integrar en el dominio** la norma: 

$$\begin{align}
\int\int_D\sqrt{1+x^2+y^2}\;dxdy
\end{align}$$

Se podría integrar directamente ocupando las restricciones pero el cálculo se hace muy difícil, entonces es conveniente ocupar [[Departamento de Ingeniería Matemáticas/Cálculo Diferencial e Integral/Aplicaciones de la integral/Coordenadas polares|coordenadas polares]]: 

$$\begin{align}
\int\int_D\sqrt{1+x^2+y^2}\;dxdy&=\int^{2\pi}_{0}\int^{3}_{0}\sqrt{1+r^2}\;r\;drd\theta\\  \\
&=\int^{2\pi}_{0}\frac{1}{3}\left(1+r^2\right)^{\frac{3}{2}}\bigg\vert^{3}_{0}d\theta\\  \\
&=2\pi\frac{10^{\frac{3}{2}}-1}{3}
\end{align}$$

Notemos que al hacer el [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Cambio de variable|cambio de variable]] se multiplicó por $r$, correspondiente al [[matriz Jacobiana|Jacobiano]] del cambio de coordenadas. 
