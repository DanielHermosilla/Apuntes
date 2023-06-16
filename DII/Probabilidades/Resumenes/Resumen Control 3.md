
# Probabilidad conjunta 

Muchas veces, en vez de querer estudiar la probabilidad de una variable por sí sola, es interesante estudiar el comportamiento de dos o más variables en conjunto, sean independientes o no. 

## Variables Discretas 

Para el caso discreto, similarmente a lo usual, se definen las siguientes características: 

### Probability Mass Function (PMF)

Sean dos variables aleatorias $X$ e $Y$, se define la PMF de dos variables aleatorias discretas bajo la siguiente fórmula: 

$$\begin{align}
\mathbb{P}_{XY}(x,y)&=\mathbb{P}(X=x,Y=y)\\\\
&=\mathbb{P}(X\cap Y)\end{align}$$ 
Vale decir, por lo tanto, que el rango de ambas variables aleatorias se define bajo un producto cartesiano de la siguiente manera: 

$$R_{XY}=\lbrace (x_i,y_j)\;\vert\; x_i\in R_X, y_j\in R_Y\rbrace$$ 
Donde se cumplen las propiedades básicas de toda distribución, en particular, la suma de cada valor debe ser 1: 

$$\sum_{(x_i,y_j)\in R_{XY}}\mathbb{P}_{XY}(x_y, y_j)=1$$ 
### Marginal Probability Mass Function (PMF Marginal)

La PMF conjunta otorga la información de todas las variables aleatorias actuando en conjunto. Pero, aun así, es posible obtener la PMF de una variable aleatoria en partícular ocupando la Ley de Probabilidades Totales: 

$$\begin{align} 
\mathbb{P}_x(x)&=\mathbb{P}(X=x)\\\\
&=\sum_{y_j\in R_y}\mathbb{P}(X=x, Y=y_j)&\text{(Probabilidades totales)}\\\\
&=\sum_{y_j\in R_y}\mathbb{P}_{XY}(x,y_j)\end{align}$$ 
En palabras simples, la PMF marginal es la suma de todas las variables aleatorias dejando como constante la variable a estudiar: 

$$\mathbb{P} _Y(Y)=\sum_{x_i\in R_X}\mathbb{P}_{XY}(x_i,y)$$ 
### Joint Cumulative Distributive Function (CDF)

Acordándonos que para una variable aleatoria nos definíamos una CDF como $F_X(x)=\mathbb{P}(X\leq x)$, entonces, si se tienen dos variables aleatorias y se quieren estudiar en conjunto, la CDF se define de la siguiente forma: 

$$\begin{align} 
F_{XY}&=\mathbb{P}(X\leq x,Y\leq y)\\\\
&=\mathbb{P}\left((X\leq x)\cap(Y\leq y)\right)\end{align}$$ 
Esto se puede ver reflejado gráficamente en la siguiente figura: 

![[Pasted image 20230615223744.png|center|400]]

Donde la CDF representa la región sombreada. 

### Marginal Joint Cumulative Distributive Function (CDF Marginal)

Similarmente al caso anterior, para poder estudiar variables aleatorias por sí mismasse puede establecer el siguiente argumento: 

$$\begin{align} 
F_{XY}(x,\infty)&=\mathbb{P}(X\leq x,Y\leq\infty)\\\\
&=\mathbb{P}(X\leq x)=F_X(x)\end{align}$$ 
Vale decir, para el caso discreto, se establecen los límites tendiendo al infinito: 

$$F_X(x)=F_{XY}(x,\infty)=\lim_{y\to\infty}F_{XY}(x,y)$$
Entonces, notemos que se cumplen las propiedades básicas para cualquier CDF: 

$$\begin{align}
F_{XY}(\infty,\infty)&=1\\\\
F_{XY}(-\infty,y)&=0,\;\;\;\forall y\in R_y\\\\
F_{XY}(x,-\infty)&=0,\;\;\;\forall x\in R_x 
\end{align}$$ 
### Condicionales e Independencia 

Previamente se había introducido el concepto de una probabilidad condicional, donde se derivó a la siguiente definición: 

$$\mathbb{P}(A\;\vert\; B)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(B)}$$ 
A partir de esta fórmula se puede derivar cualquier otro tipo de fórmula. En partícular, para el caso de variables conjuntas, se puede definir lo siguiente: 

$$\mathbb{P}(X\in C\;\vert\; Y\in D)=\frac{\mathbb{P}(X\in C, Y\in D)}{\mathbb{P}(Y\in D)}$$ 
Por lo tanto, se introduce el concepto de PMF condicional bajo la siguiente formulación: 

$$\begin{align}\mathbb{P}_{X\vert A}(x_i)&=\mathbb{P}(X=x_i\vert A)\\\\
&=\frac{\mathbb{P}(X=x_i\;\land\; A)}{\mathbb{P}(A)}\end{align}$$ 
Por ende, se define la PMF condicional para una variable $X$ e $Y$ cualquiera bajo el siguiente cálculo: 

