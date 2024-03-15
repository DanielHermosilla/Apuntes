
Consideremos un volumen $V$ y la [[Superficie|superficie]] que lo encierra $S$, orientada a la normal externa $\hat{n}$. 

Sabemos que la carga encerrada en un volumen se representa como: 

$$Q=\int_V\rho dz$$

Por lo tanto, para calcular como varía una carga encerrada en un volumen: 

$$\begin{align}
\frac{dQ}{dt}&=\frac{d}{dt}\int_V\rho\;dz\\  \\
&=\int_V\frac{\partial\rho}{\partial t}\;dz
\end{align}$$

Si $\frac{dQ}{dt}>0$, entonces entra carga al volumen. 

Por el otro lado, nos podemos definir [[Corriente estacionaria]|la corriente que sale del volumen]]: 

$$\int_{S=\partial V}\vec{J}\cdot d\vec{s}=-I$$

Por lo tanto, aplicando la definición de corriente 

$$\begin{align}
I&=\int_V\frac{\partial\rho}{\partial t}\;dz\\  \\
&=-\int_{s=\partial V}\vec{J}\cdot d\vec{s}
\end{align}$$

Por [[Ley de Gauss]], se tiene lo siguiente, valido para cualquier volumen: 

$$\int_V\frac{\partial\rho}{\partial t}\;dz=-\int_V\vec{\nabla}\cdot\vec{J}\;dz$$


Luego, 

$$-\vec{\nabla}\cdot\vec{J}=\frac{\partial\rho}{\partial t}$$

Por último, nos podemos definir la **ecuación de continuidad de carga**: 

$$\vec{\nabla}\cdot\vec{J}+\frac{\partial\rho}{\partial t}=0$$

Esta es una forma de expresar la conservación de carga a nivel local. Viéndolo de otra forma: $\vec{\nabla}\cdot\vec{J}$ nos dice cuanto o en qué cantidad una carga va a *"diverger"* o irse de la superficie. Por el otro lado, $\partial\rho/\partial t$ es la pérdida de densidad de carga. 