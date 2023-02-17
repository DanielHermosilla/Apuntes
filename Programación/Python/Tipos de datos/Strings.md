
En Python vamos a considerar a los *strings* o cadena como cualquier secuencia finita de símbolos tomados del alfabeto. Se representan bajo una **lista inmutable** en la sintaxis de *"str"*. 

Para poder declarar un string se pueden ocupar comillas dobles, simples o triples. Aún así, si se quisiera declarar las comillas de inicio dentro del texto se puede ocupar el "$/$" (backslash): 

```jupyter 

s1 = "Hola \"mundo\" !! "

print(s1)

```

También se pueden dividir líneas con los backslash:

```jupyter

s2 = "Hola " \
	"Python"

print(s2)
```


### Formato de cadenas 

Existe un método denominado *str.format* para poder generar oraciones de una forma más eficiente que consiste en el reemplazo de palabras por variables. 

#### Ejemplo 

```jupyter

s = "Son las {0} y es el momento de {1}".format("9:00 am", "desayunar")

print(s)

```


También se pueden hacer referencias a [[Listas|listas]] y los elementos de aquella: 

```jupyter

l = ["Mari", "playa", "hoy"]
s = "{0[0]} fue a la {0[1]} {0[2]}".format(l)
print(s)

```

Por el otro lado se podrían ocupar [[Diccionarios|diccionarios]] para la concanetación: 

```jupyter

dict = {"nba":"mj", "musica":"sting"}
s = "{0[nba]} y {0[musica]}".format(dict)
print(s)

```


Además es posible omitir los nombres de los campos, ya que Python los llenará por nosotros: 

```jupyter

s = "{} {} {}".format("Viva", "Python", "!!!")
print(s)

```

Por último, se pueden acceder a variables predefinidas anteriormente con la función *****locals. 

```jupyter

a = 10
b = 8 

s = "Yo tengo {a} manzanas y {b} peras".format(**locals())
print(s)

```
