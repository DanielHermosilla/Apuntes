
En los juegos anteriores, se suponía que los jugadores conocían: 

- El número de los jugadores 
- Las [[Estrategia|estrategias]] de los jugadores 
- Los [[Función Utilidad|pagos]] de los jugadores 

Alguna excepción podría ser los juegos de [[Falta de información|información incompleta]].

Ahora, al igual que el concepto de [[Social trust|social trust]], supondremos que hay incertidumbre sobre los pagos que los jugadores obtienen en el juego. 

>[!danger] Juego Bayesiano 
>
>Un juego Bayesiano $(N,G,P,I)$ donde: 
>
>-$N$ es el [[Conjuntos|conjunto]] de jugadores 
>
>-$G$ es un conjunto de juegos con jugadores $N$ tal que cada jugador $i\in N$ tiene las mismas acciones en cada juego $g\in G$. 
>
>-$P$ es una distribución de [[Probabilidades|probabilidad]] sobre $G$. Eso se llama *"creencias a priori" (prior beliefs)*. 
>
>-$I=(I_1,\dots,I_n)$ es un perfil de particiones de $G$, uno para cada jugador. (Conjuntos de información de cada jugador). 


#### Ejemplo 

Se tiene un juego donde el Jugador $1$ quiere acompañar al Jugador $2$ al Cine ($C$) o a ver Fútbol ($F$). Sin embargo, él no sabe lo que jugará Jugador $2$. 

Existen dos tipos de Jugador $2$: 

- **Tipo A**: 

|       |  **C**  |  **F**  |
|:-----:|:-------:|:-------:|
| **C** | $(2,1)$ | $(0,0)$ |
| **F** | $(0,0)$ | $(1,2)$ |

- **Tipo B**: 
  
|       |  **C**  |  **F**  |
|:-----:|:-------:|:-------:|
| **C** | $(2,0)$ | $(0,2)$ |
| **F** | $(0,1)$ | $(1,0)$ |

Supondremos que la probabilidad de que el Jugador $2$ sea de tipo $A$ o $B$ es $1/2$ para cada uno. 



