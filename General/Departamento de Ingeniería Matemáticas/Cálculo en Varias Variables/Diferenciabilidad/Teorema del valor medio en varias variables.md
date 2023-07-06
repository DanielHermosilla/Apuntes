
Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ con A [[Conjuntos abiertos y cerrados|abierto]], $x,y\in A$ tal que el segmento que une a $x$ e $y$ está contenido en $A$. Si $f$ es [[Diferenciabilidad|diferenciable]] en cada punto $S\subset A$, entonces existe un $c\in S$ tal que:

$$f(x)-f(y) = Df(c) · (x,y)\;\text{(Producto punto)}$$ 
Es muy similar al [[Teorema del Valor Medio|teorema del valor medio]] en una variable pero se pasaría multiplicando el denominador. Es como una *variante*. 

## Demostración 

Se ocupa el [[Teorema del Valor Medio]] del curso de *Cálculo Diferencial e Integral*. Definamos  $g: \mathbb{R}\rightarrow\mathbb{R}$ con $g(t) = f(\gamma(t))$ donde $\gamma(t) = (1-t)x + ty\;\;t\in[0,1]$. 

El resultado sigue aplicando el [[Teorema del Valor Medio|teorema del Valor Medio en una variable]] a $g$ y usando [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Diferenciabilidad/Regla de la cadena|regla de la cadena]]. Entonces: 

$$\exists \bar{t}\;\text{tal que} \;\;g(t_1) - g(t_2) =  g'(\bar{t})(t_1-t_2)$$ 
Al [[Diferenciabilidad|derivar]] $g$ y ocupar [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Diferenciabilidad/Regla de la cadena|regla de la cadena]] estariamos obteniendo la función original con una composición de funciones, ya que: 

$$ g'(t) = Df(x + (y-t)t)(t_1-t_2), \;\;\forall t\in[0,1] $$ 