


def mergeSort(array):

	if len(array) > 1:
		izquierda = array[:len(array)//2]
		derecha = array[len(array)//2:]

		# Recursión 
		mergeSort(izquierda)
		mergeSort(derecha)
	
		# Merge 
	
		i = 0 # Elementos de la izquierda del array izquierdo
		j = 0 # Elementos de la izquierda del array derecho
		k = 0 # índice del k-esimo array unido
		
		while i < len(izquierda) and j < len(derecha):
		
			if izquierda[i] < derecha[j]:
				array[k] = izquierda[i]
				i += 1
	 
			else: 
	
				array[k] = derecha[j]
				j += 1
				
			k += 1
	
		while i < len(izquierda):
			array[k] = izquierda[i]
			i += 1
			k += 1 
	
		while j < len(derecha):
			array[k] = derecha[j]
			j += 1
			k += 1
			
lista = [4,5,2,34,3,6,2,4,2,1,4,5,1,3,56,93,1,2,4,6,1,2,33,501,21433,213,2,1]

mergeSort(lista)
print(lista)