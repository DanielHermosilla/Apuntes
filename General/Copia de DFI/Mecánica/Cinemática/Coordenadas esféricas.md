
Corresponde a la proyección de vectores; 

![[CoordenadasEsfericas.png|center]]

Donde: 
$$z =\rho\cos\phi\;\land\;y=\rho\sin\phi\sin\theta\;\land\;x=\rho\sin\phi\cos\theta$$

### [[Posición]] 

La [[Posición|posición]] se caracteriza por 

$$\vec{r} = r\hat{r}$$ 
### [[Velocidad]] 

La [[Velocidad|velocidad]] se caracteriza por: 

$$\vec{v}=\dot{r}\hat{r} + r\frac{d\hat{r}}{dt}$$ $$\vec{v} = \dot{r}\hat{r} + r[\dot{\theta}\hat{\theta}+\sin(\theta)\dot{\phi}\hat{\phi}]$$ 
### Aceleración 

Tiene una componente en $\hat{r}$, $\hat{\theta}$ y $\hat{\phi}$. 

- $a_r = \ddot{r}  - r\dot{\theta}^2 - r\sin^2(\theta)\dot{\phi}^2$ 
- $a_\theta = 2\dot{r}\dot{\theta} + r\ddot{\theta} - r\sin(\theta)\cos(\theta)\dot{\phi}^2$ 
- $a_\phi = 2\dot{r}\sin(\theta)\dot{\phi} + 2r\cos(\theta)\dot{\theta}\dot{\phi} + r\sin(\phi)\ddot{\theta}$


#### Ejemplo 

Se tiene la siguiente figura, donde la [[Partícula|partícula]] se mueve bajo un radio $\rho_0$ , ángulo $\theta$  y velocidad constante.   

![[EjemploEsfericas.jpeg|center]]

Entonces, sabemos que: 

$$\dot{\theta} = \ddot{\theta} = 0$$

La partícula va bajando formando un ángulo $\alpha$ perpendicular al radio bajando con una velocidad $v_0$. 

Entonces; 

$$\vec{v} = \dot{r}\hat{r} + r\dot{\alpha}\hat{\alpha} + r\sin(\alpha)\dot{\theta}\hat{\theta}$$ $$\implies\vec{v} = \dot{r}\hat{r} + r\sin(\alpha)\dot{\theta}\hat{\theta}$$ 
$$\implies\vec{v} = -V_0\sin(\alpha)\hat{r} + V_0\cos(\alpha)\hat{\phi}$$ 
Entonces, la velocidad radial llegaría a ser: 

$$\hat{r} = -V_0\sin(\theta)$$
$$r - r_0 = -(V_0\sin(\theta))t$$ $$r(t) = r_0 - (V_0\sin(\alpha))t$$ 
Ahora para la velocidad en función de $\phi$: 

$$V_0\cos(\alpha) = r\sin\theta_0\dot{\phi}$$

Y también: 

$$\frac{d\theta}{dt} = \frac{V_0\cos\alpha}{r\sin\theta_0}$$ 
Entonces, si integramos en función de t: 

$$\int^{0}_{2\pi}d\phi = \frac{V_0\cos\theta}{\sin\theta_0}\int^{t*}_{0}\frac{1}{r_0 - v_0\sin\theta t}dt$$ 
Por conclusión se llega a 

$$2\pi = \frac{V_0\cos\theta}{\sin\theta_0}\frac{1}{V_0\sin\theta}\ln(\frac{r_0}{r_0 - v_0\sin(\theta)t^*})$$ 
 

