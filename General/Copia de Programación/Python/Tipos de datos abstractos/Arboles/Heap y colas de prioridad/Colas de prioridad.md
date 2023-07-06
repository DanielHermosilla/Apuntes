Las colas de prioridad consisten en un algoritmo sustentado fuertemente por [[Heap]], en específico, *heapify*. La idea es tener un algoritmo tal que los elementos con mejor prioridad estén al inicio de la cola, y los elementos de menor prioridad estén al final. Esto se puede representar perfectamente con un árbol [[Heap]]. 

Los valores que tienen el mayor número son aquellos que tienen mejor prioridad, entonces en el caso de querer sacar un elemento, se sacaría el de mejor prioridad. No obstante, el de menor número estaría en los últimos niveles y se sacarían de último. En caso de obtener una lista desordenada ésta se puede ordenar por [[Heap sort|heap sort]]. 

Por el otro lado, si los nodos quisieran representar más información  a parte de su prioridad, se puede ocupar un [[Arboles cartesianos|árbol cartesiano]], es decir, un árbol cuyo nodo tiene dos valores de información.  

Los usos de estos son inlimitados, pueden representar la prioridad en muchos sentidos con tal de poder ser representado por un número, y cada elemento tenga una prioridad no equivalente. 
