Daniel Hermosilla, Sebastián Jana 
# Pregunta 1 

Para esta pregunta, se asumira $n=1.000.000$, vale decir, la cantidad total de tuplas que hay. 
## Caso A: Encontrar todas las tuplas de $R$ 

- Análisis de $R$ sin ningún indice: 
Dado que no existe índice alguno, se consultan la cantidad de tuplas existentes. 

$$\lceil\frac{n}{B}\rceil$$

- Usando un $B+$ Tree *unclustered* sobre el atributo $a$. 
En este tipo de árboles, dado que no hay una "memoría" de que bloque se visitó dado un puntero desordenado, podría ser que se visiten más bloques de lo necesario. En el peor caso se debe pasar por todos los punteros, acceder a todos los bloques de memoria y además hacer el recorrido entero del árbol. 

$$h+\lceil\frac{n}{P}\rceil+n$$

- Usar un $B+$ Tree clustered sobre el atributo $a$ con páginas llenas a un $60\%$. 
Dado que con $10$ bloques se harían $6$ bloques llenos, la relación sería $5/3$. Por lo tanto: 

$$\frac{5}{3}n\lceil\frac{n}{B}\rceil$$

- Usar un *Hash Index unclustered*. Cada página del índice contiene $P$ punteros ($P>B$)
Con un Hash no es posible hacer un escaneo dado que se desconoce la función o cómo interactua. 

- Usar un *Hash Index clustered* 
Mismo argumento anterior 

## Caso B: Encontrar todas las tuplas de $R$ tal que $a<50$

- Análisis de $R$ sin ningún índice: 
Habría que hacer un paso por **todos** los valores, tal que se pueda discriminar si $a<50$ o no. 

$$n$$
- Usar un $B+$ Tree unclustered sobre el atributo $a$ con páginas llenas a un $60\%$. 
En este caso, se tiene algo análogo al argumento anterior. Sin embargo, al tener "punteros desordenados", hay que recorrer bloques que pudieron haber sido recorridos anteriormente, siendo menos eficiente que el método anterior. 

$$h+\lceil\frac{n}{P}\rceil+n$$

- Usar un $B+$ Tree clustered sobre el atributo $a$ con páginas llenas a un $60\%$. 
El gran fuerte y naturaleza de los árboles $B+$ son que están ordenados. Por lo tanto, bastaría únicamente recorrer la altura y obtener todos los bloques posteriores al recorrido de ésta: 

$$h + \frac{5}{3}\left(\lceil\frac{n}{B}\rceil-\lceil\frac{50}{B}\rceil\right)$$

Donde $n/B - 50/B$ son la cantidad de bloques posteriores al recorrido del árbol, vale decir, la cantidad de bloques mayor a $a=50$


- Usar un *Hash Index unclustered*. Cada página del índice contiene $P$ punteros ($P>B$)
Bajo el mismo argumento que se utilizo para el inciso anterior, en una estructura *Hash* se desconoce la función, por ende, no se sabe cómo están ordenados los datos. No se podría obtener el cálculo de un rango por esto mismo. 

- Usar un *Hash Index clustered* 
Mismo argumento anterior 

## Caso C: Encontrar todas las tuplas de $R$ tal que $a = 50$

- Análisis de $R$ sin ningún índice: 
Asumiendo que los datos están distribuidos bajo una distribución uniforme, la esperanza de encontrar un dato en específico sin indexación sería la mitad de los número de bloques por sala, vale decir: 

$$\frac{1}{2}\lceil\frac{\lceil n\rceil}{B}\rceil$$

- Usando un $B+$ Tree *unclustered* sobre el atributo $a$. 
Bastaría recorrer la altura, que está ordenada y un recorrido extra que toma el puntero al bloque desordenado. 

$$h+1$$

- Usar un $B+$ Tree clustered sobre el atributo $a$ con páginas llenas a un $60\%$. 
Dado que los datos están ordenados, bastaría únicamente recorrer la altura del árbol. Aquí da lo mismo los "espacios libres" que se dejan entre bloques.  

