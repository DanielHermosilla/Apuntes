
Al tener definida las [[Bolas|bolas]] podemos empezar a caracterizar conjuntos en varias variables, algo en lo que se basa principalmente la [[Topología|topología]]. 

## Conjunto abierto 

Un subconjunto de $A$ de $\mathbb{R}^n$ se dice abierto si para cualquier elemento $x\in A$ existe una [[Bolas|bola abierta]] tal que $B(x,r)\subset A$. 

## Conjunto cerrado 

Un conjunto $A$ de $\mathbb{R}^n$ se dice cerrado si su complemento $A^c$ es abierto. 

## Clopen 

Son aquellos conjuntos que son abiertos y cerrados, como el caso de $\mathbb{R}^n$ y $\emptyset$.  También está el caso de cuando no son ni abiertos ni cerrados. 

## Ejemplos importantes

Estos ejemplos sirven para entender de mejor forma como se comportan los distintos tipos de [[Bolas|bolas]]: 

### Bolas abiertas: 

Toda bola abierta $B(x_0, r)$ es un conjunto abierto. 

En efecto, sea un $\bar{x}\in B(x_0,r)$ arbitrario de la bola, entonces, si demostramos que cada elemento  se le puede trazar una bola que esté dentro de $B(x_0,r)$ ganamos. Es decir, por demostrar que:


$$ \forall\bar{x}\in B(x_0,r)\enspace\exists B(\bar{x},\bar{r})\subset B(x_0,r) $$

Antes que nada, notar que para que esto ocurra, se debe cumplir que $\bar{r} < r$. Podemos definir a $\bar{r}$ bajo el siguiente análisis: la resta del radio original con la [[Distancia|distancia]] entre ambos puntos, es decir:

$$ \bar{r} = r - ||\bar{x} - x_0|| $$

Este sería el **máximo radio** posible, aunque estaría el caso donde habrían puntos externos al conjunto $B(x_0,r)$. Por eso mismo, consideramos a la mitad de $\bar{r}$. 

![[Captura de Pantalla 2022-12-15 a la(s) 18.55.13.png]]

Por ende, nuestra bola, que llegaría a ser subconjunto de $B(x_0,r)$ está definida por $B(\bar{x},\frac{\bar{r}}{2})$, ya que $r = \bar{r} - ||\bar{x} - x_0||\implies r >\frac{\bar{r}}{2} - ||\bar{x} - x_0||$ 

Tomando lo anterior, definamos un elemento $y \in B(\bar{x}, \frac{\bar{r}}{2} )$. Si probamos que todo $y$ pertenece a $B(x_0,r)$ ganamos. 

Notemos que: 

$$ ||y-x_0|| = ||y-\bar{x} + \bar{x} - x_0||$$
$$\implies ||y-\bar{x}+\bar{x}-x_0|| \leq ||y-\bar{x}|| + ||\bar{x} - x_0||$$ $$\implies ||y-x_0|| <\frac{r_0}{2} + ||\bar{x} - x_0|| $$ 
Recordemos que $r_0 = r - ||\bar{x} - x_0||$, entonces reemplazando: 

$$\iff ||y-x_0|| < \frac{r - ||\bar{x} - x_0||}{2} + ||\bar{x} - x_0||$$ $$\iff ||y - x_0|| < \frac{r}{2} + \frac{||\bar{x} - x_0||}{2} $$ 
Notemos que $\bar{x}$ al estar definida dentro de una bola abierta, la expresión $\frac{||\bar{x} - x_0||}{2}$ se mueve entre $(0,\frac{r}{2})$, entonces, por mayoración: 


 $$\iff ||y - x_0|| < \frac{r}{2} + \frac{||\bar{x} - x_0||}{2} < r $$
 $$\implies ||y - x_0|| < r $$ 
 Es decir, un punto cualquiera dentro de la bola abierta contenida en $B(x_0,r)$ pertenece, efectivamente, a la bola más grande. Esto se debe a que la [[Distancia|distancia]] entre el punto y el centro de la bola es menor **estricto** que su radio. Por lo tanto, queda demostrado que las bolas abiertas son conjuntos abiertos. 

