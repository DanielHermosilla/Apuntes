


#### Ejemplo 

Hay dos jugadores negociando sobre $1$. Jugador $1$ ofrece una división $(s_1, 1-s_1)$  a el Jugador $2$. Si el Jugador $2$ rechaza, se cambian los roles y jugador $2$ hace una contraoferta $(s_2, 1-s_2)$. 

Ahora, añadiendo otro aspecto, en el período $1$ hay $1$ para dividir, pero si las negociaciones se alargan a período $2$ sólo queda $\delta<1$ para dividir. Esto se debe a que el tiempo es costoso. Esto se puede racionalizar bajo los siguientes argumentos: 

- Si las negociaciones acaban en el primer dia, se puede ingresar el dinero en el banco y obtener un interés al dia $2$. 

- Los jugadores son impacientes y valoran el dinero de hoy más que el dinero de mañana. 

En ambas interpretaciones, el $1$ de mañana vale $\delta$ de hoy. 

Este juego es [[Juegos secuenciales|secuencial]] y se resuelve con inducción hacia atrás. De hecho, es igual a un juego de [[Últimatos|últimato]]. El segundo jugador ofrecerá lo mínimo posible y el jugador $1$ va a aceptar todas las ofertas. 

Si hacemos la inducción correctamente, el jugador $1$ va a tratar de hacer una oferta coherente al primer dia para evitar la devaluación. 

De hecho, si la negociación sigue un patrón que sigue una [[Series geométrica|serie geométrica]]. Notemos que si hay 10 iteraciones, se llega que el pago es: 

$$(1-\delta+\delta^2-\delta^3+\dots-\delta^9,\delta-\delta^2+\delta^3-\dots+\delta^9)$$

Por lo tanto, notemos que: 

$$\begin{align}
s&=1-\delta+\delta^2-\delta^3+\dots-\delta^9\\  \\
\delta s&=\delta-\delta^2+\delta^3+\dots+\delta^9-\delta^{10}\\  \\
1-\delta^{10}&=s+\delta s\\  \\
s&=\frac{1-\delta^{10}}{1+\delta}\\  \\
1-s&=\frac{\delta + \delta^{10}}{1+\delta}
\end{align}$$

Si $t\to\infty$, entonces se llega a una **división equitativa**. Aun así, esto no modela la realidad, no todas las ofertas son equitativas. En una negociación verdadera no se sabe si el otro es más paciente que el otro. 

Además, tampoco se definieron los [[Medición del excedente|excedentes]], es decir, no se considera el máximo precio a pagar y el mínimo precio a pagar. Esto nos da una [[Falta de información|falta de información]] haciendo que sea un juego de **información incompleta**. 

El último concepto es muy importante, **cuando el mínimo precio aceptable para el vendedor no se sabe**, es posible llegar a resultados ineficientes. 












