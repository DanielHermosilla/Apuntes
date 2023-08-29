
Un perfil de [[Estrategias Mixtas|estrategias mixtas]] $\sigma^*=(\sigma_{1}^{*},\sigma_{2}^{*},\dots,\sigma_{n}^{*})$ es un **[[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|Equilibrio de Nash]] en estrategias mixtas** si para cada jugador $i$, $\sigma_{i}^{*}$ es una mejor respuesta a $\sigma_{-i}^{*}$

$$EU_i(\sigma_{i}^{*},\sigma_{-i}^{*})\geq EU_i(\sigma_{i}^{'},\sigma_{i-1}^{*})\;\;\forall\sigma_{i}^{'}\in\Sigma_i$$

Si se mira la desigualdad de cerca: 

$$\sum_{s_i\in S_i}\left[\sigma_{i}^{*}(s_i)EU_i(s_i,\sigma_{-i}^{*}\right)\geq\sum^{}_{s_i\in S_i}\left[\sigma_{i}^{'}(s_i)EU_i(s_i,\sigma_{-i}^{*})\right]\;\;\forall\sigma_{i}^{'}\in\Sigma_i$$

#### Ejemplo 

En el tenis los jugadores quieren confundir al otro al servir, entonces una estrategia pura no es un [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|Equilibrio de Nash]]. 

![[Captura de pantalla 2023-08-29 a la(s) 10.42.25.png|center|450]]


De la matriz se deduce que: 

- Jugador 1 tira mejor a la izquierda 
- Jugador 2 defiende mejor su derecha que su izquierda 

Como solo son dos estrategias, se busca el punto donde ambas estrategias dan el mismo pago. 

Para calcular la mejor respuesta de Jugador 2, se debe calcular los pagos esperados de Jugador 1. 

Entonces, los pagos esperados de Jugador $1$ con la estrategia mixta $(q,1-q)$: 

$$EU_1[L,(q,1-q)]=qU_1(L,l)+(1-q)U_1(L,r)=80-30q$$

Por el otro lado, para la estrategia $R$: 

$$EU_1[R,(q,1-q)]=qU_1(R,l)+(1-q)U_1(R,r)=20+70q$$

Los pagos deben ser iguales en una mejor respuesta, entonces: 

$$80-30q=20+70q\implies q^*=0.6$$

Ahora, si se hace lo mismo para los pagos del Jugador 2 con probabilidad mixta $(p,1-p)$, se llega también que: 

$$10+40p=80-60p\implies p^*=0.7$$

Entonces, el equilibrio de Nash, llegaría a ser: 

$$(p^*,q^*)=(0.6,0.7)$$

Si se quiere verificar que es un equilibrio de Nash, entonces los pagos de los jugadores no deben mejorar con una estrategia diferente. 