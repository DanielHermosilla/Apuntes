
Nace de tratar de explicar las fuerzas de atracción entre cuerpos celestes. Donde se plantea lo siguiente: 

$$|\vec{F_{12}}| = G\frac{m_1m_2}{r^2}$$ 
Donde $G$ es una constante. 

Ahora, si se quisiera encontrar la fuerza de atracción que ejerce una [[Partícula|partícula]] diminuta en la tierra, considerando que es tridimensional, se tendría que llegar a lo siguiente: 

$$|\vec{F_{12}}| = G\frac{dm\;m_2}{r^2}$$ 

![[AtraccionGravitacional.jpeg|center]]

Se tendría que hacer un análisis geométrico

![[AtracciónGravitacional 3.jpeg]]

Y asumir un [[Sistema de referencia|sistema de coordenada]] esféricas. El volúmen de $dm$ llegaría a ser $(dr)(rd\theta)(r\sin\theta d\theta)$  dado a lo siguiente: 

![[AtracciónGravitacional 2.jpeg]]

Entonces, la fuerza llegaría a ser la siguiente integral: 

$$F_g = GmD\int\int\int^{}_{\theta\phi r}\frac{\cos(\theta)r^2\sin(\theta)drd\theta d\phi}{(R^2 + (R+2)^2 - 2R(R+Z)\cos\theta)}$$

Esta integral tiene como solución lo siguiente: 

$$F_g = \frac{GmM_t}{(R+z)^2}$$ 
Donde:
$$\frac{GM_t}{R_{T}^{2}} = g = 9.807 m/s^2$$ 
Si se quisiera saber la fuerza gravitatoria cuando ya se pasa el radio de la tierra, se podría definir la siguiente función: 

$$f(z) = (R+z)^{-2}$$ 
Donde $z$ es la distancia tomando como referencia el *piso* de la tierra. 

$$f(z) = f(z=0)