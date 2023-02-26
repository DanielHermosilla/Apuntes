
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


array = [55,66,22,33,99,88,11,44]


# Función que cambia de lugar elementos de la lista 

def swap(lst, i , j):

	lst[i], lst[j] = lst[j], lst[i]
	
# Algoritmo QuickSort optimizado 

def QuickSort2(array):

	largo = len(array)
	
	if largo == 0:
	
		return []

	pivote = array.pop()
	
	menores = list()
	
	mayores = list()
	
	for i in range(-1, largo-1, 1):
	
		for j in range(largo-1):
		
			if array[j] > pivote:
				None

			else:
				i += 1
				swap(array, i, j)

		
		array.insert(i+1, pivote)
		menores = array[0:i+1]
		mayores = array[i+2:]
		break

	return QuickSort(menores) + [pivote] + QuickSort(mayores)

# TEST 

array = [55,66,22,33,99,88,11,44]

print(QuickSort(array))


print(QuickSort2(array))