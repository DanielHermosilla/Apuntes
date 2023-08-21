
Se define como: 

$$W\bigg\vert_{A}^{B}=\int^{B}_{A}\vec{E}\cdot d\vec{l}$$

Vale decir, es una [[Integral de línea|integral de línea]] asociado a la trayectoria.  Aunque, aun así, al expander la integración se llega que el trabajo no depende de la trayectoria, si no del radio final e inicial. Es decir, es una **fuerza conservativa**. 

$$W\bigg\vert_{A}^{B}=\frac{q}{4\pi\epsilon_0}\left(\frac{1}{r_A}-\frac{1}{r_B}\right) $$

De otra forma, también se puede definir de la siguiente forma al ser una campo conservativo: 

$$\oint_\epsilon\vec{E}\cdot d\vec{l}=0$$
## Trabajo de una fuerza externa 

El trabajo de una fuerza externa en equilibrio con el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] también se puede escribir como una [[Diferencia de potencial|diferencia de potencial]]. 

$$-\int^{\vec{b}}_{\vec{a}}\vec{E}\cdot d\vec{l}=V(\vec{b})-V(\vec{a})$$

Es decir, el trabajo de una fuerza externa para llevar una carga unitaria de $\vec{a}$ a $\vec{b}$. Por lo general, se estudia el caso cuando $\vec{a}\to\infty$. Por ende, **el potencial electrico** se define como: 

$$V(\vec{r})=-\int^{\vec{r}}_{\vec{r_0}}\vec{E}\cdot d\vec{l}$$

Se puede probar lo siguiente con el [[Gradiente y plano tangente|gradiente]]: 

$$\vec{E}=-\vec{\nabla}V$$

Donde el [[Gradiente y plano tangente|gradiente]] en coordenadas cartesianas corresponde a: 

$$\vec{\nabla}V=\frac{\partial V}{\partial x}\hat{i}+\frac{\partial V}{\partial y}\hat{j}+\frac{\partial V}{\partial z}\hat{k}$$

Y, de la misma forma, se puede llegar que: 

$$\nabla^2 V=\frac{-\rho}{\epsilon_0}$$

Notar que el potencial también cumple el [[Principio de superposición|principio de superposición]]. 

## Teorema de Stokes 

Con $\vec{E}$ un [[Campos escalares y vectoriales|campo vectorial]] diferenciable: 

$$\oint_{\xi=\partial S}\vec{E}\cdot d\vec{l}=\int^{}_{S}\vec{\nabla}\times\vec{E}\cdot d\vec{s}$$

Donde $\vec{\nabla}\times\vec{E}$ es el [[Rotor|rotor]]. 

Para $\vec{E}$, si se cumple: 

$$\oint_\xi\vec{E}\cdot d\vec{l}=0=\int_S\vec{\nabla}\times\vec{E}\cdot d\vec{S}$$

Para un $S$ cualquiera, entonces se tiene los siguientes resultados: 

- $\vec{\nabla}\times\vec{E}=0$
- $\vec{\nabla}\cdot\vec{E}=\frac{\rho}{\epsilon_0}$ 


#### Ejemplo 

Se tiene un cable infinito con corriente en el eje x, y densidad $\lambda=\frac{C}{m}$. Por lo tanto, se pregunta el potencial en un punto $z$. 

