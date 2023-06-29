
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

Entonces, dado que se eliminan los elementos de la raiz, sea el siguiente árbol donde se quiere eliminar el $50$: 

![[IMG_63D6F5B87A6E-1.jpeg|center]]

Al sacar el $50$ fuera de la raiz, este debe ser inmediatamente reemplazado por el **último elemento**, en este caso, el $16$. 

![[IMG_54649A456EA3-1.jpeg|center]]

El $50$ estaría quedando por ahora, "fuera del array", pero en realidad se swapea con el $16$. Ahora, se tendría un árbol completo pero que viola el principio del orden, entonces se hacen comparaciones hacia abajo para rellenar los vacios: 

![[IMG_298631F87240-1.jpeg|center|650]]

La línea vértical roja que está en el array representa una división. De la izquierda en adelante representa el array perteneciente al árbol. El resto son los elementos que se van eliminando. Por lo tanto, el árbol final sería el siguiente: 

![[IMG_A45FE836DFFA-1.jpeg|center|650]]

Ahora, veamos el siguiente fenómeno que ocurre al seguir eliminando nodos: 

![[IMG_CC841D337B1C-1.jpeg|center]]

Los elementos que van sobrando son elementos **ordenados**. De hecho, esto introduce a lo que llegaría a ser el algoritmo de [[Heap sort]], cuyo algoritmo depende de la cantidad de elementos a ordenar y la altura del árbol, es decir, sería de orden $O(nlog(n))$ 

## Heapify 

Es una forma alternativa de crear un árbol *Heap*. Veamos el siguiente ejemplo de un árbol desordenado: 
