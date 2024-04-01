
Existen distintos tipos de datos dentro de Apache Pig: 

- **Pig Relations**: Análogo a las tablas relacionales, son tuplas que pueden ser incompletas. 

- **Pig Schema**: Nombre para los campos 

- **Pig Fields:** Se puede referenciar ocupando variables. También es posible hacer referencias de la siguiente forma: 

```pig 
premium = FILTER raw BY price >= 1000 
```

