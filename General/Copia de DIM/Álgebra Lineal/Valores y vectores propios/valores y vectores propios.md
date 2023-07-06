
Consideremos una [[transformaciones lineales|transformación lineal]]  $T:K^n \rightarrow K^n$, donde tenemos lo siguiente: 

$$ T(\begin{bmatrix}x_{1}\\ \vdots \\ x_{n} \end{bmatrix}) =A · \begin{bmatrix}x_{1}\\ \vdots \\ x_{n} \end{bmatrix} $$
Por lo tanto, nos preguntamos si $\exists$ una [[base]] de $K^n$ tal que 
$$M_{\beta \beta} = diag (\alpha_{1,}\alpha_{2,}\dots,\alpha_n ) = \begin{bmatrix} \alpha_{1} & \dots & \dots & 0 \\ 0 & \alpha_{2} & \dots & 0 \\ \vdots & \vdots & \vdots & \vdots \\  0 & \dots & \dots & \alpha_{n}\end{bmatrix} $$
Esto, es lo equivalente a tener: 
$$ \begin{equation}T(u_{1}) =  \alpha_{1} u_{1}\end{equation}$$
$$ T(u_{2)}= \alpha_{2}u_2$$
$$ \vdots $$
$$ T(u_{n)}= \alpha_{n}u_{n}$$
Para que exista esto, necesitamos que $\exists$ una [[base]] con tales [[vectores]] y [[escalares]].

Por lo tanto, podemos ponernos de acuerdo que es lo equivalente a preguntarnos: *¿Cuándo una matriz $A$ se puede descomponer de la siguiente forma?*

$$ A = PDP^{-1}\enspace\text{con D diagonal} $$

A partir de esto, salen las primeras nociones de **[[valor propio]]** y **[[vector propio]]**. 

## [[vector propio|Vector propio]]

Diremos que $x \in V$ es un **vector propio** de $L$ si: 

1. $x \neq 0$
2. $\exists \lambda \in K$ tal que $L(x) = \lambda x$ 

Y en este caso, el valor $\lambda$ se denomina **[[valor propio]]**. 

Por lo tanto, diremos que $x \in V$ es un [[vector propio]] de $A \in M_{nn}$ si es [[vector propio]] de la [[transformaciones lineales|transformación lineal]] dada por $L(x) = Ax$. Es decir: 

$$\exists \lambda \in K, Ax = \lambda x$$
Lo mismo a decir que la [[transformaciones lineales|transformación lineal]] nos da únicamente una [[matriz]] diagonal. Por ende, su [[matriz representante]] serían los [[valor propio|valores propios]] de tales [[combinaciones lineales]]. 


## Proposiciones importantes 

1. $\exists x$ solución no trivial del sistema $(A - \lambda I)x = 0$
Esta proposición es **fundamental**, pues nos dice como encontrar los [[valor propio|valores propios]] de una matriz. 

2. $Ker(A - \lambda I) \neq \lbrace0\rbrace$ 
3. $(A - \lambda I)$ no es invertible. 

#### Ejemplo

Sea A $\in M_{22} (R)$:

$$ A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} $$
Busquemos [[vectores]] tal que: 

$$ A \begin{bmatrix} x \\ y \end{bmatrix} = \alpha \begin{bmatrix} x \\ y \end{bmatrix} $$
Lo mismo que tener la siguiente [[matriz]]: 

$$\begin{bmatrix} x + y \\ x + y \end{bmatrix} = \begin{bmatrix} \alpha x \\ \alpha y \end{bmatrix}$$
Entonces, buscamos aquellos valores $\alpha$ tal que el sistema **no sea igual a 0**. 
$$\implies \alpha_{1}= 0, \space \alpha_{2} = 2$$
Entonces buscamos los vectores tal que se cumpla que: 
$$ A \begin{bmatrix} x \\ y \end{bmatrix} = 2 \begin{bmatrix} x \\ y \end{bmatrix} $$$$ A \begin{bmatrix} x \\ y \end{bmatrix} = 0 \begin{bmatrix} x \\ y \end{bmatrix} $$
$$\implies \beta = \lbrace \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \begin{bmatrix}   1 \\ -1 \end{bmatrix} \rbrace$$
--- 



