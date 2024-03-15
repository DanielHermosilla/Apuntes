
Se tiene que la [[Fuerza electromotriz|fuerza electromotriz]] se puede definir como: 

$$\epsilon=-L\frac{dI}{dt}$$

Además, una fuente externa debe hacer [[Departamento de Física/Mecánica/Energía/Trabajo|trabajo]] para pasar una [[Corriente estacionaria|carga]] por una [[Departamento de Física/Electromagnetismo/Inducción electromagnética/Inductancia|inductancia]]:

$$W=-\epsilon q$$

Además, por definición de trabajo se puede hacer lo siguiente: 

$$\frac{dW}{dt}=-\epsilon\frac{dq}{dt}=-\epsilon I$$

Si hacemos esto con la inductancia, podemos reemplazar la definición de la fuerza electromotriz. 

$$\frac{dW}{dt}=LI\frac{dI}{dt}$$

Haciendo la cancelación de mierda que se ocupa en física: 

$$\begin{align}
\frac{dW}{\cancel{dt}}&=LI\frac{dI}{\cancel{dt}}\\  \\
\int^{W}_{0}dW&=L\int^{I}_{0}I\;dI\\  \\
W&=\frac{1}{2}LI^2\tag{1}
\end{align}$$

Así, $(1)$ llegaría a ser el **trabajo de una fuerza externa para establecer una corriente $I$ en inductancia**.

### Analogía con el condensador 

Recordar además que para el [[Condensadores|condensador]] se tenía lo siguiente: 

$$\begin{align}
W&=\frac{1}{2}CV^2\\  \\
&=\frac{1}{2}\int v\rho\;d\tau\\  \\
&=\frac{\epsilon_0}{2}\int E^2\;dz\\  \\
\rho_E&=\frac{\epsilon_0}{2}E^2\tag{2}
\end{align}$$


Se puede demostrar que para el caso de $\vec{B}$: 

$$\begin{align}
W_\text{mag}&=\int\left(\vec{A}\cdot\vec{J}\right)\;d\tau\tag{Fuente}\\  \\
&=\int\left(\frac{1}{2\mu_0}B^2\right)\tag{Todo el espacio}
\end{align}$$

Ocupando el resultado anterior de la analogía con el condensador $(2)$, entonces se define la **densidad de energía eléctrica y densidad de energía magnética**: 

$$\text{Densidad de energía}=\begin{cases}\rho_E=\frac{\epsilon_0}{2}E^2&\text{Eléctrica}\\  \\
\rho_M=\frac{1}{2\mu_0}B&\text{Magnética}\end{cases}$$

