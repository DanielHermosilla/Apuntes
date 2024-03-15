
## Pregunta 1 

Se ocupo el siguiente código para crear todas las tablas: 

```SQL 

CREATE TABLE trx_p.sebadani_estado (
    	nombre varchar (255) PRIMARY KEY,
	voto_electoral smallint,
	cierre time,
	num_candidatos smallint
	
);

INSERT INTO sebadani_estado SELECT * FROM estado;


CREATE TABLE trx_p.sebadani_condado (
    nombre varchar(255),
    estado varchar(255),
    reportado float,
    CHECK (reportado <= 1 AND reportado >= 0),
    FOREIGN KEY (estado) REFERENCES trx_p.sebadani_estado(nombre),
	PRIMARY KEY(nombre, estado)	
);


INSERT INTO sebadani_condado SELECT * FROM condado;


CREATE TABLE trx_p.sebadani_candidato (
    nombre varchar (255) PRIMARY KEY,
	partido varchar (255)
);

INSERT INTO sebadani_candidato SELECT * FROM candidato;

CREATE TABLE trx_p.sebadani_votosPorCondado (
    candidato varchar (255),
	condado varchar (255),
	estado varchar (255),
    	votos int,
	
	FOREIGN KEY(candidato) REFERENCES trx_p.sebadani_candidato(nombre),
	FOREIGN KEY (condado, estado) REFERENCES trx_p.sebadani_condado(nombre, estado),
	
	PRIMARY KEY(candidato, condado, estado)
);

INSERT INTO sebadani_votosPorCondado SELECT * FROM votosPorCondado;
```

## Pregunta 2 

Para poder actualizar los datos se ocupará la siguiente sintaxis: 

```SQL 
UPDATE table_name
SET column1 = value1,
    column2 = value2,
    ...
WHERE condition;
```

Así, la consulta llegaría a ser: 

```SQL 
UPDATE trx_p.sebadani_votosPorCondado 

SET candidato = votosPorCondado1.candidato,
condado = votosPorCondado1.condado,
estado = votosPorCondado1.estado,
votos = votosPorCondado1.votos

FROM votosPorCondado1

WHERE trx_p.sebadani_votosPorCondado.candidato = votosPorCondado1.candidato AND
trx_p.sebadani_votosPorCondado.condado = votosPorCondado1.condado AND
trx_p.sebadani_votosPorCondado.estado = votosPorCondado1.estado;
```

## Pregunta 3 

Al igual que en la pregunta pasada: 


```SQL 
UPDATE trx_p.sebadani_condado 

SET nombre = condado1.nombre,
estado = condado1.estado,
reportado = condado1.reportado

FROM condado1

WHERE
trx_p.sebadani_condado.nombre = condado1.nombre AND
trx_p.sebadani_condado.estado = condado1.estado;
```

## Pregunta 4 

```SQL 
START TRANSACTION; 
	UPDATE trx_p.sebadani_votosPorCondado 

	SET candidato = votosPorCondado2.candidato,
	condado = votosPorCondado2.condado,
	estado = votosPorCondado2.estado,
	votos = votosPorCondado2.votos
	
	FROM votosPorCondado2
	
	WHERE trx_p.sebadani_votosPorCondado.candidato = votosPorCondado2.candidato AND
	trx_p.sebadani_votosPorCondado.condado = votosPorCondado2.condado AND
	trx_p.sebadani_votosPorCondado.estado = votosPorCondado2.estado;
	
	UPDATE trx_p.sebadani_condado 

	SET nombre = condado2.nombre,
	estado = condado2.estado,
	reportado = condado2.reportado
	
	FROM condado2
	
	WHERE
	trx_p.sebadani_condado.nombre = condado2.nombre AND
	trx_p.sebadani_condado.estado = condado2.estado;

COMMIT; 
```
## Pregunta 5 

Para la tercera hora: 
```SQL 
START TRANSACTION;

UPDATE trx_p.sebadani_votosPorCondado 
SET
  candidato = votosPorCondado3.candidato,
  condado = votosPorCondado3.condado,
  estado = votosPorCondado3.estado,
  votos = votosPorCondado3.votos
FROM votosPorCondado3
WHERE
  trx_p.sebadani_votosPorCondado.candidato = votosPorCondado3.candidato AND
  trx_p.sebadani_votosPorCondado.condado = votosPorCondado3.condado AND
  trx_p.sebadani_votosPorCondado.estado = votosPorCondado3.estado;

UPDATE trx_p.sebadani_condado 
SET
  nombre = condado3.nombre,
  estado = condado3.estado,
  reportado = condado3.reportado
FROM condado3
WHERE
  trx_p.sebadani_condado.nombre = condado3.nombre AND
  trx_p.sebadani_condado.estado = condado3.estado;

COMMIT;
```

