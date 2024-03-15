
Son aquellas [[Diseño de tablas|tablas]] que aceptan valores dinámicos. Como su nombre dice, no están materializadas dentro de la base de datos. 

```SQL 
CREATE VIEW ÁlbumEval AS 
SELECT album, artista, 
FLOOR(AVG(eval)) AS pm, 
COUNT(eval) AS num 
FROM Evaluación 
GROUP BY album, artista 
```

También sirven para abreviar consultas y patrones comunes, evitando repeticiones de patrones comunes. 

Además, se usan para **problemas de seguridad** donde se pueden dar acceso a una vista y no a todos los datos. 

## Vistas materializada 

Si muchas veces se ocupa una tabla virtual, es posible *materializar* la vista. Es casi como crear una tbala, pero es una tabla que depende de otras tablas. 

```SQL 
CREATE MATERIALIZED VIEW ÁlbumEval AS 
SELECT álbum, artista, FLOOR(AVG(eval)) AS pm, 
COUNT(eval) AS num 
FROM Evaluación 
GROUP BY álbum, artista 
```

Sin embargo, al materializar es necesario ir **refrescando datos**, pierde en cierto sentido la dinamicidad. Se impone al comienzo `REFRESH MATERIALIZED VIEW ÁlbumEval`.  