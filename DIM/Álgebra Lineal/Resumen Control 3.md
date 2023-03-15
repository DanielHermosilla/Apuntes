
El control se basa principalmente en [[valores y vectores propios]], saber diagonalizar y determinar [[polinomio característico|polinomios característicos]]. 

## Valores y vectores propios 

Basicamente se obtienen al encontrar las raíces del [[polinomio característico|polinomio característico]] de la [[matriz]] con sus diagonales restadas por $\alpha$. 

$$\begin{bmatrix} a - \alpha & b & c \\ d & e - \alpha & f \\ g & h & j - \alpha \end{bmatrix} $$ 
Elegimos una fila o columna para ocupar como pivote y calculamos el [[polinomio característico]]. Sus raices nos determinaran los valores propios.  

### Cálculo de vectores propios 

Cuando uno ya obtiene los [[valor propio|valores propios]] puede empezar a calcular la **[[Base|base]]  de [[vector propio|vectores propios]].**  Hacer esto es trivial, pues consiste en reemplazar $\alpha$ por los [[valor propio|valores propios]] encontrados y luego calcular el [[núcleo]]. 

Supongamos que $\alpha = 3$ es raiz: 

$$\begin{bmatrix} a - 3 & b & c &| \enspace 0 \enspace\\ d & e - 3 & f&| \enspace 0 \enspace \\ g & h & j - 3 &| \enspace 0 \enspace\end{bmatrix} $$

El grado algebraíco del [[polinomio característico]] nos dirá la [[multiplicidad algebraica]] y la dimensión del [[subespacios propios]] nos dirá la [[multiplicidad geométrica]]. 

## Matriz diagonalizable 

Diremos que una [[matriz diagonalizable|matriz]] es diagonalizable si admite una [[Base|base]] de su misma dimensión de vectores propios. Por lo tanto, tenemos nuestra primera **propiedad importante**: 

$$\text{Si}\enspace\forall\alpha\enspace\text{Multiplicidad geométrica}_{\alpha_i} = \text{Multiplicidad algebraica}_{\alpha_i}\implies A\enspace\text{es diagonalizable} $$ 
## Ortogonalidad 

Diremos que dos [[vectores]] son **ortogonales** cuando su [[producto escalar]] es 0. Esto significa que ambos [[vectores]] son perpendiculares. 

## Ortonormalidad 

Diremos que dos [[vectores]] son **ortonormales** cuando son **ortogonales** y su [[norma]] es 1. 

### Proyección ortogonal 

Por lo tanto, diremos que la [[proyecciones ortogonales]] se define de la siguiente forma; siendo $\lbrace u_1,\dots,u_k\rbrace$ una [[Base|base]] ortogonal. 

$$P(x) =\sum^{k}_{i=1}\langle x,u_i\rangle u_i $$ 
## Método de Gram-Schmidt

Un método para formar una [[Base|base]] cualquiera a una **ortonormal**. Se basa bajo la siguiente recursión, con $\lbrace e_1,\dots,e_k\rbrace$ los [[vectores]] originales, $\lbrace w_1,\dots,w_k\rbrace$ las [[proyecciones ortogonales]] y $\lbrace u_1,\dots,u_k\rbrace$ los [[vectores]] de la base **ortonormal**. Por lo tanto, entendiendo todo esto, se define la siguiente recursión: 


$$ w_n =e_n - \langle e_n,u_1 \rangle u_1 - \langle e_n,u_2 \rangle u_2 - \dots - \langle e_n,u_{n-1} \rangle u_{n-1} $$

Luego, se normaliza $w_n$: 

$$ u_n = \frac{w_n}{\|w_n\|} $$

## Matriz representante de vectores propios

Sabemos que si una [[matriz diagonalizable|matriz]] es diagonalizable podemos encontrar su [[matrices representantes de vectores propios|matriz representante de vectores propios]]. De tal forma, podemos reescribir cualquier [[matriz diagonalizable]] como: 

$$ A = PDP^{-1}$$ 
Donde $P$ es una matriz cuyas columnas son los [[vector propio|vectores propios]] ortonormales de la [[matriz]] A y $D$ es la [[matriz diagonalizable]] con los [[valor propio|valores propios]] correspondientes: 

$$D = \begin{bmatrix} \alpha_1 & 0 & 0 & 0 &\dots & 0  \\ 0 & \alpha_2 & 0 & 0 & \dots & 0 \\ \vdots&\vdots&\vdots &\vdots&\vdots&\vdots \\ \dots & \dots & \dots & \dots & \dots & \alpha_n \end{bmatrix} 
$$
### Matriz simétrica 

Notemos que en las matrices simétricas también se cumplen que: 

$$ A = PDP^T $$ 
## Propiedades importantes 

Si la [[matriz]] es triangular o diagonal: 
1. El [[determinante]] es la multiplicación de sus elementos diagonales. 
2. Los [[valor propio|valores propios]] son los elementos de la diagonal 

Si la [[matriz]] es simétrica: 
1. Siempre son [[matriz diagonalizable|diagonalizables]]. 
2. Se pueden construir una base ortonormal de vectores propios. 
3. Los [[vector propio|vectores propios]] asociados a [[valor propio|valores propios]] distintos son ortogonales. 
4. Los [[valor propio|valores propios]] siempre son reales. 

Se puede ocupar el [[teorema del núcleo-imagen]] para tener la dimensión de $\ker (A-\lambda I)$. Recordar que el [[rango]] es la dimensión de la imagen.  