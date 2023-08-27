
Dada la [[Superficie|superficie]] $\Sigma$ de ecuación $\vec{X}=\vec{F}(u,v)$ con $(u,v)\in D$, si $\Sigma$ es suave y simple, el área de la misma se puede calcular mediante: 

$$A(\Sigma)=\int\int_D\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv$$

Con $D\subset\mathbb{R}^2$ acotado y de [[Fronteras|frontera]] de área nula, vale decir, un [[Conjuntos abiertos y cerrados|conjunto abierto]].

![[Captura de pantalla 2023-08-27 a la(s) 11.50.18.png|center]]

Acordándonos que el plano tangente se devine como $\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)$, entonces lo que se está haciendo es recorrer la superficie mediante el plano tangente a través todo el dominio. 

Ahora, notemos que al hacer el cálculo $\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv$ lo que se está haciendo, en realidad, es obtener la [[Norma en varias variables|norma]] del vector normal a la superficie. Y justamente esta norma representa el área del pequeño paralelógramo que se forma en el producto cruz. 

Un ejemplo trivial es el [[Producto vectorial|producto cruz]] de los vectores $\vec{v_1}=(1,0,0)$ y $\vec{v_2}=(0,0,1)$. Esto claramente forman un cuadrado de área $1$ entre ellos, y al hacer el producto $\vec{v_1}\times\vec{v_2}$ se obtiene el vector $\vec{v_3}=(0,1,0)$, que casualmente es perpendicular a $\vec{v_1}$ y $\vec{v_2}$ y además $\$
