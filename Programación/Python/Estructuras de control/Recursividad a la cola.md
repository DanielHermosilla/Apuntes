
Aprovechando el [[Bucles|bucle]] *while*, se podría implementar optimizaciones en recursiones al ir implementando un contador que va decreciendo: 

```Python
def Hanoi(n, a, b, c): # Mover n discos desde "a" a "c", usando "b" como auxiliar

	if n>0:

		Hanoi(n-1, a, c, b)

		print(a, "-->", c) # Mueve 1 disco desde "a" hasta "c"

		Hanoi(n-1, b, a, c)
```

Esto se podría optimizar al hacer lo siguiente: 

```Python 
def Hanoi(n, a, b, c): # Mover n discos desde "a" a "c", usando "b" como auxiliar

	while n>0: # reemplaza a "if n>0:"

		Hanoi(n-1, a, c, b)

		print(a, "-->", c) # Mueve 1 disco desde "a" hasta "c"

		n-=1

		(a,b)=(b,a) # reemplaza a "Hanoi(n-1, b, a, c)"
```


