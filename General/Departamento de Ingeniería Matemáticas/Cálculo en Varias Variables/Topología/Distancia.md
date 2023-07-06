En Cálculo Diferencial e Integral habiamos definido la distancia en $R^2$ como la [[Distancia entre dos puntos|distancia entre dos puntos]] segun una [[Norma en varias variables|norma]] Euclidiana. Ahora, en este curso, se va a generalizar el concepto de distancia para cualquier dimension. Por lo tanto, sea $M$ un conjunto, se dice que la aplicación $d: M \times M\rightarrow [0, +\infty)$ es una distancia sobre $M$ si verifica que: 

1) $d(x,y) = 0 \iff x = y$
2) $d(x,y) = d(y,x)$
3) $d(x,z) \leq d(x,y) + d(y,z)$ 
4) $d(x,y) \geq 0$ 

Aca es donde hacemos el gran vínculo con la [[Topología|topología]] y las [[Norma en varias variables|normas]], ya que podemos verificar que las normas **cumplen con la definición de distancia**. Por eso mismo, **las normas nos van a representar distancia entre puntos**. Esto es importante, ya que de aquí podemos decir que **existen varias formas de definir distancia entre distintos puntos por la [[Equivalencias de Normas|equivalencia de normas]]**.

Por eso mismo, vamos a definir una distancia entre dos puntos por la siguiente equivalencia: 

$$ d(x,y) = ||x,y||$$ 

