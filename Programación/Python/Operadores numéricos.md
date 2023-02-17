
En Python existen las clásicas operaciones matemáticas que funcionan para cualquier tipo de dato. En este caso analizaremos el caso de los [[Enteros|enteros]] y [[Flotantes|flotantes]]: 

- Suma y multiplicación algebraica: Funcionan exactamente como funcionaría en la vida cotidiana 

```jupyter

print(3+4)
print(4*5)

```

- Divisiones: Se tienen dos operaciones de división; la primera, representada por el doble backslash ($//$ ) representa la división truncada al entero. Es decir, devuelve un numero de tipo [[Enteros|entero]]. Por el otro lado, la operación resto devuelve el resto de una división, representada con el porcentaje (%) 

```jupyter

print(5//2)
print(5%2)

```

- Potencia: También se puede ocupar el operador potencia al efectuar un doble asterísco ($**$). Del mismo modo se podría ocupar la función *pow*. 

```jupyter

5**2 == pow(5,2)

```

Existen varios operadores que se representarían con funciones implementadas del lenguaje. Dentro de estas destacan *abs*, *round* o *bin*.  