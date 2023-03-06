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
                   for friend in user["friends"]  # Por cada uno de mis amigos
                   for foaf in friend["friends"]  # Contar a cada amigo
                   if not_the_same(user, foaf)    # Que no sean "yo"
                   and not_friends(user, foaf))   # Y que no sean mis amigos


# Se compila una lista de intereses de cada usuario 

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

# Función de gente con intereses similares 

def data_scientist_who_like(target_interest): 
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

from collections import defaultdict

# Se van a ocupar las llaves para añadir el interes y los valores para poner los 
# ids de los usuarios con ese interés 

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests: 
    user_ids_by_interest[interest].append(user_id)

# Se crea otro diccionario que funciona al inverso; del usuario al interés
interests_by_user_id = defaultdict(list)

for user_id, interests in interests:
    interests_by_user_id[user_id].append(interest)

# Por lo tanto, se podría ver quien tiene mas interés en común con otro usuario bajo 
# una simple función 

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])

