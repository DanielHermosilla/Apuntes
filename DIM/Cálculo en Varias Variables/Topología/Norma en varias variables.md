Es una extensión a la definición de [[norma]] que viene del curso de Álgebra Lineal. Vamos a definir a la norma bajo la siguiente ecuación; sea $x$ un [[vectores|vector]] cualquiera de un [[Espacios vectoriales|espacio vectorial]]: 

$$ ||x|| = \sqrt{x\cdot x} = \sqrt{x_{1}^2 + x_{2}^2 + \dots + x_{d}^2} $$ 
Esto ya es conocido para [[vectores]] en varias dimensiones, pero, aún así, vamos a introducir propiedades nuevas a tal definición: 

1) $||x|| > 0 \; \forall x\in E$
2) $||x|| = 0\iff x = \vec{0} \; \forall x \in E$
3) $||\alpha x|| = |\alpha| \;||x||\;\forall x\in E, \forall\alpha\in\mathbb{K}$ 
4) $||x + y|| \leq ||x|| + ||y|| \; \forall x,y\in E \;\;\enspace\enspace\text{(desigualdad triangular)}$

Por lo tanto, para demostrar que tenemos una norma hay que demostrar que cumpla cada condición. Claramente la más difícil de demostrar es la desigualdad triangular, que normalmente sale por la [[Desigualdad de Cauchy-Schwartz|desigualdad de Cauchy-Schwartz]]. 

### Norma en $\mathbb{R}^1$ 

Sobre vectores de una dimensión la norma va a corresponder simplemente al valor absoluto de tal valor, es decir: 

$$||x|| = |x| \; \;\forall x\in\mathbb{R}^1$$ 
### Norma Euclidiana 

Vamos a definir la norma con la que más se va a trabajar en [[Topología|topología]] que corresponde a la norma euclidiana.  Se va a denotar con el subíndice 2: 

$$||x||_2 = \sqrt{\sum_{i=1}^{n} (x_i)^2}$$ 
Por lo tanto, es de notar que lo único que se ha hecho es poner nombres y añadir propiedades a los conceptos ya definidos anteriormente. En este curso se responderá a la pregunta *¿Por qué la norma Euclidiana es una norma?*. Corroborar las primeras tres propiedades es trivial, no así la cuarta, que la vamos a demostrar bajo la [[Desigualdad de Cauchy-Schwartz|desigualdad de Cauchy-Schwartz]]. 

#### Demostración 

Voy a demostrar la cuarta propiedad: la de desigualdad triangular. Por lo tanto, por demostrar que: 

$$||x + y||_2 \leq ||x||_2 + ||y||_2 \; \forall x,y\in E\;\;\enspace\enspace\text{(desigualdad triangular)}$$

$$\iff||x + y||_2 = ||x||_{2}^2 + \mathbf{2\langle x,y\rangle} + ||y||_{2}^2 $$

Veamos que por la [[Desigualdad de Cauchy-Schwartz|desigualdad de Cauchy-Schwartz]] tenemos lo siguiente, ya que nuestro término medio es un [[producto punto]]:

$$||x + y||_2 \leq ||x||_{2}^2 + 2||x||_2 \;||y||_2 + ||y||_{2}^2$$
$$\iff ||x + y||_2 \leq (||x||_2 + ||y||_2)^2$$

Por lo tanto, como es menor o igual que el binomio al cuadrado, entonces implica que también se cumplirá lo siguiente: 

$$\implies ||x + y||_2 \leq ||x||_2 \; ||y||_2$$ 
Por lo tanto, demostramos la desigualdad triangular, la cuarta propiedad de las [[norma|normas]]. 

La norma Euclidiana llega a ser la mas útil ya que al fin y al cabo nos muestra la longitud de un [[vectores|vector]]. 




Ahora notemos la siguiente observación; definamos la siguiente [[función]]: $\langle ·, ·\rangle: \mathbb{R}^n \times \mathbb{R}^n \rightarrow \mathbb{R}$ comprendida por lo siguiente: 

$$ \langle x,y \rangle:= \sum^{n}_{i=1} x_i y_i$$

Basicamente, estamos definiendo el [[producto punto]]. Notemos que es un producto interno, es decir, verifica que: 

1) $\langle \alpha x,y \rangle = \alpha\langle x,y\rangle\enspace\enspace\forall x,y\in\mathbb{R}^n, \enspace\forall\alpha\in\mathbb{R}$ 
2) $\langle x + y,z\rangle = \langle x,z\rangle + \langle y,z\rangle\enspace\enspace\forall x,y,z\in\mathbb{R}^n$
3) $\langle x,y\rangle = \langle y,x \rangle\enspace\enspace\forall x,y\in \mathbb{R}^n$
4) $\langle x,x\rangle > 0 \enspace\enspace\forall x \neq 0_\mathbb{R}$ 

Más aún, podemos **volver a definir** la norma Euclidiana de la siguiente forma: 

$$ ||x||_2 = \sqrt{\langle x,x \rangle} $$

Esto nos está diciendo que a partir de un **producto interno** estamos definiendo una norma. Por lo tanto, este ejemplo nos permite preguntarnos si será posible dado un producto interno arbitriario de un [[Espacios vectoriales|espacio vectorial]] definir una norma. Y, de hecho, podemos llegar que a cualquier norma se le puede definir un producto interno para redefinirla: 

