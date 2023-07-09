$$\int^{\infty}_{0} \frac{arctan(x)}{x} dx $$
Es de tercera especie, pues se indefine en x = 0 y el límite superior tiende al infiníto. 

Puedo llegar a lo siguiente: 

$$ \int^{1}_{0} \frac{arctan(x)}{x} dx + \int^{\infty}_{1} \frac{arctan(x)}{x} dx = \int^{\infty}_{0} \frac{arctan(x)}{x} dx $$
Por lo tanto, 

$$ \int^{\infty}_{1} \frac{arctan(x)}{x} dx \space\text{diverge} \implies \int^{\infty}_{0} \frac{arctan(x)}{x} dx \space\text{diverge} $$

Por **criterio de comparación** en $[1, \infty)$:

$$ 0 \leqq \frac{\arctan (x)}{x} \leqq \arctan(x) $$

Entonces, 

$$ \int^{\infty}_{1} \arctan(x)dx \space\text{diverge} \implies  \int^{\infty}_{1} \frac{arctan(x)}{x} dx \space\text{diverge} \implies \int^{\infty}_{0} \frac{arctan(x)}{x} dx \space\text{diverge} $$ 
Analizando la primera integral, puedo calcularla de la siguiente forma: 

$$ \lim_{x \rightarrow \infty} \int^{x}_{1} \arctan(t)dt $$ 
Por lo tanto,  voy a **integrar por partes**: 

$$ u = \arctan (t) \enspace \enspace \enspace \enspace \enspace du = \frac{1}{1 + t^2}dt$$
$$ v = t \enspace \enspace \enspace \enspace \enspace dv = dt$$ 
Entonces:
$$ \lim_{x \rightarrow \infty} \arctan (t) t \lvert^x_1 - \int^{x}_{1}\frac{t}{1+t^2}dt $$ Notemos que:

$$\arctan (t) t \lvert^x_1 = \arctan(x)x-\arctan(1)$$

Por lo tanto, 
$$ \nexists \lim_{x \rightarrow \infty} \arctan(x)x - arctan(1) \implies \text{diverge}$$

Entonces, toda la integral va a diverger por álgebra de límites (¿) $\implies$ $\int^{\infty}_{0} \frac{arctan(x)}{x} dx$ también dierge
