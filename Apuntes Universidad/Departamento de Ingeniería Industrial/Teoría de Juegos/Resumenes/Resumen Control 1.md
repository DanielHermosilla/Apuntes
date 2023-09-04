
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

#### Ejemplo 

Se tiene el siguiente juego, donde las estrategias del Jugador $1$ corresponde a $(U,\; M,\; D)\in S_1$ y $(L,\; M,\; R)\in S_2$ para el Jugador $2$. 


|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(4,3)$ | $(5,1)$ | $(6,2)$ |
| **M** | $(2,1)$ | $(3,6)$ | $(8,4)$ |
| **D** | $(3,0)$ | $(9,6)$ | $(2,8)$ |


Se asume que todos los jugadores son racionales y todos saben entre sí que son racionales. 

Por lo tanto, notemos que el Jugador $1$ no tiene estrategias estrictamente dominadas, esto se puede ver al notar la mejor jugada ante una estrategia del Jugador $2$. 

|       |          **L**           |          **M**           |          **R**           |
|:-----:|:------------------------:|:------------------------:|:------------------------:|
| **U** | $(\textcolor{red}{4},3)$ |         $(5,1)$          |         $(6,2)$          |
| **M** |         $(2,1)$          |         $(3,6)$          | $(\textcolor{red}{8},4)$ |
| **D** |         $(3,0)$          | $(\textcolor{red}{9},6)$ |         $(2,8)$          |