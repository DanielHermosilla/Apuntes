
Una [[Variable Aleatoria|variable aleatoria]] es una variable que toma valores numéricos y tiene resultado determinado por un **proceso aleatorio de generación de datos**. La asignación se da uno a uno, cada resultado corresponde a un único valor (es *inyectiva*).  Se dice que $X$ es una variable aleatoria puesto que no se sabe el valor que tomará efectivamente. 

En el mundo de las variables aleatorias, para cada elemento del recorrido, se le determina una [[Probabilidades|probabilidad]] en partícular. 

### Variable Aleatoria Discreta 

Una variable aleatoria es discreta cuando el rango puede tomar $k\in\mathbb{N}$ valores posibles $(\lbrace x_1, x_2,\dots, x_k\rbrace)$. 

La **distribución de probabilidad** de $X$ corresponde a la probabilidad que la variable aleatoria **tome dentro de un determinado rango**. Así, se cumplen las siguientes tres propiedades: 

$$\begin{align}
p_j&=P(X=x_j)\in [0,1]\tag{1}\\  \\
\sum^{k}_{j}p_j&=1\tag{2}\\  \\
f(x)&=0\;\text{si se está fuera del dominio}\tag{3}
\end{align}$$


### Variable Aleatoria Continua 

La variable aleatoria puede tomar infinitos valores. En ese sentido, la probabilidad que $X$ tome un valor en específico es $0$. 

Por eso, a las variables aleatorias continuas se les asignan intervalos de probabilidad para **intervalos de valores** en el rango de $x$. A tal caso, se le denomina **función densidad de probabilidad** que corresponde a la integral entre el rango a estudiar: 

$$P(a\leq x\leq b)=\int^{b}_{a}f(x)\;dx$$

Así, se cumplen las siguientes propiedades: 

$$\begin{align}
\int^{\infty}_{-\infty}f(x)\;dx&=1\tag{1}\\  \\
f(x)&=0\;\text{si está fuera del dominio}\tag{2}\\  \\
P(a\leq x\leq b)=P(a\leq x<b)&=P(a<x\leq b)=P(a<x<b)\tag{3}
\end{align}$$

