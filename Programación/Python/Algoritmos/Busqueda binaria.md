Este algoritmo se ocupa para bases de datos grandes y es extremadamente eficiente. Como ejemplo, se podría encontrar un elemento en un [[Listas|arreglo]] de 1000000 elementos en un máximo de 20 comparaciones. 

El algoritmo se basa en la idea de asumir una [[Listas|lista]] ordenada. En caso de estar ordenada se divide la lista en la mitad y compararlo con el elemento buscado. Si la comparación resulta falsa, se sigue la busqueda con una recursión. Esta técnica emplea una técnica llamada *backtracking*. 

```jupyter 

def busquedaBinaria(lista, elemento):
	inicio = lista[0]
	fin = lista[len(lista)]
	centro = (fin - inicio)//2 + inicio 

	if elemento < centro: 
		return busquedaBinaria(lista[0:centro], elemento)

	elif elemento > centro: 
		return busquedaBinaria(lista[centro:fin], elemento)

	else: 
		return elemento[inicio] is x
	