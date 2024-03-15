Solo se puede usar SQL I, los operadores son: 

```SQL 
SELECT -- Atributo
DISTINCT -- Elimina duplicados 
FROM -- Relación 
WHERE AND -- Booleanos 
ORDER BY a DESC -- Ordenar, descender o ascendiente 
JOIN -- Se puede ocupar para unir tablas, normalmente se ocupa ","
INTERSECT -- Intersecta tablas 
IN -- Verifica si está dentro
NATURAL JOIN -- Une dos relaciones con columnas en común. 
LEFT OUTER JOIN -- Une dos tablas y deja las filas no en común de la tabla izquierda 
FULL OUTER JOIN -- Une dos tablas y deja las filas no en común entre tablas 

```
## Pregunta 1 

```SQL 
SELECT nombre
FROM pelicula
WHERE anho > 1980
AND anho < 1989
ORDER BY calificacion; 
```
## Pregunta 2 

```SQL 
SELECT personaje
FROM  personaje 
WHERE a_nombre = 'Zacapa, Daniel'
ORDER BY p_anho DESC; 
```
## Pregunta 3 

```SQL 
SELECT nombre 
FROM pelicula 
WHERE nombre IN 
	(SELECT p_nombre 
	FROM personaje 
	WHERE a_nombre = 'Zacapa, Daniel')
ORDER BY calificacion DESC; 
```
## Pregunta 4 

```SQL 
SELECT personaje
FROM personaje 
WHERE a_nombre IN 
	(SELECT nombre 
	FROM actor
	WHERE genero = 'F')
AND p_anho IN
	(SELECT anho
	FROM pelicula 
	WHERE calificacion >= 8.5
	AND anho >= 1990
	AND anho <= 1999);
```

## Pregunta 5 

```SQL 
SELECT nombre 
FROM pelicula 
WHERE nombre LIKE 'The Lord of the Rings%'
ORDER BY calificacion, anho;
```

## Pregunta 6 

```SQL 
SELECT personaje.a_nombre
FROM personaje 
WHERE EXISTS (
	SELECT 1 
	FROM personaje AS personaje2
	WHERE personaje2.a_nombre = personaje.a_nombre
	AND personaje2.p_nombre = personaje.p_nombre 
	AND personaje2.personaje != personaje.personaje
)
LIMIT 15;
```
## Pregunta 7 

```SQL 
SELECT p_nombre
FROM personaje 
WHERE a_nombre = 'Thurman, Uma'
INTERSECT 
SELECT p_nombre 
FROM personaje 
WHERE a_nombre = 'Jackson, Samuel L.';
```
## Pregunta 8 

```SQL
SELECT DISTINCT personaje.p_nombre
FROM personaje 
WHERE personaje.p_nombre NOT IN (
	SELECT p_nombre 
	FROM personaje 
	WHERE a_nombre = 'Thurman, Uma'
	INTERSECT 
	SELECT p_nombre 
	FROM personaje 
	WHERE a_nombre = 'Jackson, Samuel L.');
```
## Pregunta 9 

```SQL 
SELECT DISTINCT personaje.a_nombre, personaje2.a_nombre 
FROM personaje 
CROSS JOIN personaje AS personaje2 
WHERE personaje.a_nombre < personaje2.a_nombre
WHERE EXISTS (
	SELECT 1 
	FROM personaje AS personaje3
	WHERE personaje.a_nombre != personaje3.a_nombre 
	AND EXISTS (
		SELECT 1
		FROM personaje AS personaje4
		WHERE personaje4.a_nombre = personaje2.a_nombre 
		AND personaje3.p_nombre = personaje4.p_nombre
		AND personaje3.p_nombre != personaje.nombre
)
LIMIT 15;
```


## Pregunta 10 

```SQL 
SELECT pelicula.nombre, pelicula.calificacion 
FROM pelicula 
WHERE NOT EXISTS (
	SELECT 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
	FROM pelicula AS pelicula2 
	WHERE pelicula2.calificacion > pelicula.calificacion 
);
```
