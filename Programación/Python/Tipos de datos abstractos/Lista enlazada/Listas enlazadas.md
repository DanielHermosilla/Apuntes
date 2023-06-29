
Normalmente existen dos formas de guardar datos en la memoria, una siendo los arrays, y otra siendo las listas enlazadas. Estas últimas se crearon ante algunas limitaciones que ofrecian los arrays. A pesar de todo, existen varios tipos de listas enlazadas: 

- Lista simple: La navegación es solamente hacia adelante. 

![[Pasted image 20230628195718.png|center|400]]

- Lista doblemente enlazada: Está permitida la navegación hacia atrás y adelante

- Lista circular: El último elemento esta enlazado con el primero

Normalmente las listas enlazadas están compuestas por **nodos**, compuesto por dos partes, **la información** y **el énlace**: 

```python  

class Nodo: 
	def __init__(self,info, sgte=None):
		self.info = info 
		self.sgte = sgte 

```

Ahora, para poder acceder a la lista se define el *head*, vale decir, el primer elemento de la lista. El *head* es un puntero que tiene la dirección a la lista. 

![[Pasted image 20230628200157.png|center]]


