
Recordemos que una sucesión en un [[Espacios vectoriales|espacio vectorial]] $E$ es una [[función]] $x:\mathbb{N}\rightarrow V$ que a cada $n \in \mathbb{N}$ le asocia $x(n) = x_n$. A esto le denotamos por $x = (X_{n}) \;\; n \in \mathbb{N}$ 

## Convergencia 

Diremos que una sucesión $(X_n)$ en un [[Espacios vectoriales|espacio vectorial]] [[Norma en varias variables|normado]] converge a un [[vectores|vector]] o elemento $x_0 \in E$ si para toda [[Bolas|bola abierta]] $B(x_0, \epsilon)$ existe un $n_0 \in \mathbb{N}$ tal que $x_n \in B(x_0, \epsilon)$ para todo $n \geq n_0$. Es decir: 

$$\forall \epsilon > 0 \;\;\exists n_0 \in \mathbb{N}\;\;\text{tal que si}\;\; n\geq n_0 \implies ||x_n - \bar{x}|| < \epsilon$$ 
Esta definición es muy parecida a la definición de convergencia en $\mathbb{R}^1$, pues ahí el concepto de [[Norma en varias variables|norma]] aplica para la norma 1, es decir, el valor absoluto de un número. 

Lo anterior lo denotaremos como $\lim_{n \rightarrow\infty} X_n = X_0$ 

### Observaciones 

1) Al igual que en $\mathbb{R}^1$, si el límite existe entonces es único. 
2) $\lim_{n\rightarrow\infty} X_n = X_0 \iff \lim_{n\rightarrow\infty} ||X_n - X_0|| = 0$ 
3) También existe la linealidad, es decir, álgebra de límites y multiplicaciones por [[escalares]]: 
$$ \alpha x_n + \beta y_n \rightarrow \alpha x_0 + \beta y_0 $$ 4) En $\mathbb{R}^n$ diremos que una sucesión de [[vectores]]: $x_k = (x_{k}^1, x_{k}^2, x_{k}^3, \dots, x_{k}^n)$ converge al vector $x = (x^1, x^2, x^3, \dots, x^n$) si y sólo si cada sucesión $(x_{k})^j$ converge a $x^j$ en $\mathbb{R}$. 

Notemos también que **toda sucesión convergente es [[Conjuntos compactos|acotada]]**. Esto se demuestra facilmente; sea $x_n$ un [[vectores|vector]] perteneciente a un [[Conjuntos compactos|conjunto acotado]], entonces $\forall x_i \in x_n\;\;\text{se cumple que}\;\;\exists M\;\;\text{tal que}\;\;||x_i|| \leq M$. Por lo tanto, basta definir a $M$ como la máxima [[Norma en varias variables|norma]] de cada componente. 


![[Captura de Pantalla 2022-12-18 a la(s) 18.10.26.png|center]]

Por último notar que al igual que en $\mathbb{R}^1$, en varias variables también se cumple el [[Teorema Bolzano-Weierstrass|teorema de Bolzano-Weierstrass]]. La demostración se realizar al aplicar el teorema en cada [[coordenadas|coordenada]] de un [[vectores|vector]]. 

## Teorema: Caracterización de [[Conjuntos abiertos y cerrados|conjuntos cerrados]]

$$ A\;\;\text{es cerrado}\;\;\iff\;\;\text{para cualquier sucesión}\;\;(x_n)\subset A\;\;\text{tal que}\;\;x_n\rightarrow x\;\;\text{se tiene que}\;\;x\in A$$ 
