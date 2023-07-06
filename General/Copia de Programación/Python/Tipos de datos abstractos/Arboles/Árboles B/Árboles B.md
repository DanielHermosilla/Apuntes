Notemos que la descripción de la [[Estructura del disco|estructura del disco]] para almacenar datos con pointers se asimila mucho a un árbol de mucha entradas: 

![[IMG_572A7AEE8304-1.jpeg|center|400]]

![[IMG_CEDBA8CF83B8-1.jpeg|center|400]]


Por lo tanto, la filosofía de estos arboles es ordenar los datos por conjuntos. Haciendo alusión a los [[Busqueda binaria|arboles de busqueda binaria]], estos árboles hacen referencia a aquellos datos que están entre medio de ciertos índices. Por ejemplo: 

![[IMG_C223C960A175-1.jpeg|center]]

Al medio iría el nodo cuyos valores estén entre $[20,50]$. Por el otro lado, a la derecha irían los valores $50>$  y a la izquierda los valores $20<$.  En este caso, se tiene un árbol $2-3$, es decir, se tienen dos entradas y tres hijos. Pero esto se puede extrapolar a $n$ entradas y $n+1$ hijos. 

Por lo tanto, los árboles en realidad se pueden ver por grados. Por ejemplo, el [[Busqueda binaria|árbol de busqueda binaria]] se podría percibir como un árbol de grado dos, es decir, tiene dos entradas. 

## Creación 

Para crear un árbol tal como están impuestas las reglas, se caería en el mismo caso erróneo de la inserción de los [[Busqueda binaria|árboles binarios]] que tendría costo $O(n)$. Por lo tanto, las reglas a seguir son: 

- Cuando se va a crear el nodo, este se tiene que llenar con $\lceil \frac{m}{2}\rceil$, es decir, con $m$ siendo el grado del árbol. 
- Para imponer esta condición en la **raiz**, éste debe tener como mínimo dos hijos. 
- Todos las hojas deben estar a la misma altura. 
- La creación es "*bottom-up*". 


### Ejemplo 

Sea el árbol de grado $3$ y se quiere insertar el arreglo $[10,20,40,50]$. Primero se parte insertando los primeros tres datos, pero se llega al límite: 

![[IMG_FC74D850E175-1.jpeg|center|500]]

Entonces, se manda al mayor dato como padre y se crea un nuevo nodo hijo: 

![[IMG_6529F8187734-1.jpeg|center]]

Se podría ver como si se hubiera *spliteado* el nodo. Y podemos ver que el árbol está creándose de abajo hacia arriba.  