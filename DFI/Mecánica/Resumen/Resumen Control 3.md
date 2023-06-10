
# Momento Angular  

Notemos que la rotación de una partícula no solamente depende del momentum $\vec{p}$ de la partícula, si no también del punto respecto del cual se está observando.

![[Ecuación Binet.png|center|500]]


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

# Torque 

A partir del análisis anterior, se puede llegar a analizar que el toque es aquel que hace cambiar el movimiento angular de una partícula. Por lo tanto, se puede definir de las siguientes dos maneras: 

$$\begin{align}\vec{\tau_0}&=\vec{r}\times\vec{F}\\\\\vert\vec{\tau_0}\vert&=\vert\vec{r}\vert\;\vert\vec{F}\vert\sin(\alpha)\end{align}$$ 

# Momento angular constante 

Notemos que el caso más notorio del momento angular es cuando éste se mantiene constante. Notemos que por la ecuación anterior, se había llegado a lo siguiente: 

$$\begin{align}\frac{d\vec{l_0}}{dt}&=\vec{\tau_0}\\\\
\implies\vert\vec{\tau_0}\vert&=0\end{align}$$ 
Es decir, **el momento angular es constante cuando el torque es nulo**. Por esto mismo, se puede llegar a concluir que esto ocurre cuando los vectores de posición **se mantienen en el mismo plano de la trayectoria**.  Por esto mismo, el movimiento de la partícula deja de ser tridimensional. Por ende, acordándonos de la definición del torque en coordenadas polares se llega que: 

$$mr^2\dot{\theta}=\text{cte}$$ 
# Fuerzas Centrales 

A partir del caso anterior, se introduce el concepto de fuerzas centrales, donde se tiene el movimiento de una masa sometida a una acción de una fuerza central única: 

$$\vec{F}=F(r)\hat{r}$$ 
Es decir, a partir de un sistema polar de coordenadas, la fuerza tiene una magnitud que sólo depende de la distancia de la partícula al centro de la fuerza y tiene dirección radial. Nuevamente, el torque es nulo, el momento angular se conserva. Por lo tanto, se introduce el nuevo concepto de $h$, que significa la magnitud del momento angular por unidad de masa: 

$$\begin{align}
\vec{l_0}&=mr^2\dot{\theta}\hat{k}=\text{constante}\\\\
\textcolor{green}{h}&=\textcolor{green}{r^2\dot{\theta}}\\\\
\vec{l_0}&=m\textcolor{green}{h}\hat{k}
\end{align}$$ 

Las fuerzas centrales también representan la características de ser **fuerzas conservativas,** es decir, la partícula conserva su energía mecánica total. Por lo tanto, también se puede definir su energía mecánica por unidad de masa: 

$$\epsilon=\frac{E_M}{m}$$ 
## Ecuación de Binet 

Dada las condiciones iniciales, se tiene que la ecuación de movimiento de la partícula en la dirección radial es: 

$$m(\ddot{r}-r\dot{\theta}^2)=F(r)$$ 
Ahora, si consideramos únicamente su aceleración en la dirección radial, se llega que: 

$$\ddot{r}-r\dot{\theta}^2=a_r$$ 
Acordándonos de la definición de $h$, donde $\textcolor{green}{h=r^2\dot{\theta}}$, se puede despejar el ángulo $\theta$ (acordándonos de que imponemos que $h$ es constante):

$$\begin{align}
\dot{\theta}&=\frac{h}{r^2}\\\\
\implies\ddot{r}-\frac{h^2}{r^3}&=a_t
\end{align}$$ 
Se llega a una ecuación diferencial, cuya solución es la siguiente, haciendo el cambio de variable $\zeta=\frac{1}{r}$. 

$$-h^2\zeta^2(\frac{d^2\zeta}{d\theta^2}+\zeta)=a_t$$ 
Es importante considerar esta ecuación ya que se ocupará después para el análisis de cónicas. 

## Orbitas gravitacionales 

Un caso particular de una fuerza central es la de atracción gravitacional, definida como: 

$$F(r)=-\frac{GMm}{r^2}$$ 
Acordándonos del cambio de variable anterior, donde $\zeta=\frac{1}{r}$, se puede llegar que la aceleración resulta ser: 

$$a_t(\zeta)=-GM\zeta^2$$ 
Dado que tenemos la ecuación gravitacional, se puede reemplazar la aceleración en la ecuación de Binet: 

$$\frac{d^2\zeta}{d\theta^2} + \zeta = \frac{C}{h^2}$$ 
Donde $C=GM$. Nuevamente se llega a una ecuación diferencial. Se puede resolver rápidamente, donde se llega a lo siguiente: 

- Homogénea: 

$$\begin{align}
\frac{d^2\zeta}{d\theta^2}+\zeta &= 0\\\\
\lambda^2 + 1 &= 0\\\\ 
\implies\lambda_{1,2}&\pm i
\end{align}$$ 
Por lo tanto la solución homogénea es la siguiente: 

$$A\cos(\theta)+B\sin(\theta) = 0$$ 
Aquí las ecuaciones se pueden sobreponer, donde se llega que: 

$$A\cos(\theta-\delta) = 0$$ 
- Particular: 

Ocupando coeficientes indeterminados, imponemos lo siguiente: 

$$\begin{align}
At + B &= \frac{C}{h^2}\\\\
\implies A &= \left(\frac{C}{h^2}\right)'=0
\end{align}$$


Por lo tanto, la solución general sería la suma de ambas soluciones donde se llega que: 

$$\zeta(\theta)=A\cos(\theta-\delta)+\frac{C}{h^2}$$ 
Ahora, deshaciendo el cambio de variable $\zeta=\frac{1}{r}$, la trayectoria es: 

