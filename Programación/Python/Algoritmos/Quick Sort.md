El algoritmo quick sort consiste en ocupar pivotes dentro de las [[Listas|listas]] e ir dividiendo los elementos en distintos [[Listas|arrays]] según su tamaño. 

### Quick Sort no optimizado 

El algoritmo Quick Sort no optimizado ocuparía una variable única en el [[Bucles|bucle]] que va recorriendo la lista del pivote. Esto reduciría su rendimiento al recorrer la [[Listas|lista]] únicamente de izquierda a derecha. 

```jupyter 

# Algoritmo QuickSort no optimizado 

def QuickSort(array):

	largo = len(array)
	
	if largo == 0:
	
		return []
	
	pivote = array.pop()
	
	menores = list()
	
	mayores = list()
	
	for i in range(largo-1):
	
		if array[i] < pivote:
		
			menores.append(array[i])
		
		else:
		
			mayores.append(array[i])
	
	return QuickSort(menores) + [pivote] + QuickSort(mayores)

# TEST 

array = [55,66,22,33,99,88,11,44]

print(QuickSort(array))

```

