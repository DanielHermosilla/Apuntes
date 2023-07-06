
Antes de aprender sobre los árboles B, es necesario saber como funciona la estructura del disco para saber como los datos son guardados.

![[IMG_26AD66CE8374-1.jpeg|center|500]]

El disco está dividido por *sectors*, que llegaría a ser el área roja, por *tracks*, que equivale a los distintos niveles y *blocks*, que son la intersección de los sectors con los tracks. Normalmente los blocks son de $512$ bytes. Un bloque normalmente se refiere como: 

$$\text{Block}=(\text{Track},\;\text{Sector})$$

Los bloques de $512$ bytes se ven de la siguiente forma

![[IMG_AB92CCB8C623-1.jpeg|center]]

Donde cada byte se llama *offset*. Para alcanzar un byte en específico, entonces, hay que saber la dirección del bloque y su *offset*. 

La memoria RAM, conocida como *main memory*, es, por así decirlo, la memoria instantánea, tiene que acceder a los datos a través del disco. Dentro de la RAM es lo que se hacen las estructuras de datos.

Normalmente, la eficiencia o rápidez para acceder los datos, depende de en cuantos bloques pueden ser almacenados. Por ejemplo, si tengo un [[Diccionarios|diccionario]] con $100$ entradas y me ocupa $25$ bloques, entonces se va a demorar más en acceder que si estuvieran guardados en $15$ bloques. 

Esto se debe dado que el disco, para acceder a la información del diccionario, no sabe en que bloque exactamente está guardada la información de un ítem, entonces tiene que recorrer los $25$ bloques para hacer una llamada. 

Ahora, un método para optimizar esto es ocupar *pointers*. Es decir, ocupar índices que representen un dato en específico del diccionario. Si se quiere acceder a la entrada número $23$, entonces se preguntaría al *pointer* del índice $23$. Ahora, crear los pointers también ocupan espacios en bloques, pero es mucho menor al espacio de un diccionario. Por ejemplo,  se pueden usar $4$ bloques en pointers que señalen al diccionario de $100$ entradas y $25$ bloques. De tal forma, si se quiere acceder a un dato en específico, sólo se requiere acceder a los *pointers*. 

También se puede tener un *pointer* de un *pointer*. Es decir, supongamos que se tienen $1000$ entradas y los bloques de los índices llegasen a ser demasiados. Además, supongamos que se pueden almacenar a lo más $32$ *pointers* por bloques, entonces se puede hacer un bloque con índices $1,33,65,\dots$ que señalen los *pointers* en aquellos intervalos de información. Esto se llama *sparce index*.  Esta es la idea que origina a los árboles B. 


