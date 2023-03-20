
Son aquellas [[Condicionales|condiciones]] que se mantienen constantes en un [[Bucles|bucle]] o recursión. Cuando se cumple esta [[Condicionales|condición]] es donde el [[Bucles|bucle]] se rompe.  El invariante **debe tener algún término**, de no ser así, se haría un [[Bucles|bucle]] infinito. 

### Ejemplo 

En el caso de una función que calcule la potencia: 

```Python 

def potencia(x, n):

	y=1
	k=n
	z=x

	while k>0:

		y*=z
		k-=1

	return y
```

El invariante llegaría a ser $y=x^k$ donde se rompe el bucle cuando $n=k$. 