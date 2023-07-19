
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
Eso si esto tiene una limitación, y es cuando se tienen **distancias negativas**. Existen contraejemplos donde las distancias calculadas bajo este algoritmo llegarían a no ser las optimas. 

## Algoritmo de Floyd 

Para aplicar este algoritmo, los nodos se numeran arbitrariamente $1,2,\dots,n$. El algoritmo va a ir construyendo una matriz $D$ tal que al final, $D[i,j]$ va a ser el largo del camino más corto que va desde el nodo $i$ hasta el nodo $j$. Es una forma de **programación dinámica** para resolver el problema del camino más corto. 

Es decir, como input se recibe una matriz "$d$",  $n\times n$, donde la posición $i,j$ es el largo del arco $(i,j)$ o $+\infty$ si no hay arco. 

Como output, se tiene la matriz de los caminos. 

### Método *Greedy* 

Una forma simple y *greedy* de hacerlo, es simplemente aplicar el algoritmo de Dijkstra para cada vértice posible. Esto tomaría una complejidad de $n^{2}\times n$. Obviamente no es lo óptimo. 

El invariante es, al comenzar la *k-esima* iteración, con $k=1,2,3,\dots,n$. $D[i,j]$ es el largo más corto desde $i\to j$ que pasa solo por los puntos intermedios de numeración $<K$, en otras palabras, que no pase por puntos intermedios.  


### Ejemplo 

Un ejemplo del resultado de este algoritmo sería el siguiente: 

![[Captura de pantalla 2023-07-18 a la(s) 22.44.52.png|center|350]]


Este algoritmo tomaría como input la siguiente matriz: 

$$A^0=\begin{bmatrix}
 & \mathbf{1} & \mathbf{2} & \mathbf{3} & \mathbf{4} \\
\mathbf{1} & 0 & 3 & \infty & 7 \\
\mathbf{2} & 8 & 0 & 2 & \infty \\
\mathbf{3} & 5 & \infty & 0 & 1 \\
\mathbf{4} & 2 & \infty & \infty & 0
\end{bmatrix}$$

Que sería, basicamente, la matriz con todos los pesos de cada arco. 

Ahora, para resolver para $A^1$, es decir, el vértice $1$, primero nos paramos en aquel vértice, dejando intactas las filas y columnas pertenecientes a $A^1$. 

$$A^1=\begin{bmatrix}
 & \mathbf{1} & \mathbf{2} & \mathbf{3} & \mathbf{4} \\
\mathbf{1} & 0 & 3 & \infty & 7 \\
\mathbf{2} & 8 & 0 & \dots & \dots \\
\mathbf{3} & 5 & \dots & 0 & \dots \\
\mathbf{4} & 2 & \dots & \dots & 0
\end{bmatrix}$$


Entonces, para llenar la matriz restante, revisamos la matriz original. Por ejemplo, queremos llenar la coordenada $(2,3)$, que representaría el camino $2\to 3$, entonces se realiza la siguiente operación: 

$$A^0[2,3]=2$$

Pero, como estamos parados en el primer nodo, entonces se hace la comparación al pasar por el nodo uno dado que es el intermedio (acordar del [[Invariante|invariante]]): 

$$A^0[2,1]+A^0[1,3]=8+\infty$$

Claramente el primero es más chico, entonces se queda en $2$. 

$$A^1=\begin{bmatrix}
 & \mathbf{1} & \mathbf{2} & \mathbf{3} & \mathbf{4} \\
\mathbf{1} & 0 & 3 & \infty & 7 \\
\mathbf{2} & 8 & 0 & 2 & \dots \\
\mathbf{3} & 5 & \dots & 0 & \dots \\
\mathbf{4} & 2 & \dots & \dots & 0
\end{bmatrix}$$

La otra iteración sería comparar para $(2,4)$, donde claramente se puede apreciar que $A^0[2,4]=\infty$ y $A^0[2,1]+A^0[1,4]$ es $8+7$, entonces existe un camino indirecto que pasa por el vértice $1$ donde se puede lograr la conexión $2\to4$. 

Luego, al llenar la matriz, se llega a lo siguiente (Esta vez se va a omitir la numeración de filas y columnas): 

$$A^1=\begin{bmatrix}
0 & 3 & \infty & 7 \\
8 & 0 & 2 & 15 \\
5 & 8 & 0 & 1 \\
2 & 5 & \infty & 0
\end{bmatrix}$$

Ahora, se hace lo mismo pero para el vértice $2$ y tomando como base la matriz $1$, es como un método de memoización 