$$\begin{align}\mathbb{P}_{X\vert Y}(x_i\vert y_j)&=\mathbb{P}(X=x_i\vert Y=y_j)\\\\
&=\frac{\mathbb{P}(X=x_i, Y=y_j)}{\mathbb{P}(Y=y_j)}\\\\ 
&=\frac{\mathbb{P}_{XY}(x_i,y_j)}{\mathbb{P}_Y(y_j)}
\end{align} $$ 
En palabras simples, el numerador llegaría a ser la intersección de que ocurra cierto evento $x_i$ dado que ocurrió $y_j$. Se divide por la probabilidad marginal de que ocurra ese evento dado por separado. Técnicamente esta fórmula se podría extrapolar aun más si se quisiera meter la definición de $\mathbb{P}_Y(y_j)$. En particular, reemplazando por la definición de PMF marginal se llega que: 

$$\mathbb{P}_{X\vert Y}(x_i\vert y_j)=\frac{\mathbb{P}_{XY}(x_i,y_j)}{\sum_{x_k\in R_X}\mathbb{P}_{XY}(x_k,y_j)}$$ 
A partir de eso, se pueden hacer varias equivalencias interesantes entre las probabilidades marginales y condicionales, específicamente una relación triangular entre probabilidad marginal, condicional y conjunta.  

Ahora, similarmente para la definición de **independencia** definida anteriormente, se puede concluir que dos variables $X$ e $Y$ son independientes si: 

$$\mathbb{P}_{XY}(x,y)=\mathbb{P}_X(x)\mathbb{P}_Y(y)\;\;\;\forall x,y\in R_{XY}$$ 
Lo mismo aplica la CDF: 

$$F_{XY}(x,y)=F_X(x)F_Y(y)\;\;\;\forall x,y\in R_{XY}$$

Intuitivamente se decir que la independencia de variables independientes es lo mismo a pedir únicamente la PMF marginal de la variable en cuestión: 

$$\mathbb{P}_{X\vert Y}(x_i\vert y_j) = \mathbb{P}_X(x_i)$$ 
### Esperanza condicional 

La esperanza condicional se define como una esperanza común, solo que únicamente se estaría computando una PMF condicional: 

$$\mathbb{E}[X\vert A]=\sum_{x_i\in R_x}x_i\cdot\mathbb{P}_{X\vert A}(x_i)$$ 
Similarmente, se puede llevar al caso para la condición de un evento en particular: 

$$\mathbb{E}[X\vert Y=y_j]=\sum_{x_i\in R_x}x_i\cdot\mathbb{P}_{X\vert Y}(x_i\vert y_j)$$ 
La esperanza condicional se extrapola y asocia directamente con la **Ley de Probabilidades Totales**. De hecho, acordándonos de la definición de ésta: 

$$\mathbb{P}(A)=\sum_{i}\mathbb{P}(A\cap B_i)=\sum_{i}\mathbb{P}(A\vert B_i)\mathbb{P}(B_i)$$ 
Ahora, notemos que esto se puede escribir de la siguiente forma ocupando los conceptos de distribución conjunta: 

$$\mathbb{P}(X\in A)=\sum_{y_j\in R_y}\mathbb{P}_{X\vert Y}(x\vert y_j)\mathbb{P}_Y(y_j)$$ 
Ahora, este mismo concepto se puede extrapolar al caso de la esperanza. Esto se denomina como **Ley de la Esperanza Total**. 

$$\mathbb{E}[X]=\sum_{y_j\in R_y}\mathbb{E}[X\vert Y=y_j]\cdot\mathbb{P}_Y(y_j)$$ 
Ahora, notemos que la esperanza condicional puede ser descrita como una función escalar, es decir, se puede formular como $g(Y)=\mathbb{E}[X\vert Y]$. 


### Funciones de dos variables aleatorias 

Analizar las funciones de una sola variable es prácticamente lo mismo a analizar una función de una variable. Supongamos que se tienen dos variables aleatorias discretas $X$ e $Y$ y supongamos que $Z=g(X,Y)$, con $g:\mathbb{R}^2\to\mathbb{R}$ entonces, la PMF de $Z$ sería lo siguiente: 

$$\begin{align}
\mathbb{P}_z(z)&=\mathbb{P}\left(g(X,Y)=z\right)\\\\
&=\sum_{(x_i,y_j)\in A_z}\mathbb{P}_{XY}(x_i,y_j)&A_z=\lbrace(x_i,y_j)\in R_{XY}:g(x_i,y_j)=z\rbrace
\end{align}$$ 
Es decir, la PMF llegaría a ser la suma de todos los valores de la PMF conjunta tal que el resultado sea el valor $z$ que se pide. 

Ahora, para la esperanza $\mathbb{E}[g(X,Y)]$ se puede ocupar directamente el cambio de variable: 

$$\mathbb{E}[g(X,Y)]=\sum_{x_i,y_j\in R_{XY}}g(x_i,y_j)\mathbb{P}_{XY}(x_i, y_j)$$ 
