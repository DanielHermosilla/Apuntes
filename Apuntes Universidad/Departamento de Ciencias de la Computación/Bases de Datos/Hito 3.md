
```SQL 
SELECT O.cargo, 
P.género, 
COUNT(O.cargo) as conteo, 
AVG(R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna) AS Ingreso
FROM udechile.Remuneraciones AS R
FULL OUTER JOIN udechile.Ocupacion AS O
ON R.T2_ido = O.ido
FULL OUTER JOIN udechile.Persona AS P
ON R.T2_idp = P.idp
GROUP BY O.cargo, P.género
HAVING COUNT(O.cargo) > 4 
ORDER BY conteo
LIMIT 15;
```

```SQL 
SELECT O.cargo,
COUNT(O.cargo) AS conteo,
CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Masculino,
CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Femenino,
CAST(ABS(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END)) AS INT) AS Brecha_Salarial
FROM udechile.Remuneraciones AS R
FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido
FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp
GROUP BY O.cargo
HAVING COUNT(O.cargo) > 4 
AND COUNT(P.género='M') > 4
AND COUNT(P.género='F') > 4
ORDER BY conteo DESC
LIMIT 15;
```

```SQL 
SELECT O.cargo,
COUNT(O.cargo) AS conteo,

COUNT(CASE WHEN P.género = 'M' THEN 0 END) as conteoH,

COUNT(CASE WHEN P.género = 'F' THEN 0 END) as conteoM,

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Masculino,

CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Femenino,

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS brecha_salarial

FROM udechile.Remuneraciones AS R
FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido
FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp
GROUP BY O.cargo
HAVING COUNT(CASE WHEN P.género = 'M' THEN 0 END) > 4 AND COUNT(CASE WHEN P.género = 'F' THEN 0 END) > 4
AND COUNT(O.cargo) != 0
ORDER BY brecha_salarial ASC;
```


```SQL 
DO $$ 
DECLARE
    IngresoMasculino INTEGER;
BEGIN
    SELECT AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END)::INT
    INTO IngresoMasculino
    FROM udechile.Remuneraciones AS R
	FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido
	FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp;

END $$;
```

```SQL 
DO $$ 
DECLARE
    IngresoFemenino INTEGER;
BEGIN
    SELECT AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END)::INT
    INTO IngresoFemenino
	FROM udechile.Remuneraciones AS R
	FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido
	FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp;
    
END $$;
```

```SQL 
SELECT O.cargo,
COUNT(O.cargo) AS conteo,
COUNT(CASE WHEN P.género = 'M' THEN 1 END) as conteoH,
COUNT(CASE WHEN P.género = 'F' THEN 1 END) as conteoM,
IngresoMasculino,
IngresoFemenino,
ABS(IngresoMasculino - IngresoFemenino) as dif
FROM udechile.Remuneraciones AS R
FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido
FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp
GROUP BY O.cargo
HAVING COUNT(CASE WHEN P.género = 'M' THEN 1 END) > 4
AND COUNT(CASE WHEN P.género = 'F' THEN 1 END) > 4
AND COUNT(O.cargo) != 0
ORDER BY brecha_salarial ASC;
```

## 2da consulta 

```SQL 
SELECT p.facultad, -- Selecciona la facultad 

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Masculino, -- Ingreso promedio de todos los trabajadores masculinos

CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Femenino, -- Ingreso promedio de todos los trabajadores femeninos

ABS(CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT)) AS brecha_salarial

FROM udechile.Remuneraciones AS R
FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido
FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp
GROUP BY p.facultad -- Agrupa por facultad 
HAVING COUNT(p.facultad) != 0 AND 
COUNT(CASE WHEN P.género = 'M' THEN 0 END) > 4 AND COUNT(CASE WHEN P.género = 'F' THEN 0 END) > 4
ORDER BY brecha_salarial ASC
LIMIT 5;
```
```sql 
SELECT p.facultad, -- Selecciona la facultad 

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Masculino, -- Ingreso promedio de todos los trabajadores masculinos

CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Femenino, -- Ingreso promedio de todos los trabajadores femeninos

CAST(ABS(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END)) AS INT) AS brecha_salarial

FROM udechile.Remuneraciones AS R

FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido

FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp

GROUP BY p.facultad -- Agrupa por facultad 

HAVING COUNT(p.facultad) != 0 AND 

COUNT(CASE WHEN P.género = 'M' THEN 0 END) > 4 AND 

COUNT(CASE WHEN P.género = 'F' THEN 0 END) > 4


ORDER BY brecha_salarial ASC 
LIMIT 5;
```

