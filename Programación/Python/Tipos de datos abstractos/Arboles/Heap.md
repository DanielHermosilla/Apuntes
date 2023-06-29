
El uso del heap nace principalmente de la necesidad de poder representar un array en forma de un [[Busqueda binaria|arbol binario]].  La teoría del Heap ordena los arboles a partir del nivel,  por nivel, como lo muestra las siguientes imagenes: 

![[IMG_BBDF64BC556F-1.jpeg|center|500]]


![[IMG_0FBED61D9233-1.jpeg|center|500]]

![[IMG_D515F37E3507-1.jpeg|center|500]]


Todas estas representaciones son, en efecto, una ordenación por Heap. De hecho, es posible modelarlo matemáticamente para un nodo en el índice $i$.  

Dado un nodo de índice $i$ se cumple que: 

- Su hijo izquierdo está en $2i$ 
- Su hijo derecho está en $2i + 1$ 
- Su padre está en $\lfloor\frac{i}{2}\rfloor$ 

Además, si se tiene un arbol completo, su áltura está garantizada de ser $\log(n)$. En el caso de Heap, se ocupará en arboles completos. 

Por consiguiente se define *max heap* y *min heap*, donde el primer arbol está ordenado en orden ascendiente, es decir, como un árbol de busqueda original y en *min heap* se ordena de la forma contraria. 

## Inserción 

La inserción ocurre en el **nodo que falta para tener el árbol completo**. Para ver esto, primero se verá un ejemplo de una inserción **errónea** y de ahí de una inserción correcta. La siguiente sería una inserción errónea, tratando de insertar $60$ al árbol:

![[IMG_1B17493D6DFE-1.jpeg|center]]

Aquí se violaría el principio de ser un árbol completo, entonces no hay forma de arreglarlo. Sin embargo, la inserción correcta sería **primero insertar desde la hoja correspondiente a aquella que llene el árbol** 

![[IMG_EFB3AF35A760-1.jpeg|center]]

De ahí hacer comparaciones con los padres para ir *swapeando* hasta llegar a su lugar correspondiente

![[IMG_A2CADD2E9C9B-1.jpeg|center]]

Eso sería una inserción exitosa, y de hecho, es la forma de insertar un elemento. Notemos que en el peor de los casos recorre a todos sus padres, vale decir, sería del orden $O(log(n))$. No obstante, en el mejor de los casos se tiene que la inserción es ideal y el nodo es menor que su padre, siendo de orden $O(1)$. 

## Eliminación 

La eliminación es lo contrario a la inserción, en este caso, **para todo elemento** se elimina por la **raiz**. Es contraintuitivo pero hace sentido para no violar los principios de *Heap*. 