### Bolas cerradas

Por demostrar que todas las bolas cerradas son un conjunto cerrado.

Si nos acordamos de la definición de conjunto cerrado, son aquellos donde su complemento son abiertos. Por lo tanto, el complemento de una bola $A = \bar{B}(x,r)$  llegaría a ser $A^c = \mathbb{R} \setminus\lbrace ||x-x_0||>r\rbrace$. Entonces, por demostrar que $A^c$ es un conjunto abierto. 

Sea un $y \in A^c$ y también definimos su radio en torno al centro $x_0$ como la [[Distancia|distancia]] de $x_0$ con $y$. Entonces, veamos lo siguiente: 

![[Captura de Pantalla 2022-12-15 a la(s) 21.16.21.png|center]]

Claramente $r_0$ se define como $r_0 = ||y - x_0|| - r$. Entonces, si $r_0$ siempre llegase a ser mayor estricto que 0 para cualquier punto $y \in A^c$, ganamos. Notemos lo siguiente: 

$$||y - x_0||>r\enspace\text{No llega a tocar la bola por definición del propio conjunto} $$ 
Entonces $r_0 > 0$, para evitarnos problemas, podemos definir la siguiente bola que siempre cumplirá con el requisito de ser un conjunto abierto: $B(y,\frac{r_0}{2})\enspace\forall y\in A^c$ 


### Unión de conjuntos abiertos 

Por demostrar que la unión arbitraria de conjuntos abiertos es abierta. Por lo tanto, tenemos la siguiente denotación: 

$$ A = \bigcup_{i\in I}X_i $$

Donde los conjuntos $X_i$ son abiertos. 

Sea un $x_0\in A$, por demostrar que $\forall x_0$ se cumple que existe una [[Bolas|bola]] abierta. En efecto, como $x_0\in A\implies x_0\in X_i$, para un $i$ arbitrario. Entonces como $x_0 \in X_i$ implica la siguiente existencia: 

$$ \implies\exists x_0\in B(x_0,r)\subset X_i\implies B(x_0,r)\subset A\implies\enspace\text{A es un conjunto abierto}$$ 
### Intersección de conjuntos cerrados

Por demostrar que la intersección arbitraria de conjuntos cerrados es cerrada. Por lo tanto, definamos lo siguiente: 

$$A = \bigcap_{i\in I} X_i$$ 
Por lo tanto, por demostrar que su complemento es abierto, es decir: 

$$ A^c = \bigcup_{i\in I} X_i^c \stackrel{!}{\iff}\enspace\text{Conjunto abierto}$$ 
Por el ejemplo anterior sabemos que si es un conjunto abierto, entonces queda demostrado. 

### Ejemplo 5: 

Sea el siguiente conjunto: 

$$ A = \lbrace (x,y)\in\mathbb{R}^2\setminus 1<x^2 + y^2<4\;\rbrace$$

Notemos que esta es la resta de dos circunferencias, una de radio 1 y otra de radio 2. Por lo tanto, sea un $y\in A$, por demostrar que $\forall y$ se cumple que $\exists B(y,r) \setminus r>0$. Podemos definir a $r$ de la siguiente forma: 

$$ r = ||y-1|| $$

Notemos que en este caso $r>0$ ya que $||y||>1$ por la definición del conjunto A. Entonces, como  $r$ siempre es mayor que 0 cuando se aproxima a la bola interior, basta tomar $\frac{r}{2}$ para tener que siempre existe una bola abierta en torno a la circumferencia interior. 

Ahora, para la exterior hacemos el proceso análogo, pero definimos a $r$ de la siguiente forma: 

$$ r = ||2-y|| $$ 
Vamos a llegar a lo mismo que antes, entonces podemos afirmar que siempre podremos formar una bola abierta para todo elemento perteneciente a $A$, y por ende, es un conjunto abierto. 