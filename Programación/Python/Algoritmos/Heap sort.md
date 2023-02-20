Realiza un ordenamiento en el lugar, ordenando solo un número constante de elementos fuera de la [[Listas|lista]] de entrada e introduce una técnica del diseñó de algoritmos donde se emplean estructuras de datos para manejar información durante la ejecución del algoritmo.

Este modelo se puede representar bajo un arbol binario:

![[heapsort.png|center]]


Por lo tanto, se intenta ordenar una [[Listas|lista]] al dividir los elementos en un arbol binario. Un video que lo explica bien es el [siguiente](https://www.youtube.com/watch?v=28KxhS8P2Bg&ab_channel=IVANANDRESGUAPACHABARRERO). Por lo tanto se van creando hijos a través de una raiz principal que lo representa el primer elemento indexado.  

La idea es que **cada nodo padre debe ser mayor que los nodos hijos**. Por eso mismo, si no se cumple la condición los elementos se deberían permutar. 

Entonces, se realiza el siguiente procedimiento para poder ordenar el arbol cumpliendo las condiciones: 

```Python 

# Recibe la lista (l), el indice (i) y el tamaño (valor 
# entero asociado al nodo) del arbol binario. 


def maxHeapify(l, i, tamano):
	izq = 2 * i + 1
	der = 2 * i + 2

	if izq < tamano and l[izq] > l[i]:
		maximo = izq
	else: 
		maximo = i

	if der < tamano and l[der] > l[maximo]:
		maximo = der 

	if maximo is not i: # Generación de un subarbol 
		temp = l[i]
		l[i] = l[maximo]
		l[maximo] = temp
		maxHeapify(1, maximo, tamano)

```

La idea del algoritmo es que al ir permutando todos los elementos entre sí se va a llegar a un punto donde la raiz sea el mayor elemento. Por lo tanto, se guarda ese elemento en la **nueva lista ordenada** y se vuelve a realizar el procedimiento por recursión. La recursión partiría con el último elemento en el arbol, de derecha a izquierda. 

Para construir el heap (arbol binario ordenado) se considera la siguiente función: 

```Python

def construyeHeap(l):
	heapTamano = len(l)
	for i in range(int(len(l)/2), -1, -1):
		maxHeapify(l, i, heapTamano)

```

Por último, el algoritmo completo sería el siguiente: 

```jupyter

def maxHeapify(l, i, tamano):
	izq = 2 * i + 1
	der = 2 * i + 2

	if izq < tamano and l[izq] > l[i]:
		maximo = izq
	else: 
		maximo = i

	if der < tamano and l[der] > l[maximo]:
		maximo = der 

	if maximo is not i: # Generación de un subarbol 
		temp = l[i]
		l[i] = l[maximo]
		l[maximo] = temp
		maxHeapify(1, maximo, tamano)


def construyeHeap(l):
	heapTamano = len(l)
	for i in range(int(len(l)/2), -1, -1):
		maxHeapify(l, i, heapTamano)

def heapSort(l):
	construyeHeap(l)
	heapTamano = len(l)
	for i in range(len(l), 0, -1):
		temp = l[0]
		l[0] = l[i]
		l[i] = temp
		heapTamano -= 1
		maxHeapify(l, 1, heapTamano)

# Prueba 

l = [3,5,2,1]
heapSort(l)

```
