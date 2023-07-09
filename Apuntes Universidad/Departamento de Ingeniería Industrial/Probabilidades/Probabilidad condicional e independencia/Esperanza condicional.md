
La [[Esperanza|esperanza]] condicional de $X$ dado $Y=y$ es lo mismo a tener: 

- [[Variable aleatoria discreta|Caso discreto]]: $$E[X\vert Y=y]=\sum_{x\in R_x}x\cdot p_{X\vert Y}(x\vert y)$$ 
- [[Variable aleatoria continua|Caso continuo:]] $$E[X\vert Y=y]=\int_{-\infty}^{+\infty}x\cdot f_{X\vert Y}(x\vert y)dx$$

Es posible que al calcular $E[X\vert Y]$ se llega a una variable aleatoria, ya que $Y$ no tiene un valor fijo, entonces es posible calcular $E_Y[E_X[X\vert Y]]$. Esto se llama [[Ley de la Esperanza Total]]. 