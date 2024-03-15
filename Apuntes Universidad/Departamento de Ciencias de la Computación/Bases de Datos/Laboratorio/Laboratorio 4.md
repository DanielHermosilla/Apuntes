Hecho por Daniel Hermosilla y Sebastian Jana 
### Pregunta 1 

```SQL 
SELECT COUNT(nombre)
FROM pelicula; 
```

### Pregunta 2 

```SQL 
SELECT COUNT(DISTINCT anho)
FROM pelicula;
```

### Pregunta 3 

```SQL 
SELECT calificacion, nombre, anho 
FROM pelicula 
ORDER BY calificacion DESC, nombre ASC, anho DESC 
LIMIT 10;
```

### Pregunta 4 

```SQL 
SELECT DISTINCT a_nombre 
FROM personaje 
WHERE p_nombre IN 
(SELECT nombre 
 FROM pelicula 
 ORDER BY calificacion DESC, nombreASC, anho DESC 
 LIMIT 10) ;
```

### Pregunta 5 

```SQL 
SELECT DISTINCT nombre 
FROM actor 
WHERE genero = 'F'
AND nombre IN 
	(SELECT DISTINCT a_nombre 
	FROM personaje 
	WHERE p_nombre IN 
		(SELECT nombre 
		 FROM pelicula 
		 ORDER BY calificacion DESC, nombre ASC, anho DESC 
		 LIMIT 10) 
	);
```

### Pregunta 6 

```SQL 
SELECT DISTINCT FLOOR(p_anho/10)*10 as Década
FROM personaje 
WHERE a_nombre = 'Buscemi, Steve'
;
```
### Pregunta 7 

```SQL 
SELECT anho, COUNT(DISTINCT nombre)
FROM pelicula 
GROUP BY anho; 
```

### Pregunta 8 

```SQL 
SELECT anho, conteo 
FROM (
	SELECT anho, COUNT(DISTINCT nombre) as conteo
	FROM pelicula 
	GROUP BY anho
	ORDER BY COUNT(DISTINCT nombre) DESC) as a
WHERE a.conteo > 2 -- El ayudante dijo que debe ser mayor estricto 
;
```

### Pregunta 9 

```SQL 
SELECT a_nombre, COUNT(a_nombre) as Conteo
FROM personaje 
WHERE personaje.p_nombre IN 
	(SELECT nombre
	FROM pelicula 
	WHERE calificacion >= 8.6)
GROUP BY a_nombre -- Elimina duplicados 
ORDER BY Conteo DESC;
```
### Pregunta 10 

```SQL 
SELECT p_nombre, COUNT(DISTINCT nombre) as conteo
FROM personaje 
LEFT JOIN actor ON a_nombre = nombre AND genero = 'F' 
GROUP BY p_nombre
;
```

