
Se tiene la situación donde la barra está en reposo dado que existe una fuerza tensión que le impide el movimiento rotacional y traslacional. 

Esto implica dos cosas en específico, la sumatoria del torque es nula, dada la restricción rotacional, y la sumatoria de fuerzas también es nula, por la restricción traslacional. 

Si analizamos primero la sumatoria de fuerzas, considerando a la barra como una partícula, se tiene lo siguiente: 

$$\text{Suma de fuerzas}=\begin{cases} -\vec{F_t}+\vec{F_N}=0&\text{para}\;\hat{x}\\\\-\vec{F_p}-\vec{F_p}+\vec{F_N}=0&\text{para}\;\hat{y}\end{cases}  
$$

Es importante notar que $\vec{F_N}$ corresponde a la fuerza normal que ejerce el rodillo, cuyas componentes se descomponen en dos ejes. 

![[Imagen PNG.png|center|400]]


De la sumatoria de fuerzas, es directo que $\vec{F_T}=2mg$, aunque también se podría ver por el torque. Si se pone como pivote el rodillo, se llega a lo siguiente: 

![[Imagen PNG 2.png|center|400]]

Donde el torque total llegaría a ser:


$$\sum\tau=\vec{r_1}\times\vec{F_t}+\vec{r_1}\times\vec{F_p}+\vec{r_2}\times\vec{F_p}=0$$

El único vector a descomponer sería $\vec{r_2}$, que geométricamente equivale a $\vec{r_2}=-L\hat{x}-\frac{L}{2}\hat{y}$. 

Entonces, haciendo el producto cruz para los tres sumandos: 

$$\begin{align}
\vec{r_1}\times\vec{F_t}&=\begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
0 & \frac{-L}{2} & 0 \\
-F_T & 0 & 0
\end{bmatrix}
\end{align}$$