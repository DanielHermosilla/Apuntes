
# Índices 

Existen dos formas principales de accesso a los datos: 


- A través del disco duro 
- A través de la memoria principal (RAM)

La gran diferencia entre ambos es que la memoria principal es de **acceso casi instantáneo**, por el otro lado, el disco duro es *más barato*, persistente y tiene mayor capacidad. La latencia del disco duro se debe principalmente a su estructura física: tiene un brazo mecánico que tiene que moverse para cambiar el bloque. 

>*“La diferencia de tiempo entre tener un dato en RAM versus traerlo de disco es comparable a la de tomar el sacapuntas del escritorio donde estoy sentado versus tomarme un avión a la China para ir a buscarlo y regresar.*

## Modelos de costos 

Dada la instanteniedad de la memoria RAM, los análisis se hacen principalmente en la memoria secundaria donde la lectura se hace por **bloques**. Cada bloque tiene un tamaño $B$ de tuplas. Así, se llegan a los primeros modelos donde la $M$ es la capacidad de la memoria y $n$ el número total de tuplas: 

- Costo de leer **$n$ tuplas desde la memoria secundaria: 

$$\lceil\frac{n}{B}\rceil$$ 
- Cuantos bloques **caben en la memoria** 

$$\lfloor\frac{M}{B}\rfloor$$

- Cuantos bloques **usa una relación $R$** 

$$\lceil\frac{\vert R\vert}{B}\rceil$$ 

## Tipos de busqueda 

SQL al ser un lenguaje **declarativo** no se sabe con total certeza lo que se está ejecutando a través de la “*caja negra*”. Así, se definen los distintos tipos de busqueda con una breve descripción. 

### Búsqueda secuencial 

Como dice su nombre, es literalmente una búsqueda secuencial por cada tupla de cada bloque 

![[Pasted image 20231130220457.png|center]]

- Se leen $\vert R\vert$ tuplas 
- En términos de bloques cuesta $\lceil\frac{\vert R\vert}{B}\rceil$ 

Esta búsqueda es muy ineficiente, sólo vale la pena en conjuntos de datos muy chicos. 

La formá más efectiva es al ocupar **índices**. 

### Índice Hash 

Es una función matemática que toma un valor de *"input"* y dar una identificación a los bloques teniendo un acceso casi instantáneo. 

Así, el costo de busqueda llegaría a dividirse por: 

- **Caso ideal** $O(1)$
- **Peor caso**: $O(\lceil\frac{\vert R\vert}{B}\rceil)$
- **Caso ideal para devolver $k$ tuplas**: $O(\lceil\frac{k}{B}\rceil)$

No obstante, este costo son para **búsquedas donde se sabe el valor exacto de la llave**. Vale decir, una busqueda del siguiente estilo: 

```SQL 
SELECT *
FROM Planeta 
WHERE nombre = 'Venus' 
```

Las busquedas por rango es donde tienen un peor rendimiento. 

### Índice Árbol B 

Los árboles $B$ son básicamente árboles ordenados y balanceados, que a diferencia del binario, se tienen $B$ hijos. Las hojas guardan **todas las llaves y sus valores**. 

El costo de búsqueda depende de la profundidad del árbol. Pero por lo general tiene un costo de $O(\log_b(\lceil\frac{\vert R\vert}{B}\rceil))$

![[Pasted image 20231130222800.png|center]]

Este árbol es **mucho** más eficiente que el índice hash para búsquedas en rango. No obstante, es un poco menos eficiente en búsquedas por rango. 

## Creación de índices 

Por lo general para crear un índice en SQL se hacen en las llaves primarias de las tablas. No obstante, se recomienda hacer en aquellos valores más utilizados: 

```SQL 
CREATE INDEX nombre ON tabla (atr1,atr2) -- por defecto es btree 
CREATE INDEX nombre ON tabla USING hash (atr1, atr2)
```

## Índices agrupados 

Se dice que un índice es *clustered* o agrupado cuando el orden de las tuplas en la memoria secundaria coincide con el orden de las tuplas en el índice. Por ejemplo, sea la siguiente relación: 

$$\text{Empleados(\textbf{id}, nombre, edad)}$$

Un índice agrupado se aplicaría en la llave primaria, como lo sería el **id** en este caso. Un desagrupado lo aplicaria sobre el atribubto edad para ordenar más rápido. 

![[Pasted image 20231130223317.png|center|700]]

De tal manera, se llega a la siguiente tabla de **costos de acceso**: 

![[Pasted image 20231130223445.png|center|700]]

Con: 

- $B_R=\lceil\frac{\vert R\vert}{B}\rceil$ número de bloques de la tabla. 
- $B_m$ = $n\degree$ de bloques con regs que calzan búsqueda 
- $b=$ números de hijos máximo de un nodo de un $B$-tree 


