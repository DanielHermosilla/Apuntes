
## Álgebra Relacional 


>[!tip] Selección 
>Sea $R$ una relación (tabla), entonces $\sigma_{\text{condición}}(R)$ es una **nueva relación** que deja solo las tuplas que satisfacen la relación. 
>
>Solo se permiten los siguientes operadores: $=,\leq,\geq,<,\neq$, se puede combinar con las condiciones booleanas $\land$ (*and*) y $\lor$ (or). 

>[!tip] Proyección 
>Selecciona un conjunto de atributos a través de $\pi_{\text{condición}}(R)$. Básicamente sirve para **seleccionar columnas** dentro de la tabla. 

>[!note] Intersección 
>Sean $R_1$ y $R_2$ relaciones. $R_1\;\cap\;R_2$ devuelve una nueva relación con todas las tuplas en $R_1$ y $R_2$. Ambos deben tener los mismos atributos. 

>[!note] Diferencia 
>Sean $R_1$ y $R_2$ relaciones. $R_1 - R_2$ devuelve una nueva relación con las tuplas en $R_1$ que **no estén** en $R_2$. Ambas relaciones deben tener los mismos atributos. 

>[!note] Producto cartesiano 
>Sean $R_1$ y $R_2$ relaciones. $R_1\times R_2$ devuelve una nueva relación con todas las tuplas $(r_1,r_2)$ tal que $r_1\in R_1$, $r_2\in R_2$. Ambas relaciones **no pueden tener atributos en común**. 

>[!note] Renombramiento 
>
>Sea $R$ una relación. $\rho_{A_i/A_j}(R)$ devuelve una nueva relación igual a $R$ pero con $A_i$ renombrado como $A_j$. 

>[!note] Join 
>Se escribe como $R_1\Join R_2$ y es equivalente a $\sigma_{\text{condición}}(R_1\times R_2)$. 
>
>En rigor, no es un operador, porque está cubierto por los operadores de producto y selección. Pero *join* es tán común que se abrevia así. 
>

>[!note] División 
>Su consulta es $R\divsymbol\pi_B(R)$, y se define como: 
>
>$$\pi_A(R)-\pi_A(\pi_A(R)\times\pi_B(R)-R)$$

<div style="page-break-after: always;"></div>

#### Ejemplos 

Se tienen las siguiente tablas relacionales:

- Cervezas: 

| **Marca** | **Nombre** | **Tipo** | **Grados** | **Origen**   | **mL** | **Precio** |
|:---------:|:----------:|:--------:|:----------:| ------------ |:------:|:----------:|
|  Austral  |   Lager    |  Lager   |   $4.6$    | Punta Arenas | $330$  |   $2000$   |
|  Austral  |   Yagan    |   Ale    |   $5.0$    | Punta Arenas | $330$  |   $2400$   |
|   Raco    |   Amber    |   Ale    |   $4.5$    | Maipo        | $500$  |   $3000$   |


- Vinos: 

|     **Marca**     | **Nombre** | **Año** |  **Tipo**  | **Grados** | **Origen** | **mL** | **Precio** |
|:-----------------:|:----------:|:-------:|:----------:|:----------:|:----------:|:------:|:----------:|
|   ** Tarapaca**   |    Gran    |  $2014  |  Carmenere |   $13.5$   |    Maipo   |   750  |    4500    |
| **Concha y Toro** |   Amelie   |  $2016$ | Chardonnay |   $14.0$   | Casablanca |   700  |    3000    |
| **Concha y Toro** |   Gravas   |  $2015$ |    Syrah   |   $14.0$   |    Maipo   |   700  |    3100    |


- *¿Qué ales son más fuertes que $4.8$?* 

$$\sigma_{\text{tipo=Ale}\;\land\;\text{grados}>4.8}(Cerveza)$$

- *¿Qué tipos de cerveza hay?*

$$\pi_\text{tipo}(\text{Cerveza})$$


- *¿Qué tipos tienen una cerveza más fuerte que $4.8$?*

$$\pi_\text{tipo}(\sigma_{\text{grados}>4.8}(Cerveza))$$

**La proyección siempre va de último (afuera del paréntesis)**. 

- *¿Qué marcas de vino tienen un tipo que sea Carmenere o Syrah?*

$$\pi_\text{marca,tipo}\left(\sigma_{\text{tipo=Carmenere}\lor\text{tipo=Syrah}}(\text{Vino})\right)$$

- *¿Qué marcas de cerveza tienen un ale y lager?*

$$\pi_\text{marca}\left(\sigma_\text{tipo=Ale}(\text{Cerveza})\right)\cap\pi_\text{marca}\left(\sigma_\text{tipo=Lager}(\text{Cerveza})\right)$$
<div style="page-break-after: always;"></div>

## SQL 

La forma básica de una consulta en SQL es de la siguiente forma: 

```SQL 
SELECT [atributos]
FROM [tablas]
WHERE [condición] 
```

En álgebra relacional, `SELECT` sería el equivalente a la proyección ($\pi$) y `WHERE` sería la selección ($\sigma$). 

SQL por sí sólo devuelve tuplas que tienen repeticiones. Para evitar las repeticiones se ocupa `DISTINCT`. 

```SQL 
SELECT DISTINCT planeta 
FROM Aterrizaje 
```

### Funciones básicas: 

- `ORDER BY`: Ordena las consultas según un atributo. Se puede poner `DESC` o `ASC` para ordenar de forma ascendente o descendente. 

- `UNION`: Une dos columnas de relaciones distintas. Los duplicados se borran. 

