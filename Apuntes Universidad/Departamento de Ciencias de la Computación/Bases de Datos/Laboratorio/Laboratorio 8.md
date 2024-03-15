Daniel Hermosilla, Sebastián Jana
## Pregunta 1

#### Inciso A

Se va a utilizar el siguiente formato para la consulta: 

```sql 
SELECT 
	COUNT(opt.pelicula100.nombre) as "Cantidad de tuplas en pelicula100"
FROM 
  opt.pelicula100;
```

```sql 
SELECT 
	COUNT(opt.pelicula1000.nombre) as "Cantidad de tuplas en pelicula1000"
FROM 
	opt.pelicula1000; 
```

```sql 
SELECT 
	COUNT(opt.pelicula10000.nombre) as "Cantidad de tuplas en pelicula10000"
FROM 
	opt.pelicula10000;
```

```sql 
SELECT 
	COUNT(opt.actor100.nombre) as "Cantidad de tuplas en actor100"
FROM 
	opt.actor100;
```

```sql 
SELECT 
	COUNT(opt.actor1000.nombre) as "Cantidad de tuplas en actor1000"
FROM 
	opt.actor1000;
```

```sql 
SELECT 
	COUNT(opt.actor10000.nombre) as "Cantidad de tuplas en actor10000"
FROM 
	opt.actor10000; 
```

```sql 
SELECT 
	COUNT(opt.personaje100.a_nombre) as "Cantidad en personaje100"
FROM 
	opt.personaje100; 
```

```sql 
SELECT 
	COUNT(opt.personaje1000.a_nombre) as "Cantidad en personaje1000"
FROM 
	opt.personaje1000; 
```

```sql 
SELECT
	COUNT(opt.personaje10000.a_nombre) as "Cantidad en personaje10000"
FROM 
	opt.personaje10000; 
```

Así, se llega a la siguiente tabla: 

|    **Relacion**   | **Cantidad de consultas** |
|:-----------------:|:-------------------------:|
|   **Pelicula100**  |           72696           |
|  **Pelicula1000**  |           22490           |
|  **Pelicula10000** |           6401            |
|    **Actor100**    |          856421           |
|    **Actor1000**   |          440234           |
|   **Actor10000**   |          197219           |
|  **Personaje100**  |          2170526          |
|  **Personaje1000** |          944964           |
| **Personaje10000** |          372367           |


Por el otro lado, para los bloques se tiene: 

```sql 
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'pelicula100';
```
```sql
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'pelicula1000';
```
```sql
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'pelicula10000';
```
```sql
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'actor100';
```
```sql
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'actor1000';
```
```sql
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'actor10000';
```
```SQL
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'personaje100';
```
```sql
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'personaje1000';
```
```sql
SELECT DISTINCT relname, relpages FROM pg_class WHERE relname = 'personaje10000';
```
Así, se llega a la siguiente tabla: 

|    ** Relacion**   | **Cantidad de consultas ** | **Cantidad de bloques** |
|:------------------:|:--------------------------:|:-----------------------:|
|   **Pelicula100**  |            72696           |           598           |
|  **Pelicula1000**  |            22490           |           183           |
|  **Pelicula10000** |            6401            |            52           |
|    **Actor100**    |           856421           |           5278          |
|    **Actor1000**   |           440234           |           2712          |
|   **Actor10000**   |           197219           |           1215          |
|  **Personaje100**  |           2170526          |          21410          |
|  **Personaje1000** |           944964           |           9330          |
| **Personaje10000** |           372367           |           3684          |

Por lo tanto, si queremos calcular la cantidad promedio de tuplas por bloque en tablas se hará el siguiente cálculo: 

