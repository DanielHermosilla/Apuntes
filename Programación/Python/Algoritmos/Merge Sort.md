Este algoritmo consiste en el lema de *dividir y conquistar.*  Es decir, se van a ir realizando [[Listas|sublistas]] dentro del *[[Listas|array]]* principal para luego poder comparar, reordenar y juntar cada resultado. Esto se va logrando con recursividad. 

Se generan dos funciones; una que va dividiendo la lista recursivamente y otra que va uniendo las listas en orden.

![Merge Sort Algorithm - 101 Computing](https://www.101computing.net/wp/wp-content/uploads/Merge-Sort-Algorithm.png)

```jupyter 

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


# Prueba 

lista = [11,22,55,77,22,33,99,77,88,22,44,55,400,300]
mergeSort(lista)
print(lista)

```

