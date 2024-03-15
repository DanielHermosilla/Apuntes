
Hay dos jugadores posicionados lejos uno de otro. Cada jugador tiene una pistola con una sóla bala. Los jugadores, secuencialmente, hacen una decisión entre disparar al adversario o dar un paso para cortar la distancia. 

Si un jugador da un paso, el turno pasa al adversario. Si el jugador dispara y acierta, gana el juego. Si el jugador dispara pero no acierta, como no tiene una otra bala, pierde el juego. Cuando un jugador decide tirar, el juego acaba en ese turno, de una manera u otra. 

Aquí cada jugador va a tener un nivel de precisión que se escribirá como la [[Probabilidades|probabilidad]] de acertar, que depende de la distancia del tiro. 

Para un jugador $i$ representamos con $p_i(d)$ con probabilidad de acertar de distancia $d$. 

Los jugadores saben su propia precisión como lo del adversario. Suponemos que uno de los jugadores es mejor tirador que el otro. *¿Quién va a disparar primero?* 

La anticipación es clave. Los jugadores van a intentar predecir qué va a hacer su adversario en su turno. 

Observemos que si aun nadie había tirado: 

- Si jugador $i$ sabe que jugador $j$ no va a tirar en su turno, ¿qué va a hacer en su turno? No va a disparar y dará un paso, porque en su próximo turno va a tener la oportunidad de disparar a una distancia más corta. 

- Si jugador $i$ sabe que $j$ va a disparar en su turno, ¿qué va a hacer? Va a disparar si su probabilidad de acertar es más que la probabilidad de $j$ de acertar en su turno. De tal forma, la probabilidad de ganar de cada uno es: 

$$\begin{align}
p_i(d)\tag{Jugador i}\\  \\
1-p_j(d-1)\tag{Jugador j}
\end{align}$$

Si uno está seguro que va a ganar, hay que imponer: 

$$p_i(d)>1-p_j(d-1)$$

De tal forma, hay que imponer: 

$$p_i(d)+p_j(d-1)>1$$

El jugador $i$ no va a disparar aunque sepa que $j$ va a disparar si: 

$$p_i(d)+p_j(d-1)<1$$

Como empiezan muy distantes, en el principio se va a satisfacer la desigualdad estricta. Es posible representar $d^*$ como la distancia más larga donde se cumple que: 

$$p_i(d^*)+p_j(d^*-1)\geq 1$$

En un caso hipotético donde se llega a la distancia $d^*$, un jugador ha dado el último paso para llegar a distancia cero, entonces el jugador sabe que su oponente va a disparar. Como la distancia $1$ satisface $p_i(d)+p_j(d-1)\geq 1$, en lugar de dar el último paso, dispara. 

El juego nunca llegaría a una distancia $0$, un jugador va a disparar a una distancia $1$. Pero, el jugador que tiene que dar el paso para llegar a distancia $1$, como sabe que su adversario va a disparar, no va a dar el paso, pero disparar. Entonces el juego nunca llegará a distancia $1$. Induciendo hacia atrás, el juego nunca llegará a distancia $d^*-1$.  En $d^*$ es el momento oportuno donde ambos deben disparar. Antes de $d^*$ se tiene una [[Eliminación Iterada de Estrategias Estrictamente Dominadas|estrategia estrictamente dominada]]. 