
Es la forma formal de comunicar entre el cliente y el software de [[Bases de Datos|base de datos]]. Sea una tabla relacional $R(A,B,C,D)$, se definen ciertas operaciones. 

Las más fundamentales son las proyecciones $\sigma$ y $\pi$, que son **operadores para seleccionar componentes de la tabla de Base de Datos**. 

## Algebra relacional 

Por lo tanto, se define dentro del álgebra relacional los operadores: 

- Intersección $(\cap)$ 
- Unión $(\cup)$
- Resta $(-)$

Y todo esto se le suman los operadores de proyección $\sigma$ para las filas y $\pi$ para las columnas. Al juntar esto con un [[Producto cartesiano|producto cartesiano]] se tienen los operadores relacionales. 

>[!tip] Selección 
>Sea $R$ una relación (tabla), entonces $\sigma_{\text{condición}}(R)$ es una **nueva relación** que deja solo las tuplas que satisfacen la relación. 
>
>Solo se permiten los siguientes operadores: $=,\leq,\geq,<,\neq$, se puede combinar con las condiciones booleanas $\land$ (*and*) y $\lor$ (or). 

>[!tip] Proyección 
>Selecciona un conjunto de atributos a través de $\pi_{\text{condición}}(R)$. Básicamente sirve para **seleccionar columnas** dentro de la tabla. 

Dentro de selección y proyección está permitido hacer combinaciones. Por ejemplo, si se quiere saber que tipo de cerveza son más fuertes que $4.8$: 

|       | **Marca** | **Nombre** | **Tipo** | **Grados** | **Origen** | **mL** | **Precio** |
|:-----:|:---------:|:----------:|:--------:|:----------:| ---------- |:------:|:----------:|
| **Austral** |  $(4,3)$  |  $(5,1)$   | $(6,2)$  |            |            |        |            |
| **Austral** |  $(2,1)$  |  $(8,4)$   | $(3,6)$  |            |            |        |            |
| **Raco** |  $(3,0)$  |  $(9,6)$   | $(2,8)$  |            |            |        |            |