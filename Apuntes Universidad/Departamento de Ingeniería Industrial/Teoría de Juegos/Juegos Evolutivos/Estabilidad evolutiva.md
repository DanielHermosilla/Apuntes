
Corresponde a la estrategia que ganaría en un [[Juegos Evolutivos|juego evolutivo]]. 

>[!cite] 
>En un juego simétrico de dos jugadores, una estrategia pura $s$ es **evolutivamente estable** si hay un $\bar{\epsilon}>0$ tal que para toda $\epsilon<\bar{\epsilon}$:  
$$(1-\epsilon)u_i(s,s)+\epsilon u_i(s,s')>(1-\epsilon)u_i (s',s)+\epsilon u_i(s',s')\;\;\forall s'\neq s$$

>[!cite] 
> En un juego simétrico de dos jugadores, una estrategia pura $s$ es **evolutivamente estable** si: 
> 
> - $(s,s)$ es un [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|Equilibrio de Nash]] simétrico, vale decir; 
> 
> $$u_i(s,s)\geq u_i(s',s),\;\forall s'$$
> 
> - Si existe un $s'\neq s$ tal que $u_i(s,s)=u_i(s',s)$, entonces $u_i(s,s')>u_i(s',s')$ 

Ambas definiciones son equivalentes, se puede demostrar al hacer $\epsilon\to 0$.

Notemos que si $s$ es una estrategia evolutivamente estable, entonces $(s,s)$ es necesariamente un [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrio de Nash]], porque si $s$ no era una [[La mejor respuesta|mejor respuesta]] contra $s$, la mejor respuesta podía invadir a una población que juega $s$. 

De aquí se denota que si $(s,s)$ es un [[Departamento de Ingeniería Industrial/Economía/Teoría de juegos/Equilibrio de Nash|equilibrio de Nash]] estricto, entonces $s$ es una estrategia evolutivamente estable. 

- Pueden haber multiples estrategias evolutivamentes estables. 

- Una estrategia evolutivamente estable puede ser más eficiente que una otra estrategia. Se puede observar diferentes costumbres en diferentes paises. No es fácil cambiar una costumbre, aunque es ineficiente. (por ejemplo, la esclavitud, discriminación de género, etc). 
#### Ejemplo 

Se tiene el siguiente juego, donde $(A,A)$ y $(B,B)$ son equilibrios de Nash: 

![[Pasted image 20230831105230.png|center]]

¿*Es $B$ una estrategia evolutivamente estable?* 

$$\begin{align}
EU_B[\epsilon,1-\epsilon]&=0\\  \\
EU_A[\epsilon,1-\epsilon]&=\epsilon
\end{align}$$

A partir de esto, no lo sería. 

#### Ejemplo: Juego de la gallina 

Dos autos conducen uno contra otro hacia un choque frontal. Si un conductor gira para evitar el choque, es una gallina.

![[Pasted image 20230831111915.png|center]]


Hay dos equilibrios de Nash, $(S,G)$ y $(G,S)$. Ninguno es un [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|equilibrio de Nash]] simétrico. No existe una estretagia evolutivamente estable, entonces se tendrá que buscar una [[Estrategias Mixtas|estrategia mixta]] que sea evolutivamente estable. 

Por lo tanto, para $\sigma=(p, 1-p)$ se busca la utilidad esperada: 

$$\begin{align}
EU_1[S,\sigma]&=2-2p\\  \\
EU_1[G,\sigma]&=p \\ \\
p&=\frac{2}{3}
\end{align}$$

Entonces, *¿será un equilibrio de Nash estricto?*. Como es un [[Equilibrio de Nash en Estrategias Mixtas|equilibrio de Nash en estrategias mixtas]], no es un equilibrio de Nash estricto. 

