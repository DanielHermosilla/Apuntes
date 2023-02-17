
En Python existen dos tipos de bucles; el *for*  y *while*: 

### While 

El bucle *while* requiere una sentencia [[Condicionales|condicional]]. Lo que nos dice es que el bloque de código se va a ejecutar mientras la sentencia sea **verdadera**. 

#### Ejemplo 

```jupyter 

a = 0
while a < 5: 
	print("a")
	a += 2 

print("El bucle se ejecuta tres veces al cumplir la condición 3 veces") 

```


### For 

El bucle *for*  requiere una estructura iterable. Es decir, va a ir recorriendo ordenadamente cierta variable. 

####  Ejemplo 

```jupyter 

a = [5, 10, 15]
b = 0

for i in a: 
	b += i

print(b)

```

En un caso hipotético se podría poner una sentencia [[Condicionales|condicional]] dentro del bucle que termine la iteración cuando se cumpla. Esto se realiza con la palabra *break*. 