
>[!tip] Grafos 
>
>Se define como un [[Grafo|grafo]] dirigido $G=(V,A)$ consiste en un conjunto de nodos o vértices $V$ y un conjunto de arcos $A\subseteq V\times V$

>[!hint] Flujos 
>Una red es un [[Grafo|grafo]] dirigido con algunas de las siguientes características: 
>
>- $b_i$: Cantidad de flujo que origina (desaparece) en el nodo $i$
>  
>  - $c_{ij}$: Costo unitario de ir de $i$ a $j$
>    
> - $I_{ij}, u_{ij}$: Capacidades inferiores y superiores del flujo por el arco $(i,j)$

### Flujo a costo mínimo 

Por lo tanto, para modelar esto, $x_{ij}$ llegaría a ser la cantidad de flujo mínimo que viaja de $i$ a $j$ y la restricciones llegarían a ser: 

- $I_{ij}\leq x_{ij}\leq u_{ij}$: flujo entre capacidades inferior y superior en cada arco $(i,j)$. 

- Flujo se mantiene en cada nodo (Kirchhoff)

$$\sum_{j:(i,j)\in A}x_{ij}=\sum_{k:(k,i)\in A}x_{ki}$$

- Flujo se mantiene en cada nodo 

$$\sum_{j:(i,j)\in A}x_{ij}-\sum_{k:(k,i)\in A}x_{ki}=b_i$$

- La función objetivo llegaría a ser: 

$$\min\sum_{(i,j)\in A}c_{ij}x_{ij}$$

