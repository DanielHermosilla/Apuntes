
Este algoritmo se ocupa en aplicaciones como *Waze*, donde se trata de buscar la distancia mínima. Considerando un grafo dirigido $G=(V,E)$ donde para cada arco $e=(u,v)$ se conoce su largo o distancia, donde $d(e)=d(u,v)\geq 0$ . Se puede extener la función $d$ a todo $V\times V$ si se define $d(u,v)=\infty$ cuando $(u,v)\notin E$ .

Este problema se resuelve con dos variantes: 

- Encontrar todos los caminos más cortos desde un origen $s$ hasta todos los demás nodos del grafo. 

- Encontrar todos los caminos más cortos entre todos los pares de nodo del grafo. Es decir, iterar $n$ veces el problema anterior cambiando el nodo de origen. 

## Algoritmo de Dijkstra 

Este algoritmo está hecho para resolver el primer problema. La idea es mantener un conjunto $A$ de nodos alcanzables desde el nodo de origen e ir extendiéndolos con cada iteración. Por eso mismo, en la primera iteración se define $A=\lbrace s\rbrace$ . Es decir, se define $A$ como el conjunto de todos los cáminos óptimos desde $s$. 

```python 

def Dijkstra(V,E,d,s):

	A=[s]
	
	for v in V:
	
		D[v]=d(s,v)
	
	D[s]=0
	
	# D[] almacena las distancias óptimas desde s para los nodos en A
	
	# y las distancias óptimas tentativas para los nodos en V-A
	
	while A!=V:
	
		# Encontramos el nodo v de menor distancia óptima tentativa
		
		v = findmin(D[u] for u in V-A)
		
		# Agregamos v al conjunto alcanzable
		
		A.append(v)
		
		# recalculamos las distancias óptimas tentativas
		
		# considerando la posibilidad de pasar por el nuevo nodo v
		
		for w in vecinos[v]: # los nodos w tal que (v,w) in E
		
			D[w] = min(D[w],D[v]+d(v,w))
		
	# Al terminar, D[] almacena las distancias óptimas definitivas
	
	return D
```

