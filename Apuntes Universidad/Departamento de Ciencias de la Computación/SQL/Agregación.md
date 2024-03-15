
Existen operadores estadísticos en [[SQL]], que muchas veces depende de la implementación: 

```SQL
COUNT ([DISTINCT] A) 
SUM ([DISTINCT] A)
AVG ([DISTINCT] A)
MAX (A)
MIN (A)
```

Donde $A$ y $B$ son atributos de una [[Diseño de tablas|tabla]]. El **COUNT** no cuenta valores en blanco, se ignoran los nulos. 