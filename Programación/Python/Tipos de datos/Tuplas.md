Las tuplas son tipos de datos inmutables, es decir, no pueden ser alteradas al ser creadas. La única forma es reescribirlas al redefinir otra tupla con el mismo nombre. Las siguientes son todas formas válidas para definir una tupla: 

```jupyter

t = tuple([1,2])
t = 1,2
t = (1,2)

```

Al igual que en la listas o [[Strings|strings]], para poder acceder a una tupla se ocupa la misma sintaxis: 

```jupyter

t = 5,10
t[0]

```

Entre los **métodos** que se encuentran dentro de las tuplas existen dos principales: 

- Count: recibe como parámetro un valor y retorna la cantidad de veces que el vallor se halla en la tupla. 

```jupyter

t = 1 , 2, "Andrés", [1,5,7], 1, "Roberto"
t.count(1) # Retornará las veces que se encuentra el entero 1

```

- Index: recibe un valor y retornará el primer índice donde se encuentra el elemento. 

```jupyter
t = 1 , 2, "Andrés", [1,5,7], 1, "Roberto"
t.index([1,5,7]) # Retornará el lugar donde se encuentra la lista [1,5,7]

```

- In: para verificar la existencia de un elemento en 