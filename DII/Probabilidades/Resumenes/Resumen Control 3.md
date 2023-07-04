
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
Ahora, notemos que la esperanza condicional puede ser descrita como una función escalar, es decir, se puede formular como $g(Y)=\mathbb{E}[X\vert Y]$. Es decir, $g(y)$ es una función cuyo valores puede tomar la esperanza condicional de para distintos valores de $y$: 


$$E[X\vert Y]=\begin{cases}\mathbb{E}[X\vert Y=y_1]&\text{con probabilidad}\;\mathbb{P}(Y=y_1)\\\\
\mathbb{E}[X\vert Y=y_2]&\text{con probabilidad}\;\mathbb{P}(Y=y_2)\\\\
\vdots&\vdots\end{cases}$$ 
Por último, se postula la **regla de esperanzas iteradas** donde se llega a lo siguiente, y se puede demostrar por definición: 

$$\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\vert Y]]$$ 

### Varianza condicional 

Similarmente al caso de la esperanza, se puede definir la varianza condicional, que corresponde a la varianza de $X$ en el espacio condicional conocido $Y=y$. Nuevamente se puede describir por definición donde: 

$$\begin{align}Var(X\vert Y=y)&=\mathbb{E}\left[(X-\mu_{X\vert Y}(y))^2\vert Y=y\right]\\\\
&=\sum_{x_i\in R_x}\left(x_i-\mu_{X\vert Y}(y)\right)^2\mathbb{P}_{X\vert Y}(x_i)\\\\
&=\mathbb{E}\left[X^2\vert Y=y\right]-\mu_{X\vert Y}(y)^2\\\\&=\mathbb{E}\left[X^2\vert Y=y\right]-\left(\mathbb{E}[X\vert Y=y]\right)^2\end{align}$$ 
Donde $\mu_{X\vert Y}(y)=\mathbb{E}[X\vert Y=y]$. Básicamente, se llega a la misma fórmula de varianza de siempre. Ahora, de la forma anterior con la **Ley de la Esperanza Total**, se puede definir de la misma forma la **Ley de la Varianza Total**, donde: 

$$Var(X)=\mathbb{E}[Var(X\vert Y)]+Var(\mathbb{E}[X\vert Y])$$ 
La forma intuitiva de ver la Ley de la Varianza Total es pensar en una población dividida en distintos grupos. En particular, en un experimento aleatorio se puede escoger a una persona y ver su altura. Este resultado se denominaría $X$. Por el otro lado, se tiene otra variable $Y$ donde el valor depende del pais de la persona, donde $Y=1,2,3,\dots,n$ el número de países en el mundo. 

Por lo tanto, notemos que $Var(X\vert Y=i)$ es la varianza de $X$, es decir la altura, en un país determinado $i$. Por ende, su esperanza sería el promedio de las varianzas de tal país. 

En el otro término se tendría de la altura en distintos países. 

### Funciones de dos variables aleatorias 

Analizar las funciones de una sola variable es prácticamente lo mismo a analizar una función de una variable. Supongamos que se tienen dos variables aleatorias discretas $X$ e $Y$ y supongamos que $Z=g(X,Y)$, con $g:\mathbb{R}^2\to\mathbb{R}$ entonces, la PMF de $Z$ sería lo siguiente: 

$$\begin{align}
\mathbb{P}_z(z)&=\mathbb{P}\left(g(X,Y)=z\right)\\\\
&=\sum_{(x_i,y_j)\in A_z}\mathbb{P}_{XY}(x_i,y_j)&A_z=\lbrace(x_i,y_j)\in R_{XY}:g(x_i,y_j)=z\rbrace
\end{align}$$ 
Es decir, la PMF llegaría a ser la suma de todos los valores de la PMF conjunta tal que el resultado sea el valor $z$ que se pide. 

Ahora, para la esperanza $\mathbb{E}[g(X,Y)]$ se puede ocupar directamente el cambio de variable: 

$$\mathbb{E}[g(X,Y)]=\sum_{x_i,y_j\in R_{XY}}g(x_i,y_j)\mathbb{P}_{XY}(x_i, y_j)$$ 
## Variables Continuas 

En el caso para las variables continuas se cumple un estandar y similitud bien parecido al de las variables discretas. De hecho, muchas definiciones se extrapolan hacia el otro lado pero reemplazando sumatorias con integrales y así sucesivamente. Por lo tanto, las demostraciones de muchos teoremas o propiedades son en realidad. 

### Joint Probability Density Function (PDF)

