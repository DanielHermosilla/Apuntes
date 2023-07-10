
## Modelo estacionario 

Se tiene la situación donde la barra está en reposo dado que existe una fuerza tensión que le impide el movimiento rotacional y traslacional. 

Esto implica dos cosas en específico, la sumatoria del torque es nula, dada la restricción rotacional, y la sumatoria de fuerzas también es nula, por la restricción traslacional. 

Si analizamos primero la sumatoria de fuerzas, considerando a la barra como una partícula, se tiene lo siguiente: 

$$\text{Suma de fuerzas}=\begin{cases} -\vec{F_t}+\vec{F_{N_\hat{x}}}=0&\text{para}\;\hat{x}\\\\-\vec{F_p}-\vec{F_p}+\vec{F_{N_\hat{y}}}=0&\text{para}\;\hat{y}\end{cases}  
$$

Es importante notar que $\vec{F_N}$ corresponde a la fuerza normal que ejerce el rodillo, cuyas componentes se descomponen en dos ejes. 

![[Imagen PNG.png|center|400]]


La magnitud de las fuerzas normales del rodillo son desconocidas, por lo que lo más conveniente sería hacer un análisis rotacional. 

![[Imagen PNG 2.png|center|400]]

Donde el torque total llegaría a ser:


$$\sum\tau=\vec{r_1}\times\vec{F_t}+\vec{r_1}\times\vec{F_p}+\vec{r_2}\times\vec{F_p}=0$$

El único vector a descomponer sería $\vec{r_2}$, que geométricamente equivale a $\vec{r_2}=-\frac{L}{2}\hat{x}-L\hat{y}$. 

Entonces, haciendo el producto cruz para los tres sumandos: 

$$\begin{align}
\vec{r_1}\times\vec{F_t}&=\begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
0 & \frac{-L}{2} & 0 \\
-F_T & 0 & 0
\end{bmatrix}=\frac{F_{T\cdot}L}{2}\hat{z}\\\\  
\vec{r_1}\times\vec{F_P}&=\begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
0 & \frac{-L}{2} & 0 \\
0 & -mg & 0
\end{bmatrix}=0\\\\ 
\vec{r_2}\times\vec{F_p}&=\begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
-\frac{L}{2} & -L & 0 \\
0 & -mg & 0
\end{bmatrix}=\frac{Lmg}{2}\hat{z}
\end{align}$$

Por lo tanto, imponiendo la condición rotacional: 

$$\begin{align}\frac{F_{T}\cdot L}{2}+\frac{Lmg}{2}&=0\\\\  
F_T&=-mg\end{align}$$

Dado que el análisis vectorial se hizo bajo un sistema de coordenadas donde los valores positivos son hacia la derecha y arriba, entonces el vector de la fuerza tensión apunta hacia la izquierda **con magnitud** $mg$ cuando el sistema está estacionario. 

## Modelo rotacional 

Ahora, a diferencia de la situación anterior, se tiene que el sistema rota en torno al pivote. Aquí es util saber la relación $I_o\ddot{\theta}=\vec{\tau}^{\text{ext}}$. Haciendo un análisis trigonométrico, se llegan a las siguientes relaciones: 

![[Imagen PNG 3.png|center|220]]


Ahora los vectores $\vec{r_1}$ y $\vec{r_2}$ estarían descompuestos de forma distinta. Además, el torque ya no llegaría a ser nulo. A través del análisis trigonométrico esbozado en el dibujo, se puede llegar que: 

$$\begin{align}
\vec{r_1}&=\frac{L}{2}\sin\theta\;\hat{x}\;-\frac{L}{2}\cos\theta\;\hat{y}\\\\  
\vec{r_2}&=\left(L\sin\theta-\frac{L}{2}\cos\theta\right)\;\hat{x}\;+\left(-L\cos\theta-\frac{L}{2}\sin\theta\right)\;\hat{y}
\end{align}$$


Por lo tanto, nuevamente calculando el torque: 

