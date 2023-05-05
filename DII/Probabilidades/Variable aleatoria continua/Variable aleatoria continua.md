
Una variable aleatoria $X$ con CDF $F_x(x)$ es [[Continuidad|continua]] si es que $F_x(x)$ es [[Continuidad|continua]] para todo $x\in\mathbb{R}$. 

Consideramos que la CDF de una variable aleatoria continua es diferenciable en *casi todos los puntos reales.* 

## CDF 

Se define la CDF como: 

$$F_x(x) = \begin{cases}
0 & x<a \\ 
\frac{x-a}{b-a} & x\in [a,b] \\ 
0 & x>b \end{cases}$$ 

Por lo tanto, se podría definir de la siguiente forma: 

$$F_X(x) = \frac{x-a}{b-a} = \int_{a}^{x}\frac{1}{b-a}dx = \int_{-\infty}^{x}f(x)dx$$ 
Pero ahora hay que definir ese $f(x)$. Eso es equivalente a la [[Función de Densidad de Probabilidad (PDF)]], lo equivalente a decir: 

$$f_x(x)=\frac{dF_x(a)}{dx}$$ 