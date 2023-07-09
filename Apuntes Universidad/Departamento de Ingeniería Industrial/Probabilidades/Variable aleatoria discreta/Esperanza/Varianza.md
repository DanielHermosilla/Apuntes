
La **varianza** de una [[Variable aleatoria discreta|variable aleatoria]] $X$ la denotamos por $Var(X)$ o $\sigma_{x}^{2}$. 

$$Var(X) = E[(X-E[X])^2]$$ 
Calcular la varianza también es equivalente a calcular la varianza de una función de $X$ con $g(X) = X - E[X]$. 

## Propiedades 

1. $Var(aX + b) = E(aX + b - E[aX + b])^2 = \mathbf{a^2\ Var(X)}$  
2. $Var(X) = E[(X-E(X)^2)] = \sum_{x\in R_x}(x-E[X])^2\ P(X=x) = \mathbf{E[X^2] - E[X]^2}$   


### Ejercicio 

Se tiene una caja con bolas del 1 al 100 y se saca al azar, la variable aleatoria se llamará $X$. El segundo experimento es una caja con bolas pero va del 2 al 101, la saca al azar y se llamará $Y$. 