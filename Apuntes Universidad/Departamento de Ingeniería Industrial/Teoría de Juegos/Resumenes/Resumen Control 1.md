
La teoría de juegos es el estudio de interacciones estratégicas, donde las decisiones de los agentes influyen en el resultado del *juego*. Si se quisiera definir de forma formal, es la **rama de las matemáticas** que estudia las decisiones de **agentes que quieren maximizar beneficios**. 

## Formalidades técnicas 

Antes de definir los teoremas y aplicaciones de la teoría de juegos, es importante conocer los dos conceptos fundamentales que equivalen a las variables de cada juego. 

>[!tip] Jugadores 
>Son los agentes participantes del juego, por lo general se van a tener $n\geq 2$. 

>[!tip] Estrategias 
>Para un jugador $i$ se va a representar con $S_i$ el conjunto de estrategias de $i$. Un elemento representativo de $S_i$ será $s_i\in S_i$. 
>
>Por consecuencia, se representará como $S=S_1\times S_2\times\dots S_n$ el conjunto de todas las jugadas posibles-
>
>Las jugadas de los jugadores opuestos a $i$ se representaran con un $-i$. En este caso, $S_{-i}=S_1\times S_2\times S_n$ representaría el conjunto de jugadas de todos los jugadores excepto $i$. 

Por lo tanto, una jugada $s\in S$ se le llamará un **perfil de estrategias**, equivalente a un vector con todas las jugadas de cada jugador: 

$$s=\begin{pmatrix}
s_1 \\
s_2 \\
\vdots \\
s_n
\end{pmatrix}$$

Notemos que el perfil de estrategias tiene la misma cantidad de dimensiones que de jugadores. 

>[!tip] Pagos 
>Se representarán los pagos de un jugador $i$ como una función de utilidad $U(s)=U(s_1,s_2,\dots,s_n)$ que dependen de las decisiones de todos los jugadores. 

Durante el transcurso del curso, lo normal será **maximizar** la función de utilidades en función del conjunto de jugadas $S_{-i}$. Cuando no se tiene certeza absoluta del perfil de estrategias se ocupa el concepto de **utilidad esperada**, haciendo alusión al concepto de **esperanza** de Probabilidades. 

###  Dominancia estricta 

>[!important] Estrategia **estrictamente** dominada 
>Una estrategia es **estrictamente dominada** si existe una otra estrategia que da mayores pagos para cualquier juego de los otros jugadores.
>
>Para un jugador $i$, una estrategia $s_i\in S_i$ es **estrictamente dominada** si existe una estrategia $s_{i}^{'}\in S_i$ tal que: 
>
>$$u_i(s_i,s_{-i})<u_i(s_{i}^{'},s_{-i})\;\;\;\forall s_{-i}\in S_{-i}$$

Algo a considerar es que **los jugadores racionales no juegan estrategias estrictamente dominadas**. Esto se llama *conocimiento común de racionalidad*. 

#### Ejemplo: Dominancia estricta 

Se tiene el siguiente juego, donde las estrategias del Jugador $1$ corresponde a $(U,\; M,\; D)\in S_1$ y $(L,\; M,\; R)\in S_2$ para el Jugador $2$. 


|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(4,3)$ | $(5,1)$ | $(6,2)$ |
| **M** | $(2,1)$ | $(8,4)$ |$(3,6)$   |
| **D** | $(3,0)$ | $(9,6)$ | $(2,8)$ |


Se asume que todos los jugadores son racionales y todos saben entre sí que son racionales. 

Por lo tanto, notemos que el Jugador $1$ no tiene estrategias estrictamente dominadas, esto se puede ver al notar la mejor jugada ante una estrategia del Jugador $2$. El análisis se hace por el método de **dominancia estricta**, a diferencia de **mejor respuesta**. 

- Comparando $U$ con $M$: 

|       |          **L**           |          **M**           |          **R**           |
|:-----:|:------------------------:|:------------------------:|:------------------------:|
| **U** | $(\textcolor{red}{4},3)$ |         $(5,1)$          |         $(\textcolor{red}{6},2)$          |
| **M** |         $(2,1)$          |   $(\textcolor{red}{8},4)$            |   $(3,6)$   |


$U$ domina en dos jugadas, sin embargo, $M$ domina en una. 

- Comparando $U$ con $D$: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(5,1)$ | $(\textcolor{red}{6},2)$ |
| **D** | $(3,0)$ | $(\textcolor{red}{9},6)$ | $(2,8)$ |


Nuevamente, $U$ no es la mejor jugada. 

- Comparando $M$ con $D$: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **M** | $(2,1)$ | $(8,4)$ |$(\textcolor{red}{3},6)$   |
| **D** | $(\textcolor{red}{3},0)$ | $(\textcolor{red}{9},6)$ | $(2,8)$ |


Lo mismo en este juego. Por lo tanto, no hay estrategia estrictamente dominada para el Jugador $1$. 

Aun así, notemos que para el Jugador $2$ si existen estrategias estrictamente dominadas:

- Comparando $L$ con $M$: 

|       |           **L**           |           **M**           |
|:-----:|:-------------------------:|:-------------------------:|
| **U** | $(4,\textcolor{blue}{3})$ |          $(5,1)$          |
| **M** |          $(2,1)$          | $(3,\textcolor{blue}{6})$ |
| **D** |          $(3,0)$          |          $(9,\textcolor{blue}{6})$          |


Aquí se puede ver que no hay estrategía estrictamente dominada. 

- Comparando $M$ con $R$: 

|       |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(5,1)$ | $(6,\textcolor{blue}{2})$ |
| **M** | $(8,4)$ | $(3,\textcolor{blue}{6})$ |
| **D** | $(9,6)$ | $(2,\textcolor{blue}{8})$ |


En este caso **$M$** **está estrictamente dominada por $R$**. 

- Comparando $L$ con $R$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,\textcolor{blue}{3})$ | $(6,2)$ |
| **M** | $(2,1)$ | $(3,\textcolor{blue}{6})$ |
| **D** | $(3,0)$ | $(2,\textcolor{blue}{8})$ |


Acá tampoco hay una estrategia dominada. 

Como el segundo Jugador es racional, no va a jugar $M$, entonces esa estrategia se eliminaría. La tabla quedaría de la siguiente forma: 


|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,3)$ | $(6,2)$ |
| **M** | $(2,1)$ | $(3,6)$ |
| **D** | $(3,0)$ | $(2,8)$ |


Ahora, para el Jugador $1$, notemos lo siguiente: 

- Comparando $U$ con $M$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(\textcolor{red}{6},2)$ |
| **M** | $(2,1)$ | $(3,6)$ |


Aquí, notemos que $M$ **está estrictamente dominada** por $U$. 

- Comparando $M$ con $D$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **M** | $(2,1)$ | $(\textcolor{red}{3},6)$ |
| **D** | $(\textcolor{red}{3},0)$ | $(2,8)$ |


Aquí no hay una estrategia estríctamente dominada. 

- Comparando $U$ con $D$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(\textcolor{red}{6},2)$ |
| **D** | $(3,0)$ | $(2,8)$ |


En este caso $U$ **domina a D**. Por lo tanto, se eliminarían dos estrategias. 

Por ende, se llega a la siguiente tabla: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,3)$ | $(6,2)$ |


