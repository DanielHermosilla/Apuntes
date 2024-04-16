
Se define la [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Esperanza|esperanza]] condicional como: 

$$E[Y\vert X]=\int y\cdot f_{Y\vert X}(y)\;dy$$

Donde $f_{Y\vert X}(y)$ es la [[Probabilidad Condicional|distribución condicional]] de $Y$ dado $X$. 

Decimos que $X$ provee información sobre $Y$ cuando se cumple que: 

$$E[Y]\neq E[Y\vert X]$$

### Descomposición de la función Esperanza Condicional

Cualquier variable aleatoria puede ser expresada como: 

$$Y=E[Y\vert X]+\epsilon$$

Donde $\epsilon$ es una variable aleatoria que satisface: 

- $E[\epsilon\vert X]=0$
- $E[\epsilon]=0$
- $\text{Cov}(h(X),\epsilon)=0$, con $h(X)$ cualquier función de $X$. 

Luego, cualquier varaible aleatoria $Y$ puede ser expresada como una función de $X$ mas un término de error. 

### Ley de Esperanzas Iteradas 

Por ley de probabilidad total, se cumple que: 

$$E(Y)=E_X(E(Y\vert X))$$

Como intuición, *la [[Ley de la Esperanza Total|esperanza]] global de una variable puede calcularse tomando el promedio de todos los promedios condicionales*. 