Se dice que dos variables aleatorias continuas son conjuntamente continuas si existe una función $f:\mathbb{R}^2\to\mathbb{R}$ tal que para cualquier conjunto $A\in\mathbb{R}^2$ se tiene que: 

$$\mathbb{P}\left((X,Y)\in A\right)=\int\int_{A} f_{XY}(x,y)dxdy$$

La función $f_{XY}(x,y)$ es denominada como la PDF conjunta de $X$ e $Y$. En este caso, el rango se define como el siguiente: 

$$R_{XY}=\lbrace(x,y)\;\vert\;f_{X,Y}(x,y)>0\rbrace$$ 
Esta definición, al igual que en el caso de las variables aleatorias continuas, deben cumplir lo siguiente: 

$$\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f_{XY}(x,y)dxdy=1$$ 
### Marginal Joint Probability Density Function (PDF Marginal)

Es posible encontrar la PDF marginal de las variables aleatorias conjuntas de la misma forma que se explicó en el caso discreto, lo único sería que en vez de definirse en una suma se estaría definiendo sobre una integral: 

$$f_X(x)=\int_{-\infty}^{\infty}f_{XY}(x,y)dy\;\;\;\forall x\in R_{XY}$$ 

### Joint  Cumulative Distribution Function (CDF)

Aplicando la definición de CDF, la CDF en variables conjuntas se define simplemente como lo siguiente: 

$$F_{XY}=\mathbb{P}(X\leq x, Y\leq y)$$ 
Esto cumple varias propiedades, aun así, la más importante es la de **independencia**: Si $X$ e $Y$ son independientes, entonces $F_{XY}(x,y)=F_X(x)F_Y(y)$

### Condicionales e Independencia 

Nuevamente, si se aplica la definición de independencia, se llega a las siguiente fórmula para la PDF condicional para cierto evento: 

$$f_{X\vert A}(x)=\frac{\partial}{\partial x}\mathbb{P}(X\leq x\vert X\in A)=\begin{cases}\frac{f_X(x)}{\mathbb{P}(X\in A)}&\text{si}\;x\in A\\\\0&\text{si no}\end{cases}$$  
Y por ende, de la misma forma, se puede definir la PDF condicional de la siguiente forma: 

$$f_{X\vert Y}(x\vert y)=\frac{f_{XY}(x,y)}{f_Y(y)}$$ 

Ahora, para el caso de la CDF, si bien se podría llegar a integrar sobre la PDF, se puede definir de la siguiente forma para una variable $X$ cuyo rango es $R_x = (a,b)$

$$F_{X|A}(x)=\begin{cases}1&x>b\\\\\frac{F_X(x)-F_X(a)}{F_X(b)-F_X(a)}&a\leq x<b\\\\0&x<a\end{cases}$$ 
Ahora, si se quisiera saber sobre dos variables aleatorias continuas, se tiene lo siguiente:

$$F_{X\vert Y}(x\vert y)=\mathbb{P}(X\leq x\;\vert\; Y=y)=\int_{-\infty}^{x}f_{X\vert Y}(x\vert y)dx$$ 
Para el caso de la **varianza** y **esperanza** es análogo: 

$$\begin{align}\mathbb{E}[X\vert A]&=\int_{-\infty}^{\infty}xf_{X\vert A}(x)dx\\\\\mathbb{E}[g(X)\vert A]&=\int_{-\infty}^{\infty}g(x)f_{X\vert A}(x)dx\\\\ Var(X\vert A)&=\mathbb{E}[X^2\vert A]-\left(\mathbb{E}[X\vert A]\right)\end{align} $$ 
Esto se cumple tanto para un evento $A$ dado como con una variable aleatoria. 

Ahora,  para el caso de dos variables continues e independientes se cumple lo siguiente: 

$$\begin{align} 
f_{XY}(x,y)&=f_X(x)f_Y(y)\\\\F_{XY}(x,y)&=F_X(x)F_Y(y)\\\\\mathbb{E}[XY]&=\mathbb{E}[X]\mathbb{E}[Y]\end{align}$$ 

### Ley de Probabilidades Totales 

Esto es completamente análogo al caso discreto, en específico, se tiene que la probabilidad de un evento $A$ está definido en las variables continuas como: 

$$\mathbb{P}(A)=\int_{-\infty}^{\infty}\mathbb{P}(A\vert X=x)f_X(x)dx$$ 
Y también esta la **Ley de la Esperanza Total**: 

