
En los otros tipos de juegos que se han analizado, los jugadores decidían simultaneamente sin observar las acciones de los otros jugadores. La diferencia con los juegos secuenciales consiste que los jugadores **juegan en turnos** y **observan la historia del juego**. 

Notemos que si los jugadores no pudiesen observar la acción del resto, daría lo mismo si las desiciones fueran simultáneas o secuenciales. Pero ahora, como existen decisiones en secuencias, se tiene, valga la redundancia, juegos secuenciales. 

>[!success] Juegos Secuenciales
>Un juego secuencial es un tipo de juego en Teoría de Juegos donde los jugadores toman decisiones en secuencia, y cada jugador puede observar las acciones de los jugadores que le precedieron antes de tomar su decisión. Estos juegos suelen representarse con un árbol de juego, que muestra las posibles acciones en cada etapa y los pagos asociados.

Como dice la definición, estos juegos se visualizan a través de **árboles de decisiones**. Por esto mismo, la forma de ver los juegos es pensar *hacia adelante*, en la decisión que hará el otro posterior a la tuya. 

En este tipo de juegos, a diferencia de los anteriores, existen equilibrios **no eficientes**. Esto es muy común en el ámbito de las inversiones y se denomina normalmente como *"riesgo moral" (moral hazard)*. 

#### Ejemplo: El juego de la entrada al mercado 

Este ejemplo se utilizará únicamente para dar a entender en qué consisten los árboles de decisiones y cual es su lectura. 

Se tienen dos firmas, donde la empresa $A$ es dueña de un monopolio y la empresa $B$ está evaluando en entrar o no al mercado. 

- Si la empresa $B$ no entra, la empresa $A$ mantiene el monopolio y recibe un pago de 10, mientras que la empresa $B$ no pierde ni gana. 

- Si la empresa $B$ entra se tienen dos opciones de réplica por parte de $A$: competir o acomodarse. 

- Si la empresa $A$ compite, ambos reciben un pago de $1$, mientras que si se acomoda, $A$ recibe $4$ y $B$ recibe $6$. 

![[test-3.png|center|500]]


Por lo tanto, claramente el equilibrio de Nash sería $(4,6)$. Pareciera ser una respuesta *eficiente*, pero esto no ocurre en todos los casos. 

Notemos que en un juego de información, tanto con información perfecta como imperfecta, **es posible llegar a equilibrios de Nash irracionales** al resolver ocupando [[matriz|matrices]]. Entonces se llegan a [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrio de Nash]] no intuitivos. 