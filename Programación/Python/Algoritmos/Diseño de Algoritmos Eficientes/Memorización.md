
Cuando se tienen algoritmos recursivos, algunas veces se calcula el mismo valor varias veces a pesar de sólo necesitarlo una vez. Un claro ejemplo es el algoritmo de Fibonacci. Por lo tanto, se ocupa la técnica de *memorización* donde se calculan únicamente los datos que aparecen por primera vez. 

### Ejemplo 

```python 

import numpy as np

def fibonacci(n):

	F=np.zeros(n+1,dtype=int)

		def fib_rec(k):

			if k>0 and F[k]==0: # primera vez que se calcula

				if k<=1:

					F[k]=k

				else:

					F[k]=fib_rec(k-1)+fib_rec(k-2)

			return F[k]

return fib_rec(n)

```

