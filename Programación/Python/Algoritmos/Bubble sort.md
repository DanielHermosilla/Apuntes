O también conocido como *ordenamiento burbuja* consiste en un algoritmo que funciona intercambiando pares de elementos adyacentes previamente desordenados. La invariante del algoritmo es que despues de la *i-esima* iteración, el *i-esimo* elemento queda en la posición correcta en la lista ordenada. En este escenario i puede tomar valores de $0,1,2,\dots,n$. 

![[Bubblesort.svg|center]]

Por lo tanto, se realiza un recorrido desde la última posición hasta la primera, intercambiando pares de elementos adyacentes si el elemento de la derecha es menor. Entonces, el código podría ser el siguiente: 

```jupyter 

def b
