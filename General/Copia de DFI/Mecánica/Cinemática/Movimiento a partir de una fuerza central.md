
Recordando la ecuación de [[Cinemática|movimiento]] en [[Coordenadas cilíndricas|coordenadas cilíndricas]]:

$$m(\ddot{\rho}-\rho\dot{\theta}^2) = f(\rho)$$ 
Y acordándonos que la variable $h$ es constante.
$$\rho^2\dot{\theta}=h$$ 
También, definiendo la nueva variable, $\xi=\frac{1}{p}$ . Entonces, en el eje $\hat{\theta}$ se tiene: 

$$\dot{\theta}=\frac{h}{\rho^2}=h\xi^2$$ 
Primero, buscando la derivada de $\rho$ respecto al tiempo es equivalente a lo siguiente: 

$$\frac{d\rho}{dt}=\frac{d}{dt}(\frac{1}{\xi})=\frac{d}{d\theta}(\frac{1}{\xi})\frac{d\theta}{dt}=-\frac{1}{\xi^2}\frac{d\xi}{d\theta}h\xi^2=-h\frac{d\xi}{d\theta}$$

Ahora, para conseguir $\ddot{\rho}$, derivamos de nuevo. 

$$\ddot{\rho}=\frac{d}{dt}\left[-h\frac{d\xi}{d\theta}\right]\frac{d\theta}{dt}$$ $$\ddot{\rho}=-h\frac{d^2\xi}{d\theta^2}(h\xi^2)$$ 
Entonces, reemplazando en la ecuación de movimiento: 

$$m(-h\frac{d^2\xi}{d\theta^2}(h\xi^2)-\frac{1}{\xi}h^2\xi^4)=f(\frac{1}{\xi})$$ 
Factorizando se llega que: 

$$-mh^2\xi^2\left[\frac{d^2\xi}{d\theta^2}+\xi\right]=f(\frac{1}{\xi})$$ 
Esto se llama la **ecuación de Binet**. 

Ahora, si nos acordamos de la **fuerza gravitatoria**, se llega que: 

$$-mh^2\xi^2\left[\frac{d^2\xi}{d\theta^2}+\xi\right]=-GMm\xi^2$$ $$\frac{d^2\xi}{d\theta^2}+\xi=\frac{GM}{h^2}$$ 
Si se resuelve la EDO, la solución queda como: 

$$\xi(\theta)=\frac{GM}{h^2} + A\cos(\theta-\delta)$$
$$\iff\rho(\theta)=\frac{1}{\frac{GM}{h^2}+A\cos(\theta-\delta)}$$ 
Entonces, para encontrar las constantes, es necesario encontrar lo siguiente: 

$$\theta_0\;\;\frac{d\xi}{d\theta}\bigg\vert_{\theta_0}=-\frac{1}{\rho^2}\frac{d\rho}{d\theta}\bigg\vert_{\theta_0}$$ 
## Secciones cónicas 

Tenemos la siguiente sección cónica, definida por un punto focal y un eje polar: 

![[IMG_396909361349-1.jpeg|center]]

Tenemos que $p$ es la distancia con una recta arbitraria (la directriz). Entonces, la ecuación de este punto geométrico es la siguiente: 

$$\rho(\theta)=\frac{ep}{1+e\cos(\theta-\delta)}$$ $$\rho(\theta)=\frac{ep}{1 + e\cos(\theta)}$$ 
Donde $\frac{\delta}{p-\rho\cos(\theta-\delta)}=e$ (excentricidad de la cónica). Entonces, de tal forma se podría encontrar $\rho_0$, donde: 

$$\rho_0=\frac{ep}{1 + e}$$ 
Y por último, 

$$ep=\rho_0(1+e)$$ $$\implies\rho(\theta)=\rho_0\frac{(1+e)}{1+e\cos(\theta)}$$ 
Entonces, ahora se hace el análisis con la excentricidad.  Veamos que si la excentricidad es $0$ se tiene una circumferencia, y se llegaría que: 

$$\rho(\theta)=\rho_0$$ 
En un segundo caso, donde $0<e<1$,  donde el máximo de $\rho$ se produce en el mínimo de $\cos(\theta)$.  Lo llamaremos $\rho_1:$

$$\rho_1 = \rho_0\frac{1+e}{1-e}$$

Entonces, queda una trayectoria elíptica:

![[IMG_A94C81DE0AA2-1.jpeg|center]]

Por el otro lado, cuando la excentricidad es 1 se tiene una parábola. 

Por último, en $e>1$ se tiene una hipérbola

![[IMG_47CBAC655B06-1.jpeg|center|400]]


Ahora, haciendo la conexión con la [[Cinemática|cinemática]]:

$$\rho=\rho_0\frac{1+e}{1+e\cos(\theta)}\;\;\bigg\vert\;\;\rho=\frac{\frac{h^2}{GM}}{1+\frac{Ah^2}{GM}\cos(\theta)}$$ 
Para hacer parecer la **ecuación de Binet** con la cónica, definimos $\rho_0(1+e)=\frac{h^2}{GM}$ y también $e=\frac{Ah^2}{GM}$  



