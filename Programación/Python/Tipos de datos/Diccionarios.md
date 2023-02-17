
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

dicc[Edad] 
dicc[Carrera]