
Luego de [[Finding Key Connectors|organizar]] la red social se pide incorporar una sugerencia de posible *Data scientists* que podrían conocerse. 

El primer instinto sería sugerir al usuario los amigos de los amigos. Que es fácil de computar: 

```Python 

def amigosDeAmigos(usuario):
	# "foaf" sería "friend of a friend" (amigo del amigo)
	return [foaf["id"]
			for friend in user["friends"]
			for foaf in friends["friends"]]


""" 

Si esto se llamaría en el usuario 0 (Hero) retornaría lo siguiente: 

[0, 2, 3, 0, 1, 3]

"""
```

Incluye al usuario "0" dos veces ya que Hero es amigo del amigo de cero dos veces. Otros ejemplos más serían: 

```Python 

print [friends["id"] for friend in users[0]["friends"]] # [1,2]

print [friends["id"] for friend in users[1]["friends"]] # [0,2]

print [friends["id"] for friend in users[2]["friends"]] # [0, 1, 3]

```

Saber quienes son amigos-de-amigos pareciera ser util, por lo tanto, se podrían contar la cantidad de amigos mutuos. En este caso se puede ocupar el módulo nativo [[Collections]] para poder tener un contador. 

```Python 

from collections import Counter 

def noElMismo(usuario, otroUsuario): 

	""" Dos usuarios no son el mismo si tienen distinto id """
	
	return usuario["id"] != otroUsuario["id"]

def noAmigos(usuario, otroUsuario): 

	""" otroUsuario no es amigo si no está en la lista de amigos del usuario (user["friends"]) """ 

	return all(noElMismo(amigo, otroUsuario)
			for amigo in user["friends"])

def amigoDelAmigoIds(usuario): 

	return Counter(foaf["id"]
					for amigo in user["friends"] # Por cada amigo 
					for foaf in amigo["friends"] # Contar "sus" amigos 
					if noElMismo(usuario, foaf) # Que no son ellos mismos 
					and noAmigos(user, foaf) # Y no son sus amigos directos 
print amigoDelAmigoIds(usuario[3]) # Counter({0:2, 5: 1})

```

Esto nos estaría diciendo que Chi tiene dos amigos mutuos con Hero y un amigo mutuo con Clive. 

También sería importante conocer usuarios con el mismo interés.  A partir de unas consultas se obtienen las siguientes tuplas: 

```Python 

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


