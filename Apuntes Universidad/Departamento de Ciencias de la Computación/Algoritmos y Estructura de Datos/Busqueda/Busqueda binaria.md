Este algoritmo se ocupa para bases de datos grandes y es extremadamente eficiente. Como ejemplo, se podría encontrar un elemento en un [[Listas|arreglo]] de 1000000 elementos en un máximo de 20 comparaciones.  Aun así, el array **debe estar ordenado**. 

El algoritmo se basa en la idea de asumir una [[Listas|lista]] ordenada. En caso de estar ordenada se divide la lista en la mitad y compararlo con el elemento buscado. Si la comparación resulta falsa, se sigue la busqueda con una recursión. Esta técnica emplea una técnica llamada *backtracking*. 

```python 

def busquedaBinaria(lista, elemento):

	try:
		inicio = lista[0]
		fin = lista[len(lista) - 1]
		centro = len(lista)//2
	
		if elemento < lista[centro]: 
			return busquedaBinaria(lista[0:centro], elemento)
	
		elif elemento > lista[centro]: 
			return busquedaBinaria(lista[centro:fin], elemento)
	
		else: 
			return "El elemento \"{}\" se encuentra en la lista".format(elemento)

	except: 
		return "El elemento \"{}\" no se encuentra en la lista".format(elemento)

# Test 

lista = [1,5,8,10,15,70,80,400,467,697,700,893,10000] 

busquedaBinaria(lista,893)


```

