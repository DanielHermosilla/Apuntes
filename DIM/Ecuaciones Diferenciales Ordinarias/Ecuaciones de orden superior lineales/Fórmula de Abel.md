
Lo que hizo abel fue derivar la [[Matriz Wronskiana]] y encontro lo siguiente:

$$W' = -\bar{a_1(x)}W$$ 
## Extensión de la fórmula 

Si se tiene la siguiente [[Base|base]] de las soluciones de una [[EDO de coeficiente variables]]: 
$$\langle\lbrace y_1^{(n)},y_1^{(n-1)},\dots,y\rbrace\rangle$$

Entonces *¿Cuanto vale $W'$?* 

Se tendría una matríz de la siguiente forma: 

$$W = \begin{bmatrix}y_1&y_2&\dots& y_n\\y_1'&y_2'&\dots&y_n'\\\vdots&\vdots&\vdots&\vdots\\y_{1}^{n-1}&y_{2}^{n-1}&\dots&y_{n}^{n-1}\end{bmatrix}$$ 
El caso de la derivada de una matriz $2\times 2$ sería: 

$$\begin{bmatrix}a&b\\c&d\end{bmatrix}'=(ad-bc)'= a'd + ad' - b'c - bc' =\begin{bmatrix}a'&b'\\c&d\end{bmatrix}+\begin{bmatrix}a&b\\c'&d'\end{bmatrix}$$ 
Esto se extrapola al caso *n-esimo*. Entonces, se llega que la derivada es: 

$$W' = \begin{bmatrix}
y_1'&y_2'&\dots&y_n'\\ 
y_1'&y_2 '&\dots&y_n'\\\vdots&\vdots&\vdots&\vdots\\y_{1}^{n-1}&y_{2}^{n-1}&\dots&y_{n}^{n-1}\end{bmatrix} + \begin{bmatrix}
y_1 & y_2 &\dots& y_n\\ 
y_1''&y_2''&\dots&y_n'\\\vdots&\vdots&\vdots&\vdots\\y_{1}^{n-1}&y_{2}^{n-1}&\dots&y_{n}^{n-1}\end{bmatrix} + \dots + \begin{bmatrix}y_1 & y_2 &\dots& y_n\\ 
y_1' & y_2'&\dots&y_n'\\\vdots&\vdots&\vdots&\vdots\\y_{1}^{n} & y_{2}^{n}&\dots&y_{n}^{n}\end{bmatrix}$$ 
Notemos que se forman [[dependencia|dependencias]] lineales entre las filas, entonces el [[determinante]] de cada uno es $0$ a excepción del último donde son linealmente independiente. 

Notemos que de la solución de la ecuación diferencial sale que: 

$$y_1^{(n)} = -\sum^{n-1}_{j=0}\bar{a_j}(x)y_1^{(j)}$$ 
O, extrapolándolo al caso general: 

$$y_i^{(n)} = -\sum^{n-1}_{j=0}\bar{a_j}(x)y_i^{(j)}\;\;\;y_1\in H\;\;\;i=1,2,3,\dots,n$$

Entonces, esto se puede reemplazar en la derivada de la matriz: 

$$W' = \begin{bmatrix}
y_1&y_2&\dots&y_n\\y_1'&y_2'&\dots&y_n'\\\vdots&\vdots&\vdots&\vdots\\-\sum^{n-1}_{j=0}\bar{a_j}(x)y_1^{(j)}&-\sum^{n-1}_{j=0}\bar{a_j}(x)y_2^{(j)}&\dots&-\sum^{n-1}_{j=0}\bar{a_j}(x)y_n^{(j)}\end{bmatrix}$$

Por linealidad de la constante, se puede reescribir como: 

$$W' = -\sum^{n-1}_{j=0}\bar{a_j}(x)\begin{bmatrix}
y_1&y_2&\dots&y_n\\y_1'&y_2'&\dots&y_n'\\\vdots&\vdots&\vdots&\vdots\\y_{1}^{j}&y_{2}^{j}&\dots&y_{n}^{j}\end{bmatrix}$$ 
Notemos que cuando $j=0$, entonces se tiene la primera fila y una [[dependencia]] lineal, cuando $j=1$ pasa lo mismo con la segunda fila, y así sucesivamente. Notemos que el único caso donde no se anula es cuando se tiene la última suma. Por ende, se llega a lo siguiente: 

$$W' = -\bar{a_{n-1}}(x)W$$ 
Entonces, si dejamos el determinante expresado como función: 

$$f(\lambda_1x_1 + \lambda_2x_2) = \lambda_1f(x_1) + \lambda_2f(x_2)$$ $$\vdots$$
$$f(\sum^{}_{i}\alpha_ix_i, y) = \sum\alpha_if(x_i,y)$$

Esto implica que el determinante es **multilineal por filas y por columnas**. Esto llega a la fórmula de Abel general. 

## Fórmula de Abel general 

Se tiene que: 

$$W' = -\bar{a_{n-1}}(x)W$$
Implica que: 

$$W = ce^{-\int\bar{a_{n-1}}}\;\;\;\;\; c\in\mathbb{R}$$ 
Esto implica que el [[Matriz Wronskiana|Wronskiano]] siempre será de signo constante. Por ende, ¿se podría asegurar lo siguiente?

$$y_1\;\;\;l.i\;\;\;y_2\iff W(x;y_1,y_2)\neq 0$$ 
Esto llega a un sistema de ecuación y existen contraejemplos que dicen que no es una equivalencia. Sin embargo, si $y_1$ y $y_2$ fueran solución de una misma solución homogenea, entonces, por la fórmula de Abel, el Wronskiano sería o siempre positivo o siempre negativo $\implies\neq 0$. 

Por lo tanto, en general, si $W(x_0)\neq 0\implies\alpha=\beta=0$ y también $\implies y_1, y_2\;\;\text{son linealmente independientes}$ 