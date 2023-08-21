
Se basan en modelos que relacionan los datos a través de tablas. Nace de la componente matemática para relacionar tablas. Esto enlaza toda la teoría matemática de relaciones y álgebras al procesamiento de información.

- Relación: A cada tabla se le llama una relación, en las matemáticas relacionales se describe como: *Sea $r$ una relación tal que $r\subseteq D_1\times D_2\times\dots\times D_n$ 

- Esquema: Es la serie de tipos, contiene el nombre de la relación, atributos, tipos, restricciones. Por ejemplo; <font style="color:green">Cervezas</font>(<font style="color:blue">nombre: </font><font style="color:red">string</font>, <font style="color:blue">tipo: </font><font style="color:red">string</font>,  <font style="color:blue">grados: </font><font style="color:red">float</font>, <font style="color:blue">ciudad-origen: </font><font style="color:red">string</font>). 

- Instancia: Los datos que contiene un esquema. Son dinámicos (varían en el tiempo)

- Atributo: A cada columna se le llama atributo 

- Tupla: A cada fila se le llama tupla 

![[Captura de pantalla 2023-08-21 a la(s) 10.28.10.png|center]]

Una instancia de un esquema **es un [[conjunto]] de tuplas** para la relación de cada esquema. Vale decir; 

1. No hay orden en las filas 
2. No se pueden tener filas duplicadas 

Esto también trae otras implicancias, por ejemplo, las [[Llaves|llaves]] no pueden ser duplicados, etc. 

Existe el dato **Null** que está implementado en todos los tipos de datos. Esto representa que no existe o se conoce ese dato. 
#### Ejemplo 

|      Cervezas      |         |        |               |
|:------------------:| ------- | ------ | ------------- |
|       Nombre       | Tipo    | Grados | Ciudad Origen |
|                    |         |        |               |
|   Austral Lager    | Lager   | 4,6    | Punta Arenas  |
|                    |         |        |               |
|   Austral Yagan    | Ale     | 5      | Punta Arenas  |
|                    |         |        |               |
|  Austral Pale Ale  | Ale     | 5      | Valdivia      |
|                    |         |        |               |
| Kunstmann Torobayo | Ale     | 5,1    | Curacaví      |
|                    |         |        |               |
|      Kross 5       | Ale     | 7,2    | Curacaví      |
|                    |         |        |               |
|    Kross Golden    | Ale     | 5,3    | Curavaví      |
|                    |         |        |               |
|   Kross Pilsner    | Pilsner | 4,9    | Curacaví      |

En este ejemplo, la cerveza sería una **relación**, los nombres, tipos, grados, etc sería el **atributo** y las **tuplas** serían las filas, en este caso, Kunstmann Torobayo, Ale, 5,1, etc. 

Por lo tanto, para cada relación se le asigna su propio esquema donde se especifíca los **atributos** y los **tipos**: 

- <font style="color:green">Cervezas</font>(<font style="color:blue">nombre: </font><font style="color:red">string</font>, <font style="color:blue">tipo: </font><font style="color:red">string</font>,  <font style="color:blue">grados: </font><font style="color:red">float</font>, <font style="color:blue">ciudad-origen: </font><font style="color:red">string</font>)




