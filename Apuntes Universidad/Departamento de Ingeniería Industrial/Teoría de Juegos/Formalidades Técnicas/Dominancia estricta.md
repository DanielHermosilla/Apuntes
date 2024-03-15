
Se dice que una [[Estrategia|estrategia]] es **estrictamente dominada** si existe una otra estrategiia que da mayores pagos para *cualquier* [[Departamento de Ingeniería Industrial/Economía/Teoría de juegos/Juego|juego]] de los otros jugadores. 

Aun así, jugar con dominancia estricta no siempre puede llegar al mejor resultado: 

![[Captura de pantalla 2023-08-08 a la(s) 11.09.27.png|center|400]]

Aca la estrategia por dominancia estricta sería $(\alpha,\alpha)$, pero la [[Estrategia|estrategia]] que conviene a ambos sería $(\beta,\beta)$.  

Aun así, **no existen incentivos para jugar $\beta$**. De hecho, a pesar de haber comunicación entre ambas partes, decisiones racionales pueden conducir a malo resultados para todos. 

# Definición formal 

Un jugador $i$, una [[Conjunto de jugadas|estrategia]] $s_i\in S_i$ es **estrictamente dominada** si existe una estrategia $s_{i}^{'}\in S_i$ tal que: 

$$u_i(s_i,s_{-i})<u_i(s_{i}^{'},s_{-i})\;\;\;\forall s_{-i}\in S_{-i}$$

Diremos que $s_i$ es estrictamente dominada $s_{i}^{'}$. 