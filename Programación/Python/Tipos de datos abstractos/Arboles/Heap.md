
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