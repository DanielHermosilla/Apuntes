
Se define como $X$ es uniforme en $(a,b)$ si cumple que: 

$$f_x(x)=\begin{cases}\frac{1}{b-a}&\text{si}\;x\in [a,b]\\\\0&\text{si no}\end{cases}$$ 
## Esperanza 

Por lo tanto, su [[Esperanza de una variable continua|esperanza]] por definición, llegaría a ser: 

$$E[x] = \int_{-\infty}^{\infty}xf_x(x)dx$$ $$\iff\int_{a}^{b}x\frac{1}{b-a}dx$$ $$\iff\frac{x^2}{2(b-a)}\bigg\vert_{x=a}^{x=b}$$ $$\iff\frac{a+b}{2}$$ 
Lo que hace sentido si se analiza el gráfico de su [[Función de Densidad de Probabilidad (PDF)|PDF]]:

![[Uniforme.png|center]]

## Varianza 

Si se calcula la [[Varianza de una variable aleatoria continua|varianza]] por definición: 

$$Var(X)=E[X^2]-E[X]^2$$ 
Donde, se llega que: 

$$E[X^2] = \int_{a}^{b}x^2\frac{1}{b-a}dx$$ $$\iff\frac{a^2 + ab + b^2}{3}$$ 
Por ende, $$\frac{a^2 + ab + b^2}{3}-E[X]^2 = \frac{(a-b)^2}{12}$$ 