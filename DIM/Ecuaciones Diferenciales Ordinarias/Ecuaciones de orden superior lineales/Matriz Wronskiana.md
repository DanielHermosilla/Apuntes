Se define como la siguiente [[matriz]]:

$$\begin{bmatrix} y_1(x) & y_2(x) \\ y_1'(x) & y_2'(x)\end{bmatrix}$$ 
Los determinantes son lineales por filas o por columnas de una [[matriz]] **Wronskiana**, por lo tanto, se puede sacar del [[determinante]] un factor común. 

### Definición 

Se dice que $y_1, y_2\in\mathbb{C}^1(I)$ son [[dependencia|linealmente independientes]] si $\alpha y_1(x) + \beta y_2(x) = 0, \forall x\in I$, entonces $\alpha = \beta = 0$ .

Esto es importante, ya que si se tiene:

$$\alpha y_1(x) + \beta y_2(x) = 0$$

Al derivar se obtiene: 

$$\alpha y_1'(x) + \beta y_2'(x) = 0$$

Por lo tanto, la matriz wronskiana nos asegura que es invertible y por lo tanto, $\alpha=\beta=0$: 

$$\begin{bmatrix}y_1(x) & y_2(x) \\ y_1'(x) & y_2'(x)
\end{bmatrix}
\begin{bmatrix}
\alpha \\\beta\end{bmatrix}=\begin{bmatrix}0 \\0\end{bmatrix}$$ 