
Algunas típicamente usadas: 

- **Bernoulli** ($1$ intento): $P(X=1)=\alpha$, $P(X=0)=1-\alpha$. Con $0\leq\alpha\leq1$ 

- **Binomial** ($n$ intento): $P(X=x)=\binom{n}{x}\alpha^x(1-\alpha)^{n-x}$. El valor esperado es $\alpha n$ con una varianza de $n\alpha (1-\alpha)$

- **Poisson**: Si el número de intentos crece $n\to\infty$ al mismo tiempo que la probabilidad de éxito decae, se tiene que la binomial se aproxima a una *Poisson*, con $P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}$ con $\lambda=n\cdot\alpha$. Por ejemplo, la cantidad de goles que hace un equipo de fútbol al año. *¿Cuánto veces ocurre algo en un tiempo continuo?* 