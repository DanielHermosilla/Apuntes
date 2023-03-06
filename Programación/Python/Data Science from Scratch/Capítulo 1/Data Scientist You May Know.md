
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



