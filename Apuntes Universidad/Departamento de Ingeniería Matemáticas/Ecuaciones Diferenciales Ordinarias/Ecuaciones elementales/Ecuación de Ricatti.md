
### Motivación 

Sea la siguiente ecuación: 

$$y' = y^2 + by + c\ \ \ a,b,c\in\mathbb{R}$$ 
Donde $\lambda_1,\lambda_2$ son las raíces reales del polinomio. Entonces se puede factorizar: 

$$y' = (y-\lambda_1)(y-\lambda_2)$$ 
Entonces, sea $y_1 = \lambda_1$- Entonces el cambio de variable sería $y = y_1 + \frac{1}{z}$. La [[Departamento de Ingeniería Industrial/Probabilidades/Repasos/Funciones/Derivada|derivada]] sería $$y' = -\frac{z'}{z^2} = (\lambda_1 + \frac{1}{z})^2 + b(\lambda_1 + \frac{1}{z}) + c$$ 
$$-\frac{z'}{z^2} = \lambda_{1}^{2} + 2\frac{\lambda_1}{z} + \frac{1}{z^2} + b\lambda_1 + \frac{b}{z} + c$$ 
Pero, como $\lambda_1$ es una raiz, es decir, $\lambda_{1}^{2} + b\lambda_1 + c = 0$, entonces queda: 

$$-z' = 2\lambda_1z + 1 + bz$$ Y queda un [[sistema de ecuación|sistema de ecuación lineal]]: 

$$z' + (2\lambda_1 + b)z = -1$$ 