
La mayoria de las [[Estrategia|interacciones estratégicas]] son **repetidas**. Un claro ejemplo de esto es la *guerra de desgaste*. 

#### Ejemplo 

Es posible realizar una especie de juego del prisionero, donde se puede elegir entre ser "Malo" o ser "Bueno".


|           | **Bueno** | **Malo** |
|:---------:|:---------:|:--------:|
| **Bueno** |  $(2,2)$  | $(-1,3)$ |
|  **Malo** |  $(3,-1)$  |  $(0,0)$ |


La forma de resolver el juego, es mirar la última interacción, al igual que los [[Juegos secuenciales|juegos secuenciales]]. Si nos fijamos en el $n$-ésimo día, sería trivial ver que se va a ser malo. Pero, en el día $n-1$, sabiendo que se va a ser malo, se va a ser bueno. Esto se conoce como **game end effect**. 

#### Ejemplo 

Queremos que la solución del juego sea $(A,A)$, asumiendo que ese es el buen comportamiento. El juego se repetirá sólamente dos veces. 


|       |  **A**  |  **B**  |  **C**  |
|:-----:|:-------:|:-------:|:-------:|
| **A** | $(4,4)$ | $(0,5)$ | $(0,0)$ |
| **B** | $(5,0)$ | $(1,1)$ | $(0,0)$ |
| **C** | $(0,0)$ | $(0,0)$ | $(3,3)$ |


Claramente $(A,A)$ no es [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrio de Nash]], pero hay que analizar los equilibrios del último dia. 

Si los jugadores se llegasen a coordinar para jugar $(A,A)$ y dejarán para el último dia la jugada del equilibrio de Nash, se tendría lo siguiente: 

$$\begin{align}
(A,A)&\to (C,C)\\  \\
4+3&=7
\end{align}$$

Esto siendo, claramente, distinto a jugar *"egoistamente"*, donde se jugaría lo siguiente: 

$$\begin{align}
(B,A)&\to(B,B)\\  \\
5+1&=6
\end{align}$$

Esto quiere decir que los jugadores no quieren perder el premio de mañana. En el cálculo $4+3>5+1$, los pagos de mañana se les llamará **pagos de continuación**. 