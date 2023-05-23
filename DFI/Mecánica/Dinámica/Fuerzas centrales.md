
Son fuerzas que se definen como: 

$$\vec{F}= F(r)\hat{r}$$ 
Que se pueden definir como fuerzas de **atracción** o **repulsión**. Está demostrado que el [[Torque|torque]] es nulo. Por ende, por la [[Relación entre el Momento Angular y Torque|relación entre el momentum angular y el torque]], se llega que: 

$$\frac{d\vec{l_0}}{dt}=0\implies\vec{l_0}\;\;\text{Es constante}$$ 
Se tiene, además, que en $t=0$, $\vec{r}=\vec{r_0}$ y $\vec{v}=\vec{v_0}$ se llega que: 

$$\vec{l_0} = \vec{r_0}\times m\vec{v_0}$$ 
Donde se cumple que $\vec{r}\times m\vec{v}\cdot\vec{r}-\vec{r}\times mv_0\cdot\vec{r_0}=\vec{l_0}\cdot(\vec{r}-\vec{r_0})$. Notemos que $\vec{r}\cdot\vec{r}=0$ . En conclusión, se tiene que: 

$$(\vec{r}-\vec{r_0})\cdot\vec{l_0}=0\;\;\forall\vec{r}$$ 
Esto quiere decir que **la forma en que se mueve una [[Partícula|partícula]]  en un plano tiene un [[Momentum Angular|momentum angular]] que es siempre perpendicular**. 


## Conservación de la fuerza. 

Notemos que esta fuerza es **conservativa**. Si reescribimos la fuerza en [[Coordenadas polares|coordenadas polares]] se llega a lo siguiente: 

$$\vec{F}=F(\rho)\hat{\rho}$$ $$\vec{F}\cdot d\vec{r}=F(\rho)\hat{\rho}\cdot(d\rho\hat{\rho}+\rho d\theta\hat{\theta})$$ $$F\cdot d\vec{r}=F(\rho)d\rho = -dV$$ 
Por lo tanto, se define el potencial de la fuerza central como: 

$$V(\rho)=-\int F(\rho)d\rho + C$$ 
Por ende, se llega a lo siguiente: 

$$E_0 = \frac{1}{2}m(\dot{\rho}^2 + \rho^2\dot{\theta}^2)+V(\rho)$$ 
A partir de esto, se descubre la **ley de Kepler**. 


## Ejemplo 

Sea una plataforma horizontal  que está sometido a una fuerza central y sometida a una fuerza que tira hacia abajo: 

![[IMG_E923FFEF6838-1.jpeg|center]]

Por lo tanto, 

$$\vec{F_c}=-T\hat{\rho}$$ 
Notemos que $\dot{\rho}=V_1$

Posteriormente se tiene una velocidad hacia arriba. 

![[IMG_F0BCAF00492C-1.jpeg|center]]

Por definición, esto sería que la velocidad sea: 

$$\vec{v}=\dot{\rho}\hat{\rho}+\rho\dot{\theta}\hat{\theta}$$ 
Por conservación del [[Momentum Angular|momentum angular]], se tiene que $h=\rho_0 v_\theta$. Si se reemplaza $v_\theta$ se llega que: 

$$v_\theta=\frac{\rho_0 v_0}{\rho}$$ 
Entonces, $\vert\vec{v}\vert$ para $\rho=\frac{\rho_0}{2}$. Si se reemplaza todo en la velocidad final: 

$$\vec{v}=(-v_1)\hat{\rho}+2v_0\hat{\theta}$$ 
$$\vert\vec{v}\vert=\sqrt{v_{1}^{2}+4v_{0}^{2}}$$ 
Ahora, para encontrar la tensión, se ocupa la ecuación de movimiento en la dirección radial: 

$$m(\ddot{\rho}-\rho\dot{\theta}^2)=-T$$ $$T=m\rho\dot{\theta}^2 = m(\rho\dot{\theta})\dot{\theta}$$ 