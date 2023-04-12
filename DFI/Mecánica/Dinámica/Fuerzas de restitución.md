Aquellas fuerzas que tratan de restituir una posición de equilibrio. El más común es el **resorte**. 

## Resorte 

Tienes dos atributos importantes, su largo natural donde no se ejerce ninguna fuerza de restitución y su constante elástica. Es decir, cuando se extiende más de su largo natural, ocurre una fuerza que lo restituye para querer volver al largo natural. 

Sea la siguiente situación, donde la masa experimenta únicamente la fuerza elástica. 

![[resorte.jpeg]]

Entonces su movimiento en $x$ se puede describir por: 

$$m\ddot{x} = -k(x-l_o)$$ 
Esto queda de la forma de una EDO, donde la solución particular es $x=l_0$ y la homogénea sería: 

$$\ddot{x} + \frac{k}{m}x = 0$$ 
Por lo tanto, un cambio de variable podría ser $\omega_{0}^{2} = \frac{k}{m}$ . Por ende: 

$$\ddot{x} + \omega_{0}^{2}x = 0$$ 
Donde se llega que: 

$$x(t) = \cos(\omega_0 t)$$
$$\dot{x}(t) = -\omega_0\sin(\omega_0 t)$$ $$\ddot{x}(t) = -\omega_{0}^{2}\cos(\omega_0 t)$$ 
Como hay dos soluciones, también se puede escribir como: 

$$x(t) = A\sin(\omega t) + B\cos(\omega t)$$ 