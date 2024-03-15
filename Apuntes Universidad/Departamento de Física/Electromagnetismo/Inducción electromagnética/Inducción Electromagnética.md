
En la [[Magnetostática|magnetostática]] y [[Fuerza electrostática|electrostática]] se había llegado a las siguientes ecuaciones: 

$$\begin{align}
\vec{\nabla}\cdot\vec{E}&=\frac{\rho}{\epsilon_0}\\ \\
\vec{\nabla}\times\vec{E}&=0\\  \\
\vec{\nabla}\cdot\vec{B}&=0\\  \\
\vec{\nabla}\times\vec{B}&=\mu_0\vec{J}\\  \\
\vec{J}&=\rho\vec{v}
\end{align}$$

Además, se había definido la [[Fuerza electromotriz|fuerza electromotriz]]. Para poder mover cargas dentro de un circuito es necesario tener una fuerza externa que pueda contrarrestar la [[Fuerza de Coulumb|fuerza de Coulomb]]. Así, en realidad, lo que uno le llama a la fuerza electromotriz llegaría a ser: 

$$\epsilon=\oint\vec{f\cdot d\vec{l}}$$

Ahora, lo que hizo Faraday fue poner una espira dentro de un circuito: 

![[Pasted image 20231110091647.png|center|500]]

Al hacer fluir las cargas eléctricas, la carga $q$ experimenta una fuerza: 

$$\vec{F}=q\vec{v}\times\vec{B}=qvB\hat{j}$$

Intuitivamente la [[Fuerza magnética|fuerza magnética]] iría hacia arriba en $\hat{y}$ en la parte vertical. De ese modo, se forma una especie de bateria que va empujando las cargas a través del circuito.  Así, calculando la *fem*:

$$\begin{align}
\epsilon&=\oint\vec{f}\cdot d\vec{l}\\  \\
\vec{f_m}&=\frac{\vec{F_m}}{q}=vB\\  \\
\epsilon&=Vbh\tag{Como una batería}
\end{align}$$

Esto implica que se produce una corriente en el circuito. Por lo tanto: 

$$\begin{align}
\phi&=RI\\  \\
I&=\frac{\phi}{R}=\frac{VBh}{R}
\end{align}$$

Pero esto no haría sentido sin que la espira esté sin movimiento, ya que se necesitaria una *fem* por todo el circuito. Por lo tanto, se mueve la espira y se genera **el primer generador**. Otra forma de verlo es a través de la [[Regla de flujo|regla de flujo]]. 

A partir de diversos experimentos hechos por Faraday, se llego que un $\vec{B}(t)$ induce un [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]]. Así: 

$$\begin{align}
\epsilon&=-\frac{d\Phi}{dt}\\  \\
\oint\vec{E}\cdot d\vec{l}&=-\frac{d}{dt}\int\vec{B}\cdot d\vec{s}\tag{Ley de Farady integral}
\end{align}$$

Esto se puede convertir con el [[Teorema de Stokes|teorema de Stokes]] y así se llega que, para cualquier superficie: 

$$\begin{align}
\int\vec{\nabla}\times\vec{E}\;d\vec{s}&=-\int_s\frac{\partial\vec{B}}{\partial t}\;d\vec{s}
\end{align}$$

Por lo tanto; 

$$\vec{\nabla}\times\vec{E}=-\frac{\partial\vec{B}}{\partial t}\tag{Ley de Faraday diferencial}$$

Análogo a $\vec{\nabla}\times\vec{B}=\mu_0\vec{J}$

Ahora, notemos que se tienen las siguientes ecuaciones después de postular las leyes de Faraday: 

$$\begin{align}
\vec{\nabla}\cdot\vec{B}&=0\\  \\
\vec{\nabla}\times\vec{B}&=\mu_0\vec{J}\\  \\
\vec{\nabla}\cdot\vec{E}&=\frac{\rho}{\epsilon_0}\\  \\
\vec{\nabla}\times\vec{E}&=-\frac{\partial\vec{B}}{\partial t}
\end{align}$$

Para que se tenga una analogía total, lo ideal sería que $\vec{\nabla}\times\vec{E}=0$. Sin embargo, cuando $\rho=0$ se tiene una analogía. 

#### Ejemplo 

Un solenoide largo de radio $a$ y $n$ vueltas por unidad de largo tiene un corriente $I(t)$ en $\hat{\phi}$. Encuentre el campo $\vec{B}(r)$ en todo el espacio. 

Notemos que el campo es nulo cuando $r>a$. Por el otro lado, por la mano derecha, esto va en $\hat{k}$. Así, por ley de Ampere: 

$$B_z\cancel{l}=\mu_0\cdot n\cancel{l}I$$

Por lo tanto, el campo llegaría a ser: 

$$\vec{B}=\begin{cases}
\mu_0nI\;\hat{k}&r<a\\ \\
0&r>a
\end{cases}$$


No obstante, como varía la intensidad de corriente, también es posible calcular el campo eléctrico. Así: 

$$\oint\vec{E}\cdot d\vec{l}=-\frac{d}{dt}\int\vec{B}\cdot d\vec{s} $$

Por lo tanto, para el caso $r<a$: 

$$\begin{align}
E\cancel{2\pi}\cancel{r}&=-\mu_0n\frac{dI}{dt}\cancel{\pi}r^{\cancelto{1}{2}}\\  \\
\vec{E}&=-\frac{\mu_0n\;dI}{2\;dt}r\hat{\phi}
\end{align}$$

Ahora, para el caso $r>a$: 

$$\begin{align}
E\;2\pi r&=-\mu_0n\frac{dI}{dt}\pi a^2\\  \\
\vec{E}&=-\mu_0\frac{na^2}{2}\frac{dI}{dt}\cdot\frac{1}{r}\hat{\phi}
\end{align}$$


