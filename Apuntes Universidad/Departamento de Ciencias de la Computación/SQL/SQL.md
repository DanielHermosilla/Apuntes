
SQL es un [[Lenguajes de Consulta|lenguaje de consulta]] de [[Bases de Datos|base de datos]], de hecho su propio nombre lo indica, *structured query language*. 

Esto es un lenguaje **procedural**, vale decir, el usuario indica lo que se quiere lograr. Vale decir, traspasar el *lenguaje natural* a un lenguaje computacional. Se podría decir que es una mezcla del álgebra relacional con la lógica de primer orden.

Muchas distribuciones del lenguaje tiene muchos detalles y cosas únicas, pero todos comparten algo común denominado *core*. 

## Forma básica de consulta 

Al igual que en el álgebra relacional, existe un equivalente con los *operadores* **SELECT, FROM y WHERE**: 

- **SELECT**: Selecciona atributos, vale decir, filas de la tabla. Análogo al operador $\sigma$. 
- **FROM**: La relación o tabla de la que se está seleccionando. Análogo al operador $\pi$. 
- **WHERE**: Es la condición que se impone al seleccionar. 

Una diferencia con el álgebra relacional es que se entregan **elementos duplicados**. Esto se puede hacer bajo el operador **SELECT DISTINCT**.  Un ejemplo simple sería con las siguiente tablas donde las relaciones se llama *planeta*, *aterrizaje* y *satélite* respectivamente:


|   **Nombre**  | **Distancia** | **Radio** | **Grav** | ** D i a s ** | **Años** | **Temperatura** | **Anillo** |
|:-------------:|:-------------:|:---------:|:--------:|:-------------:|:--------:|:---------------:|:----------:|
|  **Mercurio** |      0,39     |    0,38   |    2,8   |     58,646    |   0,241  |       440       |    false   |
|   **Venus**   |      0,72     |    0,95   |    8,9   |    -243,019   |   0,615  |       730       |    false   |
|   **Tierra**  |      1,00     |    1,00   |    9,8   |     0,997     |   1,000  |       288       |    false   |
|   **Marte**   |      1,52     |    0,53   |    3,7   |     1,026     |   1,880  |       186       |    false   |
| **  Jupiter** |      5,20     |   10,97   |   22,9   |     0,414     |  11,862  |       152       |    true    |
|  **Saturno**  |      9,54     |    9,14   |    9,1   |     0,444     |  29,447  |       134       |    true    |
|   **Urano**   |     19,19     |    3,98   |    7,8   |     -0,719    |  84,017  |        76       |    true    |
|  **Neptuno**  |     30,07     |    3,86   |   11,0   |     0,617     |  164,791 |        53       |    true    |

|    **Nave**   | **Planeta** | **País** | **Año** |
|:-------------:|:-----------:|:--------:|:-------:|
|   Messenger   |   Mercurio  |   EEUU   |   2015  |
|    Venera 3   |    Venus    |   URRS   |   1966  |
|    Pioneer    |    Venus    |   EEUU   |   1978  |
| Mars 2 lander |    Marte    |   URRS   |   1971  |
|    Viking 1   |    Marte    |   EEUU   |   1976  |
|    Beagle 2   |    Marte    |    ESA   |   2003  |
|    Galileo    |   Jupiter   |   EEUU   |   2003  |


|  **Nombre**  | **Planeta** |   **Descubridor**  | **Año** |
|:------------:|:-----------:|:------------------:|:-------:|
|     Luna     |    Tierra   |         Null         |    Null   |
|   Ganimedes  |   Jupiter   |   Galileo Galilei  |   1610  |
|    Calisto   |   Jupiter   |   Galileo Galilei  |   1610  |
|  E u r o p a |   Jupiter   |   Galileo Galilei  |   1610  |
|      Io      |   Jupiter   |   Galileo Galilei  |   1610  |
|     Titan    |   Saturno   | Christiaan Huygens |   1655  |
|    Triton    |   Neptuno   |   William Lassell  |   1846  |

```SQL 
SELECT DISTINCT planeta 
FROM aterrizaje 
```

