Sea $A\subset\mathbb{R}^n$, su frontera, denotada por $Fr(A)$ es el conjunto de puntos $x\in\mathbb{R}^n$ que verifican: 

$$ B(x,r)\cap A\neq\emptyset\;\land\;B(x,r)\cap A^c\neq\emptyset$$

Basicamente, es como la *capa* o *manto* que define a un [[Conjuntos abiertos y cerrados|conjunto abierto y/o cerrado]]. 

![[Captura de Pantalla 2022-12-15 a la(s) 22.12.28.png|center]]


## Ejemplo 1: 

Por demostrar que la frontera de una bola abierta $B(x_0, r)$ es la esfera.  Es decir: 

$$S(x_0,r) \stackrel{!}{=} \lbrace x \in\mathbb{R}^n\; /\; ||x - x_0|| = r\rbrace$$ 
Sea un $\bar{x} \in S(x_0,r)$, notemos que la [[Bolas|bola]] al ser [[Conjuntos abiertos y cerrados|abierta]] admite a los valores $||x-x_0|| < r$, es decir, $\bar{x} \notin B(x_0,r)\implies\bar{x} \in B^c(x_0,r)$.

Asi, si trazamos una bola propia para $\bar{x}$ podemos llegar a lo siguiente: 

$$\bar{x} \in B(x, r_0) \cap B^c(x_o,r) \implies B(x, r_0) \cap B^c(x_o,r) \neq \emptyset $$ 
Por otro lado, sea un $\epsilon > 0$ y definamos: 

$$x_\epsilon = x_0 + (1-\epsilon)(\bar{x} - x_0)$$ 
Tenemos que: 

$$|| x - x_e || = || x - x_0 - (1-\epsilon)(x-x_0) ||$$ $$\iff || \bar{x} - x_e || = || \epsilon (\bar{x} - x_0) || $$ $$\iff || \bar{x} - x_e || = \epsilon ||(\bar{x} - x_0)|| $$ $$\implies || \bar{x} - x_e || = \epsilon r < r_0 \;\;\;\text{Para}\;\epsilon\;\text{pequeño}$$ 
Además: 

$$ ||x_0 - x_\epsilon|| = ||x_0 - x_0 - (1 - \epsilon)(\bar{x} - x_0)|| $$ $$ ||x_0 - x_\epsilon|| = ||(1-\epsilon)(\bar{x}-x_0)|| $$
$$ ||x_0 - x_\epsilon|| = (1-\epsilon)|| \bar{x} - x_0 || $$ 
$$ ||x_0 - x_\epsilon|| = (1-\epsilon)r < r $$ 
Por lo tanto, $x_\epsilon \in B(\bar{x}, r_0) \cap B(x_0,r)$ lo cual implica que $B(\bar{x},r_0) \cap B(x_0,r) \neq \emptyset$ 

Por último, si $\bar{x} \notin S(x_0,r)$ entonces existe una bola de radio pequeño que no intersecta a $B(x_o,r)$ o bien a su complemento. 

## Ejemplo 2

Consideremos $A = [0,1] \cap \mathbb{Q} \subset \mathbb{R}$. Entonces $Fr(A) = [0,1]$. Notemos que $A \subset Fr(A)$ pues cualquier intervalo de la forma $(x-\delta, x+\delta)$ donde $x\in A)$ y $\delta > 0$ intersecta a los conjuntos $A$ y $A^c$, pues los números racionales e irracionales son densos en $\mathbb{R}$. 

## Teorema 

Si tenemos un [[Conjuntos abiertos y cerrados|conjunto cerrado]] entonces su frontera es subconjunto del mismo conjunto, es decir: 

$$ A\;\;\text{cerrado}\iff Fr(A)\subset A$$ 
### Demostración 

$\implies |$  Tenemos que A es cerrado, es decir, $A^c$ es abierto. Consideremos $x \in Fr(A)$ y supongamos que $x \notin A \implies x \in A^c$. Por lo tanto, $\exists B(x,r_0) \subset A^c$. Por lo tanto, si intersectamos a la bola con A vamos a tener el conjunto vacio: 

$$ B(x,r_0) \cap A = \emptyset $$ 
Lo que contradice que $x\in Fr(A)$, entonces $x\in A$ 

$\impliedby |$ Supongamos que $Fr(A) \subset A$, entonces veremos que $A^c$ es abierto.  Si tomamos $x \in A^c$, entonces $x\notin Fr(A)$ por hipótesis. Así, existe $r_0 > 0$ tal que: 

$$ B(x, r_0) \cap A = \emptyset\enspace\enspace\lor\enspace\enspace B(x, r_0)\cap A^c = \emptyset$$ 
Como $x \in A^c$, entonces no puede ocurrir que $B(x, r_0) \cap A^c = \emptyset$. Por lo que tenemos: 

$$ B(x,r_0) \cap A = \emptyset $$ $$ \implies B(x,r_0) \subset A^c$$ Así, $A^c$ es abierto y $A$ es cerrado. 