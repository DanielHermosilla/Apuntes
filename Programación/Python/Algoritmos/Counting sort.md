Counting sort u ordenamiento por conteo es un algoritmo que ordena una [[Listas|lista]] de elementos en tiempo computacional lineal. Determina para cada elemento el número de elementos menores a este, luego utiliza esa información para ubicar directamente el elemento en su posición en la [[Listas|lista]] ordenada.  Para hacer este algoritmo se supone que lose elementos están comprendidos en un rango $\lbrace a_0,\dots,a_n\rbrace$ para algun [[Enteros|entero]] $k$. 

```jupyter

def countingSort(lista, k):
	result = [0] * (len(l))
	c = [0] * (k+1)
	numero_elementos_iguales_i(l,c)
	numero_elementos_menores_i(c)
	for i in range(len(l)-1,-1,-1):
		c[l[i]] -= 1
		result[c[l[i]]] = l[i]

	return result 

def numero_elementos_iguales_i (l,c):
	for i in range(len(l)):
		c[l[i]] += 1

def numero_elemento_menores_i(c):
	