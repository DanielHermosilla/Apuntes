
El [[Flujo del campo eléctrico|flujo del campo eléctrico]] a través de cualquier **superficie cerrada** es igual a la carga $q$ contenida dentro de la superficie, dividida por la constante $\epsilon_0$. Las superficies cerradas, correspondiendo a volumenes cerrados, como las esferas, cubos, etc. 

$$\Phi=\oint_S\vec{E}\cdot d\vec{S}=\frac{q}{\epsilon_0}$$

Para poder aplicar la ley de Gauss es necesario conocer la dirección y el sentido del [[Flujo del campo eléctrico|flujo del campo]] generado por la distribución de cargas. 

La demostración de esto subyace del [[Principio de superposición|principio de superposición]], que establece que: 

$$\vec{E}=\sum^{n}_{i=1}\vec{E_i}$$

Por lo tanto, el [[Flujo del campo eléctrico|flujo]] que encierra a todos ellos es: 

$$\intop E\cdot d\mathbf{a}=\sum^{n}_{i=1}\left(\oint E_i\cdot d\mathbf{a}\right)=\sum^{n}_{i=1}\left(\frac{1}{\epsilon_0}q_i\right)$$

## Forma diferencial

A partir de la ley de Gauss y [[Divergencia y rotación del campo eléctrico|teorema de la divergencia]] se puede llegar a las siguientes equivalencias: 

$$\oint_Sd\vec{S}\cdot\vec{E}=\int^{}_{V}d^3x\vec{\nabla}\cdot\vec{E}=\frac{1}{\epsilon_0}\int^{}_{V}d^3x\rho(x)$$

Por conclusión, se llega a la siguiente **forma diferencial de la Ley de Gauss**: 

$$\vec{\nabla}\cdot\vec{E}(\vec{x})=\frac{\rho(x)}{\epsilon_0}$$

### Ejemplo 

Se tiene una esfera de radio $R$, con carga $q$ uniforme.

![[Captura de pantalla 2023-08-16 a la(s) 08.45.46.png|center]]


Ocupando el sistema de [[Departamento de Física/Mecánica/Cinemática/Coordenadas esféricas|coordenadas esféricas]], el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] sería: 

$$\vec{E}(\vec{r})=E(\vec{r})\hat{r}+\cancel{E(\vec{r})\hat{\theta}}+\cancel{E(\vec{r})\hat{\phi}}$$

Notemos que en $\hat{\theta}$ y en $\hat{\phi}$ se cancelan las coordenadas dado que no hay coordenadas privilegiadas. 

Notemos que la densidad de carga adentro de la esfera llegaría a ser: 

$$\rho=\frac{q}{\text{Vol}}=\frac{q}{\frac{4\pi}{3}R^3}$$

Lo más conveniente es hacer una integral de superficie y ocupar la Ley de Gauss integral. Primero, para el caso $r>R$: 

$$\begin{align}
\oint\vec{E}\cdot d\vec{s}=&\int^{\pi}_{0}\int^{2\pi}_{0}E_r(r)\hat{r}\cdot r^2\sin\theta\;d\theta\; d\phi\; \hat{r}\\  \\
&=E_r
\end{align}$$

