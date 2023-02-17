
En Python las funciones pueden tener $n$ argumentos, con $n\in [0,+\infty]$. Estos pueden ser **obligatorios** o **predefinidos**. 

Los argumentos se presentan como una lista de valores separados por comas, por ende, poseen la siguiente sintaxis: 

```Python

def f(arg1, ... , argn): 
	Sentencias

```

### Funciones con valores opcionales 

Las funciones que no requieren una cantidad fija de argumentos se declaran como pares llave-valor, es decir: 

```Python

def f(a, b = 2):
	return a + b 

```

En este caso, la función va a tener predefinidamente el valor "b" asociado al valor [[Enteros|entero]] 2. Por lo tanto, se podría llamar a la función con solo un argumento: 

```jupyter

def f(a, b = 2):
	return a + b 

print(f(5))

```

Ahora, si se quisiera modificar el valor "b" se podría realizar al llamar la variable dentro de la función: 

```jupyter

def f(a, b = 2):
	return a + b 

print(f(5,b=0))

```

Por otra parte, se podría indicar que una función reciba una cantidad no definida de argumentos mediante el argumento ****args** 

```Python

def f(*args):
	Sentencias 

```

Un ejemplo claro sería una función que calcule la suma ponderada de un conjunto de elementos: 

```jupyter

def sumaPonderada(*args):
	result = 0
	for i in args: 
		result += i[0] * i[1] 

	return result 

print(sumaPonderada((1,2),(3,4),(5,6)))

```

También es posible ocupar argumentos de tipo *****args*** , que serán [[Diccionarios|diccionarios]] conteniendo argumentos definidos como llave-valor. La principal diferencia con el anterior es que el segundo recibe valores ligados a una variable: 

```jupyter 

def obtenerCasas(**casas):
	for c in casas: 
		s = int(c.split("_")[1])
		if int(c.split("_")[1]) > 0:
				print(casas)