A partir de aquí es claro ver que el Jugador $2$ va a jugar $L$, por ende, la solución llegaría ser $(U,L)$. 

#### Ejemplo: Mejor respuesta 

Muchas veces, comparar estrategia por estrategia puede llegar a ser muy tedioso. En este caso, se tenía una matriz $3\times 3$, pero en el caso de una matriz $n\times n$ se tendría que hacer las siguiente cantidad de comparaciones por jugador: 

$$\sum^{n}_{i=1}\;(N-i)=\frac{N(N-1)}{2}$$

Si consideramos las comparaciones del jugador $2$, serían $N(N-1)$ comparaciones en total. Esto, **solamente para la primera tanda de estrategias estrictamente dominadas**. Si siguieramos bajo la misma lógica, y suponiendo el peor caso (una eliminación por tanda), se repetiría el proceso: 

$$\sum^{n}_{i=1}(N-i)(N-(i-1))=\frac{N^2(N+1)}{2}+\frac{N^3-N^2}{6}$$

Esto quiere decir que, bajo este método, **el peor caso es $\Theta(N^3)$**, algo completamente ineficiente. 

De aquí es donde se introduce el método de **mejor respuesta**, que se enfoca en encontrar la estrategia óptima ante una posible jugada del otro jugador. Viéndolo con el mismo juego con el Jugador 1: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(5,1)$ | $(\textcolor{red}{6},2)$ |
| **M** | $(2,1)$ | $(8,4)$ |$(3,6)$   |
| **D** | $(3,0)$ | $(\textcolor{red}{9},6)$ | $(2,8)$ |


Por **mejor respuesta** se elimina la estrategia $M$, quedando con la siguiente matriz: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(4,3)$ | $(5,1)$ | $(6,2)$ |
| **D** | $(3,0)$ | $(9,6)$ | $(2,8)$ |


Ahora, para el Jugador $2$: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(4,\textcolor{blue}{3})$ | $(5,1)$ | $(6,2)$ |
| **D** | $(3,0)$ | $(9,6)$ | $(2,\textcolor{blue}{8})$ |


Se eliminaría la estrategia $M$, quedando con la siguiente tabla: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,3)$ | $(6,2)$ |
| **D** | $(3,0)$ | $(2,8)$ |


Ahora, nuevamente, analizando para el Jugador $1$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(\textcolor{red}{6},2)$ |
| **D** | $(3,0)$ | $(2,8)$ |


Se elimina $D$, quedando con la siguiente matriz: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,3)$ | $(6,2)$ |


Y aquí se llega **a la misma situación anterior**, donde trivialmente se llega al equilibrio $(U,L)$. Notemos que en este caso, se hicieron $3$ comparaciones en vez de $9$. 

