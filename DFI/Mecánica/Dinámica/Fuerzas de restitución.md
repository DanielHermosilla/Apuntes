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
Donde $A$ y $B$ lo determina las condiciones iniciales o de borde. Si se imponen condiciones iniciales como $X_0$ por posición inicial y $v_0$ una velocidad final, entonces: 

$$x(t) = X_0\cos(\omega_0 t) + \frac{v_0}{\omega_0}\sin(\omega_0 t)$$ 
Con un [[periodo]] de oscilación de $\frac{2\pi}{\omega_0} = T$ 

O análogamente se podría tener lo siguiente, al aplicar la fórmula de suma de angulos:

$$x(t) = C\sin(\omega_0 t +\phi)$$ 
Con $C^2 = x_{0}^{2} + \frac{V_{0}^{2}}{\omega_{0}^{2}}$ 

Por el otro lado, si se deriva al cuadrado, se llega que: 

$$\dot{x}^2 = v_{0}^2 + (\omega_0 x_0)^2 - \omega_{0}^{2} x^2$$ ![[VelocidadCuadrado.jpeg|center]]

Cuya forma es esta, es decir, la velocidad alcanza su máximo en $x=0$. 

### Ejemplo 1 

![[Ejemplo2 Resorte.jpeg|center]]

Se tiene un resorte unido a dos resortes con distinta constante elástica ($k_1, k_2$) y distinto largo natural. Al hacer la sumatoria de fuerzas se llega que la constante elástica **total** es $K* = k_1 + k_2$. 

### Ejemplo 2

![[Ejemplo1 Resorte.jpeg|center]]

Se tiene que en el sistema definido, 

$$\vec{F_1} = -K_1(x-l_1)\hat{i}$$
$$\vec{F_2} = -K_2(y-l_2)\hat{j}$$ 
Para dejar en los mismos sistemas, sabemos que $\hat{j} = -\hat{i}$. 

Por suma de fuerzas, se llega que $m\ddot{x} = -(K_1 + K_2)x + cte$ 

Por el otro lado, si dejamos todo en función 
### Ejemplo 3

Se puede analizar también el caso de 