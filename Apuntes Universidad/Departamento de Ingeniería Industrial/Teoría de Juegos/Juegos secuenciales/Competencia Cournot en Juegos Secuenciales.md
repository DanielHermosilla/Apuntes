---
~
---

La [[Competencia Cournot|competencia Cournot]] ya fue definida anteriormente, donde firmas en un oligopolio compiten por cuanto producir. Por lo tanto, la [[Estrategia|estrategia]] es $S_i=\mathbb{R}_+$. Pero, **ahora la Firma $1$ decide primero y luego decide la Firma $2$**. Por lo tanto, los pagos los determinan los costos de producción y el precio del mercado: 

$$\begin{align}
c(q)&=c\cdot q\tag{Costo marginal}\\  \\
p(q_1,q_2)&=a-b(q_1+q_2)\tag{Precio del mercado}
\end{align}$$

Nuevamente, se tienen las mismas utilidades de antes: 

$$\begin{align}
\Pi_1(q_1,q_2)&=(p-c)q_1=[a-b(q_1+q_2)-c]q_1=pq_1-cq_1\\  \\
\Pi_2(q_1,q_2)&=(p-c)q_2=[a-b(q_1+q_2)-c]q_2=pq_2-cq_2
\end{align}$$

Pero como esto es [[Juegos secuenciales|secuencial]], se le denominará **competencia Stackelberg**. Entonces, la pregunta a hacer es *¿A qué firma le conviene partir variando su producción?*. Lo mejor es verlo en **retrospectiva**, vale decir, una **inducción hacia atrás**. En el *último dia*, al tener un juego simultáneo, se tiene que las utilidades del Equilibrio de Nash para el Jugador $2$ es: 

$$\begin{align}
BR_2(q_1)&=\frac{a-c}{2b}-\frac{q_1}{2}
\end{align}$$

Por lo tanto, en cierto sentido, la firma $1$ entiende que las utilidades de $2$ depende de su producción ($q_1$). Notemos lo siguiente: 

$$\frac{\partial BR_2(q_1)}{\partial q_1}<0$$

Esto quiere decir, **cuando $q_1$ aumenta, como respuesta, $q_2$ baja**. Y ahora, si nos fijamos en las utilidades de la firma $1$: 

$$BR_1(q_2)=\frac{a-c}{2b}-\frac{q_2}{2}$$

Entonces, **le conviene que $q_2$ sea menor para obtener más utilidades**. Y eso se logra, justamente, al producir más. 

Aunque, algo a notar es que la relación $q_1\to q_2$ no es unitaria, de hecho, nos podemos fijar que: 

$$\frac{\partial BR_2(q_1)}{\partial q_1}=-\frac{1}{2}$$

Esto quiere decir que, al cabo que $q_1$ produce $2$ unidades, $q_2$ reduce una unidad. Esto implica que la proporción $q_1+q_2$ aumenta, teniendo un impacto positivo en los precios a los consumidores $\downarrow p(\uparrow\Delta)=a-b(\uparrow\Delta)$. 

Notemos, por lo tanto, que si se volviera a la función utilidad y se deja utilidad de la Firma $1$ en función de su propia producción: 

$$\frac{\partial\Pi_1[q_1,q_2(q_1)]}{\partial q_1}=0\implies q_1=\frac{a-c}{2b}$$

Esto es una cantidad mayor que el caso donde se llega al equilibrio simultáneo. Por esto mismo, **es mejor decidir primero**. 

Ahora, existe un teorema que nos dice que, en este tipo de juegos, bajo ciertas condiciones, siempre se puede forzar una victoria del primer jugador o el segundo fuerza una victoria o *empate*. 

>[!check] Teorema de Zermelo
>
>En cualquier juego finito de suma cero y de información perfecta para dos jugadores (en el que el azar no interviene), si el juego se juega sin errores, entonces o el primer jugador puede forzar una victoria, o el segundo jugador puede forzar un empate, o el segundo jugador puede forzar una victoria.
>
>En otras palabras, con estrategia óptima de ambos jugadores:
>
>- Si el juego es favorable para el primer jugador, él tiene una estrategia ganadora.
>
>- Si el juego es desfavorable para el primer jugador, entonces el segundo jugador tiene una estrategia ganadora.
>  
>  - Si ninguno de los jugadores tiene una estrategia ganadora, entonces el juego terminará inevitablemente en empate.
>    
>    En otras palabras, con estrategia óptima de ambos jugadores: 
>    
> - Si el juego es favorable para el primer jugador, él tiene una estrategia ganadora. 
> - Si el juego es desfavorable para el primer jugador, entonces el segundo jugador tiene una estrategia ganadora. 
> - Si ninguno de los jugadores tiene una estrategia ganadora, entonces el juegoterminará en un empate
>   
>   
Es importante resaltar que este teorema no proporciona una estrategia explícita para ganar o empatar; simplemente establece que tal estrategia existe.

Notar que esto es un teorema de **existencia**, vale decir, nos dice que la posibilidad, no así del cómo llegar. 

Visto de forma gráfica, sería el siguiente árbol de decisión: 

![[test2.png|center|500]]


La demostración de esto se puede hacer bajo inducción. Claramente el caso base a elegir depende que parte del teorema se quiere demostrar.  