Para la cuarta hora: 

```SQL 
START TRANSACTION;

UPDATE trx_p.sebadani_votosPorCondado 
SET
  candidato = votosPorCondado4.candidato,
  condado = votosPorCondado4.condado,
  estado = votosPorCondado4.estado,
  votos = votosPorCondado4.votos
FROM votosPorCondado4
WHERE
  trx_p.sebadani_votosPorCondado.candidato = votosPorCondado4.candidato AND
  trx_p.sebadani_votosPorCondado.condado = votosPorCondado4.condado AND
  trx_p.sebadani_votosPorCondado.estado = votosPorCondado4.estado;


UPDATE trx_p.sebadani_condado 
SET
  nombre = condado4.nombre,
  estado = condado4.estado,
  reportado = condado4.reportado
FROM condado4
WHERE
  trx_p.sebadani_condado.nombre = condado4.nombre AND
  trx_p.sebadani_condado.estado = condado4.estado;


COMMIT;
```

Para la quinta hora: 

```SQL 
START TRANSACTION;


UPDATE trx_p.sebadani_votosPorCondado 
SET
  candidato = votosPorCondado5.candidato,
  condado = votosPorCondado5.condado,
  estado = votosPorCondado5.estado,
  votos = votosPorCondado5.votos
FROM votosPorCondado5
WHERE
  trx_p.sebadani_votosPorCondado.candidato = votosPorCondado5.candidato AND
  trx_p.sebadani_votosPorCondado.condado = votosPorCondado5.condado AND
  trx_p.sebadani_votosPorCondado.estado = votosPorCondado5.estado;


UPDATE trx_p.sebadani_condado 
SET
  nombre = condado5.nombre,
  estado = condado5.estado,
  reportado = condado5.reportado
FROM condado5
WHERE
  trx_p.sebadani_condado.nombre = condado5.nombre AND
  trx_p.sebadani_condado.estado = condado5.estado;

COMMIT;
```

Para la sexta hora: 

```SQL 
START TRANSACTION;

UPDATE trx_p.sebadani_votosPorCondado 
SET
  candidato = votosPorCondado6.candidato,
  condado = votosPorCondado6.condado,
  estado = votosPorCondado6.estado,
  votos = votosPorCondado6.votos
FROM votosPorCondado6
WHERE
  trx_p.sebadani_votosPorCondado.candidato = votosPorCondado6.candidato AND
  trx_p.sebadani_votosPorCondado.condado = votosPorCondado6.condado AND
  trx_p.sebadani_votosPorCondado.estado = votosPorCondado6.estado;


UPDATE trx_p.sebadani_condado 
SET
  nombre = condado6.nombre,
  estado = condado6.estado,
  reportado = condado6.reportado
FROM condado6
WHERE
  trx_p.sebadani_condado.nombre = condado6.nombre AND
  trx_p.sebadani_condado.estado = condado6.estado;

```

Para la séptima hora: 

```SQL 
UPDATE trx_p.sebadani_votosPorCondado 
SET
  candidato = votosPorCondado7.candidato,
  condado = votosPorCondado7.condado,
  estado = votosPorCondado7.estado,
  votos = votosPorCondado7.votos
FROM votosPorCondado7
WHERE
  trx_p.sebadani_votosPorCondado.candidato = votosPorCondado7.candidato AND
  trx_p.sebadani_votosPorCondado.condado = votosPorCondado7.condado AND
  trx_p.sebadani_votosPorCondado.estado = votosPorCondado7.estado;

-- Actualización de sebadani_condado para la tabla 7
UPDATE trx_p.sebadani_condado 
SET
  nombre = condado7.nombre,
  estado = condado7.estado,
  reportado = condado7.reportado
FROM condado7
WHERE
  trx_p.sebadani_condado.nombre = condado7.nombre AND
  trx_p.sebadani_condado.estado = condado7.estado;
```

Para la octava hora: 

