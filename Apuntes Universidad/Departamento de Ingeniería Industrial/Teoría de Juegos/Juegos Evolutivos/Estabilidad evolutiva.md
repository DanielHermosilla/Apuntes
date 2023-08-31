
Corresponde a la estrategia que ganaría en un [[Juegos Evolutivos|juego evolutivo]]. 

>[!cite] 
>En un juego simétrico de dos jugadores, una estrategia pura $s$ es **evolutivamente estable** si hay un $\bar{\epsilon}>0$ tal que para toda $\epsilon<\bar{\epsilon}$:  
$$(1-\epsilon)u_i(s,s)+\epsilon u_i(s,s')>(1-\epsilon)u_i (s',s)+\epsilon u_i(s',s')\;\;\forall s'\neq s$$

>[!cite] 
> En un juego simétrico de dos jugadores, una estrategia pura $s$ es **evolutivamente estable** si: 
> 
> - $(s,s)$ es un [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|Equilibrio de Nash]] simétrico, vale decir; 
> $$u_i(s,s)\geq u_i(s',s),\;\forall s'$$
> - Si existe un $s'\neq s$ tal que $u_i(s,s)=u_i(s',s)$, entonces $u_i(s,s')>u_i(s',s')$ 








Notemos que si $s$ es una estrategia evolutivamente estable, entonces $(s,s)$ es necesariamente un [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrio de Nash]], porque si $s$ no era una [[La mejor respuesta|mejor respuesta]] contra $s$, la mejor respuesta podía invadir a una población que juega $s$. 

De aquí se denota que si $(s,s)$ es un [[Departamento de Ingeniería Industrial/Economía/Teoría de juegos/Equilibrio de Nash|equilibrio de Nash]] estricto, entonces $s$ es una estrategia evolutivamente estable. 
#### Ejemplo 

Se tiene el siguiente juego, donde $(A,A)$ y $(B,B)$ son equilibrios de Nash: 

![[Pasted image 20230831105230.png|center]]

¿*Es $B$ una estrategia evolutivamente estable?* 

$$\begin{align}
EU_B[\epsilon,1-\epsilon]&=0\\  \\
EU_A[\epsilon,1-\epsilon]&=\epsilon
\end{align}$$

