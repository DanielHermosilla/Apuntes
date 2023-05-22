Es posible *rotar*  un arbol de [[Busqueda binaria|busqueda binaria]] de tal forma que un padre pueda intercambiar con su hijo. Se llega a una especie de *balancín*: 

![[Arbol rotación.png|center|]]

Su implementación es la siguiente: 

```python

class Nodoi:

	def __init__(self, izq, info, der):
	
		self.izq=izq
		
		self.info=info
		
		self.der=der

	def right_rotation(self):
	
		return(Nodoi(self.izq.izq,

			self.izq.info,

			Nodoi(self.izq.der,self.info,self.der)))

	def left_rotation(self):

		return(Nodoi(Nodoi(self.izq,self.info,self.der.izq),

		self.der.info,

		self.der.der))

	def root_insert(self,x):
	
		assert x!=self.info

		if x<self.info:

			self.izq=self.izq.root_insert(x) # x queda como raíz del hijo izquierdo

			return self.right_rotation() # la rotación deja a x como raíz

		else:

			self.der=self.der.root_insert(x) # x queda como raíz del hijo derecho

			return self.left_rotation() # la rotación deja a x como raíz

	def __str__(self):

		return "("+self.izq.__str__()+str(self.info)+self.der.__str__()+")"
		
		  

class Nodoe:

	def __init__(self):

		pass

	def root_insert(self,x):

		return Nodoi(Nodoe(),x,Nodoe())

	def __str__(self):

		return"☐"

  

class Arbol:

	def __init__(self,raiz=Nodoe()):
	
		self.raiz=raiz

	def root_insert(self,x):

		self.raiz=self.raiz.root_insert(x)

	def __str__(self):

		return self.raiz.__str__()

	def dibujar(self):

	btd = aed.BinaryTreeDrawer(fieldData="info", fieldLeft="izq", fieldRight="der", classNone=Nodoe, drawNull=True)
	
	btd.draw_tree(self, "raiz")
```

Esto puede servir para implementar un **nuevo método de inserción en los árboles**. A partir de esto se introduce la inserción en la raiz, donde el elemento que entra **debe estar en la raiz**. 

Una forma de hacerlo es insertar el nodo directamente por un nodo externo. De tal forma, se hace una rotación con el padre y así sucesivamente hasta llegar a la raíz. 
