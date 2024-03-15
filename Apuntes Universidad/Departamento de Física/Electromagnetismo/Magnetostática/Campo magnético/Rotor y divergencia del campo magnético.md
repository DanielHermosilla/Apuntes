
El caso general y directo de la [[Campo magnético|ley de Biot-Savart]] es posible pero muy complicado. 

Por ejemplo, si se volviera al ejemplo del cable con corriente, se tendría que: 

$$\begin{align}
\vec{B}(r)&=\frac{\mu_0I}{2\pi}\frac{1}{r}\hat{\phi}\tag{Coordenadas cilíndricas}
\end{align}$$

Ahora, *¿qué pasaría si calculara la [[Integral de superficie|integral de superficie]] del campo magnético?*. Por un lado, sabemos que el elemento de [[Integral de línea|línea]] en cilíndricas corresponde a. 

$$d\vec{l}=dr\hat{r}+rd\phi\hat{\phi}+dz\hat{k}$$

Entonces, se llega que: 

$$\begin{align}
\oint\vec{B}\cdot d\vec{l}&=\oint\frac{\mu_0I}{2\pi}\;d\phi\\  \\
&=\frac{\mu_0I}{2\pi}\oint d\phi
\end{align}$$

La idea de esto, es que **se debe cerrar el cable**. Vale decir, **hay que elegir un camino que encierre el cable**. Por eso mismo, trivialmente, los límites llegarían a estar definidos en $\phi\in[0,2\pi]$: 

$$\begin{align}
\oint\vec{B}\cdot d\vec{l}&=\mu_0I
\end{align}$$

Esto, pareciera ser un **análogo a la [[Ley de Gauss|ley de Gauss]]**. 

Ahora, cuando el camino no encierra el cable, se tiene la siguiente situación:

![[Captura de pantalla 2023-10-11 a la(s) 09.26.13.png|center]]


Notemos que la integral llegaría a ser: 

$$\begin{align}
\oint d\phi&=\int^{\phi_2}_{\phi_1}d\phi+\int^{\phi_1}_{\phi_2}d\phi\\  \\
&=(\phi_2-\phi_1)+(\phi_1-\phi_2)\\  \\
&=0
\end{align}$$

>[!bug] Ley de Ampere Integral
Se concluye lo siguiente, **para el caso general**: $$\oint\vec{B}\cdot d\vec{l}=\mu_0I_\text{enc}$$Donde: 	$$I_\text{enc}=\sum^{n}_{i=1}I_i$$ Para los cables con [[Corriente estacionaria|corriente]] encerrado por el camino de integración. 

Otra forma de describir la corriente encerrada es por la integral, ocupando [[Principio de superposición|principio de superposición]]: 

$$I_\text{enc}=\int^{}_{S}\vec{J}\cdot d\vec{s}$$

Esta integral se puede reescribir por el [[Teorema de Stokes|teorema de Stokes]], donde: 

$$\oint_{\partial S}\vec{B}\cdot d\vec{l}=\mu_0\int_S\vec{J}\cdot d\vec{s}$$

Entonces, por teorema de Stokes: 

$$\int_S(\vec{\nabla}\times\vec{B})\cdot d\vec{s'}=\mu_0\int_S\vec{J}\cdot d\vec{s}$$ 
Como es para cualquier [[Superficie|superficie]]: 

$$\vec{\nabla}\times\vec{B}=\mu_0\vec{J}\tag{Ley de Ampere diferencial}$$

Y, por el otro lado, si se hace el cálculo de la [[Divergencia|divergencia]]: 

$$\vec{\nabla}\cdot\vec{B}=0$$

En resumen, haciendo el análogo al [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]]

$$\text{Divergencia y rotor en campos}=\begin{cases}\vec{\nabla}\times\vec{B}=\mu_0\vec{J}&\vec{\nabla}\times\vec{E}=0\\  \\
\vec{\nabla}\cdot\vec{B}=0&\vec{\nabla}\cdot\vec{E}=\frac{\rho}{\epsilon_0}\end{cases}$$

A partir de esto se concluye que **no hay monopolos magnéticos**. 

#### Ejemplo 

Encontrar $\vec{B}$ producido por una superficie plana infinita con corriente $\vec{K}=K\hat{i}$ en el plano $x-y$.

![[Captura de pantalla 2023-10-16 a la(s) 08.54.41.png|center]]

El primer método, *más directo*, es agarrar cables infinitesimalmente chicos $dy=I_c=Kdy$. Esto llegaría a ser tomar una especie de *línea* que se dirijen en la dirección de $\hat{i}$. Sabiendo que $\vec{K}=\sigma\vec{v}$, entonces bastaría con sumar cada aporte. 

La otra forma de solucionar es ocupar la **ley de Ampere**, primero, descomponiendo el campo magnético: 

$$\vec{B}=B_x\hat{i}+B_y\hat{j}+B_z\hat{k}$$

Dado que $\vec{B}$ debe ser perpendicular a $\vec{K}$ (la corriente), entonces la componente $\hat{i}$ se iría. 

Por el otro lado, haciendo el análisis para $\hat{k}$, es posible notar que por simetría esta componente se cancela. 

Sólamente se conservaría $B_y\hat{j}$: 

$$\vec{B}=\cancelto{0}{B_x\hat{i}}+B_y\hat{j}+\cancelto{0}{B_z\hat{k}}$$ 
Por lo tanto, llegaríamos a la siguiente función para el campo vectorial: 

$$\vec{B}(x,y,z)=B_y(x,y,z)\hat{j}$$

Notemos que esto **no depende de $x$ ni de $y$**. Por lo tanto, se llega a lo siguiente: 

$$\vec{B}(\cancel{x},\cancel{y},z)=B_y(\cancel{x},\cancel{y},z)\hat{j}$$ 
Entonces, ocupando la **ley de Ampere**, sabemos lo siguiente: 

$$\begin{align}
I_\text{enc}&=\int\vec{J}\cdot d\vec{s}\\  \\
&=\int\vec{k}\cdot d\vec{l}_\perp
\end{align}$$

Lo más conveniente para poder trazar el camino sería **trazar un rectángulo en el eje $y$**. Entonces, trazando la integral de línea con el rectángulo (ver fígura): 

$$\begin{align}
\oint\vec{B}\cdot d\vec{l}&=\mu_0\cdot I_\text{enc}
\end{align}$$

Notemos que las únicas componentes necesarias para la integral de línea llegaría a ser aquellas corrientes que van perpendicular al plano $\hat{y}$.  Esto se debe a que las otras cumplen ser perpendiculares **con el campo magnético**, es decir, $\vec{B}\perp d\vec{l}$. Por lo tanto: 

$$\begin{align}
Bl+Bl+0+0&=\mu_0\;Kl\\  \\
2Bl&=\mu_0 Kl\\  \\
B&=\frac{\mu_0 K}{2}
\end{align}$$

Entonces, se llega a lo siguiente: 

$$\vec{B}=\begin{cases}-\frac{\mu_0 k}{2}\hat{j}&z>0\\  \\
\frac{\mu_0 k}{2}\hat{j}&z<0\end{cases}$$ 