## 3era consulta 

```sql 
SELECT O.cargo, -- Selecciona el cargo 

COUNT(O.cargo) AS conteo, 

COUNT(CASE WHEN P.género = 'M' THEN 0 END) as conteoH,

COUNT(CASE WHEN P.género = 'F' THEN 0 END) as conteoM,

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Masculino,

CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Femenino,

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS brecha_salarial -- Negativo a favor de la mujer y viceversa

FROM udechile.Remuneraciones AS R

FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido

FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp

WHERE p.facultad = 'Facultad de Ciencias Físicas y Matemáticas' -- Imponemos busqueda en Beauchef

GROUP BY O.cargo

HAVING COUNT(CASE WHEN P.género = 'M' THEN 1 END) > 1

AND COUNT(CASE WHEN P.género = 'F' THEN 1 END) > 1
-- Bajamos la búsqueda a almenos 2 personas del mismo género por cargo
AND COUNT(O.cargo) != 0

ORDER BY brecha_salarial ASC;
```
```sql 
SELECT O.cargo, -- Selecciona el cargo 

COUNT(O.cargo) AS conteo, 

COUNT(CASE WHEN P.género = 'M' THEN 0 END) as conteoH,

COUNT(CASE WHEN P.género = 'F' THEN 0 END) as conteoM,

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Masculino,

CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Femenino,

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS brecha_salarial -- Negativo a favor de la mujer y viceversa

FROM udechile.Remuneraciones AS R

FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido

FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp

WHERE p.facultad = 'Facultad de Ciencias Físicas y Matemáticas' -- Imponemos busqueda en Beauchef

GROUP BY O.cargo

HAVING COUNT(CASE WHEN P.género = 'M' THEN 0 END) > 1

AND COUNT(CASE WHEN P.género = 'F' THEN 0 END) > 1
-- Bajamos la búsqueda a almenos 2 personas del mismo género por cargo
AND COUNT(O.cargo) != 0

ORDER BY brecha_salarial ASC;
```
## 4ta consulta 

```sql 

COUNT(CASE WHEN P.género = 'M' THEN 0 END) as conteoH,

COUNT(CASE WHEN P.género = 'F' THEN 0 END) as conteoM,

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Masculino,

CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Femenino,

CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS brecha_salarial -- Negativo a favor de la mujer y viceversa

FROM udechile.Remuneraciones AS R

FULL OUTER JOIN udechile.Ocupacion AS O ON R.T2_ido = O.ido

FULL OUTER JOIN udechile.Persona AS P ON R.T2_idp = P.idp

WHERE p.facultad = 'Facultad de Ciencias Físicas y Matemáticas' -- Imponemos busqueda en Beauchef
AND O.ido IN (
SELECT ido FROM udechile.Ocupacion 
FULL OUTER JOIN udechile.Remuneraciones as R ON R.T2_ido = O.ido

ORDER BY (R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna) ASC 
LIMIT (COUNT(*)/2 FROM udechile.Persona 
	  WHERE facultad = 'Facultad de Ciencias Físicas y Matemáticas')
);


``` 

