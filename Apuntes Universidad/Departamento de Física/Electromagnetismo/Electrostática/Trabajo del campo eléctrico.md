
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

Se tiene un cable infinito con corriente en el eje $z$, y densidad $\lambda=\frac{C}{m}$. Por lo tanto, se pregunta el potencial en un punto $P$ que está a una distancia $r$ del cable verticalmente. Calcular el potencial. 

![[IMG_B253E51672BA-1.jpeg|center]]

Sabemos que el potencial es: 

$$-\int^{\vec{r}}_{\vec{r_0}}\vec{E}\;d\vec{l} $$

Por lo tanto, el campo se podría ver en [[Coordenadas cilíndricas|coordenadas cilíndricas]] como: 

$$\vec{E}=E_r(r)\hat{r}+E_\phi(\vec{r})\hat{\phi}+E_z(\vec{r})\hat{z}$$

Notar que en $z$ es infinito, entonces hay simetría. Idem en $\phi$ dado que los vectores se cancelan. Ocupando la [[Ley de Gauss]] se pueden hacer cilíndros con superficie cerrada en vez de ocupar la [[Ley de Coulomb]]: 

$$\begin{align}
\oint\vec{E}\;d\vec{s}&=\frac{Q_{enc}}{\epsilon_0}
\end{align}$$

Además notar que la carga encerrada es $\lambda\cdot l$. Por lo tanto, resolviendo la [[Integral de superficie|integral de superficie]]: 


$$\begin{align}
\oint\vec{E}\;d\vec{s}&=\int^{}_{\text{tapa 1}}\vec{E}\;d\vec{s}+\int^{}_{\text{tapa 2}}\vec{E}\;d\vec{s}+\int^{}_{\text{manto}}\vec{E}\;d\vec{s}\\  \\
&=\cancelto{0}{\int^{}_{\text{tapa 1}}E_r(r)\hat{r}\cdot\left(r\;dr\;d\phi\;-\hat{k}\right)}+\cancelto{0}{\int^{}_{\text{tapa 2}}\vec{E}\;d\vec{s}}\\  \\
&+\int^{2\pi}_{0}\int^{l}_{0}
E_r(r)\hat{r}\cdot dz\;r\;d\phi\;\hat{r}\\  \\
&=E_r(r)r\int^{2\pi}_{0}d\phi\int^{l}_{0}dz\\  \\
&=E_r(r)\cdot r\cdot 2\pi\cdot l\\  \\
&=E_r(r)\cdot(\text{Area del manto})
\end{align}$$



