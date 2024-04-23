
Describimos el comportamiento de $Y$ a nivel poblacional bajo el siguiente modelo: 

$$y=\beta_0+\beta_1X+u$$

Donde: 

- $y$ es la variable dependiente 

- $X$ es un [[vectores|vector]] de variables independientes 

- $u$ es un término de error 

- Nos interesa estimar $\beta_0$ y $\beta_1$. 

Para poder escoger estos valores, interesa el método de **mínimo cuadrados ordinarios**: 

### Mínimo Cuadrados Ordinarios 

La idea principal es ajustar coordenadas de datos $(y_i, X_i)$

Hay que encontrar los valores de $\beta_0$ y $\beta_1$ que minimicen la distancia entre coordenadas y la línea. 

Dado $\beta_0$ y $\beta_1$, la **distancia** entre el punto $(y_i, X_i)$ y la línea está dada por el residuo: 

$$e_i=y_i-(\beta_0+\beta_1X)$$

Por lo tanto, los que interesa es minimizar la [[norma]] del residuo: 

$$\min_{\beta_0,\beta_1}\sum^{n}_{i=1}e^{2}_{i}=\sum^{n}_{i=1}[y_i-(\beta_0+\beta_1X_i)]^2$$

![[Pasted image 20240423122640.png|center]]

Notar que $\beta_0$ y $\beta_1$ son **variables aleatorias**. 

Para obtener $\hat{\beta_0}$ y $\hat{\beta_1}$ se usa condiciones de primer orden: 

$$\begin{align}
\text{CPO}_{\beta_0}:\frac{\partial}{\partial\beta_0}\sum^{n}_{i=1}e^{2}_i&=0 \\\\
\text{CPO}_{\beta_1}:\frac{\partial}{\partial\beta_1}\sum^{n}_{i=1}e^{2}_i&=0
\end{align}$$

Resolviendo todo esto, se llega que: 

$$\begin{align}
\hat{\beta_1}&=\frac{\text{Cov}(X_i,y_i)}{\text{Var}(X_i)}
\end{align}$$

Puesto que tenemos el valor de $y$ con la estimación de mínimos cuadrados, es posible llegar a la siguiente equivalencia: 

$$\begin{align}
\hat{\beta_1}&=\frac{\text{Cov}(X,y)}{\text{Var}(X)}\\  \\
&=\frac{\text{Cov}(x,\beta_0+\beta_1 X+\epsilon_i)}{\text{Var}(\beta_0+\beta_1 X+\epsilon_i)}\\  \\
&=\beta_1+\frac{\text{Cov}(X,\epsilon)}{\text{Var}(X)}
\end{align}$$
