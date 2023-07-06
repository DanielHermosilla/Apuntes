
Consisten en estructuras de datos que se utilizan para hacer eficiente los algoritmos, aprovechando que su operación de búsqueda es constante. Es muy analógico a los diccionarios comunes. 

La forma en buscar sus valores consiste en la siguiente sintaxis: *diccionario[llave] = valor*, es decir, adopta la estructura de una lista pero en vez de ocupar un índice ocupa una palabra. 

### Creación de diccionarios 

- Diccionario vacio: para crear un diccionario vacio se pueden ocupar las siguientes formas: 

```jupyter

dicc = {}
dicc = dict()

```

- Diccionario no vacio:  por el otro lado, para crear un diccionario no vacio se ocupan las llaves. Cabe destacar que éstas son única e inmutables, no así su valor asignado: 

```jupyter

dicc = {"Nombre": "Daniel", "Edad": 19, "Carrera": "Ingeniería"}

```

Como fue dicho anteriormente, para llamar el diccionario habría que llamarlo por su **llave**

```jupyter

dicc = {"Nombre": "Daniel", "Edad": 19, "Carrera": "Ingeniería "}

dicc["Carrera"]

```

Es posible eliminar todas las entradas de un diccionario ocupando la función *clear* como también eliminar una entrada particular ocupando la función *del*. 

Al igual que las [[Tuplas|tuplas]], también se puede ocupar el método *in* para comprobar si una llave pertenece al diccionario: 

```jupyter

dicc = {"Comida": "Arroz"}
"Comida" in dicc

```

Además se agrega la función *items* para conocer todos los pares en el diccionario: 

```jupyter

dicc = {"Color": "Verde", "Número": 10}
dicc.items()

```

Por último, se puede generar un ciclo *for* en los diccionarios: 

```jupyter

dicc = {"Nombre": "Gretica", "Edad": 27}

for d in dicc:
	print(d, dicc[d])

```

