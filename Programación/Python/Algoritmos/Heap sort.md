Realiza un ordenamiento en el lugar, ordenando solo un número constante de elementos fuera de la [[Listas|lista]] de entrada e introduce una técnica del diseñó de algoritmos donde se emplean estructuras de datos para manejar información durante la ejecución del algoritmo.

Este modelo se puede representar bajo un arbol binario:

![[heapsort.png|center]]


Por lo tanto, se intenta ordenar una [[Listas|lista]] al dividir los elementos en un arbol binario. Un video que lo explica bien es el [siguiente](https://www.youtube.com/watch?v=28KxhS8P2Bg&ab_channel=IVANANDRESGUAPACHABARRERO). Por lo tanto se van creando hijos a través de una raiz principal que lo representa el primer elemento indexado.  

La idea es que **cada nodo padre debe ser mayor que los nodos hijos**. Por eso mismo, si no se cumple la condición los elementos se deberían permutar. 

La idea del algoritmo es que al ir permutando todos los elementos entre sí se va a llegar a un punto donde la raiz sea el mayor elemento. Por lo tanto, se guarda ese elemento en la **nueva lista ordenada** y se vuelve a realizar el procedimiento por recursión. La recursión partiría con el último elemento en el arbol, de derecha a izquierda. 

Otra forma alternativa sería ocupando [[Bucles|bucles]], ya que al trabajar con [[Listas|listas]] muy grandes se podría llegar a un error de recursión máxima. 

Por lo tanto el algoritmo sería el siguiente:

```jupyter
  

# Va a ir intercambiando los elementos del arbol

def swap(lst, i , j):

	lst[i], lst[j] = lst[j], lst[i]

# Sacar el elemento raiz

def siftDown(lst, i, upper):

	while (True):

		l, r = i*2+1, i*2+2
		
		if max(l, r) < upper:
		
			if lst[i] >= max(lst[l], lst[r]):
			
				break
			
			elif lst[l] > lst[r]:
			
				swap(lst, i, l)
				i = l
			
			else:
				swap(lst, i, r)
		
		elif l < upper:
		
			if lst[l] > lst[i]:
			
				swap(lst, i, l)
				i = l
			
			else:
				break
		
		elif r < upper:
	
			if lst[r] > lst[i]:
			
				swap(lst, i, r)
				i = r
			
			else:
				break
		
		else:
			break

# Función principal

def heapsort(lst):

	for j in range(len(lst)-2//2, -1, -1):
	
		siftDown(lst, j , len(lst))

	for end in range(len(lst)-1, 0, -1):
	
		swap(lst, 0, end)
		siftDown(lst, 0, end)

# Test

lst = [5, 16, 18, 20, 43, 90, 21, 6, 1, 32, 24, 6, 7]

heapsort(lst)
print(lst)

```
