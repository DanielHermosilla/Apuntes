# Energía cinética 

Corresponde a la variable que hacer cambiar la magnitud del vector de momentum. En este caso, se denominará por la variable $K$, que subyace de la ecuación de Newton: 

$$m\frac{d\vec{v}}{dt} = m\left(\frac{dv}{dt}\hat{t}+\frac{v^2}{\rho}\hat{n}\right)=\vec{F}$$ 

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

$$\epsilon=\frac{1}{2}\dot{r}^2+\frac{1}{2}\frac{h^2}{r^2}\frac{C}{r}$$ 
Entonces, se llega a la energía potencial (que es siempre constante) en función del radio. En específico, si se elige evaluar en $r_0$ (punto de trayectoria más cercano al origen) de forma conveniente (ya que $\dot{r}(r_0)=0$). De esta forma: 

$$\epsilon=\frac{1}{2}\;\frac{h^2}{r_{0}^{2}}-\frac{C}{r_0}$$ 
Y el radio mínimo se obtiene por la ecuación de la trayectoria:

$$r_0 =\frac{1}{\frac{C}{h^2}+A}$$ 
Juntando toda esta información, se puede despejar la constante $A$: 

$$A=\frac{C}{h^2}\sqrt{1+\frac{2\epsilon h^2}{C^2}}$$ 
Entonces, con la información completa, se llega que **la ecuación de la trayectoria** es la siguiente: 

$$r(\theta)=\frac{\frac{h^2}{C}}{1+\sqrt{1+\frac{2\epsilon h^2}{C^2}}\cos(\theta-\delta)}$$ 
### Análisis geométrico 

La trayectoria que se llego anteriormente describe una curva cónica. Es decir, se define geométricamente a partir de un foco y una recta llamada directriz: 

![[Captura de pantalla 2023-06-09 a la(s) 11.58.51.png|center]]


La cónica se forma por los puntos formados a partir de la distancia proporcional entre el foco y la directriz. Esta constante de proporcionalidad se domina excentricidad, $e$. De acuerdo a la figura, se tendría la siguiente ecuación: 

$$\overline{PF}=e\overline{PQ}$$ 
Si se utilizara un sistema polar, se cumpliría que: 

$$\begin{align}
\overline{PF}&=r\\\\\overline{PQ}&=d-r\cos(\theta-\delta)
\end{align}$$

Donde $d$ es la distancia entre el foco y la directriz. 

Entonces, si se ocupara la ecuación del movimiento orbital, se llega a lo siguiente: 

$$r(\theta)=\frac{ed}{1+e\cos(\theta-\delta)}$$ 
Donde el radio mínimo correspondería cuando $\cos=1$, es decir: 

$$r_0=\frac{ed}{1+e}$$ 

Por lo tanto, se podría eliminar $d$ en función del ángulo mínimo: 

$$r(\theta)=\frac{r_0(1+e)}{1+e\cos(\theta-\delta)}$$

Ahora, si se establece que $r(\theta=0)=r_0$: 

$$\begin{align}
r(\theta)&=\frac{h^2/C}{1+\sqrt{1+\frac{2\epsilon h^2}{C^2}}\cos(\theta)}\\\\r(\theta)&=\frac{r_0(1+e)}{1+e\cos(\theta)}
\end{align}$$

Por ende, las relaciones geométricas y físicas se determinan por las siguientes variables: 

$$\begin{align}
r_0&=\frac{h^2/C}{1+\sqrt{1+\frac{2\epsilon h^2}{C^2}}}\\\\e&=\sqrt{1+\frac{2\epsilon h^2}{C^2}}
\end{align}$$
 
Por lo tanto, a partir de esto, se pueden reconocer los siguientes tipos de órbitas: 

#### Órbita circular 

En una órbita circular de radio $R$ el radio se mantiene constante. Por lo tanto, se debe cumplir que: 

$$\begin{align}
\sqrt{1+\frac{2\epsilon h^2}{C^2}}
 &= 0\\\\e&=0\end{align}$$

Por lo tanto, haciendo relación con la energía mecánica por unidad de masa $\epsilon$, el momentum angular por unidad de masa $h$, se puede hacer la relación de la energía mecánica total en función de $R$: 

$$\begin{align}
\epsilon &=-\frac{C}{2R}\;\;\;\;\text{(Energía mecánica por unidad de masa)}\\\\\implies V &= -\frac{C}{R}\;\;\;\;\text{(Energía potencial por unidad de masa)}\\\\ 
\implies K&=\frac{C}{2R}\;\;\;\;\text{(Energía cinética por unidad de masa)}
\end{align}$$

#### Orbita elíptica 

Para tener una órbita elíptica, se debe cumplir que la excentricidad sea menor que 1. En este caso, la partícula se relaciona entre un radio mínimo y máximo por la siguiente ecuación: 

