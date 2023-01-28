Una matriz es una **tabla de doble entrada** que se ordenan acorde sus filas y columnas. 

$$ \begin{equation}
		\begin{bmatrix}
			a & b & c\\ 
			d & e & f
		\end{bmatrix}
\end{equation}
		$$$$\text{Matriz de 2x3}$$ Podemos referirnos a los coeficientes de las matrices al enumerar cada componente de la fila y columna. 

$$ a_{ij} \in \kappa \space  \forall i = 1, \dots, m, j = 1, \dots, n $$
Las **columnas** equivalen a los arreglos **verticales** y las **filas** a los arreglos **horizontales**. 


### Igualdad de matrices 

Podemos decir que dos matrices son iguales cuando tenemos que todos sus coeficientes son iguales y las dimensiones son idénticas. 

### Suma de matrices 

La suma de matrices consiste en sumar coeficiente por coeficiente. Tienen estructura de grupo Abeliano: 

$$\begin{bmatrix}
			1 & 2 & 3\\ 
			0 & -1 & -2
		\end{bmatrix} + \begin{bmatrix} 0 & -1 & 2 \\ 3&  1 &2 \end{bmatrix} = \begin{bmatrix} 1 & 1 & 5 \\ 3 & 0 & 0 \end{bmatrix}$$ 
El *neutro aditivo* vendría a ser la matriz con coeficientes igual a cero. 

### Producto de matrices 

Consideremos una matriz $A = [a_{ij}]_{m\times n}$ y $B = [a_{ij}]_{n\times p}$. Por lo tanto, las coordenadas de la matriz $C = AB$ están dadas por: 

$$ c_{ij} = \sum^{n}_{k = 1} a_{ik}b_{kj} $$
#definición 