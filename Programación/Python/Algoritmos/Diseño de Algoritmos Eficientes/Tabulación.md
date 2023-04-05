
Al igual que en [[Memorización|memorización]], se va llenando un arreglo, cosa que cuando se necesite un valor en cierto casillero, éste ya está lleno. 

## Ejemplo 

```python 

import numpy as np

def fibonacci(n):

	F=np.zeros(n+1,dtype=int)

	F[0]=0

	F[1]=1

	for k in range(2,n+1):

		F[k]=F[k-1]+F[k-2]

return F[n]
```
