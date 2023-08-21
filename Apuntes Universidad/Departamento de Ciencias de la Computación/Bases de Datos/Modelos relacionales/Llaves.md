
Un conjunto de atributos cuyos valores identifican de manera unívoca a cada entidad del conjunto. 

## Llaves primarias 

Aquellas que son obligatorias para cada entidad

![[Captura de pantalla 2023-08-14 a la(s) 15.46.35.png|center]]

## Llaves binarias 

Dos entidades son relacionadas 

![[Captura de pantalla 2023-08-14 a la(s) 15.47.12.png|center]]

Notemos que existen distintas multiplicidades de relacionales para las llaves binarias:

![[Captura de pantalla 2023-08-14 a la(s) 15.48.17.png|center]]

## Superllave 

Conjunto de atributos de una relación que define únicamente cada tupla. A partir de esto, se puede elegir una **llave candidata**, vale decir, una superllave minimal o primaria. 

#### Ejemplo 

Se tiene el siguiente [[Modelos Relacionales|modelo relacional]]: 

$$\text{Alumnos(RUT, Id-U, Nombre, Ap, Dirección, Teléfono)}$$

Por lo tanto, una llave sería $\lbrace\text{RUT}\rbrace,\;\lbrace\text{Id-U}\rbrace$. No obstante, una superllave sería: 

$$\lbrace\text{RUT,Id-U,Nombre,Ap,Dirección,K}\rbrace$$


## Llaves foráneas 

Un conjunto de atributos forma una llave foránea si esos
atributos hacen referencia a la llave primaria de otra relación. 

#### Ejemplo 

![[Pasted image 20230821105233.png|center|500]]

