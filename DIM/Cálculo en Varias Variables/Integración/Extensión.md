
Sea $A\subseteq\mathbb{R}^d$ un conjunto no necesariamente [[Conjuntos abiertos y cerrados|abierto o cerrado]], pero sí [[Conjuntos compactos|acotado]]. Sea $R$ un rectángulo cerrado que contiene completamente a $A$, esto es $A\subseteq R$. Dada una función $f$ definida sobre $A$, llamamos **extensión** de $f$ a $R$ (denotada por $\bar{f}$) a la función: 

$$ 
\bar{f}=\begin{cases} 
       f(x) & x\in A \\
      0 & x\in R\backslash A  
   \end{cases}
$$

![[Captura de Pantalla 2023-01-09 a la(s) 16.43.59.png|center]]

La siguiente imagen muestra una función $f$ definida sobre un conjunto con forma de *boomerang*, y su extensión $\bar{f}$ definida por cero a todo un cuadrado. 

La **utilidad** de la función extensión radica en que $\bar{f}$ tiene, teóricamente, la misma [[Integral en varias variables|integral]] que $f$, pero definida sobre un rectangulo cerrado donde se saben calcular [[Integral de Riemann|integrales de una variable]]. El problema se define en la [[Fronteras|frontera]] de $A$, ya que $\bar{f}$ será discontinua. Por lo tanto, para lograr que sea integrable se debe cumplir que el conjunto de discontinuidades sea de [[Medida nula|medida nula]] y que la [[Fronteras|frontera]] de $A$ también. 

## Teorema 

Sea $\bar{f}$ una [[Extensión|extensión]] de $f:A\subseteq\mathbb{R}^d\rightarrow\mathbb{R}$, con $A$ [[Conjuntos abiertos y cerrados|acotado]] y $R$ conteniendo a $A$. Entonces $\bar{f}$ será integrable sobre $R$ solamente si el **conjunto de discontinuidades de $f$ tiene [[Medida nula|medida cero]] y la [[Fronteras|frontera]] de $A$ también**. 