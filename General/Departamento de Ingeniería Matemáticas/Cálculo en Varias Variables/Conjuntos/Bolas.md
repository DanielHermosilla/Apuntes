
Al trabajar en múltiple variables ya no podremos modelar nuestros conjuntos mediante una recta en el plano. Por eso mismo, se introduce el concepto de bola, donde podremos caracterizar nuestros conjuntos a través de éstas. 

## Bola abierta

Sea $(\mathbb{R}^n, ||·||)$ el [[Espacios vectoriales|espacio vectorial]] [[Norma en varias variables|normado]]. Consideramos $x_0 \in \mathbb{R}^n$ y $r>0$ fijos. Definimos la bola abierta de centro $x_0$ y radio $r$ al siguiente conjunto: 

$$ B(x_0, r) = \lbrace x\in\mathbb{R}^n / \;||x-x_0|| < r\rbrace $$ 
Es decir, los elementos que caben dentro de una bola tal que son **menor estrictos** que el radio. Al tener el menor estricto no consideramos los puntos que bordean al conjunto. 

![[Captura de Pantalla 2022-12-15 a la(s) 18.28.37.png|center]]


## Bola cerrada 

Análogamente se define a la bola cerrada de centro $x_0$ y radio $r>0$ como lo siguiente: 

$$\bar{B}(x_0, r) = \lbrace x\in\mathbb{R}^n / \; ||x-x_0|| \leq r\rbrace$$

Aquí hay un **menor o igual**, es decir, consideramos a los puntos que están en el borde de la bola. 

![[Captura de Pantalla 2022-12-15 a la(s) 18.31.43.png|center]]


Notemos que las gráficas van cambiando a medida que ocupamos distintas normas. Por ejemplo, la bola de la norma 1 llegaría a ser un romboide. 