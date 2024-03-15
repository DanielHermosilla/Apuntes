
## Pregunta 3 

Se tiene el siguiente cascarón esférico que gira con velocidad angular $\omega$: 

![[Pasted image 20231109121307.png|center]]

Tiene radio $R$ y carga total $Q$ distribuida uniformemente. 

### Determinar el campo magnético producido por el anillo ubicado a un ángulo arbitrario 

Por Ley de Biot-Savart se postula que: 

$$B(\vec{r})=\frac{\mu_0}{4\pi}\int\frac{\vec{I}\times(\vec{r}-\vec{r'})}{\vert\vert\vec{r}-\vec{r'}\vert\vert^3}dr$$

Si ponemos el origen en el centro, definimos los siguientes parámetros: 

$$\begin{align}
\vec{r'}&=z\hat{k}+r\hat{r}\\  \\
\vec{I}&=I\hat{\phi}\\  \\
dr'&=rd\phi
\end{align}$$

La integral da el siguiente resultado: 

$$B(\vec{r})=\frac{\mu_0}{2}\frac{Ir^2}{(z^2+r^2)^{\frac{3}{2}}}\hat{k}$$

Si se ocupa geometría: 

$$\vec{B}(0)=\frac{\mu_0}{2}\frac{I}{R}\sin^2\theta\;\;\hat{k} $$

