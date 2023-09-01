
## Modelo Entidad-Relación 

Un modelo entidad relación es un modelo conceptual donde se grafican las relaciones entre las entidades. También se establecen los atributos entre ellas. Para poder hacer el modelo existen ciertas terminologías: 

>[!tip] Llaves 
>Conjunto de atributos mínimos cuyos valores identifican de forma unívoca a cada entidad del conjunto. Las **llaves primarias** son obligatorias para cada entidad 

Al ir relacionando atributos entre sí, hay que tener claro que **las relaciones no pueden tener atributos que sean llaves**. Sus atributos son, más bien, descriptivos. 

![[Captura de pantalla 2023-09-01 a la(s) 07.31.59.png|center]]

### Multiplicidad de las relaciones: 

Las relaciones pueden relacionar entidades según la cantidad de atributos que interactuan: 

![[Pasted image 20230901073335.png|center|650]]

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

>[!tip] Modelo relacional
>El modelo relacional es un modelo de datos para bases de datos en el que la información se organiza en tablas (relaciones), y estas tablas se relacionan entre sí a través de claves. Cada modelo relacional cumple ciertas características: 
>
>- **Relaciones (Tablas)**: En el modelo relacional, una "relación" es esencialmente lo que comúnmente llamamos una "tabla". Cada relación está compuesta por tuplas (filas) y atributos (columnas).
>  $$$$
>  
>- **Atributos**: Los atributos son propiedades o características de la relación, y se pueden pensar como las columnas de una tabla.
>  $$$$
>    
>-  **Tuplas**: Una tupla es un conjunto de valores para un determinado conjunto de atributos y puede pensarse como una fila en una tabla.
>  $$$$
>  
>- **Clave Primaria**: Cada relación tiene una clave primaria. Es un conjunto de uno o más atributos que identifican de manera única a cada tupla dentro de la relación.
>  $$$$
>  
>- **Clave Externa**: Es un conjunto de atributos en una relación que hace referencia a la clave primaria de otra relación. Establece una relación entre las dos tablas.

Aquí también se define lo que es la **superllave**, lo que corresponde al conjunto de atributos de una relación que define únicamente una tupla. Por ende, las llaves siguen el siguiente esquema: 

![[Pasted image 20230901082404.png|center]]

### Dependencias funcionales 

Normalmente son datos que determinan funcionalmente los otros datos de una tabla. 

>[!tip] Dependencia funcional 
>Dada una relación y dos conjuntos de atributos $(X, Y)$, $X$ **determina funcionalmente** $Y$ si y solo si cada valor de $X$ en la relación tiene asociado un solo valor de $Y$

### Llaves foráneas 

Es otro tipo de restricción ocupada normalmente para la normalización. 

>[!tip] Llave foránea
>Un conjunto de atributos forma una llave foránea si esos atributos hacen referencia a la llave primaria de otra relación. El nombre de los atributos que se hace referencia pueden ser distintos, pero deben coincidir en la cantidad de columnas y los tipos de datos.

### Pasar de modelo entidad-relación a modelo relacional 

Normalmente se siguen ciertas reglas para hacer el traspaso: 

- Las llaves de las entidades juntas forman una **super llave** para una relación (en este caso *nombre* con *nombre*): 

![[Pasted image 20230901083807.png|center]]


- Para las subclases se puede hacer referencia a la llave primaria de la entidad principal y así identifica que hereda los atributos: 

![[Pasted image 20230901084054.png|center|500]]
![[Pasted image 20230901084027.png|center|500]]

- Por lo general, **no se hacen tablas para relaciones débiles**, tampoco en relaciones *$1$-algo*

## Formas normales 

### Primera forma normal 

Se debe evitar tener lista de atributos en sólo un campo. Un mal ejemplo sería el siguiente: 

![[Pasted image 20230901084521.png|center]]

Se normalizaría a la siguiente forma: 

![[Pasted image 20230901084548.png|center]]

### Segunda forma normal 

Todos los atributos **deben** depender **directamente** de la llave primaria. Un mal ejemplo sería el siguiente: 

![[Pasted image 20230901084750.png|center|250]]


Y su corrección sería: 

![[Pasted image 20230901084854.png|center|400]]

### Tercera forma normal 

No deben haber dependencias transitivas. Esto sería un mal ejemplo: 

![[Pasted image 20230901085040.png|center|600]]

Ya que $\text{Código}\implies\text{CodCargo}\;\land\;\text{CodCargo}\implies\text{NombreCargo}$

La corrección sería la siguiente: 

![[Pasted image 20230901085239.png|center|600]]

