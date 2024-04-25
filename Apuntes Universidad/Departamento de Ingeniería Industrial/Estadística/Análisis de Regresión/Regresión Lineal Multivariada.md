

Se puede escribir como una gran suma de variables aleatorias: 

$$y=\beta_0 + \beta_1X_1+\beta_2X_2+\dots+\beta_kX_k+\epsilon$$

Es posiible escribir esto de forma [[matriz|matricial]]: 


$$\begin{align}
y&=X\beta+\epsilon\\  \\
\begin{pmatrix}
y_1 \\
y_2 \\
\dots \\
\dots \\
y_n
\end{pmatrix}&=\begin{pmatrix}
1 & x_{11} & \dots & \dots & x_{1k} \\
1 & x_{12} & \dots & \dots & \vdots \\
1 & \dots & \dots & \dots & \vdots \\
1 & \dots & \dots & \dots & \vdots \\
1 & x_{1k} & \dots & \dots & x_{nk}
\end{pmatrix}\begin{pmatrix}
\beta_0 \\
\beta_1 \\
\vdots \\
\vdots \\
\beta_k
\end{pmatrix}
+\begin{pmatrix}
\epsilon_1 \\
\epsilon_2 \\
\vdots \\
\vdots \\
\epsilon_n
\end{pmatrix}_{n\times 1}
\end{align}$$

Al igual que la [[Regresión Lineal Simple|regresión lineal simple]], los residuos se definen como: 

$$e_i(\beta)=y_i$$

Y el MCO resuelve el problema de minimización con: 

$$\arg\min_{\beta_0, \beta_1,\dots,\beta_k}\sum^{n}_{i=1}(e_i(\beta))^2$$

Se obtendrían $k+1$ ecuaciones con $k+1$ parámetros. Por construcción, los residuos quedarían como: 

- $\sum^{n}_{i=1}\hat{e_i}=0$
- $\sum^{n}_{i=1}X_{ik}\hat{e_i}=0\;\;\;\forall k=1,\dots, k$

Si definimos $\bar{r_{iK}}$ como el [[vectores|vector]] de residuos obtenidos luego de regresionar $X_{ik}$ sobre todos los restantes regresores $X_{ik}$. 