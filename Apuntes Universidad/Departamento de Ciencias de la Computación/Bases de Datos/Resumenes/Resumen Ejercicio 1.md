
## Modelo Entidad-Relación 

Un modelo entidad relación es un modelo conceptual donde se grafican las relaciones entre las entidades. También se establecen los atributos entre ellas. Para poder hacer el modelo existen ciertas terminologías: 

>[!tip] Llaves 
>Conjunto de atributos mínimos cuyos valores identifican de forma unívoca a cada entidad del conjunto. Las **llaves primarias** son obligatorias para cada entidad 

Al ir relacionando atributos entre sí, hay que tener claro que **las relaciones no pueden tener atributos que sean llaves**. Sus atributos son, más bien, descriptivos. 

![[Captura de pantalla 2023-09-01 a la(s) 07.31.59.png|center]]

### Multiplicidad de las relaciones: 

Las relaciones pueden relacionar entidades según la cantidad de atributos que interactuan: 

![[Pasted image 20230901073335.png|center]]

### Jerarquías de clases 

Corresponde a una forma de particionar una entidad en una sub-entidades que heredan los atributos de la entidad original.

### Entidades débiles 

Para entender este concepto, es necesario definir algunos conceptos: 

>[!tip] Entidad débil 
>No puede existir por sí misma. Dependiente de una entidad fuerte para su existencia. Por ejemplo, considere una entidad "Habitación" que no puede existir sin una entidad "Hotel". Aquí, "Habitación" es una entidad débil y "Hotel" es una entidad fuerte.

>[!tip] Llave parcial 
>La **llave parcial** es un atributo (o conjunto de atributos) que es capaz de identificar univocamente a las entidades de una entidad débil, pero sólo dentro del contexto de una entidad fuerte específica. Es decir, si tienes varias habitaciones en diferentes hoteles, la llave parcial podría ser el número de habitación. Sin embargo, ese número por sí solo no es suficiente para identificar una habitación de forma única en toda la base de datos, pero lo es si lo combinamos con el identificador único del hotel al que pertenece.

Las entidades débiles se representan con una línea doble, como también las llaves parciales se representan con un destacado interlineado.

![[Pasted image 20230901074112.png|center|750]]

### Entidad virtual 

Cuando se quiere referir a un conjunto de atributos dentro de un contexto, es posible hacer referencias a todas estas mediante un bloque que contenga a cada una de estas. 

## Modelo relacional 

El modelo relacionar, originalmente introducido por Edgar. F. Codd, fue hecha para aplicar la matemática lógica a los modelos de bases de datos. 