$$r(\theta)=\frac{1}{\frac{C}{h^2}+A\cos(\theta-\delta)}$$ 

### Ecuación física de la trayectoria 

Ahora, tratando de despejar la constante $A$, se puede aprovechar de la definición anterior de $\epsilon$ como la energía mecánica por unidad de masa. 

$$\epsilon = \frac{1}{2}v^2 + V(r)$$ 

Donde $V(r)$ es la energía potencial por unidad de masa asociada a la fuerza de atracción gravitacional: 

$$V(r)=-\frac{GM}{r}=-\frac{C}{r}$$ 
Entonces, la energía mecánica por unidad de masa queda expresado por lo siguiente (reemplazando la definición de velocidad en polares):

$$\epsilon=\frac{1}{2}\left(\dot{r}^2+(r\dot{\theta})^2\right)-\frac{C}{r}$$ 
Nuevamente, se puede ocupar la siguiente igualdad: 

$$\textcolor{green}{h= r^2\dot{\theta}}$$ 
Entonces, la energía mecánica queda como: 

$$\epsilon=\frac{1}{2}\dot{r}^2 + \frac{1}{2}\frac{h^2}{r^2}-\frac{C}{r}$$ 
Entonces, se llega a la energía potencial (que es siempre constante) en función del radio. En específico, si se elige evaluar en $r_0$ (punto de trayectoria más cercano al origen) de forma conveniente (ya que $\dot{r}(r_0)=0$). De esta forma: 

$$\epsilon=\frac{1}{2}\;\frac{h^2}{r_{0}^{2}}-\frac{C}{r_0}$$ 
Y el radio mínimo se obtiene por la ecuación de la trayectoria:

$$r_0 =\frac{1}{\frac{C}{h^2}+A}$$ 
Juntando toda esta información, se puede despejar la constante $A$: 

$$A=\frac{C}{h^2}\sqrt{1+\frac{2\epsilon h^2}{C^2}}$$ 
Entonces, con la información completa, se llega que **la ecuación de la trayectoria** es la siguiente: 

$$r(\theta)=\frac{\frac{h^2}{C}}{1+\sqrt{1+\frac{2\epsilon h^2}{C^2}}\cos(\theta-\delta)}$$ 
Se llega al siguiente esquema: 

![[Captura de pantalla 2023-06-09 a la(s) 11.58.51.png|center]]



# Movimiento Relativo 

Ocurre cuando el sistema de referencia está en movimiento en relación a la partícula en estudio

![[Captura de pantalla 2023-06-09 a la(s) 15.00.34.png|center|600]]


Para describir un sistema de referencia no inercial,  hay que describir de forma precisa su no inercialidad con respecto a un sistema de referencia inercial. Supongamos, entonces, que este sistema se va a denominar $\textcolor{#4A72A8}{S}$, respecto al cual se va a describir el movimiento de una partícula en $\textcolor{#39A251}{S'}$. La forma en que puede moverse $\textcolor{#39A251}{S'}$ incluye **rotación** y **traslación**. 

La traslación se describirá con el vector $\vec{R_0}(t)=O\vec{O}'$. Es decir, el vector posición del origen $O'$ referido al punto de origen del sistema inercial. 

Por el otro lado, la rotación sera medida mediante una velocidad angular, $\vec{\Omega_e}(t)$ , que es la velocidad angular de los ejes de $\textcolor{#39A251}{S'}$ respecto direcciones fijas del sistema $\textcolor{#4A72A8}{S}$. Por último, si esta rotación cambia con respecto al tiempo, se denomina el vector de aceleración angular $\vec{\alpha_e}=\dot{\vec{\Omega}_e}$. 

![[Captura de pantalla 2023-06-09 a la(s) 15.14.33.png|center|600]]


Para analizar los sistemas no inerciales, es bueno partir con dos ejemplos particulares. En el caso a) el origen $O'$ rota en torno al origen con velocidad angular constante pero los ejes de $S'$ no giran. Entonces: 

$$\begin{align}
\vec{A_0}&=-R\omega_{0}^{2}\hat{u}\;\;\;\text{(Velocidad angular)}\\\\\vec{\Omega_e} &= \vec{0}\\\\\vec{\alpha_e}&=\vec{0}\end{align}$$

Notemos que $\ddot{R_0}=\vec{A_0}$ existe a pesar que la magnitud de $R$ siempre es igual, ya que la dirección va cambiando. 

Ahora, para el caso de b), se tiene una rotación, por lo tanto: 

$$\begin{align}
\vec{A_0}&=-R\omega_{0}^{2}\hat{u}\;\;\;\text{(Velocidad angular)}\\\\\vec{\Omega_e} &= \omega_0\hat{k}\\\\\vec{\alpha_e}&=\vec{0}\end{align}$$

Ahora, en este caso, existe rotación **constante**, por eso mismo $\vec{\Omega}_e$ tiene magnitud pero $\vec{\alpha}=0$.  Eso si, cuando existen rotación, hay que estudiar los ejes del sistema  $\textcolor{#39A251}{S'}$. 


## Análisis de Movimiento 

Ahora, si se quisiera hacer el análisis analítico de este tipo de sistemas, hay que fijarnos en la siguiente figura: 

![[Captura de pantalla 2023-06-10 a la(s) 13.23.22.png|center|500]]


Lo primero a notar es que el movimiento *real* o que interesa estudiar es, en realidad, una suma vectorial entre el movimiento del sistema no inercial y de la partícula. Es decir, la ecuación de la trayectoria llegaría a ser la siguiente:

$$\vec{r}(t)=\vec{R_0}(t) + \vec{r'(t)}$$

