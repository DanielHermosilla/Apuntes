
Se define como $X$ es exponencial ($\lambda$) con $\lambda>0$ y tiene la siguiente [[Función de Densidad de Probabilidad (PDF)|PDF]]:

$$f_x(x)=\begin{cases}\lambda e^{-\lambda x}&\text{si}\;x>0\\\\0&\text{si no}\end{cases}$$ 
Tiene la siguiente forma: 

![[Distribución exponencial.png|center|500]]


## CDF 

La $CDF$ se define como la siguiente: 

$$F_x = \mathbb{P}(X\leq x)$$
$$=\int_{-\infty}^{x}f_x(x)dx$$ $$=\int_{0}^{x}\lambda e^{-\lambda x}dx$$ 

Resolviendo la integral se llega que: 

$$F_x=\begin{cases}0&\text{si}\;x\leq 0\\\\ 1-e^{-\lambda x}&\text{si}\;x>0\end{cases}$$

## Esperanza 

Calculando la [[Esperanza de una variable continua|esperanza]] por definición: 


$$E[x]=\int_{-\infty}^{\infty}xf_xdx$$ $$=\int_{0}^{+\infty}x\lambda e^{-\lambda x}dx$$
Si se hace una integración por partes:   
$$=0 + \frac{e^{-\lambda x}}{\lambda}\bigg\vert_{0}^{\infty}$$ $$E[x] = \frac{1}{\lambda}$$ 
## Varianza 

Calculando la [[Varianza de una variable aleatoria continua|varianza]] por definición, buscamos $E[X^2]$: 

$$E[X^2]=\int_{0}^{+\infty}x^2\lambda e^{-\lambda x}dx$$ $$=\frac{2}{\lambda}\int_{0}^{\infty}x\lambda e^{-\lambda x}dx$$ 
Por lo tanto: 

$$Var(X)=\frac{1}{\lambda^2}$$ 
## Pérdida de memoria 

Se tiene algo que se llama **pérdida de memoria**, es decir: 

$$\mathbb{P}(X>x+a\;\vert\;X>a)=\mathbb{P}(X>x)$$ 
#### Demostración 

Notemos que: 

$$\mathbb{P}(X>x+a\; X>a) = \frac{\mathbb{P}(X>x+a\cap X>a)}{\mathbb{P}(X>a)}$$ 

$$=\frac{\mathbb{P}(X>x+a)}{X>a}$$ 
$$=\frac{1-F(x+a)}{1-F(a)}$$ $$=e^{-\lambda x}$$ $$=1 - F_x(x) = \mathbb{P}(X>x)$$ 




