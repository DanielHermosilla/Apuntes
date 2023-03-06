
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

```

A partir de esto se podría ver que Thor no tiene amigos en común con Devin pero si tienen el mismo interes por *machine learning*. 

Por lo tanto, se podría construir una función que encuentre a usuarios con cierto interes.

```Python 

def data_scientist_who_like(target_interest):

	return [user_id
			for user_id, user_interest in interests
			if user_interest == target_interest]
```

Este código funciona pero tiene que examinar toda la lista de intereses por cada busqueda, lo que es poco óptimo (aquí se podrían aplicar algoritmos de busquedas, como la [[Busqueda binaria|busqueda binaria]]). El libro opta por construir índices de los intereses de los usuarios. 

```Python 

from collections import defaultdict 

# Las llaves son los intereses, los valores son listas de los id's de usuarios con ese interés 

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
	user_ids_by_interest[interest].append(user_id)

# Se puede realizar lo mismo pero al revéz 

interests_by_user_id = defaultdict(list)

for user_id, interests in interests:
	interests_by_user_id[user_id].append(interest)
	
```

De tal forma, se tiene un [[Diccionarios|diccionario]] que va a contener a todos los usuarios con cierto interes. Mucho más facil y cómodo que ir preguntando cada vez en una [[Listas|lista]].  

Por último, se puede integrar una función para poder encontrar a gente con intereses comunes: 

```Python 

def most_common_interests_with(user):

	return Counter(interested_user_id
	
			for interest in interests_by_user_id[user["id"]]
			
			for interested_user_id in user_ids_by_interest[interest]
			
			if interested_user_id != user["id"])

```

