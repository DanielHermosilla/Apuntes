
Son aquellos arboles que garantizadamente el peor caso de inserción, eliminación y búsqueda es $O(log n)$.

Esto nace del caso ideal para una [[Busqueda binaria|busqueda binaria]], donde se quiere tener un árbol perfectamente balanceado. 

La inserción en un árbol AVL es de la misma forma que en los árboles [[Rotación|rotacionales]]. 

La idea de este árbol nace que existen múltiples formas de ordenar un árbol binario, por ejemplo, si se tiene un arreglo de $3$ elementos, existen $3!$ formas de poder formar el árbol. Cláramente la ideal es que el arbol quede lo más simétrico posible y con la menor altura. Por lo tanto, esta edición del árbol binario es una **mejora** al árbol binario.  

Para asegurar que un árbol realmente es AVL, se ocupa un cálculo matemático llamado *balance factor*. Sea $h_l$ la altura del arbol izquierdo y $h_r$ la altura del árbol derecho, entonces se debe cumplir lo siguiente: 

$$b_f = h_l - h_r = \lbrace -1, 0 ,1\rbrace$$ 

Este cálculo puede aplicarse para cualquier nodo, es decir, se debe verificar que cumpla para todo nodo.  Dependiendo de la [[Rotación|rotación]] a realizar, se pueden clasificar los distintos imbalances. 

## Inserción 

Sea el siguiente arreglo a insertar: $[40,20,10,25,30,22,50]$. Por lo tanto, se tiene lo siguiente, insertándo normalmente se llega a lo siguiente en la tercera iteración:

![[IMG_DFBFB5BB086E-1.jpeg|center|350]]

Aquí es donde ocurre un problema, dado que el *balance factor* no entra en el rango de $\lbrace -1,0,1\rbrace$. Por lo tanto, se tiene que efectuar una rotación: 

![[IMG_9DFFA7B478F5-1.jpeg|center|350]]

Por consiguiente, se puede seguir agregando nodos al arbol hasta que se viole el *balance factor* en cualquiera de los nodos. Notemos que al agregar $30$ se tienen dos nodos imbalanceados: 

![[IMG_35B8E16F3BEF-1.jpeg|center|350]]

Ante la pregunta de qué nodo balancear dado dos imbalances consecutivos, se balancea el nodo de más abajo, es decir, el nodo $40$: 

![[IMG_79E09E60DDFC-1.jpeg|center|350]]


Nuevamente surge un problema al añadir el nodo $22$ con la raiz: 

![[IMG_E94B28BF0713-1.jpeg|center|350]]


Dado que el problema ocurre **en la raíz**, la rotación se hace en torno a los siguientes nodos: 

![[IMG_85E383720818-1.jpeg|center|350]]


Quedando el siguiente arbol: 

![[IMG_DE41DE9186BA-1.jpeg|center|500]]


Por último, insertando $50$ se llega a lo siguiente: 

![[IMG_13E90F8407FA-1.jpeg|center|550]]

Donde se tiene como el nodo problemático al $30$, entonces se hace la rotación en torno a los siguientes nodos:
![[IMG_52B73056BCC4-1.jpeg|center|]]