$$h$$

- Usar un *Hash Index unclustered*. Cada página del índice contiene $P$ punteros ($P>B$)
La gracia del Hash Index es que tiene acceso instantáneo. Si consideramos que hay que extraer el dato **y** visualizarlo, serían $2$ operaciones. Aun así, seguiría siendo $O(1)$

$$2$$

- Usar un *Hash Index clustered*: Mismo argumento anterior, se tiene acceso directo a los datos. 

$$2$$

<div style="page-break-after: always;"></div>

# Pregunta 2 

## Descripción de los índices 

Al observar los índices que se demuestran en los esquemas `opt` y `opti`, se muestra que el esquema `opti` tiene más índices para cada tabla, en comparación con el esquema `opt`, donde el único índice presente es la respectiva llave primaria. Lo anterior se puede explicar ya que al no especificar un índice, Postgres por defecto lo asigna a la llave primaria, es por esto que en algunos casos el atributo puede aparecer 2 veces en los índices, como el caso de la tabla "actor10000" en el esquema `opti`.

Evidenciando lo anterior, se tienen los siguientes índices para cada tabla (nota: pkk significa que el atributo es llave primaria):

```SQL
"pelicula10000":
Opt: (nombre, anho) pk
Opti: (nombre, anho) pk, calificacion, nombre, votos

"actor10000":
Opt: nombre pk
Opti: nombre pk, genero, nombre

"personaje10000":
Opt: (a_nombre, p_nombre, p_anho, personaje) pk
Opti: (a_nombre, p_nombre, p_anho, personaje) pk, a_nombre, p_anho, p_nombre, (p_nombre, p_anho)
```

Cabe mencionar que todos los índices utilizan el método de b-trees y un método de acceso Heap, que ocupa colas de prioridad. 


## Planificación de consultas 

Se utilizó la siguiente consulta para analizar la tabla (sólo se mostrarán aquellas para cuales terminan en $100$):

```SQL 
\d+ opt.actor100   
```

Asi, se tiene la siguiente planificación para la consulta no anidada y anidada para el esquema `opt`: 

```SQL 
- NO ANIDADO 
EXPLAIN ANALYZE SELECT DISTINCT p2.p_nombre, p2.p_anho  
FROM opt.personaje100 AS p1  
JOIN opt.personaje100 AS p2  
ON p1.p_nombre = 'Shrek 2'  
WHERE p1.a_nombre = p2.a_nombre  
AND NOT p2.p_nombre = 'Shrek 2';

- ANIDADO 
EXPLAIN ANALYZE SELECT DISTINCT p1.p_nombre, p1.p_anho  
FROM opt.personaje100 AS p1  
WHERE p1.a_nombre IN  
    (SELECT p2.a_nombre    
    FROM opt.personaje100 AS p2    
    WHERE p2.p_nombre = 'Shrek 2')
AND NOT p1.p_nombre ='Shrek 2';

```

Y la siguiente consulta para el esquema `opti`: 

```SQL 
- NO ANIDADO 
EXPLAIN ANALYZE SELECT DISTINCT p2.p_nombre, p2.p_anho  
FROM opti.personaje100 AS p1  
JOIN opti.personaje100 AS p2  
ON p1.p_nombre = 'Shrek 2'  
WHERE p1.a_nombre = p2.a_nombre  
AND NOT p2.p_nombre = 'Shrek 2';

- ANIDADO
EXPLAIN ANALYZE SELECT DISTINCT p1.p_nombre, p1.p_anho  
FROM opti.personaje100 AS p1  
WHERE p1.a_nombre IN  
    (SELECT p2.a_nombre    
    FROM opti.personaje100 AS p2    
    WHERE p2.p_nombre = 'Shrek 2')
AND NOT p1.p_nombre ='Shrek 2';
```
<div style="page-break-after: always;"></div>

## Gráfico 

Dado todos los datos recopilados, se armó el siguiente gráfico 

![[con anidar.png|center]]

![[sin anidar.png|center]]

