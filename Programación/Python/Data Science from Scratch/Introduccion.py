""" 
Este código está basado en el caso basado en el primer capítulo del libro "Data Science from Scratch: 
First Principles with Python.

Los ejemplos gráficos y explicaciones se encuentran en los archivos Markdown adjuntos a la carpeta
  
"""

#  Lista de diccionarios que contiene a los usuarios de la red social 

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

# Lista de amigos de cada usuario, reflejado por tuplas con cada ID. 

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Creación de lista de amigos para cada usuario; partimos con una lista vacia
# y luego la vamos llenando 

for user in users: # Por cada elemento en la lista de usuario
    user["friends"] = [] # Se crea un atributo del usuario que serían sus listas de amigos 

for i,j in friendships: 
    users[i]["friends"].append(users[j]) # Agrega a "i" como amigo de "j"
    users[j]["friends"].append(users[i]) # Agrega a "j" como amigo de "i"


# Creación de función que nos dice la cantidad de amigos que tiene cada usuario

def number_of_friends(user):
    return len(user["friends"])

# A partir de aquello se puede saber la cantidad total de conexiones 

total_connections = sum(number_of_friends(user)
                        for user in users) # Por elemento en la lista de usuarios 

# Para saber la cantidad total de conexiones en la red social 

num_users = len(users)
avg_connections = total_connections / num_users

# Y ordenar una lista de más amigos a menos amigos 

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_id,
       key= lambda userid_numfriends: userid_numfriends[1],
       reverse=True)

""" 

"Data Scientist You May Know" 

"""

from collections import Counter 


# Buscamos la forma en sugerir a un usuario pueda conocer a otro al mostrar amigos de amigos 

def friends_of_friends_ids_bad(user):
    return [foaf["id"]
            for friend in user["friends"] # Por cada amigo de un usuario
            for foaf in friend["friends"]] # Obtener cada uno de los amigos de estos 


# Para contar los amigos mutuos implementamos una función que los va contando 
# Antes que nada implementamos una función que nos dice que no son un mismo usuario 
# o que no son amigos 

def not_the_same(user, other_user): 
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    return all(not_the_same(friend,other_user)
               for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]  # for each of my friends
                   for foaf in friend["friends"]  # count *their* friends
                   if not_the_same(user, foaf)    # who aren't me
                   and not_friends(user, foaf))   # and aren't my friends

userX = users[3]
print(friends_of_friend_ids(userX))

