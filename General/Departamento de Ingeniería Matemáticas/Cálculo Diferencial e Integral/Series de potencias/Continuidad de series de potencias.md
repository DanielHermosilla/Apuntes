
Sea $\sum a_k x^k$ una [[Series de Potencias|serie de Potencia]] de [[Radio de convergencia|radio de convergencia]] igual a *R*. Por lo tanto, podemos definir la siguiente función: 

$$ f: (-R,R)\rightarrow\mathbb{R} $$
$$ f(x) = \sum^{\infty}_{k=0} a_k x^k $$ 
Por lo tanto, uno se pregunta: *¿Es [[Función continua|continua]]?* *¿Es derivable?* *¿Es integrable?* 

## Teorema de continuidad 

Si la serie $\sum a_k x^k$ tiene un radio de convergencia R>0, entonces $f:(-R,R)\rightarrow\mathbb{R}$ definida por $f(x) = \sum^{\infty}_{k=0}a_k x^k$ es continua en $(-R,R)$. 

### Demostración 

Sea la siguiente función: 

$$ f_n(x) = \sum^{n}_{k=0}a_k x^k $$ Y tenemos lo siguiente: 

$$|f_n(x)| \leq \sum^{n}_{k=0} |a_k|r^k = S_n\enspace\text{(desigualdad triangular)} $$ 
Notemos que la [[Series numéricas|serie]] $S_n$ es [[Convergencia absoluta|convergente]] y por ende tiene límite, que lo denominaremos $S$. Además podemos asegurar que $S_n$ es creciente. 

Ahora, veamos lo siguiente bajo dos números arbitrarios: 

$$ m > n \enspace|f(m)-f(n)|\leq\sum^{m}_{n+1}|a_k|r^k = S_m - S_n $$

Por  consiguiente, veamos que $f(m)\rightarrow f(x)$ pues la serie es convergente. Entonces, tomando el límite podemos llegar a lo siguiente: 

$$ |f(x) - f_n(x)|\leq S-S_n \enspace\forall x \in (-R,R)$$

$$\iff |f(x) - f_n(x)|\leq |f(x)-f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)|\leq 2(S - S_n) + |f_n(x) - f_n(x_0)| $$ 
Simplificando, tenemos lo siguiente: 

$$ |f(x) - f_n(x)|\leq 2(S-S_n) + |f_n(x) - f_n(x_0)| \enspace\forall x \in (-R,R)$$

Por lo tanto, para argumentar [[Función continua|continuidad]] decimos lo siguiente: 

$$\text{dado un}\enspace\epsilon > 0\enspace\exists N\in\mathbb{N}\enspace\text{tal que}\enspace 2(S-S_n)\leq\frac{\epsilon}{2}$$ 
Una vez elegido N, como $f_n$ es continua, existe un $\delta > 0$ tal que: 

$$ |x-x_0| < \delta\implies |f_n(x)-f_n(x_0)|\leq\frac{\epsilon}{2} $$ 
Y así, $$|f(x)-f(x_0)|< \epsilon$$ 
## Teorema de derivabilidad e integrabilidad 

Si $f(x) = \sum^{\infty}_{k=0} a_k x^k$ entonces por lo anterior sabemos que es continua, pero además, sabemos que es [[Integral de Riemann|integrable]] y [[Departamento de Ingeniería Industrial/Probabilidades/Repasos/Funciones/Derivada|derivable]]: 

$$ \int^{x}_{0}f(t)dt = \sum^{\infty}_{k=0} a_k \frac{x^{k+1}}{k+1} $$ $$ f'(x) = \sum^{\infty}_{k=0} k a_k x^{k-1} $$ 
Esto se obtiene al derivar e integrar término a término. 

## Proposición 

Si la [[Series numéricas|serie]] tiene [[Radio de convergencia|radio de convergencia]] igual a un número *R*, entonces se puede asegurar lo siguiente: 

$$\forall p \in\mathbb{Z}\enspace\text{la serie}\enspace\sum^{\infty}_{k=0}k^p a_k x^k\enspace\text{tiene radio de convergencia R}$$ 

