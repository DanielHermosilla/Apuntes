Es un [[Librerias|modulo]] nativo de Python que permite poder trabajar con [[Bucles|bucles]] e iteradores de una forma legible y expresible. 

## Funciones 

### Iteradores infinitos 

- *Count* : Retorna un iterador infinito que comienza en *n*  y tiene paso *step*. Su sintaxis es count(n = 0, step = 1). 

```Python 

import itertools 

for i in itertools.count(1,2):
	print(i)

"""
Consola: 

1
2
3
4
5
"""
```

- *Cycle:* Retorna un iterador que itera infinitamente por el iterable suministrado como parámetro. 

```Python 

import itertools 

for i in itertools.cycle([1,2]):
	print(i)
	

"""
Consola: 

1
2
1
2
1
"""
```

### Iteradores de filtro 

Entre los iteradores de filtro se encuentran: 

- *Dropwhile:* Retorna un iterador que desecha todos los elementos del iterable hasta que se cumple el [[Condicionales|predicad0]]. Su sintaxis es dropwhile(predicado, iterable).

```jupyter

import itertools 

for i in itertools.dropwhile(lambda x: x<=2, [1,2,3,4]):
	print(i)

```

- *Filterfalse:* Retorna un iterador que itera por aquellos elementos para los cuales el predicado devuelve el valor [[Condicionales|False]].  Su sintaxis es filterfalse(predicado, iterable)

```jupyter 

import itertools 

for i in itertools.filterfalse(lambda x: x<=2, [11,2,3,-1]):
	print(i)

```

En resumidas cuentas, son funciones que actuan como [[Bucles|bucles]] que van filtrando según las condiciones [[Condicionales|booleanas]] de los argumentos. 

### Combinatorial 

Otros usos que tienen son implementaciones combinatoriales como permutaciones, combinaciones, combinaciones sin repetición, etc. 

- *Product*: Equivalente a variaciones con repetición, recibe como [[Argumento de funciones|argumento]] una [[Listas|lista]]. 

- *Permutations*: Equivale a permutaciones, también recibe como [[Argumento de funciones|argumento]] un [[Listas|array]]. 

- *Combinations*: Lo mismo para combinaciones, con el mismo tipo de [[Argumento de funciones|argumento]] que las anteriores. 

- *Combinations_with_replacement*: Son combinaciones con repetición, que reciben una lista. 