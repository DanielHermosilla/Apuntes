
# Pregunta 1 (3 puntos)

### Función diasMes (1.0) puntos: 

- Receta de diseño $(0.2)$: (Contrato+objetivo$(0.1)$, ejemplo+prueba$(0.1)$)

- Crea un algoritmo para verificar si el año es bisiesto $(0.2)$ (Notar que es posible hacerlo mediante funciones, condicionales o importanto el módulo visto en clases). 

- `assert(diasMes(1,2000) == 31)` $(0.3)$ 

- `assert(diasMes(2,120) == 29)` $(0.3)$


###  Función esFecha (1.0) puntos: 

- Receta de diseño $(0.2)$: (Contrato+objetivo$(0.1)$, ejemplo+prueba$(0.1)$)

- `assert(esFecha(29,2,120) == True)` $(0.4)$ 

- `assert(esFecha(28,3,2027) == True)` $(0.4)$ 

### Programa (1.0) puntos

- $(0.3)$ puntos:
```python 
Fecha 1? 10010330
Fecha 2? 10020430
Fecha mayor: 10020430 
```

- $(0.4)$ puntos: El diálogo **debe** detenerse al ser una fecha incorrecta 

```python 
Fecha 1? 20010229
Fecha incorrecta 
```

- $(0.3)$ puntos: 

```python 
Fecha 1? 20240326
Fecha 2? 20250229
Fecha incorrecta 
```

# Pregunta 2 (3 puntos)

### Función producto (1.5) puntos: 

- Receta de diseño $(0.2)$: (Contrato+objetivo$(0.1)$, ejemplo+prueba$(0.1)$)

- `assert(producto(8,8)==64)` $(0.8)$ 

- `assert(producto(9,0)==0)` $(0.5)$

- Descontar $(0.5)$ si no ocupa recursividad

### Función factorial (1.5) puntos: 

- Receta de diseño $(0.2)$: (Contrato+objetivo$(0.1)$, ejemplo+prueba$(0.1)$)

- `assert(factorial(10)==3628800)` $(0.8)$

- `assert(factorial(0)==1)` $(0.5)$ 

- Descontar $(0.5)$ si no ocupa recursividad 

- Descontar $(0.4)$ si no ocupa la función producto. 