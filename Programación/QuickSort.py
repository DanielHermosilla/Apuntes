
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

print(QuickSort(array))


    