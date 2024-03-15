
O también llamada de Pascal, es ocupada por la [[Distribución geométrica|distribución geométrica]], con $p\in(0,1$) y $m\in\mathbb{N}\backslash\lbrace 0\rbrace$, si $R_x = \lbrace m, m+1, m+2, \dots\rbrace$ y su [[Función de Masa de Probabilidad|PMF]] es:

$$p_x(x)=\begin{cases}
\begin{pmatrix}
x-1 \\
m-1
\end{pmatrix}p^m(1-p)^{x-m} & \text{si}\ x = m,m+1,\dots \\ \\
0 & \text{si no}\end{cases}$$ 
Sería como una [[Función de Distribución Acumulada|función de distribución acumulada]] pero para la [[Distribución geométrica|distribución geométrica]]. 

![[Binomialnegativo.png|center]]

En palabras simples, en que cantidad de intentos se puede pasar $m$ etapas. 

## Esperanza 

Se tiene que la [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Esperanza|esperanza]] sería la multiplicación de $m$ veces la [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Esperanza|esperanza]] de la [[Distribución geométrica|distribución geométrica]]. Es decir:

$$E[X] = \frac{m}{p}$$ 
## Varianza 

Se tiene que la [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Varianza|varianza]] es: 

$$Var(X) = \frac{m(1-p)}{p^2}$$ 