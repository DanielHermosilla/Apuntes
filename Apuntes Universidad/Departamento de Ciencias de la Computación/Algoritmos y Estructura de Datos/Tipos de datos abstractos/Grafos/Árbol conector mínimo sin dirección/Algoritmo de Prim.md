
Cuando se tiene un grafo cuyos arcos tienen cierto peso, entonces existen varios algoritmos para encontrar la ruta *más baratas*. Una de ellas es el algoritmo de Prim, que consiste en, básicamente, partir por la ruta más barata posible e ir expandiéndose como una mancha de aceite. 

```python 

def prim(V,E):

	e=arco_de_costo_minimo(E)
	
	(v,w)=vertices(e)
	
	T=[e] # árbol
	
	A=[v,w] # conjunto alcanzable
	
	while A!=V:
	
		e=arco_de_costo_minimo_que_conecta(A,V-A)
		
		(v,w)=vertices(e) # suponemos v en A y w en V-A
		
		T.append(e)
		
		A.append(w)

```

Al agregar elementos nuevos, hay que verificar si mediante su adición se alcanza otro acceso barato para acceder. 

En cada iteración, se buscan $n$ vértices, de ahí, $n-1$, etc, etc. Esto tiene orden $O(n^2)$. 

Aunque, se podría ocupar un [[Heap]], que consiste en colas de prioridad, vale decir, cada vez que se quiere buscar el mínimo, se ocupa un sistema prioritario. Esto es orden $O(mlogn)$. 

Ahora, para saber qué algoritmo es mejor es una pregunta que depende de la cantidad de arcos, que se hace de la siguiente forma: 

$$\begin{align}
¿m\log n&<n^2?\\\\
m&<\frac{n^2}{\log n}
\end{align}$$ 
Es decir, conviene usar [[Heap|heaps]] cuando se tienen pocos vértices, vale decir, el grafos *poco densos*.

