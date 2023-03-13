Se considera entre la estructura de datos fundamentales de Python. Dada a su gran flexibilidad permite poder acoplarse sin inconvenientes a un sin fín de problemas. Es decir, son **modificables**.  

### Creación de una lista 

- Lista vacia: Al igual que los [[Diccionarios|diccionarios]], la listas pueden ser vacias al llamarlas por su función o sintaxis del lenguaje: 

```jupyter 

l = list()
l = []

```

- Lista no vacia: Se definen mediantes paréntesis cuadrados y separando elementos mediante comas. No es recomendable llamarlo por su función. Más adelante se discutirá de una forma alternativa de crear listas bajo un módulo externo llamado *numpy*. 

```jupyter

l = [1,5,"Daniel",10]

```

Es posible concatenar listas a partir del operador suma como también ocupando la multiplicación, es decir, posee una especie única de [[Operadores numéricos|operador numérico]]: 

```jupyter

# Concatenación por suma 

l = [1,5,"Daniel",10]
l += [8]
print(l)

# Concatenación por multiplicación 

lista = [5,6] * 3
print(lista)

```

Las listas también poseen funciones predefinidas donde destacan la función *min*, *max*  y *len*. 

Para finalizar es importante notar que las listas se indexan al igual que los [[Strings|strings]] o [[Tuplas|tuplas]] 