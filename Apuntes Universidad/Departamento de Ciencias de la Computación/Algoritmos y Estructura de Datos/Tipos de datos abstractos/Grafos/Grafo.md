
Consiste en un conjunto $V$ de vértices o nodos y un conjunto $E$ de arcos. El número de vértices se denota por $n$ y el número de arcos como $m$. Se dice que un grafo es **no dirigido** cuando no tiene dirección asociada: 

![[grafo-no-dirigido.png|center|350]]


En el ejemplo anterior, se podría describir el conjunto de vértices y arcos como: 

$$

\begin{align}

V &=\{v_1,v_2,v_3,v_4,v_5\}\\

E &=\{ \{v_1,v_2\},\{v_1,v_3\},\{v_1,v_5\},\{v_2,v_3\},\{v_3,v_4\},\{v_4,v_5\} \}

\end{align}

$$


## Representación de los grafos 

Los grafos tienen distintas formas de ser representadas en la memoria:

- **Matriz de adyacencia**: suele ser la forma más común de representar a los grafos. Consiste en una matriz $A$ donde $A[i,j]=1$ si hay un arco que conecta $v_i$ con $v_j$. Los grandes problemas de esto es que se necesitan $\Theta(n^2)$ bits de memoria y, por el otro lado, se requiere tiempo $\Theta(n)$ para encontrar la lista de vecinos de un vértice dado. 

- **Lista de adyacencia**: Consiste en almacenar para cada nodo la lista de nodos adyacentes a él: 

$$

\begin{align}

\text{vecinos}[v_1] &= [v_2]\\

\text{vecinos}[v_2] &= [v_2, v_3]\\

\text{vecinos}[v_3] &= [v_1, v_4]\\

\text{vecinos}[v_4] &= [v_3]

\end{align}

$$

Utiliza espacio $\Theta(m)$ pero no describe como son los arcos. 

## Caminos y ciclos 

Se dice que un camino es una secuencia de arcos. Por ejemplo, lo siguiente correspondería el camino de $v_2$ a $v_5$: 

![[camino.png|center|350]]


Se denominará camino *simple* aquel que no es cerrado, vale decir, no se repiten vértices. Por lo tanto, los que no tienen ciclos se les dicen *acíclicos*. Por el otro lado se dice *conexo* si para todo par de vértices existe un camino que los une. Un ejemplo de algo no conexo sería un grafo compuesto por varias islas. 

Si nos fijamos, un árbol es *conexo* y *acíclico*, de lo contrario se llamarían *spanning trees*: 

![[arbol.png|center|350]]


## Propiedades de los árboles 

De la relación *árbol-grafo* se desprende: 

- Todo árbol con $n$ nodos tiene $n-1$ arcos. 
- Si se agrega un arco a un árbol, se crea un único ciclo. 

