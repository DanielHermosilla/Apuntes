
Al tener la trayectoria no rectilinea y haber reconocido el [[Vector tangencial|vector tangencial]] como también la [[Aceleración|aceleración]] de la [[Partícula|partícula]], para calcular el radio $\rho$ del circulo osculador, se hace lo siguiente: 

$$\vec{a}\times\vec{v}=(\ddot s\hat{t} +\frac{\dot{s}^2}{\rho}\hat{n}\times(\dot{s}\hat{t}))$$ 
Equivalentemente, se tiene que: 

$$|\vec{a}\times\vec{v}| = \frac{\dot{s}^3}{\rho}\hat{n}\times\hat{t}| = \frac{v^3}{\rho}\implies\phi=\frac{v^3}{|\vec{a}\times\vec{v}|}$$ 
De otra forma, se podría ver al analizar la [[Velocidad|velocidad]] y la [[Aceleración|aceleración]]: 

$$\vec{v}=\dot{x}\hat{i} + \dot{y}\hat{j}$$
$$\vec{a} = \ddot{x}\hat{i} + \ddot{y}\hat{j}$$ 
Por lo tanto, ocupando la fórmula anterior, se llega que: 

$$\rho=\frac{(\dot{x}^2+\dot{y}^2)^{3/2}}{|(\ddot{x}\hat{i} + \ddot{y}\hat{j})\times(\dot{x}\hat{i} + \dot{y}\hat{j})|}$$

Simplificando todo, se puede llegar a que el **numerador** equivale a: 

$$\dot{x}^3(1 + (\frac{df}{dx})^2)^{\frac{3}{2}}$$ 
Y, simplificando el **denominador** se llega que: 

$$|\ddot{x}\dot{y}(\hat{i}\times\hat{j})-\ddot{y}\dot{x}(\hat{i}\times\hat{j})| = |\ddot{x}\dot{y}-\ddot{y}\dot{x}|$$ 
Además, se puede llegar que: 

$$\dot{y} = \frac{df}{dx}\dot{x}$$ $$\ddot{y} = \frac{d}{dt}(\frac{df}{dx}\dot{x}) = \frac{d}{dx}\;[\frac{df}{dx}\dot{x}]\;\dot{x}=\frac{d^2f}{dx^2}\dot{x} + \frac{df}{dx}\frac{d\dot{x}}{dx}\dot{x}\ \ \ \text{(Regla de la cadena)}$$ 
Por lo tanto, volviendo al **denominador**: 

$$|\ddot{x}\frac{df}{dx}\dot{x} - (\frac{d^2f}{dx^2}\dot{x}^2 + \frac{df}{dx}\ddot{x})\dot{x}| = |-\frac{d^2f}{dx^2}\dot{x}^3|$$ 
Por último, juntando el numerador con denominador, se llega a que: 

$$\rho = \frac{\dot{x}^3(1 + (\frac{df}{dx})^2)^{\frac{3}{2}}}{|-\frac{d^2f}{dx^2}\dot{x}^3|} = \frac{(1 + (\frac{df}{dx})^2)^{\frac{3}{2}}}{|\frac{d^2f}{dx^2}|} $$ 
### Ejemplo

Consideremos la curva $y = ax^2$ en el punto $(0,0)$
Sabemos que $\frac{df}{dx}=0$ y $\frac{df^2}{dx^2} = 2a$. 

Por lo tanto, el [[Radio de curvatura del circulo osculador|radio de curvatura del círculo osculador]] sería $\frac{1}{2a}$ 

![[EjemploOsculador.jpeg|center]]

