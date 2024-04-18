
Notar que al tener una [[Distribución Conjunta|distribución conjunta]], se tiene que una predicción $m(X)$ que depende de un [[vectores|vector]] de información $X$, la predicción **que minimiza el [[Error Cuadrático Medio]]** es: 

$$m(X)=E[Y\;\vert X]$$

Por lo tanto, la idea es encontrar un [[Estadísticos|predictor]] que pueda aproximar a $m(X)$. Suponiendo que se tiene una predicción lineal de tipo $m(X)=a+bX$, buscamos una predicción tal que se minimice el [[Error Cuadrático Medio]]: 

$$\min_{a,b} E[(Y-a-bX)^2]$$

Para resolver esto, se ocupa la condición de primer orden, donde se deriva e iguala a cero: 

$$\text{CPO}_b=E[X(Y-a-bX)]=0$$

$$CPO_a=E[Y-a-bX]=0$$

Al resolver el problema, se tiene que los parámetros son: 

$$\begin{align}
b^*&=\frac{\text{Cov}(Y,X)}{\text{Var}(X)}\\  \\
a^*&=E[Y]-b^*E[X]
\end{align}$$

Y, por lo tanto, se define la **regresión lineal** como: 

$$m(x)=a^*+b^*X$$

