Son criterios que podemos utilizar para determinar si una [[Integrales impropias|integral impropia]] converge o no. 

Podemos definir una función que me dé una [[Integrales impropias|integral impropia]]. Sabemos que una función es **convergente** si es **creciente y acotada**. Es decir: 

$$ f(x) = \int^{x}_{a} g(x) \space dx $$ $$ \text{ Si } f(x) \text{ es creciente } \land \text{ acotada } \implies \text{ converge} $$

### Criterio de comparación 

Sean dos funciones no negativas: 

$$ 0 \leq f(x) \leq g(x) \enspace \forall x \in [a,b) $$

Si sabemos que la función mayor converge, entonces $f(x)$ también convergerá. 

$$ g(x) = \int^{b}_{a} g \space dx \text{ convergente } \implies f(x) = \int^{b}_{a} f \space dx \text{ es convergente } $$ 
Y además, por contrareccíproca: 

$$ f(x) = \int^{b}_{a} f \space dx \text{ diverge } \implies g(x) = \int^{b}_{a} g \space dx \text{ es divergente } $$

### Criterio del cuociente

Si $\exists$ el siguiente límite: 
$$ \lim_{x \rightarrow b} \frac{f(x)}{g(x)} = L \space > 0 $$
$$ \text{ con b } \in \infty \lor b < \infty $$
Entonces pueden ocurrir dos cosas: 

$$ [f(x) \land g(x) \text{ convergen }] \lor [f(x) \land g(x) \text{ divergen }]$$ 
#### Ejemplo 

¿Es $\int^{\infty}_{0} x^2 e^{-x} \space dx$ convergente?

Tratemos de compararla con otras funciones: 

$$ x^2 e^{-x} = x^2 e^{-\frac{x}{2}} * e^{-\frac{x}{2}} \leq \mathbf{c e^{-\frac{x}{2}} } $$

El pensamiento va al notar que $x^2 e^{-\frac{x}{2}}$ es acotada:

```functionplot
---
title: Función acotada
xLabel: 
yLabel: 
bounds: [0,20,0,5]
disableZoom: true
grid: true
---
y = x^2 * 2.718^(-x/2)

```


Notemos que, efectivamente, la siguiente integral **es convergente**: 

$$\int^{\infty}_{0} e ^{-\frac{x}{2}} $$

Basta multiplicarla por una constante **c** mayor que $e^{-\frac{x}{2}}$ y llegamos a lo siguiente: 

$$ 0 \leq \int^{\infty}_{0} x^2 e^{-x} \space dx \space \leq \space 10 \int^{\infty}_{0} e ^{-\frac{x}{2}} \space dx$$ 

### Convergencia absoluta

Se puede demostrar que una integral converge si el valor absoluto de $f(x)$ converge. 

