
La idea es cubrir la mayor cantidad de demanda posible dado un número de facilidades. 

![[Pasted image 20240318104948.png|center|500]] 

Así, la pregunta es como es posible cubrir la mayor cantidad de demanda posible **dado una cantidad fija de facilidades** 

Se dirá que $i$ es cubierto por $j$ si $d_{ij}\leq D$. 

También se definira el conjunto $N_i$, que es el conjunto de servicios disponibles dado un punto de demanda. 

$$N_i=\lbrace j\;\vert\;d_{ij}\leq D\rbrace$$

Nos definimos una indicatriz binaria $(x_{ij})$ que nos determina si el servicio es utilizado o no.  Así, se puede definir de la siguiente forma: 

$$\begin{align}
\sum_{j\in N_i}x_{ij}&=1\\  \\
x_{ij}&\leq y_j
\end{align}$$

Por el otro lado, nos definimos otra variable binaria $y_j$ que nos determina si el lugar donde se da la facilidad tiene la demanda completa. 

Por lo tanto, la función objetivo llegaría a ser: 

$$\begin{align}
\max\sum_{i\in I}\sum_{j\in N_i}x_{ij}
\end{align}$$


