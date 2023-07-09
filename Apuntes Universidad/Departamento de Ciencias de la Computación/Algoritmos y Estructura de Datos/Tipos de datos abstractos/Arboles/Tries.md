
En el apunte se ocupa para guardar una secuencia de *bits*, pero en realidad es usado comúnmente en diccionarios que no son ordenables, como lo serían los bits o [[Strings|strings]]. Por ejemplo, sea el siguiente diccionario: 

![[Inside code - Trie data structure - Inside code [qA8l8TAMyig - 871x490 - 0m20s].png|center]]

Lo que haría el algoritmo de *trie* es ordenar cada string por su pre-fijo: 

![[Inside code - Trie data structure - Inside code [qA8l8TAMyig - 871x490 - 0m53s].png|center ]]

Esto es extremadamente util en el caso que se tengan llaves que no sean ordenables. Esto se ocupa, por ejemplo, en los buscadores donde se llenan frases: 

![[Inside code - Trie data structure - Inside code [qA8l8TAMyig - 871x490 - 1m48s].png|center ]]


## Implementación 

En su implementación es necesario que **exista un booleano** en cada nodo, indicando si una palabra termina o no. Existen cuatro formas de implementarlos, con árboles, hash tables, [[Listas enlazadas|listas enlazadas]] y arrays. La forma de implementarla depende si se quiere priorizar el almacenaje o eficiencia. 

## Insertar 

Para insertar es muy simple, se va recorriendo el conjunto de datos y por cada nodo se pregunta si existe la siguiente letra, de no ser cierto, se crea un nuevo nodo con la letra. Al finalizar la palabra, se pone *True* al booleano que marca que se termina la palabra. Esto tiene complejidad $O(m)$ con $m$ siendo el largo de la palabra.