```SQL 
SELECT nombre 
FROM Planeta 
UNION 
SELECT nombre 
FROM Satélite 
```

Cuando se tiene una columna de otra relación con un nombre distinto, se ocupa un renombramiento 

```SQL 
SELECT nombre AS planeta 
FROM Planeta 
UNION 
SELECT planeta 
FROM Satélite 
```

- `UNION ALL`: Es una *"unión bruta"* que acepta duplicados.

- `EXCEPT`: Funciona como una condicional para sacar ciertas condiciones 

```SQL 
SELECT nombre AS planeta 
FROM Planeta 
WHERE dist > 1.00 
EXCEPT 
SELECT planeta 
FROM Satélite 
```

- `INTERSECT`: Es la intersección entre dos tablas. 

- `LIKE`: Detecta patrones simples en strings.  

```SQL 
SELECT nombre 
FROM Planeta 
WHERE nombre LIKE 'M%'
```

Devolvería 

| **Nombre** |
|:----------:|
|  Mercurio  |
|    Marte   |

- `NOT`: La negación de un condicional  

- `IN`: Condicional que se puede ejecutar sobre otras columnas dentro de una misma relación 

```SQL 
SELECT planeta 
FROM Aterrizaje 
WHERE país IN ('EEUU', 'ESA')
```

- `BETWEEN`: Condicional para trabajar en un rango de valores. 

```SQL 
SELECT planeta 
FROM Aterrizaje 
WHERE año BETWEEN 1971 AND 1978
```

- `CROSS JOIN`: Es un producto cartesiano, combina tuplas de una tabla con otra tabla.  La nueva tabla va en el orden del cross join. 

```SQL 
SELECT colores.nombre, objetos.objeto 
FROM colores 
CROSS JOIN objetos;
```

- `JOIN`: Une dos tablas, pero hay que especificar bajo que parámetro se unen. Existen dos formas equivalentes: 

```SQL 
SELECT nombre, año, nave
FROM Planeta, Aterrizaje 
WHERE nombre = planeta 
AND dist > 1.00 
AND año >= 2000
```

```SQL 
SELECT nombre, año, nave 
FROM Planeta JOIN Aterrizaje 
ON nombre = planeta 
WHERE dist > 1.00 
AND año >= 2000 
```

- `NATURAL JOIN`: Combina filas de dos tablas donde los valores de todas las columnas que tienen el mismo nombre en ambas tablas coinciden. Sirve por lo general para combinar cosas con ID's. Supongamos que tenemos la tabla "empleados" y "salarios":

| id | nombre  | edad |
|----|---------|------|
| 1  | Ana     | 25   |
| 2  | Juan    | 30   |
| 3  | Marta   | 28   |

| id | salario |
|----|---------|
| 1  | 50000   |
| 2  | 60000   |
| 4  | 70000   |


```SQL 
SELECT * 
FROM empleados 
NATURAL JOIN salarios;
```
Daría como resultado: 

| id | nombre | edad | salario |
|----|--------|------|---------|
| 1  | Ana    | 25   | 50000   |
| 2  | Juan   | 30   | 60000   |



- `COALESCE`: Sirve para seleccionar primer valor no nulo. En realidad, lo del primer valor es un parámetro. 

```SQL 
SELECT nombre, COALESCE(año,0)
```

- `LEFT JOIN`: Devuelve todas las filas de la tabla de la izquierda y las filas coincidentes de la tabla de la derecha. Si no hay una coincidencia, los resultados de la tabla de la derecha serán `NULL`. Ocupando la misma tabla de antes: 

```SQL 
SELECT empleados.nombre, salarios.salario 
FROM empleados 
LEFT JOIN salarios ON empleados.id = salarios.empleado_id;
```

Daría como resultado: 

| nombre | salario |
|--------|---------|
| Ana    | 50000   |
| Juan   | 60000   |
| Marta  | NULL    |


- `FULL JOIN`: Devuelve todas las filas cuando hay una coincidencia en una de las tablas. Bajo el ejemplo anterior, se tendría lo siguiente: 

```SQL 
SELECT empleados.nombre, salarios.salario 
FROM empleados 
FULL JOIN salarios ON empleados.id = salarios.empleado_id;
```

| nombre | salario |
|--------|---------|
| Ana    | 50000   |
| Juan   | 60000   |
| Marta  | NULL    |
| NULL   | 70000   |


### Consultas anidadas 

Sirven para hacer subconsultas dentro de otras tablas: 

```SQL 
SELECT, nave, planeta 
FROM Aterrizaje 
WHERE planeta IN 
	(SELECT nombre 
	FROM Planeta 
	WHERE grav > 9.8)
AND año > 2000
```

También está `ANY` que devuelve cualquier coincidencias en subconsultas cuando algun valor es verdadero

```SQL 
SELECT nombre 
FROM Planeta P1 
WHERE P1.grav > ANY 
	(SELECT P2.grav 
	FROM Planeta P2 
	WHERE P2.dist > 1.00)
ORDER BY P1.dist DESC 
```

A diferencial de `ALL`, que devuelve coincidencias cuando **todos** los valores son verdaderos. 

Cuando se hace una subconsulta en un `FROM` hay que cambiar el alias de toda la subconsulta. 

### Agregación 

Corresponden a los siguientes operadores numéricos: 

```SQL 
COUNT ([DISTINCT] A)
SUM ([DISTINCT] A)
AVG ([DISTINCT] A)
MAX (A)
MIN(A)
```
También está el `GROUP BY`, que básicamente agrupa según atributo en común. Para añadir un condicional se ocupa `HAVING`. 