
Se dice que la [[Variable aleatoria discreta|variable aleatoria]] $X$ es geometríca con $p\in (0,1)$ si el $R_x = \lbrace 1,2,3,\dots\rbrace$ y su [[Función de Masa de Probabilidad|PMF]] es: 

$$p_x(x) \begin{cases}

p(1-p)^{x-1} & \text{si}\ x = 1,2,3\dots \\ 
0 & \text{si no} \\ 
\end{cases}$$ 
![[geométrica.png|center]]

## Esperanza 

Se define la [[Esperanza|esperanza]] de esta distribución como: 

$$E[X] = \sum_{k=1}^{n}kp(1-p)^{k-1}p$$ 
Es dificil calcularla con la variable $k$, pero se puede hacer lo siguiente por sumatoria geométrica: 

$$\sum_{k=0}^{\infty}(1-p)^k = \frac{1}{p}$$ 
Si lo derivamos queda lo siguiente: 

$$\frac{d}{dp}\ \ -\sum_{k=0}^{\infty}k(1-p)^{k-1} = \frac{-p}{p^2}$$
$$\iff \sum_{k=1}^{n}kp(1-p)^{k-1}p = \frac{1}{p}$$ 
Por lo tanto, la [[Esperanza|esperanza]] es $\frac{1}{p}$. 

## Varianza 

Por lo tanto, la [[Varianza|varianza]] sería lo siguiente: 

$$Var(X) = E[X^2] - E[X]^2$$ 
Bastaría calcular $E[X^2]$. 

$$E[X^2] = \sum_{k=1}^{\infty}k^2(1-p)^{k-1}p$$ 
Si tomamos la siguiente expresión conseguida anteriormente, se puede multiplicar por $-(1-p)$. 

$$-\sum_{k=0}^{\infty}k(1-p)^{k-1} = \frac{1}{p^2}$$

$$\implies \frac{d}{dt}\sum_{k=0}^{\infty}k^2(1-p)^{k-2} = \frac{-2 + p}{p^3}$$ 
Se llega que $E[X^2] = \frac{2-p}{p^2}$ 

Entonces, la varianza es: $Var(X) = \frac{1-p}{p^2}$ 

