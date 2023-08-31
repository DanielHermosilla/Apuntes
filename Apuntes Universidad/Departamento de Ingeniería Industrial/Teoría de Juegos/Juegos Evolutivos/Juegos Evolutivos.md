
Interpretando a los jugadores como [[Poblaciones Mixtas|poblaciones]], se pueden interpretar un [[Conjuntos|conjunto]] de juegos como **juegos evolutivos**. Esto se ocupa mucho en el área de la genética. Esto en la economía se puede ver para estudiar *costumbres*, *instituciones*, etc. 

Las costumbres, instituciones, leyes que dan mejores resultados sobreviven y van a ser copiados, vale decir, adoptados. 

#### Ejemplo 

Se tiene el siguiente juego, donde el [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrio de Nash]] es $(N,N)$ por [[Eliminación Iterada de Estrategias Estrictamente Dominadas|eliminación iterada de estrategias estrictamente dominadas]]. 

![[Pasted image 20230831103759.png|center]]


Pero, si suponemos que toda la población empieza a jugar $C$, *¿ésta podrá ser evolutivamente estable?*

Supongamos que todos empieza jugando $C$, en todos los emparejamientos ganan $2$. Ahora suponemos que aparece una pequeña minoria $\epsilon>0$ que juega $N$. En este caso, el mutante en comparación con el individuo normal gana $3$ y el resto $0$. 

Se términa llega que los mutantes van a prosperar, por lo tanto, **$C$ no es evolutivamente estable**. Esto se puede ver al calcular los pagos esperados:  

$$\begin{align}
EU_C[1-\epsilon,\epsilon]&=(1-\epsilon)\cdot 2+\epsilon\cdot 0=2-2\epsilon\\  \\ 
EU_N[1-\epsilon,\epsilon]&=(1-\epsilon)\cdot 3+\epsilon\cdot 1=3-2\epsilon 

\end{align}$$

Esto significa que los mutantes ganan más que los normales. De aquí se establecen algunas lecciones: 

1. **El resultado de la evolución no es necesariamente eficiente**. Aun así, existen ejemplos de cooperación. 
2. **Una estrategía [[Dominancia estricta|estrictamente dominada]] no puede ser una estrategia evolutivamente estable**. 

#### Ejemplo 

Ahora, se tiene el siguiente juego: 

![[Pasted image 20230831104625.png|center]]


Claramente los [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrios de Nash]] son $(A,A),\;(B,C),\;(C,B)$. *¿Es $C$ una estrategia evolutivamente estable?*. No, porque una mutación de $B$ puede invadir a $C$: 

$$\begin{align}
EU_C&=\epsilon\\  \\
EU_B&=1-\epsilon
\end{align}$$

La mutación va a prosperar, pero $B$ tampoco es evolutivamente estable. 

Notemos que ocurre lo mismo con $(B,B)$. 

Observemos que $(C,C)$ y $(B,B)$ no son [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrio de Nash]], entonces, para una estrategia $s$, si $(s,s)$ no es [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrio de Nash]], entonces $s$ no es una estrategia evolutivamente estable. 