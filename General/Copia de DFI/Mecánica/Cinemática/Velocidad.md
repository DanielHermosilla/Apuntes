
Corresponde a un vector que es la derivada del vector [[Posición|posición]]. 

$$\vec{v} = \frac{d\vec{r}}{dt}(t)=\lim_{\Delta t\rightarrow 0}\frac{\vec{r}(t + \Delta t) - \vec{r}(t)}{\Delta t} = \lim_{\Delta t\rightarrow 0}\frac{\Delta\vec{r}}{\Delta t}$$ 

### Ejemplo 

Se tiene la siguiente trayectoria de una [[Partícula|partícula]]: 

![[Velocidad.jpeg|center|600]]

Para poder calcular la velocidad habría que encontrar la derivada de la posición en el tiempo. Por lo tanto, se podría llegar a las siguientes equivalencias: 

$$\vec{v} = \frac{d\vec{r}}{dt}=\frac{d\vec{r}}{ds}\frac{ds}{dt}\ \ \ \text{(Regla de la cadena)}$$ 
O equivalentemente; 

$$\lim_{\Delta s\rightarrow 0}\frac{\Delta\vec{r}}{\Delta s}$$ 
Donde $\Delta s$ llegaría a ser lo siguiente: 

![[Velocidad2.jpeg|center|600]]

Si nos fijamos, cuando $\Delta s$ o la trayectoria tiende a 0, $\Delta\vec{r}$ también tiende a 0 al mismo tiempo, por lo tando, el límite llegaría a ser 1: 

$$\lim_{\Delta s\rightarrow 0}\frac{\Delta\vec{r}}{\Delta s} = 1$$ 
De aquí se concluye la gran conclusión sobre la velocidad: 

$$\vec{v} = \frac{ds}{dt}\hat{t}=\dot{s}\hat{t}$$ 
Donde $\dot{s}$ corresponde a la rapidez y $\hat{t}$ a un [[Vector tangencial|vector tangente]] a la trayectoria. 

De aquí nace la siguiente secuencia; la [[Posición|posición]] de una [[Partícula|partícula]] se puede describir a partir de su trayectoria y la trayectoria a partir del tiempo: 

$$\vec{r}\rightarrow s\rightarrow t$$ 
Por lo tanto, de ahí nace la regla de la cadena, ya que la posición depende de la trayectoria y la trayectoria del tiempo. 