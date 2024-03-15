
Ley de Biot-Savart para los campos circulares: 

$$\frac{\mu_0}{4\pi}\int\frac{I\times\widehat{(r-r')}}{(r-r')^2}dl'=\frac{\mu_0}{4\pi}I\int\frac{dl\times(\widehat{r-r'})}{(r-r')^2}$$

Para el semi-circulo de radio $a$: 

$$\begin{align}
dl&=a\hat{r}-x\hat{\theta}\;\;\;\;x\in [0,\pi]\\  \\
\widehat{r-r'}&=(-\hat{r}+\hat{\theta})
\end{align}$$

Por lo tanto, 

$$\begin{pmatrix}
\hat{r} & \hat{\theta} & \hat{z} \\
a & -x & 0 \\
-1 & 1 & 0
\end{pmatrix}=a-x\;\hat{z}$$

Por último notar que: 

$$(r-r')^2=(-a+x)^2$$

Entonces: 

$$\begin{align}
\frac{\mu_0}{4\pi}I\int^{\pi}_{0}\frac{a-x}{(x-a)^2}dx&=B\;\hat{z}\\  \\
\frac{\mu_0}{4\pi}I[\ln(a)-\ln(a-\pi)]&=B\;\hat{z}\tag{Wolfram}
\end{align}$$
