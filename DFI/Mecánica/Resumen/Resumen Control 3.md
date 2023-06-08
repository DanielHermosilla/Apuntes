
# Momento Angular  

Notemos que la rotación de una partícula no solamente depende del momentum $\vec{p}$ de la partícula, si no también del punto respecto del cual se está observando.

![[Captura de pantalla 2023-06-08 a la(s) 10.49.25.png|center|500]]


Por ejemplo, en $A$ la partícula no está rotando, en cambio, en $B$ y $C$ si existe una rotación. 

La variable para describir la rotación de una partícula es el **momentum angular**, donde se define en función de su vector $\vec{r}_A$ posición como: 

$$\vec{l}_A=m(\vec{r}-\vec{r}_A)\times\vec{v}$$ 
Donde $\vec{r}$ y $\vec{v}$ son el vector posición y la velocidad de la partícula. Aun así, si nos enfocamos únicamente respecto un origen $O$, el vector $\vec{l_0}$ está dado por: 

$$\vec{l_0}=m\vec{r}\times\vec{v}$$ 
Así, de la misma forma, esto se puede extrapolar para todos los sistemas de coordenadas. En este caso, cartesianas y cilíndricas se tiene que: 

$$\vec{l_0}=\begin{cases}
m\begin{pmatrix}y\dot{z}-z\dot{y}\\
z\dot{x}-x\dot{z}\\
x\dot{y}-y\dot{x}\end{pmatrix}&\text{Coordenadas cartesianas}(\hat{x},\hat{y},\hat{z})\\\\
m\begin{pmatrix}r^2\dot{\theta}\\z\dot{r}-r\dot{z}\\-zr\dot{\theta}\end{pmatrix}&\text{Coordenadas cilíndricas}\;(\hat{k},\hat{\theta},\hat{r})\\\\ mr^2\dot{\theta}\hat{k}&\text{Coordenadas polares}\end{cases}$$ 
Notemos que la definición de momentum angular es muy similar a la definición de momento lineal, donde se define como $\vec{p}=m\vec{v}$. 

## Ecuación del Momento Angular 

A partir de la definición anterior, se podría derivar con respecto al tiempo el momentum: 

$$\frac{d\vec{l_0}}{dt}=\frac{d(\vec{r}\times\vec{p})}{dt}=\textcolor{red}{\frac{d\vec{r}}{dt}\times\vec{p}}+\vec{r}\times\frac{d\vec{p}}{dt}=\vec{r}\times\frac{d\vec{p}}{dt}$$ 
La última $\textcolor{red}{\text{cancelación}}$ se debe principalmente porque ambos son vectores paralelos. Luego, notemos lo siguiente: 

$$\begin{align}\frac{d\vec{p}}{dt}&=\frac{m\vec{v}}{t}\\\\
&=\vec{F}^{\text{Neta}}\end{align}$$ 
Por último, se puede concluir lo siguiente: 

$$\begin{align}
\frac{d\vec{l_0}}{dt}=\vec{r}\times\vec{F}^{\text{neta}}\end{align}$$ 
Dado que tenemos una fuerza neta, también se puede describir como la sumatoria de las fuerzas actuando en la partícula: 

$$\begin{align}
\frac{d\vec{l_0}}{dt}=\sum_i\vec{r}\times\vec{F_i}
\end{align}$$ 
Y, justamente, la suma de cada una de estas componentes es el **torque** de una fuerza $\vec{F_i}$ respecto al origen. Es decir: 

$$\begin{align}
\tau_i &= \vec{r}\times\vec{F_i}\\\\
\frac{d\vec{l_0}}{dt}&=\sum^{}_{i}\vec{\tau}=\vec{\tau_{\text{Neto}}}\end{align}$$ 