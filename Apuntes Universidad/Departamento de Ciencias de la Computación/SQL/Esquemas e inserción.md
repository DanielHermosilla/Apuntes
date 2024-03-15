
Corresponde a una agrupación de [[Modelos Relacionales|tablas]], es como si fuera una *entidad global*: 

```SQL
CREATE SCHEMA SistemaSolar; --crear una agrupación de tablas 
CREATE TABLA SistemaSolar.Aterrizaje (
	nave VARCHAR(255),
	planeta VARCHAR(255),
	país VARCHAR (255),
	año SMALLINT
); 
```

Para insertar datos se ocupa el `INSERT INTO`: 

```SQL 
INSERT INTO Aterrizaje VALUES ('Messenger', 'Mercurio', 'EEUU', 2015)

INSERT INTO Aterrizaje (país, nave, planeta) VALUES ('EEUU', 'Mars', 'Marte')
```

Ahora, para on hacerlo manualmente, es posible crear una tabla a partir de una consulta: 

```SQL 
INSERT INTO AterrizajeEEUU (SELECT * FROM Aterrizaje WHERE pais='EEUU')
```

Por el otro lado, es posible actualizar una tabla con `UPDATE`: 

```SQL 
UPDATE Aterrizaje 
	SET año=1971, país='URRSS'
```

Análogamente, para borrar, se ocupa simplemente ``DELETE FROM``. Si se quisiera borrar una columna entera, se tendría que declarar `ÀLTER TABLE` y mencionar `DROP COLUMN`. Si se quisiera hacer lo contrario, se añade la columna y se menciona el tipo de dato 

```SQL 
ALTER TABLE Aterrizaje ADD COLUMN 'Nave' VARCHAR(255)
```

Ahora, para importar datos, se hace de la siguiente forma: 

```SQL 
COPY Aterrizaje FROM '/home/Daniel/desktop...csv' DELIMITER E'\t'; 
```

El delimitador es la forma en que los datos están separados. 