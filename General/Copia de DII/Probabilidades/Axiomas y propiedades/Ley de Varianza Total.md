
Sean las [[Variable aleatoria continua|variables aleatorias]] $X$ e $Y$, entonces: 

$$Var(X)=E_y[Var_X(X\vert Y)]+Var_Y(E_X[X\vert Y])$$ 
#### Ejemplo 

Sean 𝑁 (una VA) las personas que llegan a un restaurant. Sea $𝑋$ la VA del consumo de la 𝑖-ésima persona. Los consumos entre individuos sonindependientes entre sí, e independientes del número de personas que llega al restaurant. Además, 𝜇 = $E[X_i]$ y $\sigma_{X}^2$  = $Var[X_i]$.  Sea la VA asociado al consumo total 𝑌 = $X_1 + X_2 + \dots + X_n$. Calcular la varianza del consumo total.

Por lo tanto, 

$$\begin{align}
Var(Y)&=E_n[Var_Y(Y\vert N)] + Var_N(E_Y[Y\vert N])\\\\
&=Var(\sum_{i=1}^{n}X_i\vert N) + Var_n(\mu_x\cdot N)\\\\
&=\sum_{i=1}^{n}Var(X_i\vert N) + \mu_{x}^{2}\cdot Var(N)\\\\
&=\sum_{i=1}^{n}Var(X_i)+\mu_{x}^{2}\cdot Var(N)\\\\
&=E_n[n\sigma_{x}^{2}]+\mu_{x}^{2}\cdot Var(N)\\\\
&=\sigma_{X}^2E[N]+\mu_{x}^{2}\cdot Var(N)\end{align}$$ 
