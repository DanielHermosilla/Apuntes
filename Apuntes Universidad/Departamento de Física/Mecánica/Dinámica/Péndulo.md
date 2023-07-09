
Se tiene la siguiente [[Partícula|partícula]], atada a una cuerda de largo $L$. Por lo tanto, es posible plantear las ecuaciones de movimientos a partir de [[Departamento de Física/Mecánica/Cinemática/Coordenadas polares|coordenadas polares]].  

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
Notemos que si $L\ddot{\theta}$ se podría tratar de resolver al resolver la EDO anterior. Pero se va a llegar a una solución **no analítica**. Pero, si es válido en ángulos chicos, donde $\sin(\theta)\approx\theta$. Se llega que: 

$$L\ddot{\theta} = g\theta$$ 
Donde la solución de la EDO es: 

$$C\cos(\omega_0t + \phi)$$ 
Con $\omega_0 = \frac{2\pi}{T}\implies T(\text{Período})=2\pi\sqrt{\frac{L}{g}}$ 