$$\begin{align}\mathbb{E}[Y]&=\int_{-\infty}^{\infty}\mathbb{E}[Y\vert X=x]f_X(x)dx\\\\&=\mathbb{E}[\mathbb{E}[Y\vert X]]\end{align}$$ 
Y la **Ley de la Varianza Total**: 

$$Var(Y)=\mathbb{E}[Var(Y\vert X)] + Var(\mathbb{E}[Y\vert X])$$ 
### Funciones de dos variables aleatorias continuas 

Para la esperanza, el método de resolución sigue siendo el mismo: 

$$\mathbb{E}[g(X,Y)]=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}g(x,y)f_{XY}(x,y)\;dxdy$$ 
Ahora, para el caso de las PDF es un poco más engorroso, dado que la función $g$ estaría definida en $\mathbb{R^2}\to\mathbb{R^2}$. Para estudiar tal caso, para dos variables $X,Y$ cualesquiera, se puede ocupar el siguiente razonamiento: 

Sea la función $g(X,Y)=(Z,W)$, una función definida por dos *subfunciones*, es decir: $g(X,Y)=(g_1(X,Y),g_2(X,Y))$. Ahora, si definimos $h=g^{-1}$, es decir, $h(Z,W)=(X,Y)$, entonces $Z$ y $W$ son conjuntas y continuas y su PDF conjunta está dada por: 

$$f_{ZW}(z,w)=f_{XY}(h_1(z,w),h_2(z,w))\cdot\vert J\vert$$ 
Es decir, la PDF está definida por la **función inversa de cada *subfunción***. Por el otro lado, $J$ llegaría a ser el Jacobiano de la función inversa, definida como: 

$$J=\begin{bmatrix}\frac{\partial h_1}{\partial z}&\frac{\partial h_1}{\partial w}\\\frac{\partial h_2}{\partial z}&\frac{\partial h_2}{\partial w}\end{bmatrix}=\frac{\partial h_1}{\partial z}\cdot\frac{\partial h_2}{\partial w}-\frac{\partial h_2}{\partial z}\cdot\frac{\partial h_1}{\partial w}$$ 
### Convolución 

