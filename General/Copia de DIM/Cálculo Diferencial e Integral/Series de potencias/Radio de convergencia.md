Consiste en el supremo del conjunto de convergencia de una [[Series de Potencias|serie de Potencias]], es decir: 

$$ R = \sup\lbrace\enspace x_0\enspace\text{tal que}\enspace\sum a_n x_{0}^n\enspace\text{converge}\rbrace$$

Notemos que el 0 siempre es convergente, entonces el supremo está garantizado. 

Y, por supuesto, si converge para todos los reales, el radio de convergencia es infinito. 

## teorema 

Si la serie $\sum a_n x^n$ converge en (-R,R) con $R>0$  entonces definimos la siguiente función: 

$$f:(-R,R)\rightarrow\mathbb{R}$$
$$ x\rightarrow\sum a_nx^n $$ 
Es [[Derivada|diferenciable]] y su derivada es $f'(x) = \sum a_n nx^{n-1}\enspace x\in (-R,R)$ y por lo tanto es [[función continua|continua]] y por ende [[Integral de Riemann|integrable]] donde: 

$$ \int^{x}_{0} f(t)dt = \sum\frac{a_n}{n+1}x^{n+1} $$ 
#### Ejemplo 

Tenemos la siguiente función 

$$ f(x) = \sum \frac{x^n}{n!} $$ 
Donde se puede corroborar que: 

$$ f'(x) = f(x)\enspace\land\enspace f(0) = 1$$ 
Además: 

$$F(x) = \frac{f(x)}{e^x} \implies F'(x) = \frac{f'(x)e^x - f(x)e^x}{e^{2x}}\implies \frac{e^x(f'(x)-f(x))}{e^{2x}} = 0$$  
Entonces $F(x)$ es una constante. Podemos evaluarla en 0, donde obtenemos que: $F(0) = \frac{f(0)}{e^0} = 1 \implies f(x) = e^x$ 

Entonces, llegamos que: 

$$ e^x = \sum\frac{x^n}{n!}\forall x\in\mathbb{R} $$ 
#definición 