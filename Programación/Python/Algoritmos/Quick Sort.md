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

### Quicksort optimizado 

En este algoritmo de quicksort se ocupara un [[Bucles|bucle]] doble. La idea queda expresada bajo el siguiente [video](https://www.youtube.com/watch?v=MZaf_9IZCrc&ab_channel=KCAng)

```jupyter 

# Función que cambia de lugar elementos de la lista 

def swap(lst, i , j):

	lst[i], lst[j] = lst[j], lst[i]
	
# Algoritmo QuickSort optimizado 

def QuickSort(array):

	largo = len(array)
	
	if largo == 0:
	
		return []
	
	pivote = array.pop()
	
	menores = list()
	
	mayores = list()
	
	for i in range(-1, largo-1, 1):
	
		for j in range(largo-1):
		
			if array[j] > pivote:
				pass

			else:
				i += 1
				swap(array, i, j)
			 
		array.insert(i+1, pivote)
		menores = array[0:i]
		mayores = array[i+2:]
		break

	print(menores)
	print(mayores)
	print(pivote)
	return QuickSort(menores) + [pivote] + QuickSort(mayores)

# TEST 

array = [55,66,22,33,99,88,11,44]

print(QuickSort(array))

```