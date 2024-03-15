
Si se tienen dos distribuciones de carga, acordándonos sobre la formulación del [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] se tiene lo siguiente: 

$$\vec{E}=\frac{1}{4\pi\epsilon_0}\int\frac{\rho(\vec{r'})(\vec{r}-\vec{r'})}{\vert\vert\vec{r}-\vec{r'}\vert\vert^3}dz$$

Notemos que se cumple la siguiente relación: 

$$\begin{align}
\rho(\vec{r})&\to\vec{E_0}(\vec{r})\\  \\
2\rho(\vec{r})&\to2\vec{E_0}(\vec{r})\\  \\
f\cdot\rho(\vec{r})&\to f\cdot\vec{E_0}(\vec{r})
\end{align}$$

Entonces, lo importante saber es que hay una relación **constante** entre la distribución de carga y [[Departamento de Física/Métodos Experimentales/Circuitos eléctricos/Campo eléctrico|campo eléctrico]]. Y no sólo esto, si no que también se cumple para el [[Potencia eléctrica|potencial eléctrico]] del campo eléctrico. Por lo tanto, la [[Condensador|capacitancia]] se define como: 

$$C=\frac{Q}{V}$$

Donde $Q$ es la carga almacenada y $V$ es la diferencia de potencial. Su unidad de medida es el *faradio*, que cumple la siguiente relación: 

$$1\;\text{Farad}=1\frac{\text{Coulomb}}{\text{Volt}}$$

## Energía almacenada en el condensador 

Si suponemos que tenemos dos cargas puntuales, sabemos que el [[Trabajo y Energía en Electrostática|trabajo]] para atraer la carga sería: 

$$dW=dQ\cdot V$$

Si reemplazamos esto por la ecuación del condensador: 

$$dW=\frac{q}{C}\;dq$$

Ahora, si se quiere cargar el condensador para que ejerca un cierto trabajo $W_{total}$, se llega a lo siguiente, que sería la energía del condensador: 

$$\int^{W}_{0}dW=\int^{Q}_{0}\frac{q}{C}\;dq=\frac{1}{2}\frac{Q^2}{C}$$


## Condensador dieléctrico 

Notemos que si se tiene un condensador con una distribución de cargas, se tiene que el trabajo dipolar llega a ser: 

$$\begin{align}
W_D&=\frac{1}{2}C_dV^2\\  \\
&=\frac{\epsilon}{\epsilon_0}\cdot W_v
\end{align}$$

Donde $\epsilon$ es la permeabilidad del material, que en realidad llega a ser nombrado como el *constante dieléctrico*. 

$$\epsilon_r=1+\chi_e=\frac{\epsilon}{\epsilon_0}\tag{Constante dieléctrica}$$

Se puede llegar a demostrar que si el espacio se llena con **dieléctrico linea** con permitividad $\epsilon$, se tiene: 

$$\begin{align} 
W&=\frac{\epsilon}{2}\int E^2dz\\  \\
&=\frac{1}{2}\int\vec{D}\cdot\vec{E}\;dz\;\;\;\;\vec{D}=\epsilon\vec{E}\end{align} $$
#### Ejemplo: Condensador de placas paralelas 

Se tiene la siguiente figura: 

![[IMG_B386BF10EAA2-1.jpeg|center]]

Por las [[Departamento de Física/Electromagnetismo/Electrostática/Condiciones de borde|condiciones de borde]], se sabe que el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] es nulo al llegar a los bordes. Entonces, al mirar las placas desde cerca:  

![[IMG_4CBBA68B63EC-1.jpeg]]

Se llega al siguiente sistema de ecuaciones: 

$$\begin{align}  
E_3-E_2&=-\frac{\sigma}{\epsilon_0}\\  \\
E_2-E_1&=\frac{\sigma}{\epsilon_0}\\  \\
\implies E_2&=\frac{\sigma}{\epsilon_0}
\end{align}$$

Por lo tanto, el [[Potencia eléctrica|potencial eléctrico]] es: 

$$\begin{align}
V&=-\int^{d}_{0}\vec{E}\cdot d\vec{l}\\  \\
&=-\int^{d}_{0}\frac{-Q}{\epsilon_0 A}\;dy\\  \\
&=\frac{Q}{A\epsilon_0}\cdot d
\end{align}$$

Acordándonos de la definición de [[Condensador|capacitancia]], donde $C=Q/V$, entonces la capacitancia de este sistema es: 

$$C=\frac{Q}{\left(\frac{Qd}{A\epsilon_0}\right)}=\frac{A\epsilon_0}{d}$$

De este ejercicio se puede atribuir la siguiente relación: 

$$\begin{align}
A\;\text{aumenta}&\to C\;\text{aumenta}\\  \\
d\;\text{disminuye}&\to C\;\text{aumenta}
\end{align}$$