La convolución tiene varias aplicaciones en las matemáticas para combinar dos funciones. El [siguiente video](https://www.youtube.com/watch?v=KuXjwB4LzSA) podría ser muy útil para entender bien para qué se ocupa la convolución. En el caso de la probabilidad, se ocupa para la suma de variable aleatorias. Pero antes que nada, primero se define la convolución como: 

$$\begin{align}f_Z(z)&=f_X(z)\ast f_Y(z)\\\\=&\int_{-\infty}^{\infty}f_X(w)f_Y(z-w)dw\iff\int_{-\infty}^{\infty}f_Y(w)f_X(z-w)dw\end{align}$$

Lo que plantea el teorema es que si $X$ e $Y$ son dos variables conjuntamente continuas y $Z=X+Y$, entonces: 

$$f_Z(z)=\int_{-\infty}^{\infty}f_{XY}(w,z-w)dw=\int_{-\infty}^{\infty}f_{XY}(z-w,w)dw$$ 
Además, si se llegase a tener que $X$ e $Y$ son independientes, entonces: 

$$f_Z(z)=f_X(z)\ast f_Y(z)$$ 
También existe una forma discreta de ver la convolución, que se ve detallada en el video. 

## Covarianza 

La covarianza sirve para dar información de como $X$ e $Y$ están estadísticamente relacionados. Se define como: 

$$Cov(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\cdot\mathbb{E}[Y]$$

La covarianza tiene muchas propiedades, sin embargo, entre las más notables están: 

- $Cov(X,X)=Var(X)$ 
- Si $X$ e $Y$ son independientes, entonces $Cov(X,Y)=0$ 
- $Cov(X,Y)=Cov(Y,X)$ 
- $Cov(aX,Y)=aCov(X,Y)$ 
- $Cov(X+c,Y)=Cov(X,Y)$ 

## Correlación 

La correlación, denotada por $\rho(X,Y)$ es obtenida al normalizar la covarianza. Esto es especialmente util ya que nos asegura obtener datos entre $-1$ y $1$. Su fórmula es la siguiente: 

$$\rho(X,Y)=\frac{Cov(X,Y)}{\sqrt{Var(X)Var(Y)}}$$ 

# Métodos para más de dos variables aleatorias 

Anteriormente se describió el comportamiento de funciones para dos variables aleatorias. Si bien las distribuciones se extrapolan fácilmente a varias variables, hay algunos conceptos que no son únicos de estos. En consecuencia, muchas veces se trabajaran sobre vectores y matrices. 

## Vectores y matrices aleatorias 

Cuando se ocupan muchas variables aleatorias, muchas veces se es util ocupar vectores y matrices. Un **vector aleatorio** se define como lo siguiente: 

$$\textbf{X}=\begin{pmatrix}X_1\\X_2\\\vdots\\\vdots\\X_n\end{pmatrix}$$ 
La esperanza de los vectores se define como la esperanza de cada coordenada. Algunas veces se le llama el vector promedio. 

Similarmente se puede definir una matriz aleatoria cuyo elementos son variables aleatorias: 

$$\textbf{M}=\begin{bmatrix}X_{11}&X_{12}&\dots&X_{1n}\\X_{21}&X_{22}&\dots&X_{2n}\\\vdots&\vdots&\vdots&\vdots\\X_{m1}&X_{m2}&\dots&X_{mn}\end{bmatrix}$$ 
El concepto de esperanza es el mismo a aquel aplicado en el vector de variables aleatorias. 

Una propiedad interesante es que la linealidad de la esperanza **se mantiene** en los vectores y matrices. 

### Matriz de Correlación y Covarianza 

Para un vector $\textbf{X}$ aleatorio se define su matriz de correlación como: 

$$\mathbf{R_X}=\mathbb{E}[\mathbf{XX^T}]=\mathbb{E}\begin{bmatrix}X_{1}^{2}&X_1X_2&\dots&X_1X_n\\X_2X_1&X_{2}^{2}&\dots&X_2X_n\\\vdots&\vdots&\vdots&\vdots\\X_nX_1&X_nX_2&\dots&X_{n}^{2}\end{bmatrix}$$ 
Por el otro lado, la matriz de covarianza se define como: 

$$\mathbf{C_X}=\mathbb{E}[(X-\mathbb{E}[X])(X-\mathbb{E}[X])^T]=\begin{bmatrix}Var(X_1)&Cov(X_1,X_2)&\dots&Cov(X_1,X_n)\\Cov(X_2,X_1)&Var(X_2)&\dots&Cov(X_2,X_n)\\\vdots&\vdots&\vdots&\vdots\\Cov(X_n,X_1)&Cov(X_n,X_2)&\dots&Var(X_n)\end{bmatrix}$$ 
La matriz de covarianza es la generalización de la varianza de una variable aleatoria. Se puede reescribir como $\mathbf{R_X}-\mathbb{E}[X]\mathbb{E}[X]^T$ 

## Suma de variables aleatorias 

Muchas veces se trabajaran con suma de variables aleatorias. En particular, siempre se cumple que existe linealidad en la esperanza, y por ende, si definimos la siguiente variable $Y$: 

$$Y=X_1 + X_2 + \dots + X_n$$ 
Se puede llegar a algunas propiedades interesantes, como la de la varianza: 

$$Var\left(\sum_{i=1}^{n}X_i\right)=\sum_{i=1}^{n}Var(X_i)+2\sum_{i<j}Cov(X_i,X_j)$$ 
Sabiendo que si todas las variables aleatorias son independientes, entonces la covarianza es nula. 

Similar al caso de dos variables aleatorias, donde se definia la PDF de una suma de dos variables como la convolución entre ellas, se puede encontrar la PDF de una suma finita de variables aleatorias como una multiple convolución: 

$$f_Y(y)=f_{X_1}(y)\ast f_{X_2}\ast\dots\ast f_{X_n}(y)$$ 
## Función Generadora de Momento 

Las funciones generadoras de momento son utiles por dos cosas principalmente; para calcular los momentos e identificar distribuciones. Los momentos son descripciones de las distribuciones, como la esperanza, varianza, etc. En este caso se va a enfocar en la utilización de esta función para identificar distribuciones, que se define como lo siguiente: 

$$M_X(s)=\mathbb{E}[e^{sX}]$$ 
Es un concepto muy similar a la Transformada de Laplace y está definida bajo sus mismos preámbulos. 

Sabiendo que los *momentos* de una variable aleatoria son aquellos parámetros que describen la forma de aquellas, se puede mostrar que la función generadora de momento muestra la distribución de una variable aleatoria bajo la siguiente fórmula que se deriva de la serie de Taylor de la función exponencial: 

$$M_x(s)=\mathbb{E}[e^{sX}]=\sum_{k=0}^{\infty}\mathbb{E}[X^k]\frac{s^k}{k!}$$ 
De esto se concluye que a través de la serie de Taylor se tienen todos los momentos de $X$. 

### Aplicación en Sumas de Variables Aleatorias Independientes

Sea la siguiente variable $Y$ definida como: 

$$Y=X_1 + X_2 + \dots + X_n$$ 
Entonces, 

$$\begin{align}M_Y(s)&=\mathbb{E}[e^{sY}]\\\\&=\mathbb{E}[e^{s(X_1 + X_2 + \dots + X_n)}]\\\\&=\mathbb{E}[e^{sX_1}]\mathbb{E}[e^{sX_2}]\dots\mathbb{E}[e^{sX_n}]\;\;\;\text{(Independencia de las variables)}\\\\&=M_{X_1}(s)M_{X_2}(s)\dots M_{X_n}(s) \end{align}$$

Por lo tanto, la Función Generadora de Momento de $Y$ muestra la ponderación de los momentos de sus sumandos. 

## Distribución Normal Multivariada 

Se puede decir que dos variables $X$ e $Y$ son **bivariadas** si cumplen que $aX + bY$ siguen una distribución normal para todo $a,b\in\mathbb{R}$. Esta definición se puede extender para $n$ variables aleatorias conjuntas, es decir: 

Las variables $X_1, X_2,\dots, X_n$ se dicen **conjuntamente normales** si para todo $a_1, a_2,\dots, a_n\in\mathbb{R}$ la variable: 

$$a_1X_1 + a_2X_2 + \dots + a_nX_n$$ 
Es una variable aleatoria con distribución normal. 

Ahora, para el caso de las variables **conjuntamente normales**, se pueden definir bajo un vector que se llamará el **vector normal** o **vector Gaussiano**: 

$$\textbf{X}=\begin{pmatrix}X_1\\X_2\\\vdots\\X_n\end{pmatrix}$$ 
A partir de esto se puede notar algo muy interesante que se obtiene a partir de la definición de variable conjuntamente normales, ya que si tenemos que se cumple $a_1X_1 + a_2X_2 + \dots + a_nX_n$ para todo valor $a_1,a_2,\dots,a_n\in\mathbb{R}$, entonces el vector Gaussiano es una **combinación lineal**.

Para encontrar la PDF de un vector Normal es conveniente partir por el caso más simple donde cada variable es independiente y tienen la misma distribución; $Z_i\sim N(0,1)$.  Podriamos definirlo como un vector $\textbf{Z}$:

$$\textbf{Z}=\begin{pmatrix}Z_1\\Z_2\\\vdots\\Z_n\end{pmatrix}$$ 
Sabemos que la PMF conjunta de variable independientes es equivalente a la multiplicación de las PMFs marginales, entonces, se puede llegar a lo siguiente: 

$$\begin{align}f_\textbf{Z}(\textbf{z})&=f_{Z_1,Z_2,\dots,Z_n}(z_1,z_2,\dots,z_n)\\\\&=\prod_{i=1}^{n}f_{Z_i}(z_i)\\\\&=\frac{1}{(2\pi)^{\frac{n}{2}}}exp\left(-\frac{1}{2}\sum_{i=1}^{n}z_{i}^{2}\right)\;\;\;\text{(Definición de multiplicación de Normales)}\\\\&=\frac{1}{(2\pi)^{\frac{n}{2}}}exp\left(-\frac{1}{2}\textbf{z}^T\textbf{z}\right)\end{align}$$


Ahora, para extender este concepto para cualquier variable, nos acordamos del siguiente teorema: 

$$Z\sim N(0,1)\implies X=\sigma Z+\mu\sim N(\mu,\sigma^2)$$ 
Entonces, asumiendo que tenemos un vector Gaussiano $\textbf{X}$ con media $m$ y una matriz covarianza $C$, se puede escribir su distribución como $\textbf{X}\sim N(m,C)$. Sabemos que la matriz covarianza es definida positiva, entonces sabemos que existe una matriz $\textbf{Q}$ que satisface lo siguiente: 

$$\begin{align}QQ^T&=I\\\\C&=QDQ^T\end{align}$$ 
Donde $D$ es una matriz diagonal. De hecho, se podría definir como sigue, sabiendo que $C$ es positivo: 

$$\begin{align}D&=\begin{bmatrix}d_{11}&0&\dots&0\\0&d_{22}&\dots&0\\\vdots&\vdots&\vdots&\vdots\\0&0&0&d_{nn}\end{bmatrix}\\\\D^{\frac{1}{2}}&=\begin{bmatrix}\sqrt{d_{11}}&0&\dots&0\\0&\sqrt{d_{22}}&\dots&0\\\vdots&\vdots&\vdots&\vdots\\0&0&0&\sqrt{d_{nn}}\end{bmatrix}\end{align}$$ 

Donde se tiene que $D^{\frac{1}{2}}D^{\frac{1}{2}}=\textbf{D}$ y $D^{\frac{1}{2}}=D^{\frac{1}{2}^T}$. Entonces, se puede definir otra matriz auxiliar: 

$$\textbf{A}=QD^{\frac{1}{2}}Q^T$$ 
Lo que implica lo siguiente: 

$$\mathbf{AA^T}=\mathbf{A^T A}=\mathbf{C}$$  
Todas estas definiciones son hechas para poder definir una transformación del vector Gaussiano estándar a uno cualquiera de parámetros $m$ y $C$. Por lo tanto, sea $\mathbf{Z}\sim N(0,1)$, se define el vector $\textbf{X}\sim N(m,C)$ como: 

$$\mathbf{X}=\mathbf{AZ} + m$$ 
Para ver esto, primero notamos que $\textbf{X}$ es una combinación lineal de $\textbf{Z}$ mas una constante, lo que satisface el teorema descrito anteriormente. Faltaría confirmar que $m$ y $C$ efectivamente es la media y la covarianza. 

Para la media, notamos que por linealidad de la esperanza, que se mantiene para los vectores y matrices, lo siguiente: 

$$\begin{align}\mathbb{E}[\mathbf{X}]&=\mathbb{E}[\mathbf{AZ}+m]\\\\&=\mathbf{A}\mathbb{E}[\mathbf{Z}]+m\\\\&=m\;\;\;\text{(Z tiene media cero)}\end{align}$$ 
Por el otro lado, por definición de covarianza de vectores de la forma $aX + b$ se tiene lo siguiente: 

$$\begin{align}C_X&=AC_ZA^T\\\\&=AA^T\\\\&=C\;\;\;\text{(Z tiene covarianza 1)}\end{align}$$ 
Esta última definición se puede demostrar ocupando esperanza y definición de covarianza. 

Entonces, se demuestra que la transformación $\mathbf{X}=\mathbf{AZ} + m$ da un vector Gaussiano de media $m$ y una matriz de covarianza $C$. Por lo tanto, dado que se tiene una transformación se puede ocupar el teorema de cambio de variable para escribir la PDF de $\textbf{X}$: 

$$\begin{align}f_\mathbf{X}(\mathbf{x})&=\frac{1}{\vert det(A)\vert}f_\mathbf{Z}\left(A^{-1}(x-m)\right)\end{align} $$ 
Acordándonos de la definición de PDF de $\mathbf{Z}$ se puede reemplazar: 

$$\begin{align}f_\mathbf{X}(\mathbf{x})&=\frac{1}{(2\pi)^{\frac{1}{2}}\vert det(A)\vert}exp\left(-\frac{1}{2}(A^{-1}(x-m))^T(A^{-1}(x-m))\right)\\\\&\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\vdots\\\\&=\frac{1}{(2\pi)^{\frac{1}{2}}\sqrt{det(C)}}exp\left(-\frac{1}{2}(x-m)^TC^{-1}(x-m)\right)\end{align}$$ 

Por lo tanto, se llega que la PDF de un vector Normal con media $m$ y una matriz covarianza $C$ tiene la siguiente PDF: 

$$f_\mathbf{X}(\mathbf{x})=\frac{1}{(2\pi)^{\frac{1}{2}}\sqrt{det(C)}}exp\left(-\frac{1}{2}(x-m)^TC^{-1}(x-m)\right)$$ 



## Función característica 

Hay algunas variables aleatorias cuyas funciones generadores de momento no existe para ningún intervalo real con largo positivo. Por ejemplo, se puede considerar la variable $X$ que tiene una distribución de Cauchy: 

$$\begin{align}f_x(x)&=\frac{\frac{1}{\pi}}{1+x^2}\;\;\forall x\in\mathbb{R}\\\\
M_X(s)&=\int_{-\infty}^{\infty}e^{sx}\frac{\frac{1}{\pi}}{1+x^2}dx= \infty\end{align}$$

Si la función característica no existe, se define la **función característica**, definida como: 

$$\phi_X(\omega)=E[e^{j\omega X}]$$ 
Donde $j=\sqrt{-1}$  y $\omega$ es un número real. 
