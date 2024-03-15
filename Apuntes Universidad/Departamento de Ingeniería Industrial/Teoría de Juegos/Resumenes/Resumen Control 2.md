# Conjuntos de Información 

Hasta la fecha se han analizado dos tipos de juegos: los **simultaneos** y **secuenciales**. Sin embargo, existen situaciones estratégicas donde se tienen una mezcla de los dos casos. Vale decir, **jugadores toman decisiones secuencialmente y otros simultáneamente**. 

>[!hint] Conjunto de Información 
>Un conjunto de información del jugador $i$ es un conjunto de nodos del jugador $i$ entre cual el jugador no puede distinguir. 
>
>Utilizando los conjuntos de información se capturan situaciones donde los jugadores no saben qué pasó antes de su turno. 

Los conjuntos de información deben cumplir dos propiedades: 

- **Consistencia:** El jugador no puede tener diferentes números de estrategias en dos nodos diferentes en el mismo conjunto de información. 

- **Memoria Perfecta**: Cada jugador recuerda perfectamente que había jugado. 

>[!tip] Información imperfecta 
>Escenario donde todos los conjuntos de información en el árbol de juego tienen un sólo miembro, o en término más simples, **son los escenarios donde no hay información perfecta**. 

#### Ejemplo: 

En este caso es posible considerar el siguiente juego, donde se tiene una línea punteada entre los nodos de $J2$. Esto representa que **el Jugador $2$ no sabe cuál es la acción del Jugador $1$ en aquellos nodos.
 ![[Pasted image 20231102130734.png|center]]


Esto significaría que, si el Jugador $1$ eligiera jugar $D$, entonces el Jugador $2$ si sabría dónde se encuentra. No así si se optara por jugar $M$ o $U$. 

Para este tipo de juegos, se dirá que $M$ y $U$ estarían en el mismo conjunto de información. Formalmente, se dice que los conjuntos de información del Jugador $2$ llegarían a ser $I_2=\lbrace\lbrace D\rbrace,\lbrace M,U\rbrace\rbrace$.

Notemos que si se elige jugar $D$ se tendría un juego secuencial normal. Se resolvería por inducción hacia atrás y se llegaría a un equilibrio con la estrategia $(D,r)$. El problema está cuando el Jugador $1$ **no juega $D$.  

En tal caso, la única opción que tiene el segundo Jugador es randomizar entre $u$ y $d$ con $\sigma_2=[r,(1/2,1/2)]$. Así, el Jugador $1$ tiene un pago esperado de jugar $M$ o $U$ igual a $2$, que es mejor que jugar $D$. Por ende, como jugar $M$ o $U$ da lo mismo, el primer jugador puede randomizar las estrategias como quiera. 

Notemos que la randomización del Jugador $1$ debe ser equitativa entre $M$ y $U$, ya que de poner más probabilidad en un nodo, el Jugador $2$ jugará la estrategia que le de utilidades de $(0,4)$ con mayor probabilidad. Así, se tiene que $\sigma_1=(0,1/2,1/2)$. Por lo tanto, la solución llegaría a ser: 

$$\sigma_1=\begin{pmatrix}
0 \\
1/2 \\
1/2
\end{pmatrix}\;\land\;\sigma_2=\begin{pmatrix}
r \\
1/2 \\
1/2
\end{pmatrix}$$

Por lo tanto, se concluye que **cambiar la estructura de información cambia la solución del juego**. 
## Subjuego 

>[!tip] Subjuego 
>Un subjuego es una parte de un juego tal que: 
>
>- El subjuego empieza de un único nodo 
>  
>- Incluye todos los sucesores del nodo raíz 
>    
>- Nunca divide ningún conjunto de información 


Un ejemplo de un subjuego se ve en el ejemplo anterior, donde se tiene un subjuego desde el primer nodo. 

>[!tip] Equilibrio subjuego perfecto 
>Se dice que un **equilibrio de Nash** es un equilibrio subjuego perfecto si induce un equilibrio de Nash en **todos** los subjuegos del juego original. 

#### Ejemplo 

Se tiene el siguiente juego secuencial: 

![[Pasted image 20231102161010.png|center|400]]



Claramente en el nodo del Jugador $2$ hay un subjuego. Primero, para encontrar los equilibrios de Nash escribimos la matriz de pago del subjuego del nodo del Jugador $2$: 

|       |  **a**  |  **b**  |
|:-----:|:-------:|:-------:|
| **a** | $(2,1)$ | $(0,0)$ |
| **b** | $(0,0)$ | $(1,2)$ |

Claramente el equilibrio de Nash es $(a,a),(b,b)$ que están en estrategias puras. Por lo tanto, se reemplaza la rama del juego con los pagos del equilibrio: 

![[Pasted image 20231102161317.png|center]]

Por lo tanto, el Jugador $1$ eligirá $D$ independiente de lo que juegen. Así, se encuentran dos equilibrios de subjuegos perfectos. De hecho, existe uno más con estrategias mixtas. 






