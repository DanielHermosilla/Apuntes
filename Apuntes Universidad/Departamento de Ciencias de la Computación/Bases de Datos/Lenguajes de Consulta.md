
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

|  **Marca**  | **Nombre** | **Tipo** | **Grados** | **Origen** | **mL** | **Precio** |
|:-----------:|:----------:|:--------:|:----------:| ---------- |:------:|:----------:|
| Austral |  Lager   | Lager  |    $4.6$        | Punta Arenas           |   $330$     |    $2000$        |
| Austral |  Yagan   | Ale  | $5.0$           |  Punta Arenas          |  $330$      |  $2400$          |
|  Raco   |  Amber   | Ale  |     $4.5$       |      Maipo      |   $500$     |         $3000$   |


La operación aca sería: 

$$\pi_{\text{tipo}}(\sigma_{\text{gradoss}}> 4.8(\text{Cerveza}))$$

Lo que retornaría únicamente la tupla $(\text{Tipo},\text{Lager})$. 

Otra consulta sería *¿Qué marcas de bebida son de Maipo?*. Aquí la operación sería: 

$$\pi_{\text{marca}}(\sigma_{\text{Origen=Maipo}}(\text{Cerveza}))\;\cup\;\pi_{\text{marca}}(\sigma_{\text{origen=Maipo}}(\text{Vino}))$$

Notemos que el álgebra relacionar es **equivalente** a la **lógica de $1^{er}$ orden**. Vale decir, todas las consultas de relaciones es equivalente a las consultas matemáticas que involucran el $\exists,\;\forall,\;\text{etc}$. 

>[!note] Join (Reuniones)
>Se escribe como $R_1\Join R_2$ y es equivalente a $\sigma_{\text{condición}}(R_1\times R_2)$. 
>
>En rigor, no es un operador, porque está cubierto por los operadores de producto y selección. Pero *join* es tán común que se abrevia así. 

>[!note] División 
>Su consulta es $R\divsymbol\pi_B(R)$, y se define como: 
>
>$$\pi_A(R)-\pi_A(\pi_A(R)\times\pi_B(R)-R)$$