$$\begin{align}
\vec{r_1}\times\vec{F_p}+\vec{r_2}\times\vec{F_p}&=\tau_{0}\\\\
\vec{r_1}\times\vec{F_p}=\begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
\frac{L}{2}\sin\theta & -\frac{L}{2}\cos\theta & 0 \\
0 & -mg & 0
\end{bmatrix}&=-mg\frac{L}{2}\sin\theta\;\hat{z}\\\\
\vec{r_2}\times\vec{F_p}=\begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
\left(L\sin\theta-\frac{L}{2}\cos\theta\right) & \left(-L\cos\theta-\frac{L}{2}\sin\theta\right) & 0 \\
0 & -mg & 0
\end{bmatrix}&=-mg\left(L\sin\theta-\frac{L}{2}\cos\theta\right)\;\hat{z}
\end{align}$$

Ahora, para calcular el momento de inercia, por el *teorema de Steiner*, se llega que: 

$$\begin{align}
I_1&=\frac{1}{12}mL^{2}+m\left(\frac{L}{2}\right)^{2}\\\\  
I_2&=\frac{1}{12}mL^{2}+m\vert\vec{r_2}\vert^2

\end{align}$$

Notemos que es posible calcular la magnitud de $\vec{r_2}$ directamente, pero el análisis es más directo si nos damos cuenta que siempre se cumplirá la relación entre catetos donde el más largo es $L$ y el menos largo es $\frac{L}{2}$, entonces la magnitud es $\sqrt{L^2+\left( \frac{L}{2} \right)^2}$. Por último, se sabe que $I_0=I_1+I_2$, entonces: 

$$\begin{align}
\frac{5mL^2}{3}\ddot{\theta}&=-mg\left(\frac{L}{2}\sin\theta + L\sin\theta-\frac{L}{2}\cos\theta\right)\\\\
\frac{5}{3}L\ddot{\theta}&=-g\left(3\sin\theta-\cos\theta\right)\\\\  
\ddot{\theta}&=\frac{-3gL}{5}\left(3\sin\theta-\cos\theta\right)
\end{align}$$

Se tiene una EDO, que se expresa de la siguiente forma: 

$$\int^{\dot{\theta}_{\text{max}}}_{\dot{\theta}_{\text{inicial}}}\dot{\theta}d\dot{\theta}=\int^{\theta_{\text{max}}}_0\frac{-3gL}{5}\left(3\sin\theta-\cos\theta\right)\;d\theta$$

Claramente la velocidad angular inicial y final son $0$, entonces el lado izquierdo sería una integral entre cero y cero, lo que es nulo. Por el otro lado, resolviendo la integral del lado derecho: 

$$\begin{align}

0&=-\frac{3Lg}{5}\left(-\sin \left(θ\right)\bigg\vert_{0}^{\theta^*}-3\cos \left(θ\right)\bigg\vert_{0}^{\theta^*}\right)\\\\
0&=-\frac{3Lg}{5}(-\sin\theta^*-3\cos\theta^*+3)\\\\  
0&=-\sin\theta^*-3\cos\theta^*+3
\end{align}
$$

Por lo tanto, el ángulo máximo es $\theta^*=180\degree$. 

Por el otro lado, para determinar el **ángulo de equilibrio** habría que establecer el ángulo cuyo torque sea nulo. Para este caso, se tiene que: 

$$\begin{align}

-mg\left(\frac{L}{2}\sin\theta + L\sin\theta-\frac{L}{2}\cos\theta\right)&=0\\\\  
3\sin\theta-\cos\theta&=0\\\\  
3&=\cot\theta\\\\  
\theta&\approx30\degree
\end{align}$$

Vale decir, en los $30\degree$ se tiene que el centro de masa es perpendicular con el pivote. 

Por último, para el período de pequeñas oscilaciones, se puede hacer un polinomio de Taylor en torno al punto de equilibrio para la ecuación inicial: 

$$\begin{align}
I_0\ddot{\theta}=\cancelto{0}{f(\theta^*)}+\frac{df}{d\theta}\bigg\vert_{\theta^*}(\theta-\theta^*)
\end{align}$$

