O también conocido como *ordenamiento burbuja* consiste en un algoritmo que funciona intercambiando pares de elementos adyacentes previamente desordenados. La invariante del algoritmo es que despues de la *i-esima* iteración, el *i-esimo* elemento queda en la posición correcta en la [[Listas|lista]] ordenada. En este escenario i puede tomar valores de $0,1,2,\dots,n$. 

![[Bubblesort.svg|center]]

Por lo tanto, se realiza un recorrido desde la última posición hasta la primera, intercambiando pares de elementos adyacentes si el elemento de la derecha es menor. Entonces, el código podría ser el siguiente: 

```python 

def bubblesort(l):
	for i in range(len(l)):
		j = len(l) - 1
		while j >= i:
			if l[j] < l[j-1]: # Si el número posterior es menor
				temp = l[j] 
				l[j] = l[j-1] # Cambiar de posición al mayor
				l[j-1] = temp # Cambiar de posición al menor
			j -= 1

```


Si bien este algoritmo llega a ser sencillo, es poco eficiente ya que carece de utilidad práctica. 