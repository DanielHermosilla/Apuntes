
Esto se ocupa para ordenar arrays. Se toma un array y se van insertando de izquierda a derecha de forma ordenada. Es una ordenación *in situ* o *in place*, ya que se puede hacer ocupando el mismo array. 

El [[Invariantes|invariante]] se puede visualizar como: 

![[Seleccion.png|center]]

El iterativo es tomar el primer elemento de los desordenados e insertarlos en la lista de ordenados. Para garantizar que esté ordenado se hace la comparación sucesivamente desde *k* hasta *0*. 

```Python 

def insertar(a, k):

	j=k # señala la posición del elemento que está siendo insertado

	while j>0 and a[j]<a[j-1]:

		(a[j], a[j-1]) = (a[j-1], a[j])

	j-=1

def ordena_insercion(a):

	n=len(a)

	for k in range(0,n):

		insertar(a,k)

```

Es decir, toma el mayor número y lo pone al final, despues toma el segundo mayor y lo pone después del final y así sucesivamente.

El orden de este algoritmo es $O(n^2)$ 