
Son aquellos arboles que garantizadamente el peor caso de inserción, eliminación y búsqueda es $O(log n)$.

Esto nace del caso ideal para una [[Busqueda binaria|busqueda binaria]], donde se quiere tener un árbol perfectamente balanceado. 

La inserción en un árbol AVL es de la misma forma que en los árboles [[Rotación|rotacionales]]. 

La idea de este árbol nace que existen múltiples formas de ordenar un árbol binario, por ejemplo, si se tiene un arreglo de $3$ elementos, existen $3!$ formas de poder formar el árbol. Cláramente la ideal es que el arbol quede lo más simétrico posible y con la menor altura. Por lo tanto, esta edición del árbol binario es una **mejora** al árbol binario.  

Para asegurar que un árbol realmente es AVL, se ocupa un cálculo matemático llamado *balance factor*. Sea $h_l$ la altura del arbol izquierdo y $h_r$ la altura del árbol derecho, entonces se debe cumplir lo siguiente: 

$$b_f = h_l - h_r = \lbrace -1, 0 ,1\rbrace$$ 

Este cálculo puede aplicarse para cualquier nodo, es decir, se debe verificar que cumpla para todo nodo.  Dependiendo de la [[Rotación|rotación]] a realizar, se pueden clasificar los distintos imbalances.  