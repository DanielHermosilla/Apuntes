
Una distribución se podría graficar en función de dos [[Variable aleatoria continua|variables continuas]], como se ve en la siguiente imagen: 

![[Captura de pantalla 2023-05-22 a la(s) 08.38.48.png|center]]

Dos [[Variable aleatoria continua]] $X$ e $Y$ son **conjuntamente continuas** si existe una función $f_{xy}:\mathbb{R}^2\rightarrow\mathbb{R}_+$ tal que para todo [[Conjuntos|conjunto]] $A\subset\mathbb{R}^2$:

$$\mathbb{P}((X,Y)\in A)=\int\int_{A}f_{xy}(x,y)dx dy$$ 
A esta función se le llama **PDF conjunta**. También es tal que: 

$$f_{xy}(x,y)=\frac{\partial^2}{\partial x\partial y}F_{xy}(x,y)$$ 
Para todo $(x,y)\in\mathbb{R}^2$ donde la [[Función de Distribución Acumulada|CDF]] conjunta $F_{xy}$ es diferenciable. 

## Propiedades 

- $\int\int_{\mathbb{R}^2}f_{xy}(x,y)dxdy$ 

### Ejemplo 

Se tiene una flecha que cae en un blanco de forma circular de radio 1, en un punto aleatorio donde todas las areas tienen igual probabilidad de recibir una flecha. Si se ponen ejes cartesianos en el blanco, con origen en el centro y se denota por $(X,Y)$ la posición de la flecha, ¿cómo es la PDF conjunta? 

![[Captura de pantalla 2023-05-22 a la(s) 08.48.00.png|center]]


Por lo tanto, queremos imponer que: 

$$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f_{xy}(x,y)dxdy = 1$$ 
Notemos que si integramos el area de este círculo, nos debería dar $c\pi r^2=1$. Por lo tanto, $c=\frac{1}{\pi}$. 

Por lo tanto, la PDF conjunta llegaría a ser: 

$$f_{xy}(x,y)=\begin{cases}\frac{1}{\pi}&\text{si}\; x^2 + y^2= 1\\\\0&\text{si no}\end{cases}$$

Ahora, si se quisiera saber la probabilidad de que caiga a distancia $r$ o menos del centro: 

![[Captura de pantalla 2023-05-22 a la(s) 09.00.57.png|center]]

$$\int\int_{A}f_{xy}(x,y)dxdy$$ 
Donde $A=\lbrace(x,y)\in\mathbb{R}^2\;\bigg\vert\; x^2 + y^2\leq r^2\rbrace$ 

$$\iff\frac{1}{\pi}\int\int_{A}dxdy$$ $$\iff r^2$$ 
En resumen: 

$$\mathbb{P}((X,Y)\in A)=\begin{cases}r^2&\text{si}\;r\in[0,1]\\\\ 1&\text{si}\;r\geq 1\end{cases}$$ 