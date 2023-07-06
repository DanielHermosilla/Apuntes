
Sea $X$ una $[[Variable aleatoria continua|variable aleatoria continua]], y sea el [[Conjuntos|conjunto]] $A\subset\mathbb{R}$ tal que $\mathbb{P}(X\in A)>0$. La función de densidad de probabilidad condicional de $X$ dado el [[Departamento de Ingeniería Industrial/Probabilidades/Axiomas y propiedades/Evento|evento]] $X\in A$ se define como: 

$$f_{x\vert A}(x)=\frac{\partial}{\partial x}\mathbb{P}(X\leq x\;\bigg\vert\; X\in A)=\begin{cases}\frac{f_x(x)}{\mathbb{P}(X\in A)}&\text{si}\; x\in A\\\\0&\text{si}\; x\notin A\end{cases}$$ 
De la misma forma, se puede definir la PDF condicional de la siguiente forma: 

$$f_{X\vert Y}(x\vert y)=\frac{f_{xy}(x,y)}{f_y(y)}$$ 
Para todo $x\in R_x$ e $y\in R_y$. 

### Ejemplo 

¿Cual es la densidad de $X$ dado $Y=y$? 

![[Captura de pantalla 2023-05-22 a la(s) 08.48.00.png|center]]



Primero notemos que $y\in[-1,1]$. Aplicando la definición: 

$$f_{x\vert y}(x\vert y)=\frac{f_{xy}(x,y)}{f_y(y)}$$ $$\iff\frac{\frac{1}{\pi}\mathbb{1}_{\lbrace x^2+y^2\leq 1\rbrace}}{\frac{2}{\pi}\sqrt{1-y^2}\mathbb{1}_{y\in [-1,1]}}$$ 
$$\iff\frac{\mathbb{1}_{\lbrace x^2+y^2\leq 1\rbrace}}{2\sqrt{1-y^2}}$$ 