$$r_{\max}=r_0\frac{1+e}{1-e}$$ 
Además, se establece que la energía mecánica debe ser menor a cero. Muchas veces, en el análisis elíptico, se busca realizar el análisis según los semi-ejes de la elipse: 

![[Captura de pantalla 2023-06-11 a la(s) 14.37.44.png|center]]

Por lo tanto, se llega a lo siguiente: 

$$\text{Semiejes de la elipse}=\begin{cases}a=\frac{r_0}{1-e}&\text{(Semieje mayor)}\\\\ b=r_0\sqrt{\frac{1+e}{1-e}}&\text{(Semieje menor)}\end{cases}$$ 

#### Orbita parabólica 

Para tener una órbita parabólica se debe cumplir que $e=1$ y $\epsilon=0$.  Por ende, la fórmula del movimiento llega a ser la siguiente: 

$$r(\theta)=\frac{2r_0}{1+\cos(\theta)}$$ Descrito por la siguiente imagen: 

![[Captura de pantalla 2023-06-11 a la(s) 14.44.09.png|center|500]]

Lo importante de estas orbitas es su definición de **órbitas de escape**, es decir, cuando una partícula está en una órbita cerrada (ya sea circular o elíptica) y se le da un impulso tal que su energía $\epsilon=0$, entonces la partícula adoptaría una órbita parabólica que determinaría la velocidad mínima de escape. Donde se llega a lo siguiente: 

$$v_e=\sqrt{\frac{2C}{R}}$$ 
#### Orbita hiperbólica 

Corresponde a las órbitas que cumplen las condiciones $e>1$ y $\epsilon>0$. Estas órbitas son abiertas y se aproximan asintoticamente a rectas cuando el radio tiene a infinito: 

![[Captura de pantalla 2023-06-11 a la(s) 14.47.10.png|center|550]]

### Diagramas paramétricos 

En la sección anterior se hizo un gran análisis a los distintos tipos de órbitas según sus características físicas. Pero, el análisis se hizo para el caso puntual de una fuerza gravitatoria. Ahora, si se extrapola a un análisis general, se puede obtener el tipo de trayectoria según los distintos parámetros. 

- **Excentricidad**: Para saber el tipo de órbita a partir de la excentricidad se cumple lo siguiente: 

![[Captura de pantalla 2023-06-11 a la(s) 14.51.29.png|center|550]]

- **Energía y momento angular**: Dado una energía mecánica $\epsilon$ y un momentum angular $h$ se puede encontrar el tipo de órbita según el siguiente diagrama: 

![[Captura de pantalla 2023-06-11 a la(s) 14.53.22.png|center|550]]

Donde se llega a lo siguiente: 

$$\begin{align}
\epsilon&=-\frac{C^2}{2h^2}&\text{(Órbita circular)}\\\\\epsilon&<0&\text{(Órbita elíptica)}\\\\\epsilon&=0&\text{(Órbita parabólica)}\\\\\epsilon&>0&\text{(Órbita hiperbólica)}
\end{align}$$

- **Potencial efectivo**: Para el caso de las fuerzas gravitacionales, se tiene que el potencial efectivo es el siguiente: 

$$V_*(r)=\frac{h^2}{2r^2}-\frac{C}{r}$$ 
Acordándonos de lo que significa en sí el potencial efectivo, sabemos que ante una órbita circular y elíptica la partícula no puede escapar del pozo de potencial. La órbita parabólica nos indicaba la condición de velocidad mínima para escapar de este pozo y la órbita hiperbólica llegaría a ser cuando se escapa por completo del pozo. Entonces se llega al siguiente diagrama: 

![[Captura de pantalla 2023-06-11 a la(s) 15.01.03.png|center|600]]



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

Ahora, intuitivamente para analizar la velocidad se tendría que derivar la trayectoria. Por lo tanto, se llega a lo siguiente: 

