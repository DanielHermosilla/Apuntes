

Sabemos que una consulta básica de escribe como 

```SQL 
SELECT [atributos]
FROM [tablas]
WHERE [condición] 
```

Notemos que es posible crear tablas bajo las tres consultas. Tomando nuevamente la relación planeta, aterrizaje y satélite: 


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


Una consulta anidada llegaría a ser: 

```SQL 
SELECT nave, planeta
FROM Aterrizaje 
WHERE planeta IN 
	(SELECT nombre 
	FROM planeta 
	WHERE grav > 9.8)
AND año > 2000 
```

Aunque no es necesario hacer una consulta anidada en este caso, es ocupado para **facilitar la sintaxis**. De hecho, todas las consultas anidadas se pueden hacer con consultas básicas de [[SQL]]. 

Aún así, existen consultas anidadas que también tienen un correlación dentro del condicional, y estos no se pueden simplificar en el sintaxis. 
