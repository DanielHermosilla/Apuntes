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


Por suma de fuerzas, se llega que $m\ddot{x} = -(\frac{K_1K_2}{K_1 + K_2})x + cte$ 


### Ejemplo 3

Se tiene el siguiente problema, donde se tiene un pistón con un fluido por dentro.  

![[Ejemplo piston.jpeg|center|400]]

Por lo tanto, definiendo $y$ postivo hacia abajo: 
$$m\ddot{y} = mg - k(y-l_0) - c\dot{y}$$ $$m\ddot{y} + c\dot{y} + ky = mg + Kl_0$$ 
Por lo tanto, se tiene una EDO. Primero se busca la solución partícular, es decir, $mg + Kl_0 = 0$. Se llega que $A_0 = \frac{mg}{K} + L_0$. 

Y la solución característica sería: 

$$S_{1,2} = -\frac{C}{2m}\pm\sqrt{\left(\frac{C}{2m}\right)^2 - \frac{k}{m}}$$ 
$$\iff S_{1,2} = -\omega_1 \pm \sqrt{\omega_{1}^{2}-\omega_{0}^{2}}$$ 
Entonces, nos podríamos poner en casos: 

$$\text{Caso no homogeneo} = \omega_{0}^{2} > \omega_{1}^{2}\iff\left(\frac{C}{2m}\right)^2 > \frac{K}{m}  \implies S_1 < 0\ \land\ S_2 < 0 \implies x(t) = Ae^{s_1 t} + Be^{s_2 t}\implies\lim_{t\rightarrow\infty}x(t)=0 $$ 
Y en el homogeneo, donde $y_0  = 0$, se podría tener que la velocidad podría ser 0, negativa o positiva, donde se sabe que $y_0(t) = Ae^{s_1 t} + Be^{s_2 t}$. Se tienen los siguientes gráficos para las tres velocidades posibles: 

Para $v_0 < 0$  se tiene una función **sobre-amortiguada**. 

```functionplot
---
title: Función críticamente sobreamortiguada
xLabel: x
yLabel: t
bounds: [-0.05,5,0,1]
disableZoom: true
grid: true
---
y =  exp(-x)

```

Para $v = 0$ se tiene una función **críticamente subamortiguada**. 

```functionplot
---
title: Función críticamente subamortiguada
xLabel: x
yLabel: t
bounds: [0,5,-1,1]
disableZoom: true
grid: true
---
y =  exp(-x)cos(x)
h = exp(-x)
z = -exp(-x)
```


Para $v>0$ se tiene una función **críticamente amortiguada**. 

```functionplot
---
title: Función críticamente amortiguada
xLabel: x
yLabel: t
bounds: [0,5,0,1]
disableZoom: true
grid: true
---
y = x * exp(-x)
```

Todas convergen asíntoticamente a lo mismo