$$\vec{v}=\textcolor{#8639A2}{\vec{V_0}}+\textcolor{#397FA2}{\frac{d\vec{r}'}{dt}}$$ 
Donde $\textcolor{#8639A2}{\vec{V_0}}$ representa la velocidad del sistema de referencia nuevo en función del actual. Por el otro lado, $\textcolor{#397FA2}{d\vec{r}'/dt}$ sería la velocidad de la partícula en el nuevo sistema de referencia.  Eso si, hay que tener mucho cuidado en lo que realmente representa $\textcolor{#397FA2}{d\vec{r}'/dt}$, ya que se está derivando un vector cuyas abscisas **podrían estar en movimiento** en caso de tener rotación. Por lo tanto, los vectores unitarios ya no tendrían una derivada nula. Teniendo esto en consideración, se llega al siguiente cálculo: 

$$\begin{align}\textcolor{#397FA2}{\frac{d\vec{r}'}{dt}}=\dot{\begin{pmatrix}\dot{x}\\\dot{y}\\\dot{z}\end{pmatrix}}&=\dot{x}'\dot{\hat{x'}} + \dot{y}'\dot{\hat{y'}} + \dot{z}'\dot{\hat{z'}}\\\\&=\textcolor{#3AB9BD}{\dot{x}'\hat{x'} + \dot{y}'\hat{y'} + \dot{z}'\hat{z'}} + \textcolor{#3EBD3A}{ x'\dot{\hat{x'}} + y'\dot{\hat{y'}} + z\dot{\hat{z'}}}\end{align}$$

Por lo tanto, ya que derivamos un vector, notemos que todos los términos en $\textcolor{#3AB9BD}{azul}$ corresponderían, justamente, a la velocidad de la partícula en función del nuevo sistema de referencia. Por lo tanto, toda esa suma de términos se le podría denominar por $\textcolor{#3AB9BD}{\vec{V'}}$. 

Por el otro lado, los sumandos asociados al color $\textcolor{#3EBD3A}{\text{verde}}$ son aquellos términos asociados a la derivada de los $\textcolor{#3EBD3A}{\text{ejes del nuevo sistema de referencia}}$. Por eso mismo, dado que esto representa la rotación, se podría denominar por $\textcolor{#3EBD3A}{\Omega_e\times\vec{r}'}$. Por ende, volviendo a la ecuación original, se llega a lo siguiente: 

$$\vec{v} = \vec{V_0} + \vec{v'} + \vec{\Omega_e}\times\vec{r'}$$ 
Ahora, para obtener la aceleración se hace el mismo procedimiento anterior. Para derivar un producto cruz se hace como si fuera una multiplicación. Acordándonos que la derivada de la rotación se denotaba como $\alpha$, se llega a lo siguiente: 

$$\vec{a}=\vec{A_0} + \vec{a'} + 2\vec{\Omega_e}\times\vec{v'}+\vec{\Omega_e}\times\left(\vec{\Omega_e}\times\vec{r'}\right)+\vec{\alpha_e}\times\vec{r'}$$ 
Ahora, si se multiplica esta ecuación por la masa de la partícula se puede llegar a la segunda ley de Newton: 

$$\begin{align}\vec{F^{\text{neta}}}&=m\vec{A_0}+m\vec{a'}+2m\vec{\Omega_e}\times\vec{v'}+m\vec{\Omega_e}\times\left(\vec{\Omega_e}\times\vec{r'}\right)+m\vec{\alpha_e}\times\vec{r'}\\\\\implies m\vec{a'}&=\vec{F^{\text{neta}}}-m\vec{A_0}-2m\vec{\Omega_e}\times\vec{v'}-m\vec{\Omega_e}\times\left(\vec{\Omega_e}\times\vec{r'}\right)-m\vec{\alpha_e}\times\vec{r'}\end{align}$$ 
Esta ecuación nos dice, por lo tanto, que al obtener una ecuación de movimiento de una partícula ocupando un sistema de referencia no inercial, entonces se debe corregir la ecuación de movimiento agregando fuerzas "reales", que son las que conforman $\vec{F^{\text{neta}}}$ .

Al fijarnos en cada ecuación, podemos ver que se *crean* cuatro fuerzas nuevas. Cada una tiene su respectiva clasificación y esta asociada a los componentes $\vec{A_0}$, $\vec{\Omega_e}$ y $\vec{\alpha_e}$. 

- **Fuerza inercial por aceleración de O:** Corresponde a la fuerza $\vec{F_0}=-m\vec{A_0}$. Notar que esta fuerza depende únicamente entre la cinemática del sistema de referencia original y el nuevo. 

- **Fuerza de Coriolis**: Corresponde a la fuerza $\vec{F_{co}}=-2m\vec{\Omega_e}\times\vec{v }$. Esta fuerza existe cuando los ejes del sistema inercial rotan y la partícula se mueve dentro de este sistema. Si la partícula está en reposo, la fuerza de Coriolis que ella "siente" es nula. 

- **Fuerza Centrífuga**:  Corresponde a la fuerza $\vec{F_{cf}}=-m\vec{\Omega_e}\times(\vec{\Omega_e}\times\vec{r'})$ . Esta fuerza existe cuando ocurre una rotación dentro de los ejes del sistema inercial.  Si se efectúan los productos correspondientes se llega que la magnitud es $\vert\vec{F_{cf}}\vert=md\Omega_{e}^{2}$, donde $d$ es la distancia entre la partícula y el eje de rotación. 

- **Fuerza Transversal:** Corresponde a la fuerza $\vec{F_T}=-m\vec{\alpha_e}\times\vec{r}$.  Esta fuerza existe cuando los ejes del sistema de referencia no inercial tiene una rotación no constante. 

