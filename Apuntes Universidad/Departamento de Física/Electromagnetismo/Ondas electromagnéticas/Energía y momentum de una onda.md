
Sabemos que el trabajo se puede escribir como: 

$$\begin{align}
dW&=\vec{F}\cdot d\vec{l}\\  \\
&=q(\vec{E}+\vec{v}\times\vec{B})\cdot d\vec{l}\\  \\
&=q(\vec{E}+\cancel{\vec{v}\times\vec{B}})\cdot\vec{v}\;dt\\  \\
&=\rho\;dz\;\vec{E}\cdot\vec{v}\;dt\\ \\
&=(\rho\vec{v}\cdot\vec{E})\;d\tau\;dt\\ \\
&=\vec{J}\cdot\vec{E}\;d\tau\;dt\\  \\
\frac{dW}{dt\;d\tau}&=\vec{J}\cdot\vec{E}
\end{align}$$

Así, se define la última igualdad como **potencia [[onda electromagnética|electromagnética]] convertida en mecánica por unidad de volumen**. Si integramos en volumen: 

$$\begin{align}
\frac{dW}{dt}&=\int_V(\vec{J}\cdot\vec{E})\;d\tau
\end{align}$$

Notemos que se puede eliminar $\vec{J}$ por la [[Leyes de Maxwell|ley de Maxwell]]: 

$$\vec{\nabla}\times\vec{B}=\mu_0\vec{J}+\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}$$

Se puede demostrar que: 

$$\begin{align}
\frac{dW}{dt}&=-\frac{d}{dt}\int_V\bigg\lbrace\frac{1}{2}\epsilon_0E^2+\frac{1}{2\mu_0}B^2\bigg\rbrace d\tau+\dots \\  \\
&-\oint_{S=\partial V}\frac{1}{\mu_0}(\vec{E}\times\vec{B})\cdot d\vec{a}c
\end{align}$$

Así, la derivada es positiva. Por lo tanto, el campo de energía electromagnética pierde energía y las partículas ganan energía mecánica. Por lo tanto, se define la **densidad de energía electromagnética**: 

$$u=\frac{1}{2}\epsilon_0E^2+\frac{1}{2\mu_0}B^2$$ 
Y, como el segundo término es un flujo de energía, se define el **vector de flujo de energía** como: 

$$\vec{S}=\frac{1}{\mu_0}\vec{E}\times\vec{B}$$

Se le denomina también *vector de Poynting*. Así, se puede reescribir la expresión de energía: 

$$\frac{d}{dt}\int_Vu\;dz=-\frac{dW}{dt}-\oint_{S=\partial v}\vec{S}\cdot d\vec{a}$$

Ahora, si no hay partículas $\vec{J}\cdot\vec{E}=0$, asi que $dW/dt=0$. Por lo tanto, se tiene una ecuación del siguiente estilo: 

$$\frac{d}{dt}\int_Vu\;d\tau+\oint_{S=\partial v}\vec{S}\cdot d\vec{a} $$

Es análogo en forma diferencial con la [[Ecuación de continuidad|ecuación de continuidad]]:

$$\begin{align}
\vec{\nabla}\cdot\vec{J}+\frac{\partial\rho}{\partial t}&=0\\  \\
\vec{\nabla}\cdot\vec{S}+\frac{\partial u}{\partial t}&=0
\end{align}$$

