Consiste el primer ejemplo del primer capítulo. Es el primer dia trabajando en la red social *DataSciencester*  y nos dan los datos de los usuarios de tal red: 

```Python 

users = [
		{"id":0, "name": "Hero"},
		{ "id": 1, "name": "Dunn" },
	    { "id": 2, "name": "Sue" },
	    { "id": 3, "name": "Chi" },
	    { "id": 4, "name": "Thor" },
	    { "id": 5, "name": "Clive" },
	    { "id": 6, "name": "Hicks" },
	    { "id": 7, "name": "Devin" },
	    { "id": 8, "name": "Kate" },
	    { "id": 9, "name": "Klein" }

]
```


También nos dan los datos de los amigos que se han formado en la red social como una [[Listas|lista]] de [[Tuplas|tuplas]], donde, por ejemplo, la [[Tuplas|tupla]] (0,1) indica una amistad del id "0" con el id "1". 

```Python 


“friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

```


Esto se ilustra bajo la siguiente figura: 

![[FindingKeyConnectors.png|center]]

Con esto podriamos hacer una [[Listas|lista]] de amigos para cada usuario.  Entonces, asignamos una lista vacia de amigos para empezar. 

```Python 

for user in users:
	user["friends"] = []

```

Y de ahi, ocupando el método *append* se añaden los usuarios a la lista. 

```Python 

for i,j in friendships: 
	# Esto funciona porque users[i] es el usuario con id "i"

	users[i]["friends"].append(users[j]) 
	# Añadir "i" como amigo de "j"

	users[j]["friends"].append(users[i]) 
	# Añadir "j" como amigo de "i"
```

Ya que cada [[Diccionarios|diccionario]] de usuarios contiene una lista de amigos, se puede preguntar *¿Cual es el promedio de conexiones?*. 

Primero, obtenemos la cantidad total de conexiones al sumar el largo de cada [[Listas|array]]: 

```Python 

def numeroDeAmigos(user):
	"""¿Cuantos amigos tiene el usuario?"""

	return len(user["friends "])

conexionesTotales = sum(numeroDeAmigos(user) 
						for user in users)
```

Y luego basta con [[Operadores numéricos|dividir]] con la cantidad total de usuarios

```Python 

numeroUsuarios = len(users)

promedioConexiones = conexionesTotales / numeroUsuarios 

```

También es posible encontrar las personas más conectadas, que serían las personas que tienen la mayor cantidad de amigos.  Como son pocos los usuarios, se pueden ordenar de más amigos a menos amigos (nota; en este caso se podrían ocupar los algoritmos de ordenamiento, como [[Heap sort]], [[Counting sort]], [[Quick Sort]], por nombrar algunos). 

```Python 

# Creamos una lista de tuplas (id de usuario, numero de amigos)

numeroAmigosPorId = [(users["id"],numeroDeAmigos(user))
					for user in users] 

# Ordenamos la lista, en este caso se ocupa el método nativo de Python de sortear listas

sorted(numeroAmigosPorId, key=lambda (idUsuario, numeroAmigos): numeroAmigos, numeroAmigos, reverse = True) # Esto solo funciona en Python 2, revisar el código Introduccion.py

```

Una forma de visualizar lo que se realizó es identificar a las personas que son centrales a la red. De hecho, esto se llama *degree centrality*. 

![[degreeCentrality.png|center]]

Esto tiene la virtud de ser fácil de calcular, aunque no da los resultados que se esperarían. Por ejemplo, podríamos apreciar que el usuario "1" tiene 3 conexiones, mientras el usuario "4" tiene solamente dos. Por ende, debería dar la impresión de que Dunn (usuario 1) esté mas centralizado. 