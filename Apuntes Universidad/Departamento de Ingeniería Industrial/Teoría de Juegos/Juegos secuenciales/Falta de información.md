
En un [[Juegos secuenciales|juego secuencial]] es posible tener falta de información, donde no se sabe perfectamente lo que jugaría el otro jugador. 

![[Pasted image 20230921110241.png|center]]

Esto se representa con la linea interlineada. En el esquema se puede decir que si Jugador $1$ juega $M$ o $U$ el jugador $2$ no sabe que es lo que juega. Formalmente se pueden escribir como [[Conjuntos|conjuntos]] de información. En este caso, el conjunto de información del segundo Jugador llegaría a ser $I_2=\lbrace\lbrace D\rbrace,\lbrace M,U\rbrace\rbrace$. 

En estos juegos, el Jugador $1$ **es consciente** que hay asimetrias de información. En estos casos, por lo general, se ocupa **randomización**. 

>[!tip] Conjunto de información 
>
>Un conjunto de información $i$ es un conjunto de nodos del jugador $i$ entre el cual el jugador no puede distinguir. 
>
>Utilizando conjuntos de información capturamos las situaciones donde jugadores no saben qué pasó antes de su turno.  Esto debe satisfacer las siguientes condiciones: 
>
>1. **Consistencia**: El jugador no puede tener diferentes números de estrategias en los dos nodos diferentes en el mismo conjunto de información. Si el jugador tiene diferentes estrategias puede distinguir entre los nodos contando sus estrategias. 
>   
>   
>   
>2. **Memoria Perfecta:** Cada jugador recuerda perfectamente que había jugado y no podemos tener un conjunto de información como la siguiente imagen: 
>   
>   ![[Pasted image 20230921112303.png|center]]
>   


>[!hint] Información perfecta 
>
>Un escenario donde todos los conjuntos de información en el árbol del juego tienen un sólo miembro. 

La información imperfecta sería lo contrario a la definición de información perfecta. 