Notar que el valor $1.5$ de los árboles $B+$ agrupado salen de hacer la relación de tuplas/espacio libre dentro del bloque. 

## Planificación 

En `SQL` para poder ver la planificación de una tabla se ejecutan los siguientes comandos: 

```SQL 
EXPLAIN SELECT ... -- Muestra la planificación sin ejecutar consulta 

ANALYZE SELECT ... -- Ejecuta la consulta y muestra el análisis 

EXPLAIN ANALYZE SELECT -- Combina ambos 
```

Un ejemplo de esta consulta sería la siguiente: 

![[Pasted image 20231130223809.png|center]]

# Evaluación de consultas 

Una consulta en `SQL` puede variar ligeramente por la semántica, índices, etc. Todo esto es lo que determina la interacción entre la base de datos, el buffer (memoria RAM) y el disco duro. 

## Costos de un join 

Existen cuatro tipos principales de algoritmos para hacer un join en `SQL`: 

- Loop anidado 
- Index Nested Loop Join 
- Hash Join 
- Sort-Merge Join 

### Loop anidado (sin índices)

Este es el método más simple, donde se compara cada fila de la primera tabla con cada fila de la segunda tabla. Es eficaz para pequeñas tablas, pero su rendimiento puede degradarse significativamente con tablas más grandes. 

![[Pasted image 20231130224652.png|center]]

El costo es de $\lceil\frac{\vert R\vert}{B}\rceil+\vert R\vert\cdot\lceil\frac{\vert S\vert}{B}\rceil$. 

La decisión de elegir hacer el join entre $R\bowtie S$ depende de la cardinalidad. Por lo general, se elige $R$ si se cumple que $\vert R\vert <\vert S\vert$. 

### Loop anidado (con índices)

La diferencia cambia sustancialmente al poder hacer una búsqueda para la relación $S$. 

![[Pasted image 20231130224614.png|center]]

Así, el costo de búsqueda llegaría a ser $\lceil\frac{\vert R\vert}{B}\rceil+\vert R\vert\cdot\beta(S)$. Donde $\beta(S)$ es el costo de buscar $S$. Notemos que es muy parecido al anterior pero ahora al tener $S$ con índices $\beta$ llegaría a ser una búsqueda optimizada. 

Nuevamente se elige el orden del join en base a $\vert R\vert <\vert S\vert$

### Hash join 

Ambas tablas se dividen en bloques llamados "buckets" basados en un valor hash común. Luego, se compara cada bucket de una tabla con los buckets correspondientes de la otra tabla. Este método es eficiente para grandes conjuntos de datos.

![[Pasted image 20231130224934.png|center]]

El costo llegaría a ser $\lceil\frac{\vert R\vert}{B}\rceil+\lceil\frac{\vert S\vert}{B}\rceil$. 

Para elegir el orden del join se hace el análisis de $\vert S\vert <\vert R\vert$ para ahorrar memoria. 

### Sort-merge-join 

Ambas tablas se ordenan según la clave de unión y luego se realiza un escaneo conjunto. Este método es eficiente cuando ambas tablas ya están ordenadas o pueden ordenarse de manera eficiente.

![[Pasted image 20231130225138.png|center]]

Si hacemos un recordatorio del merge sort, este algoritmo consiste en el lema de *dividir y conquistar.*  Es decir, se van a ir realizando [[Listas|sublistas]] dentro del *[[Listas|array]]* principal para luego poder comparar, reordenar y juntar cada resultado. Esto se va logrando con recursividad. 

Se generan dos funciones; una que va dividiendo la lista recursivamente y otra que va uniendo las listas en orden.

