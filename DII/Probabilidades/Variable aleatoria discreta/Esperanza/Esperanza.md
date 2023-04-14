
La esperanza o **valor esperado** de una [[Variable aleatoria discreta|variable aleatoria]] $X$ con [[Función de Masa de Probabilidad|PMF]] $p_x$ y rango $r_x$ la denotamos por $E[X]$ o ($\mu_x$), y la definimos como: 

$$E[x] = \sum_{x\in R_x}P_x(x)·x$$ 

### Ejemplo 

Si para llegar al aeropuerto, hay un $50\%$ de probabilidad de llegar en 10 minutos y otros $50\%$ de llegar en 40 minutos. Entonces la esperanza es: 

$$E[x] = 10 · 0.5 + 40 · 0.5 = 25$$ 
### Ejemplo 

Sea $X$ una [[Variable aleatoria discreta|variable aleatoria]] tal que: 

$$X = \begin{cases}
-1 & \mathbb{P}(-1) = 0.3 \\ 
0 & \mathbb{P}(0) = 0.5 \\ 
1 & \mathbb{P}(1) = 0.2
\end{cases}$$ 
Si se define $Y = X^2$, ¿Cuanto es $E[Y]$? 
¿Se puede decir $E[Y] = E[X]^2$?

$$E[X] = -1 · 0.3 + 0 · 0.5 + 1 · 0.2$$ 
$$E[Y] = 0 · \mathbb{P}(Y=0) + 1 · \mathbb{P}(Y=1)$$ $$E[Y] = \mathbb{P}(X^2 = 0) + \mathbb{P}(X^2 = 1)$$ $$\implies E[Y] = 0.5$$ 
Esto ya que la probabilidad de $X^2$ toma dos probabilidades disjuntas, se pueden separar. 