Esto retornaría 

| **Nombre** |
|:----------:|
|    Venus   |
|    Marte   |
|  Mercurio  |
|   Jupiter  |

A diferencia de un select sin distinct, retornaría 

### Renombramiento 

Es posible renombrar los atributos de la tabla al ocupar **AS**: 

```SQL 
SELECT S.planeta AS splaneta 
FROM Satélita S, Aterrizaje A
WHERE S.planeta = A.planeta 
```

### Unión  

Se pueden hacer uniones entre consultas: 

```SQL 
(SELECT nombre AS planeta
FROM Planeta 
)
UNION 
(SELECT planeta
FROM Satélite)
```
Los paréntesis no son necesarios pero es una buena práctica. Notemos que para que nos retorne una tabla con el nombre de un atríbuto, renombramos alguno de los dos atributos. Esta unión retornaría lo siguiente: 

| **Nombre** |
|:----------:|
|    Urano   |
|    Venus   |
|  Mercurio  |
|    Tierra  |
|   Saturno  |
|   Neptuno  |
|   Jupiter  |
|    Marte   |

Notemos que es contraintuitivo, pero retorna elementos *singleton*. Vale decir, es como si ocupara **DISTINCT** por defecto. Para que retorne tuplas duplicadas se ocupa **UNION ALL** 

```SQL 
(SELECT nombre AS planeta
FROM Planeta 
)
UNION ALL 
(SELECT planeta
FROM Satélite)
```

### Patrón LIKE 

Sirve para elegir cierto string en cierta posición al ocupar $\%$. Por ejemplo, para seleccionar todos los planetas que empiezan con el string $M$: 

```SQL 
SELECT nombre
FROM Planeta 
WHERE nombre LIKE 'M%'
```

### Producto Cruz: JOIN 

Existe el **JOIN** que puede ser simplificado con una coma. Por ejemplo, ambas consultas son equivalentes aunque no necesariamente son igualmente de eficientes. 

```SQL 
SELECT nombre, año, nave 
FROM Planeta, Aterrizaje 
WHERE nombre = planeta 
AND dist > 1.00 
AND año >= 2000 
```

Es equivalente a 

```SQL 
SELECT nombre, año, nave
FROM Planeta JOIN Aterrizaje
ON nombre = planeta 
WHERE dist > 1.00 
AND año >= 2000
```
### Producto Cruz: NATURAL JOIN 

Para enlazar columnas con el mismo nombre entre dos relaciones 

```SQL
SELECT nombre, planeta
FROM Satélite 
NATURAL JOIN Aterrizaje
```

### Nulos 

Por lo general se ocupa **NULL** para llenar campos desconocidos o inaplicables, pero no es recomendable ocuparlo ya que un **NULL** tiene varias interpretaciones. Lo único que si es algo interpretable es que **no significa Falso**. 

También en las comparaciones, **no son consideradas**. Por lo general, cuando no importa el valor del desconocido, el resultado se mantiene. Cuando importa, el resultado es desconocido. Por ejemplo: 

```SQL 
SELECT nombre 
FROM Satélite 
WHERE año > 1800
```

Retornaría únicamente la tupla *Satélite (Nombre: Tritón)*. Por lo general ocupa la siguiene tabla de verdad: 

![[Pasted image 20230920112503.png|center|600]]



### Joins Externos: LEFT-RIGHT OUTER JOIN 

Se mantienen las tuplas de la izquierda si no hay datos desde la derecha. 

```SQL 
SELECT nave, nombre, dist, año 
FROM Planeta LEFT JOIN Aterrizaje 
ON nombre = planeta 
```

Lo que quiere decir, simplemente, es que del atributo *"Aterrizaje"* deben ir **todos** los valores. 

Notemos que **LEFT JOIN** es equivalente a **LEFT OUTER JOIN**. 

### Joins Externos: FULL OUTER JOIN 

Se mantienen las tuplas de la derecha y la izquierda. 

```SQL 
SELECT planeta, nave, nombre AS satélite 
FROM Sátelite S FULL OUTER JOIN 
ON S.planeta = A.planeta 
```







