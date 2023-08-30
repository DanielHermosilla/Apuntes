
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


#### Ejemplo: Condensador de placas paralelas 

Se tiene la siguiente figura: 

![[IMG_B386BF10EAA2-1.jpeg|center]]

Por las [[Condiciones de borde|condiciones de borde]], se sabe que el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] es nulo al llegar a los bordes. Entonces, al mirar las placas desde cerca:  

![[IMG_4CBBA68B63EC-1.jpeg]]

Se llega al siguiente sistema de ecuaciones: 

$$\begin{align}  
E_3-E_2&=-\frac{\sigma}{\epsilon_0}\\  \\
E_2-E_1&=\frac{\sigma}{\epsilon_0}\\  \\
\implies E_2&=\frac{\sigma}{\epsilon_0}
\end{align}$$


Por lo tanto, el potencial es: 

$$\begin{align}
V&=-\int^{d}_{0}\vec{E}\cdot d\vec{l}\\  \\
&=-\int^{d}_{0}\frac{-Q}{\epsilon_0 A}\cdot\hat{j}\;dy
\end{align}$$