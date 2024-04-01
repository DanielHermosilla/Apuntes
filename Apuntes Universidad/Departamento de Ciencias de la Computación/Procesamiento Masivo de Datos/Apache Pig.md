
Existen distintos tipos de datos dentro de Apache Pig: 

- **Pig Relations**: Análogo a las tablas relacionales, son tuplas que pueden ser incompletas. 

- **Pig Schema**: Nombre para los campos 

- **Pig Fields:** Se puede referenciar ocupando variables. También es posible hacer referencias de la siguiente forma: 

```pig 
premium = FILTER raw BY price >= 1000 
```

Los distintos tipos son *ints, long, float, double, biginteger, bigdecimal, boolean, chararray (string), bytearray (blob), datetime*. Por lo general, si no se especifica el tipo de dato, el software lo llena por sí sólo. 

A diferencia de [[SQL]] ,se tienen tipos de datos que son únicos de pig. Por ejemplo, existen tuplas dentro de tuplas: 

```pig 
cat data; 
((3,8,9),(4,5,6))
((1,4,7)),(3,7,5))
((2,5,8)),(9,5,8))
```

Si se quiere generar una tabla a partir de aquello, se llegaría a lo siguiente:

![[Pasted image 20240401145623.png|center]] 

En las tuplas el orden si importa, sin embargo, existen los `bags` donde el orden no importa: 

```Pig 
cat data; 
(3,8,9)
(2,3,6)
(1,4,7)
(2,5,8)

A = LOAD 'data' AS (c1:int, c2:int, c3:int);
B = GROUP A BY c1;
DUMP B;
(1, {(1,4,7)})
(2, {(2,5,8),(2,3,6)})
(3,{(3,8,9)})
````

Esto retornaría la siguiente tabla: 

![[Pasted image 20240401145848.png|center]]

