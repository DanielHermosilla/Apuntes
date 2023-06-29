
Una cola es una lista en que los elementos ingresan por un extremo y salen por el otro. Los elementos van saliendo en orden de llegada. 

![[Pasted image 20230628200732.png|center]]

Esto tiene utilizaciones en varios aspectos, uno de ellos en el área de [[Busqueda binaria|árboles binarios]]. 

Este tipo de dato posee dos operaciones básicas: 

- **Encolar**: Encola el elemento al final de la lista 
- **Desencolar**: Extrae y retorna el primer elemento a la cabeza de la cola. 

```python 

class Cola
	def __init__(self):
		self.q=[]

	def enq(self, x):
		self.q.insert(0,x)

	def deq(self):
		assert len(self.q)>0
		return self.q.pop()

```

Al operar usando los dos extramos, es sugerible que ésta opere mediante una [[Listas enlazadas|lista enlazada]] de doble enlace, vale decir, una lista con puntero al inicio y al final: 

![[Pasted image 20230628201157.png|center|600]]


Una utilización para las colas es para recorrer árboles binarios por niveles,  bajo la siguiente implementación: 

```python 

class Arbol: 
	def __init__(self, raiz=None):
		self.raiz=raiz

	def niveles(self):
		print("Recorrido por niveles:", end=" ")
		c = Cola()
		c.enq(self.raiz) # Mete primero la raiz
		while not c.is.empty():
			p=c.deq() # Saca el último elemento de la cola
			if p is not None:
				print(p.info, end=" ")
				c.enq(p.izq) # Mete al final el elemento izq
				c.enq(p.der) # Mete al final el elemento der
		print()

```

# Colas de Prioridad 

Muchas veces, cuando se tiene una cola, no se necesita ser atendido por orden de llegada, si no más bien por **prioridad**. Aquí básicamente se añade un dato adicional a los nodos de la lista, que son su prioridad. Por ende, las operaciones permitidas son: 

- **Insertar**: Inserta un elemento de prioridad en la cola. 
- **Extraer máximo**: Extrae y retorna el elemento de máxima prioridad de la cola de prioridad. 