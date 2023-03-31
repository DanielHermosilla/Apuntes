Funciones cuyas [[Derivada|derivadas]] son acotadas. Se denomina que es global cuando es válido $\forall y\in\mathbb{R}$ y $\forall x\in\mathbb{R}$. Por el otro lado, se denomina local cuando cumple para un subconjunto de los reales. 

### Demostración 

Para demostrar que una función es de [[Lipschitz]], justamente hay que calcular la derivada de la función y ver si es acotada. Pero para algunas funciones es más difícil lograr aquello. Por lo tanto, se hace lo siguiente: 

$$|\frac{f(y)-f(z)}{y-z}|\leq L$$ 
Esta condición se debe cumplir $\forall y,z\in\mathbb{R}$. Ahora, si $y$ llegase a ser lo mismo que $z$, se podría hacer lo siguiente: 

$$|f(y)-f(z)|\leq L|y-z|$$ 
Por lo tanto, aquello quiere decir una derivada acotada. Además, implica [[Función continua|continuidad]], ya que si $y$ tiende a $z$, $f(y)$ también tiende a $f(z)$. 

### propiedades

- Toda función [[Lipschitz]] es [[Función continua|continua]].  

- Casi todas las funciónes $\mathbb{C}^1$, es decir, derivable con [[Derivada|derivada]] continua son [[Lipschitz]] . Se verifica con el [[Teorema del Valor Medio|teorema del Valor Medio]]. 

Esto se debe a que el Teorema del Valor Medio postula a que existe un valor $\xi$ tal que: 

$$\frac{|f(y)-f(z)|}{|y-z|}\leq\max_{\xi\in\mathbb{R}}|\frac{\partial f}{\partial y}(\xi)|$$ 
Entonces, si la [[Derivadas parciales|derivada parcial]] es acotada entonces es [[Lipschitz]]. 

## Lipschitz local 

Acotar el intervalo de donde $x$ se encuentra según un $\delta$ para que la condición se cumpla. 
$$|f(x,y) - f(x,z)| \leq L|y-z|$$ $$\forall y\in [y_0 - r_1, y_0 + r]$$ $$\forall z\in [y_0 - r_1, y_0 + r]$$
$$\forall x\in I\cap[x_0 - \delta, x_0 + \delta]$$ 
Gráficamente implica que la función vive en la siguiente vecindad: 

![[Lipschitz local.jpeg|center]]