
Por lo general cuando se tiene una consulta, existen dos procesos distintos. Por lo general, dado un tipo de consulta, se generan un índice para optimizar las consultas. 

**La optimización de consultas es una de las cosas más valiosas de las [[Bases de Datos|bases de datos]]**. Pero, para hacer tal cosa hay que saber como evaluar una consulta: 

- Análisis sintáctico: ¿Está bien escrita? 

Dado dos relaciones, reserves y sailors, lo siguiente sería un error sintáctico. 

```SQL 
SELECT sname 
FROM Reserves NATURAL JOIN Zailors 
WHERE bid = 100 AND rating > 5;
```

- Análisis semántico: ¿Qué sentido tiene? 

Se realiza un árbol de consulta, permite ordenar una manera de organizar el flujo de los datos. Se ocupa [[Lenguajes de Consulta|álgebra relacional]]. 

- ¿Qué posibilidades tenemos para ejecutarla? 
- ¿Cuál es la posibilidad más conveniente? (Más *barata*, *rápida*, etc)

Los costos de evaluación dependen del **compilador de la distribución**. En el caso de *PostgreSQL*, es de código abierto y es posible ver lo que hace el compilador.  Usualmente el join es el más relevente.  

Para los join existen cuatro tipos de evaluaciones; loop anidado, index nested loop join, hash join, sort-merge join. u

## Costos del Join 

#### Loop anidado 

Consiste en tomar una relación cualquiera, traerla a memoría y evaluar si cumple para cada tupla de la otra relación. 

Es decir; 

$$R\Join S$$

Para cada tupla $r\in R$, para cada tupla $s\in S$, si $r$ y $s$ satisfacen el join, entonces se escribe $\lbrace r\rbrace\times\lbrace s\rbrace$. El costo llega a ser: 

$$\lceil\frac{\vert R\vert}{B}\rceil +\lceil\frac{\vert R\vert}{B}\rceil\cdot\lceil\frac{\vert S\vert}{B}\rceil$$

En memoria se ocupa $2B$ tuplas. 

#### Loop anidado con índices 

Para cada tupla $r\in R$, se busca $s\in S$ en el índice tal que $r$ y $s$ satisfagan el join. El costo llega a ser: 

$$\lceil\frac{\vert R\vert}{B}\rceil +\vert R\vert\cdot\beta(S)$$

Donde $\beta(S)$ es el costo de buscar dentro del índice. Para los índices de [[Árboles ordinales|árbol B+]] normalmente es $\approx 4$. 

#### Hash join 

Guardar $S$ en memoria principal. Para cada tupla $r\in R$, busca $s$ en memoria principal tal que $r$ y $s$ satisfagan el join. 

#### Sort-merge-join 

Es el mejor sistema de los enumerados. 

Ordena $R$ y $S$ por los atributos del join. Aplicar [[Merge Sort|merge sort]] y para cada tupla $r$ y $s$ que satisfagan el join, escribe. El costo de esto es lo siguiente: 

$$\text{Ord}+\lceil\frac{\vert R\vert}{B}\rceil+\lceil\frac{\vert S\vert}{B}\rceil$$

No se ocupa [[Quick Sort|quick sort]] dado que el ordenamiento se hace en **memoria secundaria**, vale decir, memoria limitada. 