![Merge Sort Algorithm - 101 Computing](https://www.101computing.net/wp/wp-content/uploads/Merge-Sort-Algorithm.png)

El costo llegaría a ser $\text{Ord}+\lceil\frac{\vert R\vert}{B}\rceil+\lceil\frac{\vert S\vert}{B}\rceil$. Donde $\text{Ord}$ es el costo de ordenar. En este caso el orden de elección del join no importa. 

## Comparación 

![[Pasted image 20231130225428.png|center]]

## Estadísticas y catálogos 

Normalmente cuando se requiere información sobre las tablas e índices para la consulta. El catálogo contendrá al menos: 

- Cantidad de tuplas y páginas para cada tabla. 
- Cantidad de valores distintos de valores y páginas 
- Valor de los valores máximos, mínimos. 

Los catálogos se actualizan periódicamente. 

# Transacciones 

Es una unidad lógica de procesamiento de una base de datos conformada por una secuencia de operaciones de acceso a los datos.  

Las transacciones parten por el principal problema de un acceso generalizado a una misma base de datos. Por lo general existen choques, pérdida de consistencia, etc. 

`SQL`ofrece un sistema de transacciones que funciona a través de la siguiente sintaxis: 

```SQL 
START TRANSACTION -- Empieza la transacción 
COMMIT -- Termina la transacción 
ROLLBACK -- En caso de error, deshace/borra los cambios hasta el inicio de la transacción 
```
Así también se definen las **cuatro operaciones principales de una transacción**: 

- $R(X)$: Lectura del elemento $X$ 

- $W(X)$: Escritura del elemento $X$ 

- $C$: Confirmación/compromiso 

- $A$: Aborto/Rollback 

## Conflictos 

En las transacciones existen varios tipos de conflictos. Los más comunes llegarían a ser: 

- **Actualización pérdida (conflicto WW)**: Una transacción sobreescribe los datos que otra transacción ya había escrito. 

![[Pasted image 20231130230325.png|center]]

- **Lectura sucia (conflicto WR)**: Una transacción lee lo que otra transacción escribió pero no se había confirmado aun. 

![[Pasted image 20231130230337.png|center]]

- **Lectura no repetible (conflicto RW)**: Una transacción sobreescirbe un dato que otra ya había leído antes pero no había confirmado.  

![[Pasted image 20231130230401.png|center]]

## Garantias ACID 

Consisten en las garantias principales para que una base de datos opere de una forma segura: 

- **Atomicidad**: La ejecución de cada transacción es atómica: Se realizan todas sus acciones o no se realiza ninguna. 

- **Consistencia**: Cada transacción debe preservar la integridad. La base de datos satisface todas las restricciones después de una transacción. 

- **Aislamiento (Isolation)**: Una transacción no puede afectar otra. Cada usuario debe sentir que es el único que está accesando la base de datos. 

- **Durabilidad**: Una vez que haya un `COMMIT` los cambios deben permanecer en la base de datos. 

Esto se implementa principalmente a través de una bitácora (libro de registros) y bloqueos. 

## Recuperabilidad 

Se dice que un plan $P$ es recuperable si ninguna transacción $T$ de $P$ se confirma antes de que se hayan confirmado todas las transacciones $T'$ que han escrito un elemento que $T$ lee posteriormente. 

![[Pasted image 20231130230749.png|center]]

Acá, si $T_1$ falla se dificulta la recuperación. Lo anterior es un ejemplo de un plan no recuperable. 

![[Pasted image 20231130230822.png|center]]

Este es un plan recuperable ya que $T_2$ tiene que esperar que $T_1$ haga commit. **Si $T_1$ falla $T_2$ también fallará en cascada**. 

# Privacidad 

Se basa en técnicas para asegurar que no se pueda vincular información delicada con la identidad de individuos. 

![[Pasted image 20231130231204.png|center]]

## Convenciones básicas 

Se tienen las cuatro categorias disjuntas 

![[Pasted image 20231130231229.png|center]]

## De-identificación 

Es el método más fácil de implementar. Simplemente se censuran nombres. Esto se puede solucionar fácilmente con una re-identificación haciendo un join con otra tabla o consultas agregadas. 

## K-anonimato 

Sea $T(A_1,\dots, A_n)$ una tabla y $Q$ los cuasi-identificadores. Se dice que $T$ satisface *k-anonimato* si y sólo si cada grupo de cuasiidentificador $Q_i\in Q$ aparece al menos $k$ veces en $T$: 

Vale decir, el menor valor de la siguiente consulta: 

```SQL 
SELECT CIds, COUNT(*) FROM T 
GROUP BY CIds; 
```

Por lo general esto se soluciona generalizando: clasificando a personas por grupos (como rangos de edad). Con eliminar datos no se hace referencia a literal la **eliminación** de datos, si no una generalización (como truncar por ejemplo a una categoria de tercera edad a los valores mayores que $60$). 

## L-diversidad 

Una tabla $T$ es $l$-diversa si para cada grupo de filas con los mismos $Clds$, por cada atributo sensible $S$, existen al meons $l$ valores distintos. Básicamente es como un *k-anonimato* pero con los datos sensibles. 

```SQL 
SELECT CIds, COUNT(DISTINCT S)
FROM T GROUP BY CIds; 
```

## Privacidad diferencial 

Básicamente garantizar un mecanismo tal que sea imposible hacer ataques de agregación independiente de posibles datos auxiliares. Se hace mediante adición de ruido mediante el mecanismo de Laplace: 

$$F(x)=f(x)+\text{Lap}(\frac{s}{\epsilon})$$

Con $s$ siendo la sensibilidad y $\epsilon$ el presupuesto de privacidad. Por lo general, $\epsilon$ es un dato público cuando se publican datos. 

- Si $F_1(x)$ satisface $\epsilon_1$-privacidad diferencial 
- Si $F_2(x)$ satisface $\epsilon_2$-privacidad diferencial 
- Entonces el mecanismo $G(x)=(F_1(x),F_2(x))$ que libera ambos resultados satisface $(\epsilon_1+\epsilon_2)$-privacidad diferencial. 