![[Captura de Pantalla 2022-12-14 a la(s) 18.15.29.png|center|600]]


### Norma infinita 

Se define norma infinita como la siguiente aplicación: $||·||_\infty:\mathbb{R}^n\rightarrow [0, +\infty)$: 

$$ ||x||_\infty = \max_{1 \leq i \leq n} \lbrace|x_i|\rbrace $$ 
#### Demostración 

1) Primera propiedad; por demostrar que: 

$$||x||_{\infty} > 0 \; \forall x\in E$$

En efecto, notemos que como estamos trabajando con valor absoluto, entonces nos podemos asegurar que se cumple para todo valor de un [[vectores|vector]] asociado a $x$ que se cumple lo siguiente: 

$$ |x_i| \geq 0 \enspace\enspace\forall i \in \lbrace1,\dots,n\rbrace\implies ||·||_\infty \geq 0$$ 
Pero, tenemos un mayor o igual a 0 y necesitamos que sea mayor **estricto** a 0.  *¿Cuándo tenemos que la norma infinita es igual a 0?*, como se define como el mayor elemento del valor absoluto de un vector entonces notemos que para que la norma sea igual a 0 necesitariamos tener que el vector sea el vector nulo. Esto se explicará en el siguiente punto, pero, podríamos decir que se cumple la primera propiedad. 

2) Segunda propiedad; por demostrar que: 

$$||x||_\infty = 0\iff x = \vec{0} \; \forall x \in E$$

Para que $||x||_\infty = 0$, por definición de la norma infinita, necesitaríamos que el vector cumpla lo siguiente: 

$$ \max_{1 \leq i \leq n} \lbrace|x_i|\rbrace = 0 $$
$$ \implies 0 \leq x_i \leq 0\enspace\enspace\forall i \in \lbrace 1,\dots,n \rbrace $$$$\implies x_i = 0\enspace\enspace\forall i \in \lbrace 1,\dots,n \rbrace $$ 
Por lo tanto, por conclusión, para que la norma $||x||_\infty$ sea igual a 0, necesitaríamos que todos los elementos que lo compongan sean igual a 0. Por ende, que la norma sea 0 implica que el vector es el vector nulo. 

3) Tercera propiedad; por demostrar que: 

$$||\alpha x||_\infty = |\alpha| ||x||_\infty \; \forall x\in E, \forall\alpha\in\mathbb{K}$$ 
Por definición, tenemos lo siguiente: 

$$ ||\alpha x||_\infty = \max_{1 \leq i \leq n} \lbrace|\alpha_i x_i| \rbrace$$ 
Notemos que $\alpha$ es constante, es decir, $\forall i$ se tiene que $\alpha_i = \alpha$. Por ende, podemos decir que el máximo valor absoluto de un valor constante es su valor absoluto. Entonces: 

$$ ||\alpha x||_\infty = |\alpha|\max_{1 \leq i \leq n} \lbrace|x_i| \rbrace$$

Por último, notar que justamente $\max_{1 \leq i \leq n} \lbrace|x_i| \rbrace = ||x||_\infty$. Entonces: 

$$||\alpha x||_\infty = |\alpha| \;||x||_\infty $$ 
4) Cuarta propiedad; por demostrar que: 

$$||x + y||_\infty \leq ||x||_\infty + ||y||_\infty \; \forall x,y\in E\;\;\enspace\enspace\text{(desigualdad triangular)}$$ 

Notar que $||x + y||_\infty = \max_{1 \leq i \leq n} \lbrace|x_i + y_i| \rbrace$. Es decir, la máxima suma de cada elemento del vector sumado por sí sólo en el valor absoluto. Sea $c = \max_{1 \leq i \leq n} \lbrace|x_i + y_i| \rbrace$, por lo tanto, $c$ está definido por un $\bar{x}$ e $\bar{y}$ arbitrario: 

$$ c = \bar{x} + \bar{y} $$ 
Para que se cumpla que $c$ sea un valor máximo, queremos que $\bar{x}$ y $\bar{y}$ sean el máximo valor posible. Por lo tanto, podemos decir que estaría acotado por la suma del valor más grande posible de $x_i$ y de $y_i$:

$$ c \leq \max_{1 \leq i \leq n} \lbrace|x_i| \rbrace + \max_{1 \leq i \leq n} \lbrace|y_i| \rbrace $$ 
Como $c$ estaba definido bajo valores arbitrarios, podemos devolvernos en las igualdades y llegar a lo siguiente: 

$$ ||x + y||_\infty \leq ||x||_\infty + ||y||_\infty $$ 



### Norma uno

Tenemos que la norma uno se define de la siguiente forma: 

$$||x||_1 = \sum^{n}_{i=1} |x_i|\enspace\forall i \in\lbrace1,\dots,n\rbrace$$

Es decir, es la suma de los elementos, en valor absoluto, del [[vectores|vector]].

### Norma p-ésima: 

Por último, vamos a definir a la norma P-ésima como la siguiente: 

$$ ||x||_p = \sqrt[p]{\sum^{n}_{i=1}(x_i)^p} $$ 
Justamente las desigualdades triangulares de tal norma se prueban bajo la [[desigualdad de Hölder]] y la [[desigualdad de Young]]. 

Ahora, el estudio de las normas son importantes ya que nos vamos a dar cuentas que, como hay distintas formas de medir cosas, **las normas nos van a representar distintas formas de medir [[Distancia|distancias]]**. 