```SQL
UPDATE trx_p.sebadani_votosPorCondado 
SET
  candidato = votosPorCondado8.candidato,
  condado = votosPorCondado8.condado,
  estado = votosPorCondado8.estado,
  votos = votosPorCondado8.votos
FROM votosPorCondado8
WHERE
  trx_p.sebadani_votosPorCondado.candidato = votosPorCondado8.candidato AND
  trx_p.sebadani_votosPorCondado.condado = votosPorCondado8.condado AND
  trx_p.sebadani_votosPorCondado.estado = votosPorCondado8.estado;


UPDATE trx_p.sebadani_condado 
SET
  nombre = condado8.nombre,
  estado = condado8.estado,
  reportado = condado8.reportado
FROM condado8
WHERE
  trx_p.sebadani_condado.nombre = condado8.nombre AND
  trx_p.sebadani_condado.estado = condado8.estado;
```


Para la novena hora: 

```SQL
UPDATE trx_p.sebadani_votosPorCondado 
SET
  candidato = votosPorCondado9.candidato,
  condado = votosPorCondado9.condado,
  estado = votosPorCondado9.estado,
  votos = votosPorCondado9.votos
FROM votosPorCondado9
WHERE
  trx_p.sebadani_votosPorCondado.candidato = votosPorCondado9.candidato AND
  trx_p.sebadani_votosPorCondado.condado = votosPorCondado9.condado AND
  trx_p.sebadani_votosPorCondado.estado = votosPorCondado9.estado;

UPDATE trx_p.sebadani_condado 
SET
  nombre = condado9.nombre,
  estado = condado9.estado,
  reportado = condado9.reportado
FROM condado9
WHERE
  trx_p.sebadani_condado.nombre = condado9.nombre AND
  trx_p.sebadani_condado.estado = condado9.estado;

COMMIT;
```

## Pregunta 6

```SQL 
START TRANSACTION;

UPDATE trx_p.sebadani_votosPorCondado 
SET
  candidato = votosPorCondadoX.candidato,
  condado = votosPorCondadoX.condado,
  estado = votosPorCondadoX.estado,
  votos = votosPorCondadoX.votos
FROM votosPorCondadoX
WHERE
  trx_p.sebadani_votosPorCondado.candidato = votosPorCondadoX.candidato AND
  trx_p.sebadani_votosPorCondado.condado = votosPorCondadoX.condado AND
  trx_p.sebadani_votosPorCondado.estado = votosPorCondadoX.estado;

UPDATE trx_p.sebadani_condado 
SET
  nombre = condadoX.nombre,
  estado = condadoX.estado,
  reportado = condadoX.reportado
FROM condadoX
WHERE
  trx_p.sebadani_condado.nombre = condadoX.nombre AND
  trx_p.sebadani_condado.estado = condadoX.estado;

COMMIT;
```

Arroja el siguiente error: 

```SQL 
ERROR:  new row for relation "sebadani_condado" violates check constraint "sebadani_condado_reportado_check"
DETAIL:  Failing row contains (Real County, Texas, 100).
```

Esto se debe a que la columna `reportado` tenía el constraint de `CHECK (reportado <= 1 AND reportado >= 0)` (para que sólo acepte números decimales). Como Putín ocupó números porcentuales no pudo entrar a la base de datos. 

Ahora, si hacemos el `COMMIT` obtenemos un `ROLLBACK`. Esto, debido que ocurrió un error que logró que la transacción no ocurra con exito. 

### Verificación del hackeo 

Si nos fijamos en la tabla `votosPorCondadoX`, se tiene lo siguiente: 

```SQL 
SELECT * FROM votosPorCondadoX;
```

Retorna; 

```sql 
 candidato  |   condado   | estado |   votos
------------+-------------+--------+-----------
 H. Clinton | Real County | Texas  | 999999999
 ```

Ahora, buscando ese valor en nuestra relación: 

```SQL 
SELECT * FROM trx_p.sebadani_votosPorCondado 
WHERE candidato = 'H. Clinton' 
AND condado = 'Real County' 
AND estado = 'Texas'; 
```

Retorna lo siguiente: 

```SQL 
 candidato  |   condado   | estado | votos
------------+-------------+--------+-------
 H. Clinton | Real County | Texas  |     0
(1 row)
```

Por lo tanto, Putín **no pudo hackear la base de datos**. 