$$\bar{X}(\text{Consulta})=\lceil\frac{\text{\# Consultas}}{\text{\# Bloques}}\rceil$$


|    ** Relacion**   | **Cantidad de consultas ** | **Cantidad de bloques** | **Cantidad promedio de tuplas por bloques** |
|:------------------:|:--------------------------:|:-----------------------:|:-------------------------------------------:|
|   **Pelicula100**  |            72696           |           598           |                     122                     |
|  **Pelicula1000**  |            22490           |           183           |                     123                     |
|  **Pelicula10000** |            6401            |            52           |                     124                     |
|    **Actor100**    |           856421           |           5278          |                     163                     |
|    **Actor1000**   |           440234           |           2712          |                     163                     |
|   **Actor10000**   |           197219           |           1215          |                     163                     |
|  **Personaje100**  |           2170526          |          21410          |                     102                     |
|  **Personaje1000** |           944964           |           9330          |                     102                     |
| **Personaje10000** |           372367           |           3684          |                     102                     |

#### Inciso B 

Para el esquema `opt` se tiene: 

```sql 
EXPLAIN ANALYZE SELECT * FROM opt.personaje100 
WHERE p_nombre='Up' AND p_anho=2009;
```

Así, se llega a la siguiente tabla 

|                             |      ** Parametros**     |
|:---------------------------:|:------------------------:|
|     **Plan de consulta**    | Parallel sequencial scan |
|   ** Tiempo de ejecucion**  |         277.933ms        |
| **Tiempo de planificacion** |          0.425ms         |
|       **Tiempo total**      |         278.358ms        |
|  **Consultas por segundo**  |           3.592          |


Por el otro lado, para el esquema `opti` se tiene: 

```sql 
EXPLAIN ANALYZE SELECT * FROM opti.personaje100 
WHERE p_nombre='Up' AND p_anho=2009;
```

Llegando a la siguiente tabla: 

|                             |              ** Parametros**              |
|:---------------------------:|:-----------------------------------------:|
|     **Plan de consulta**    | Index scan using personaje100_pnombreanho |
|   ** Tiempo de ejecucion**  |                  0.221ms                  |
| **Tiempo de planificacion** |                  0.741ms                  |
|       **Tiempo total**      |                  0.962ms                  |
|  **Consultas por segundo**  |                  1039.501                 |

#### Inciso C 

Para el esquema `opt` se tiene una búsqueda secuencial, de tal forma, se leen todos los bloques uno por uno. Por lo tanto, la cantidad de bloques leídos corresponde a todos los bloques de la relación que se ocupa. 

Por el otro lado, el esquema `opti` ocupa un Index Scan. Si nos vamos al catálogo del sistema es posible ver que se ocupa un arbol B+. Así, el costo promedio de busqueda llegaría a ser: 

$$O(h+\text{Cantidad de tuplas por bloque})$$

La cantidad de tuplas por bloque se debe que al ubicar el bloque con su índice hay que hacer una busqueda interna. Por lo general, $h$ casi siempre llega a ser igual a cuatro. Aun así , en el peor de los casos se tendría un $h=5$ para `personajes100` que corresponde a la relación con más datos. 

# Pregunta 2 

#### Inciso A
Dado que pueden existir muchas combinaciones de árboles de álgebra relacional se construyen dos bajo la premisa que se trata de un optimizador: 

![[IMG_0272117E1C34-1.jpeg|center|400]]

![[IMG_AFB6E20B279C-1.jpeg|center|450]]

La gracia de estos árboles es que se intenta filtrar lo máximo posible antes de hacer el join para poder reducir lo máximo posible el $O(n^2)$ que tiene los joins. Este argumento se va a profundizar en el último inciso. 

#### Inciso B 

Se tienen los siguientes datos preliminares: 

$$\begin{align}
n&=50000\tag{Empleados}\\ \\
n&=5000\tag{Departamentos}\\  \\
n&=5000\tag{Finanzas}
\end{align}$$

La cantidad de tuplas de las finanzas corresponde a la misma que el de departamentos dado que el enunciado nos dice que cada departamento tiene su información financiera correspondiente. Por simplicidad se va a asumir que esta información financiera es única entre ellas, ya que podría ser el caso que departamentos tengan los mismos datos financieros y apunten a la misma llave foránea. Aun así es extremadamente improbable ya que se tiene una distribución uniforme. 

Sabemos que los filtros anterior al join son los siguientes: 

$$\begin{align}
\text{D.piso}&=1\\  \\
\text{E.sueldo}&\geq 59000\\  \\
\text{E.hobby}&=\text{'magic'}
\end{align}$$

Primero, para el empleado, calcularemos la probabilidad de encontrar un sueldo mayor o igual a $59000$ y que tengan el hobby 'magic': 

$$\begin{align}
\mathbb{P}_\text{sueldo}&=\frac{1001}{50000}=0.02002\\  \\
\mathbb{P}_\text{hobby}&=\frac{1}{200}=0.005
\end{align}$$

Así, si asumimos independencia: 

$$\mathbb{P}_\text{filtro sueldo y hobby}=0.00202\cdot0.005=0.0001001$$

Así, se espera que los empleados que cumplan la condición sean: 

$$0.0001001\cdot50000=5.005\approx 5$$

Por el otro lado, para el filtro del departamento la probabilidad es $1/2$ dado que existen únicamente dos pisos. De tal forma, la cantidad de tuplas para la relación departamento llegarían a ser $2500$. 

Así, la cantidad de tuplas total estimada antes de hacer los joins llegarían a ser: 

$$n_\text{total}=2500+5+5000=7505$$

#### Inciso C

Dado que los atributos que se ocupan para el join (`did`) tienen un loop anidado con índices, el join llegaría a ser considerablemente menos costoso. La elección del orden del join depende de aquella relación cuyo número de tuplas sea menor. Así, se podría llegar a tener los siguientes árboles: 

![[IMG_016DFDCE7A15-1.jpeg|center|500]]

![[IMG_777BAE4D3F6A-1.jpeg|center|500]]

Claramente el último árbol es mucho más eficiente por las siguientes razones: 

1. **Filtros aplicados antes de los joins**: nótese que el árbol 2 filtra bastantes tuplas antes de realizar los joins. Lo anterior provoca que el join deba realizar muchas menos combinaciones de tuplas para las tablas que se desean unificar. Por ende, este método resulta ser mucho más eficiente que en el caso del 1er árbol, donde primero se realizan los joins, y luego se aplican los filtros, de modo que las combinaciones que realizan los joins son bastante más.

2. **Orden de los joins**: Anteriormente se llego que la cantidad de tuplas para cada relación antes de aplicar el join llegaría a ser: 

$$\begin{align}
\approx&\;5\tag{Empleados}\\  \\
\approx&\;2500\tag{Departamento}\\  \\
\approx&\;5000\tag{Finanzas}
\end{align}$$

Por definición del loop anidado con índices, la busqueda más óptima corresponde aquella que compara una tabla con la menor cantidad de tuplas con la de mayor cantidad de tuplas, vale decir, para un join $R\Join S$ lo más eficiente es que $\vert R\vert<\vert S\vert$. Así, el costo esperado llega a ser: 

$$\lceil\frac{\vert R\vert}{B}\rceil+\vert R\vert\cdot\beta(S)$$

Donde $\beta(S)$ es el costo de busqueda en $S$. Sabemos que las relaciones a las que se les hace el join están indexadas bajo un árbol $B+$ desordenado. De tal forma, $\beta(S)$ llegaría a ser: 

$$\beta(S)=\lceil\frac{\vert S\vert}{B}\rceil+h$$

Donde $h$ es la altura del árbol. Por lo general en los árbol $B+$ la altura no sobrepasa $h=4$. Con la cantidad de datos que se maneja, se esperaría que $h$ llegase a ser $2$. Aun así, no deja de ser una constante ínfima y despreciable. 

Al tener esto en cuenta y optimizar los joins con tal de asegurar tener el menor costo posible, se llega que el orden de unificación debe ser el siguiente: 

$$(\text{Empleados}\Join\text{Finanzas})\Join\text{Departamento}$$

Notemos que en el primer árbol esto no se cumple, mientras que el último si lo hace. 