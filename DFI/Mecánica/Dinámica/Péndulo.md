
Se tiene la siguiente [[Partícula|partícula]], atada a una cuerda de largo $L$. Por lo tanto, es posible plantear las ecuaciones de movimientos a partir de [[Coordenadas polares|coordenadas polares]].  

![[Péndulo.jpeg]]

Entonces,  se sabe que, en las coordenadas $\hat{\rho}$ se tiene que: 

$$m(\ddot{\rho}-\rho\dot{\theta}^2) = mg\cos(\theta) - T$$ 
Si analizamos el caso donde la cuerda siempre está tensa, $\dot{\rho} = \ddot{\rho} = 0$, entonces, se llega que: 

$$-mL\dot{\theta}^2 = mg\cos(\theta) - T$$ 
$$\implies T = mg\cos(\theta) + mL\dot{\theta}^2$$ 
Para obtener $\dot{\theta}$ se obtiene a través de la segunda ecuación en $\hat{\theta}$:

$$m(\rho\ddot{\theta} + 2\dot{\rho}\dot{\theta}) = -mg\sin(\theta)$$ 
Imponiendo la condición the $\dot{\rho} = 0$, entonces: 

$$L\ddot{\theta} = g\sin(\theta)$$ $$\dot{\theta}d\dot{\theta} = \frac{g}{L}\sin(\theta)d\theta$$ 
Entonces, se integra del inicio al final: 

$$\int_{\frac{v_0}{L}}^{\dot{\theta}}\dot{\theta} = \int_{\theta_0}^{\theta}\frac{g}{L}\sin(\theta)d\theta$$ 
Lo que se llega que: 

$$\dot{\theta}^2 = \left[(\frac{V_0}{L})^2-\frac{2g\cos(\theta)}{L}\right] + \frac{2g}{L}\cos(\theta)$$ 