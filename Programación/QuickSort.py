
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

def swap(lst, i , j):
    lst[i], lst[j] = lst[j], lst[i]
    

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
                pass
            
		    else:
				i += 1
				swap(array, i, j)
			 
		 array.insert(pivote, i + 1)
		menores = array[0:i]
		mayores = array[i+2:]
		break

    return QuickSort(menores) + [pivote] + QuickSort(mayores)

print(QuickSort2(array))