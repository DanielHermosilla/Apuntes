A partir de un parámetro **angular** y **radial** se puede definir la [[Posición|posición]] de una partícula-

Por lo tanto, si se tiene un vector $\hat\rho$ unitario que va siguiendo la partícula, entonces basta con definir la [[Posición|posición]] de la siguiente forma:

![[CoordenadaPolar.jpeg|center]]
$$\vec{r}=\rho\hat{\rho}$$ 
### Velocidad 

La [[Velocidad|velocidad]] se obtiene al derivar: 

$$\vec{v}=\dot{\rho}\hat{\rho} + \rho\frac{d\hat{\rho}}{dt}$$ 
También se puede definir un vector unitario perpendicular a $\hat{\rho}$ que se llamara $\hat{\theta}$.  
Donde $\hat{\rho}=\cos\theta\hat{i} + \sin\theta\hat{j}$ 

Por lo tanto, 

$$\frac{d\hat{\rho}}{dt} = \frac{d\hat\rho}{d\theta}\dot{\theta} = \dot{\theta}\hat{\theta}$$

Y se concluye que la [[Velocidad|velocidad]] en coordenadas polares se define como 

$$\vec{v} = \dot{\rho}\hat{\rho} + \rho(\dot{\theta})\hat{\theta}
$$
Que contiene componente radiales, en función de $\hat{\rho}$ y angulares en función de $\hat{\theta}$.  

O, análogicamente se podría calcular la derivada geométricamente: 

$$\frac{d\hat{\rho}}{dt} = \lim_{\Delta\rho\rightarrow 0}\frac{\hat{\rho}(\theta + \Delta\theta)-\hat{\rho}(\theta)}{\Delta\theta}=\frac{\Delta\hat{\rho}}{\Delta\theta}$$

![[EjemploPolares1.jpeg|center|400]]

 
Análogamente se puede ver de la siguiente forma: 

![[EjemploPolares2.jpeg|center|500]]

Por lo tanto: 
$$\Delta s = R\Delta\theta
$$
$$\implies\frac{|\Delta\vec{r}|}{\Delta\theta}\frac{\Delta s}{\Delta\theta} = R$$ 
### [[Aceleración]] 

La [[Aceleración|aceleración]] se obtiene al derivar la [[Velocidad|velocidad]]: 

$$\vec{a}=\frac{d\vec{v}}{dt}=\frac{d}{dt}(\dot{\rho}\hat{\rho} + \rho\dot{\theta}\hat{\theta})$$ 
Además se sabe que $\frac{d\hat{\rho}}{dt}= \dot{\theta}\hat{\theta}\ \land\ \frac{d\hat{\rho}}{d\theta}=\hat{\theta}\ \land\ \frac{d\hat{\rho}}{d\theta}=-\hat{\rho}\ \land\ \frac{d\hat{\theta}}{dt}=\dot{\theta}\hat{\theta}$.  

Por lo tanto, haciendo los cálculos: 

$$\vec{a} = (\ddot{\rho}-\rho\dot{\theta}^2)\hat{\rho}+(\rho\ddot{\theta}+2\dot{\rho}\dot{\theta})\hat{\theta}$$ 