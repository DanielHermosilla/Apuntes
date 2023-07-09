
Son las ecuaciones de la forma: 

$$y'' + \bar{a_1}(x)y' + \bar{a_0}(x)y = \bar{Q}(x)$$ 
Aquí no se puede ocupar el [[polinomio característico]], ya que se tendría algo del estilo $\lambda x$, es decir, $\lambda$ quedaría en función de $x$. 

Las soluciones homogeneas se denominaran por $H$ y las no homogeneas se denominaran por $S$ 

Notemos que si se suma $y_p\in S$ con $y_h\in H$, entonces $y = y_h + y_p \in S$. Dado que quedaría de la forma: 

$$(y_h + y_p)'' + \bar{a_1}(x)(y_h + y_p)' + \bar{a_0}(x)(y_h + y_p) = \bar{Q}$$ 
Que funciona dado la linealidad de la derivada. 

Notemos que $H$ es un [[subespacios vectoriales]] que pasa por el origen. Por el otro lado, $S$ es un [[subespacios vectoriales|subespacioi afin]], es decir, un subespacio vectorial desplazado por una solución particular. Es decir, se tiene lo siguiente: 

![[IMG_777AC196966E-1.jpeg|center]]

Primero, haciendo el análisis homogeneo: 

$$y'' + \bar{a_1}(x)y' + \bar{a_0}(x)y = 0)$$

Notemos que se puede representar [[matriz|matricialmente]]: 

$$\begin{bmatrix}y\\y'\end{bmatrix}'=\begin{bmatrix}0&1\\-\bar{a_0}(x)&-\bar{a_1}(x)\end{bmatrix}\begin{bmatrix}y\\y'\end{bmatrix}$$ 
Si se desarrolla el producto, se tiene que: 
1. $y' = y'$
2. $y'' = -\bar{a_0}y - \bar{a_1}y'$ 

Por lo tanto, se llega que: $Y' = A(x)·Y$. Además, si se imponen las [[Condición inicial|condiciones iniciales]], estas dependerían de $y$ y $y'$.

Por lo tanto, se llega a un [[Teoría de Existencia y Unicidad|problema de Cauchy]], donde: 

$$\text{Problema de Cauchy} = \begin{cases}
Y' = A(x)·Y\\\\Y(x_0) = \begin{bmatrix}
y(x_0) \\ 
y'(x_0)
\end{bmatrix}\end{cases}$$ 
Donde la [[Función continua|continuidad]] está determinada por los coeficiente de $A(x)$ y  ser [[Lipschitz]] está determinado por los coeficientes de igual forma. Se ve reflejado por el [[Teorema de Existencia y Unicidad de Orden 2]]. 

Por lo tanto, se podría conseguir una [[Base|base]] a partir de la ecuación, donde se imponen condiciones iniciales. 

### Ejemplo:

Sea la misma ecuación de antes; $y'' + \bar{a_1}(x)y' + \bar{a_0}(x)y = 0$, entonces se puede imponer lo siguiente: 

$$\text{Base} = \begin{cases} 
y'' + \bar{a_1}(x)y' + \bar{a_0}(x)y = 0)\\\\y_1(x_0) = 1,\;y_{1}^{'}(x_0) = 0\end{cases}\implies\exists!y_1\in C^2
\;\land\;\begin{cases}
y'' + \bar{a_1}(x)y' + \bar{a_0}(x)y = 0) \\ 
\\ 
y_2(x_0) = 0,\;y_{2}'=1\end{cases}\implies\exists! y\in C^2$$

Ahora, veamos que si son linealmente [[dependencia|independientes]]: 

$$\begin{bmatrix}
y_1(x) & y_2(x) \\
y_1'(x) & y_2'(x)
\end{bmatrix} \begin{bmatrix}\alpha \\\beta 
\end{bmatrix} = \begin{bmatrix}
0 \\ 
0
\end{bmatrix}$$ 
En $x_0$ queda la [[matriz|matriz identidad]], entonces $\alpha=\beta =0$, y es linealmente independiente. Para llegar a ser [[Base|base]], $\lbrace y_1, y_2\rbrace$ debe generar $H$. Es decir $<\lbrace y_1,y_2 \rbrace>$ = $H$. 

Sea $y_1\in H$, encontremos $\alpha, \beta, \in \mathbb{R}$ tal que $y_h = \alpha y_1 + \beta y_1$ y $y_h' = \alpha y_1 + \beta y_2$. Es decir: 

$$\begin{bmatrix}
y_1(x) & y_2(x) \\
y_1'(x) & y_2'(x)
\end{bmatrix} \begin{bmatrix}
\alpha \\\beta\end{bmatrix} = \begin{bmatrix}
y_h(x)\\ 
y_h'(x)
\end{bmatrix}$$

Si $x = x_0\implies \alpha = y_h(x_0), \ \beta y_h'(x_0)$. Se define: 

$$z(x) = y_h(x_0)y_1 + y_h'(x_0)y_2\ \  \in H$$ 
Una [[combinación lineal]] con los valores previamente encontrados. 

Entonces: 

$$z(x_0) = y_h(x_0)\ \land\ z'(x_0)=y'_h(x_0)$$

Notemos que por [[Teorema de Existencia y Unicidad de Orden 2]], se tiene que: 

$$\text{Problema de Cauchy} = \begin{cases}
z(x) = y_h(x_0)y_1 + y_h'(x_0)y_2 \\ 
\\ 
z(x_0) = y_h(x_0)\ \land\ z'(x_0)=y'_h(x_0) \end{cases}\implies{TEU}$$ 
Recapitulando, la solución homogenea  es una base donde $y_1, y_2$ son [[dependencia|linealmente independientes]] y la no homogénea es equivalente a $y = y_h + y_p \implies (S = H + y_p)$. 

Por ende, la solución $y_p$ con variación de parámetros es: 

$$y_p = -y_1(x)\int\frac{\bar{Q}y_2}{W} + y_2(x)\int\frac{\bar{Q}y_1}{W} \ \ \ W = y_1y_2'-y_1'y_2$$ 
No hay un método general para encontrar $y_1(x), y_2(x)$ pero si conocemos $y_1$ se puede encontrar $y_2$ usando la [[Fórmula de Abel]], que nos va a llevar a la [[Fórmula de Luiville]].