```sql 
SELECT
  COUNT(CASE WHEN P.género = 'M' THEN 0 END) as conteoH,
  COUNT(CASE WHEN P.género = 'F' THEN 0 END) as conteoM,
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Masculino,
  CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Femenino,
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS brecha_salarial
FROM
  udechile.Persona AS P
  FULL OUTER JOIN udechile.Remuneraciones AS R ON R.T2_idp = P.idp

WHERE
  P.facultad = 'Facultad de Ciencias Físicas y Matemáticas' AND
  P.idp IN (
    SELECT idp
    FROM udechile.Persona as P
    FULL OUTER JOIN udechile.Remuneraciones as R ON R.T2_idp = P.idp
    
    ORDER BY (R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna) ASC
    LIMIT (SELECT COUNT(*)/2 FROM udechile.Persona WHERE facultad = 'Facultad de Ciencias Físicas y Matemáticas')
  );
```

```SQL 
SELECT COUNT(*)/2 FROM udechile.Persona WHERE facultad = 'Facultad de Ciencias Físicas y Matemáticas';
```


```sql 
SELECT
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Masculino,
  CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS Ingreso_Femenino,
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE 0 END) AS INT) AS brecha_salarial
FROM
  udechile.Persona AS P
  FULL OUTER JOIN udechile.Remuneraciones AS R ON R.T2_idp = P.idp

WHERE
  P.facultad = 'Facultad de Ciencias Físicas y Matemáticas' AND
  P.idp IN (
    SELECT idp
    FROM udechile.Persona as P
    FULL OUTER JOIN udechile.Remuneraciones as R ON R.T2_idp = P.idp
    
    ORDER BY (R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna) ASC
    LIMIT (SELECT COUNT(*)/2 FROM udechile.Persona WHERE facultad = 'Facultad de Ciencias Físicas y Matemáticas')
  );
```

```sql 
SELECT
  COUNT(CASE WHEN P.género = 'M' THEN 0 END) as conteoH,
  COUNT(CASE WHEN P.género = 'F' THEN 0 END) as conteoM,
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Masculino,
  CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Femenino,
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS brecha_salarial
FROM
  udechile.Persona AS P
  FULL OUTER JOIN udechile.Remuneraciones AS R ON R.T2_idp = P.idp

WHERE
  P.facultad = 'Facultad de Ciencias Físicas y Matemáticas' AND
  P.idp IS NOT NULL AND 
  P.idp NOT IN (
    SELECT idp, 
    R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna 
    FROM udechile.Remuneraciones as R
    FULL OUTER JOIN udechile.Remuneraciones as R ON R.T2_idp = P.idp

    WHERE facultad = 'Facultad de Ciencias Físicas y Matemáticas'
    GROUP BY idp 
    ORDER BY (R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna) ASC
    LIMIT (SELECT COUNT(*)/2 FROM udechile.Persona WHERE facultad = 'Facultad de Ciencias Físicas y Matemáticas')
  );
  ```
```sql 
SELECT CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Masculino,
  CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Femenino,
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS brecha_salarial, 
nombre 
FROM
  udechile.Persona AS P
  FULL OUTER JOIN udechile.Remuneraciones AS R ON R.T2_idp = P.idp

WHERE
  P.facultad = 'Facultad de Ciencias Físicas y Matemáticas'
AND 
R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna > 0
LIMIT 10; 
  
ORDER BY (R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna) ASC
    LIMIT (SELECT COUNT(*)/2 FROM udechile.Persona WHERE facultad = 'Facultad de Ciencias Físicas y Matemáticas');
```

```sql 

SELECT
  COUNT(CASE WHEN P.género = 'M' THEN 0 END) as conteoH,
  COUNT(CASE WHEN P.género = 'F' THEN 0 END) as conteoM,
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Masculino,
  CAST(AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS Ingreso_Femenino,
  CAST(AVG(CASE WHEN P.género = 'M' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) - AVG(CASE WHEN P.género = 'F' THEN R.Remuneración_bruta_mensualizada + R.Asignaciones_especiales + R.Horas_extra_diurna + R.Horas_extra_nocturna ELSE NULL END) AS INT) AS brecha_salarial
FROM
  udechile.Persona AS P
  FULL OUTER JOIN udechile.Remuneraciones AS R ON R.T2_idp = P.idp
LIMIT 20;

