
Python ofrece tres datos de tipo flotantes; el típico y estándar predefinido por la syntaxis *"float"* , el tipo complejo y el decimal de la librería estándar.  

El dato complejo es un dato inmutable que almacena un par de datos de tipo flotantes. En el caso de Python, se ocupa la *j* para representar la parte imaginaria: 

### Ejemplo datos complejos 

```jupyter 

comp1 = 1.7 + 3j
comp2 = 2.3 + 4.1j 

print(comp1 + comp2)

```


### Decimales 

Cuando se requiere mas precisión se ocupa la librería *"decimal"* que es nativa al lenguaje: 

```jupyter 

import decimal 
b = decimal.Decimal("12934.392021384")

print(b)

```

