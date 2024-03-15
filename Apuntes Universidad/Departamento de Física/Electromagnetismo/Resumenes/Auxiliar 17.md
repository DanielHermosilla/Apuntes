
## Pregunta 1

Un amperímetro de inducción consiste en un solenoide toroidal, que se sitúa en torno a la corriente que se pretende medir (hilo de corriente $I$). Suponga un toroide de radio medio $b$ y sección cuadrada pequeña de lado $a$ ($a<<b$), con $N$ espiras enrolladas. 

#### Calcular el coeficiente de inducción del solenoide 

Sabemos que la inducción, por definición, corresponde a la siguiente expresión: 

$$\Phi=\int\vec{B}\cdot d\vec{S}$$ 
Por lo tanto, se necesita conocer el campo magnético dentro del solenoide. Ocupando **ley de Ampere**:

$$\begin{align}
\oint\vec{B}\cdot d\vec{l}&=\mu_0I_{\text{enc}}\\  \\
B(r)\int^{2\pi}_{0}r\;d\phi&=\mu_0NI\\  \\
\vec{B}(r)&=\mu_0\frac{NI}{2\pi r}\hat{\phi}
\end{align}$$

Ahora, se calculará el coeficiente de inducción **solamente para un alambre**. Luego se va a imponer por superposición el caso de las $N$ vueltas. 

$$\begin{align}
\Phi_1&=\oint\vec{B}\cdot d\vec{S}\\  \\
&=\int^{a}_{0}\int^{b+\frac{a}{2}}_{b-\frac{a}{2}}\frac{\mu_0NI}{2\pi r}\;dr\;dz\\  \\
&=\frac{\mu_0NIa}{2\pi}\ln(r)\bigg\vert^{b+\frac{a}{2}}_{b-\frac{a}{2}}\\  \\
&=\frac{\mu_0NIa}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)
\end{align}$$

Así, imponiendo las $N$ vueltas. 

$$\begin{align}
\Phi_T&=N\Phi_1=\frac{\mu_0N^2Ia}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)
\end{align}$$

Ahora, por definición, el coeficiente de inducción ($L$) cumple la siguiente relación: 

$$\begin{align}
L&=\frac{\Phi_T}{I}\\  \\
&=\frac{\mu_0N^2a}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)
\end{align}$$

#### Calcular el coeficiente de inducción mutua y la fem del hilo rectilíneo 

El enunciado dice que por el hilo circula una corriente $I_h=I_0\cos(\omega t)$. Así, para calcular el coeficiente de inducción mutua se ocupará la definición: 

$$\Phi_S=I_h(t)M_{sh}=N\oint\vec{B_h}\cdot d\vec{S}$$ 
El campo magnético del hilo es conocido, llegaría a ser el campo magnético de un cable cualquiera: 

$$\vec{B_h}=\frac{\mu_0I_h}{2\pi r}\hat{\phi}$$

Así, calculando la inductancia: 

$$\begin{align}
\Phi_S&=N\int^{a}_{0}\int^{b+\frac{a}{2}}_{b-\frac{a}{2}}\frac{\mu_0I_h}{2\pi r}\;dr\;dz\\  \\
&=\frac{\mu_0NI_ha}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)
\end{align}$$

Por lo tanto, el **coeficiente de inducción mutua** llegaría a ser: 

$$M=\frac{\Phi_S}{I_h}=\frac{\mu_0Na}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)$$

Por el otro lado, para la fuerza electromotriz se tiene lo siguiente: 

$$\begin{align}
\epsilon_s&=\oint\vec{f_s}\cdot d\vec{l}\\  \\
&=-\frac{d\Phi}{dt}\\  \\
&=-M\frac{dI}{dt}\\  \\
&=-MI_0\omega(-\sin(\omega t))\\  \\
&=\frac{\mu_0Na\omega I_0}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)\sin(\omega t)
\end{align}$$

#### Calcular la corriente inducida en el toroide por la fem de la parte anterior 

Si el toroide tiene una resistencia $R$, va a cumplir la Ley de Ohm, donde: 

$$\begin{align}
I_{\text{ind}}&=\frac{\epsilon_s}{R}\\  \\
&=\frac{\mu_0Na\omega I_0}{2\pi R}\ln\left(\frac{2b+a}{2b-a}\right)\sin(\omega t)
\end{align}$$

Notemos que la corriente inducida depende del tiempo, asi que al variar esta corriente **también se producirá una fem inducida ($\epsilon_T$)**. Para obtener el valor de esto, es posible ocupar el coeficiente de inducción del solenoide calculado anteriormente: 

$$\begin{align}
\epsilon_T&=-\frac{d\Phi}{dt}\\  \\
&=-L\frac{dI}{dt}\\  \\
&=-\frac{\mu_0N^2a}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)\frac{\mu_0Na\omega^2 I_0}{2\pi R}\ln\left(\frac{2b+a}{2b-a}\right)\cos(\omega t)\\  \\
&=-\frac{\mu_{0}^{2}N^3a^2\omega^2\ln^2\left(\frac{2b+a}{2b-a}\right)}{4\pi^2R}I_0\cos(\omega t)
\end{align}$$

Ahora, para obtener la razón entre ambas amplitudes se hace la división de las amplituds de las fem: 

$$\begin{align}
\bigg\vert\frac{\epsilon_s}{\epsilon_T}\bigg\vert&=\frac{\frac{\mu_0Na\omega I_0}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)\sin(\omega t)}{-\frac{\mu_{0}^{2}N^3a^2\omega^2\ln^2\left(\frac{2b+a}{2b-a}\right)}{4\pi^2R}I_0\cos(\omega t)}\\  \\
&=\frac{R\tan(\omega t)}{\mu_0N^2a\omega\ln\left(\frac{2b+a}{2b-a}\right)}
\end{align}$$

#### Calcular la energía magnética almacenada 

Notar que $\vec{B}$ está definido únicamente entre $a-b/2$ y $a+b/2$ en $\hat{r}$ y entre $0$ y $a$ en $\hat{k}$. Así: 

$$\begin{align}
W&=\frac{1}{2\mu_0}\int\vec{B^2}\;dV\\  \\
&=\frac{1}{2\mu_0}\left(\frac{\mu_0NI}{2\pi}\right)^2\int^{a}_{0}\int^{2\pi}_{0}\int^{b+\frac{a}{2}}_{b-\frac{a}{2}}\frac{r\;dr\;d\phi\;dz}{r^2}\\  \\
&=\frac{\mu_0N^2I^2}{\cancelto{4}{8}\pi^{\cancel{2}}}\cancel{2}\cancel{\pi}a\ln\left(\frac{2b+a}{2b-a}\right)\\  \\
&=\frac{\mu_0N^2I^2a}{4\pi}\ln\left(\frac{2b+a}{2b-a}\right)
\end{align}$$

#### Encontrar el coeficiente de autoinducción ocupando el trabajo 

Para hacer esto se va a ocupar la otra forma de expresar $L$: 

$$W=\frac{1}{2}LI^2$$

De tal forma, reemplazando con todos los valores obtenidos anteriormente: 

$$\begin{align}
\frac{1}{2}LI^2&=\frac{\mu_0N^2I^2a}{4\pi}\ln\left(\frac{2b+a}{2b-a}\right)\\  \\
L&=\frac{\mu_0N^2a}{2\pi}\ln\left(\frac{2b+a}{2b-a}\right)
\end{align}$$

Se llegá a lo mismo. 

## Pregunta 2 

Considere una espira cuadrada, de masa $m$ y de resistencia $R$, la cual se encuentra sumergida en una zona donde existe un campo magnético uniforme $\vec{B}=B_0\hat{i}$, para $y>0$. 

![[Pasted image 20231128144410.png|center]]

Si la espira está fija en su lado que pasa por la recta que define el eje $z$ con posibilidad de rotar, se pide: 

#### Si la espira rota con velocidad angular constante, encontrar la fem y corriente inducida 

Notar que el flujo se define como: 

$$\Phi=\int\vec{B}\cdot d\vec{S}$$ 
Pero el cálculo no es directo, ya que la espira está rotando y el campo magnético que le llega no es constante. Si lo miramos desde arriba se tendría la siguiente figura:

![[IMG_5C0F83F9D322-1.jpeg|center|550]]

Podríamos ocupar la definición de integral de superficie, donde: 

$$\begin{align}
\Phi&=\oint\vec{B}\cdot d\vec{S}\\  \\
&=\int\vec{B}\cdot\hat{n}\;dS\\  \\
&=\vec{B}\cdot\hat{n}\Delta S
\end{align}$$

Y notar que $\vec{B}\cdot\hat{n}=\vert\vec{B}\vert\cdot\vert\hat{n}\vert\cos\alpha$, donde $\alpha=\frac{\pi}{2}-\phi$ 

Otro desarrollo análogo sería ocupar el esquema de arriba. Se podría plantear la siguiente integral: 

$$\begin{align}
\Phi&=\int^{a}_{0}\int^{L}_{0}B\;dx\;dz\\  \\
&=aLB_0\\  \\
&=a^2\sin(\phi)B_0\tag{Trigonometría}
\end{align}$$

Ambos caminos llegan al mismo resultado. 

Ahora, notar que, como la espira se mueve a una frecuencia angular constante, se puede reescribir el flujo en función del tiempo a través de la sigiuente igualdad: 

$$\begin{align}
\sin(\phi)&=\sin(\omega t)\\  \\
\implies\Phi(t)&=a^2\sin(\omega t)B_0
\end{align}$$

Así, para la fuerza electromotriz se llega que: 

$$\begin{align}
\epsilon&=-\frac{d\Phi}{dt}\tag{Definición}\\  \\
&=-a^2\omega B_0\cos(\omega t)
\end{align}$$

Por lo tanto, dado que la resistencia equivalente es $R$, es posible llegar que la corriente inducida en función del tiempo es la siguiente: 

$$\begin{align}
I(t)&=\frac{\epsilon(t)}{R}\\  \\
&=-\frac{a^2B_0\omega}{R}\cos(\omega t)
\end{align}$$

#### Encontrar la velocidad angular en función de $\phi$ y ver cuantas vueltas alcanza a dar la espira antes de detenerse. 

Sabemos que cuando $\vec{B}\neq 0$ la espira va a sentir una fuerza y, por ende, un torque. Sabemos que al ser un dipolo magnético, el torque viene dado por: 

$$\vec{\tau}=\vec{m}\times\vec{B}$$

Donde $\vec{m}=I\cdot\vec{A}\;\text{(Area de la espira)}$. Así, es directo reemplazar $\vec{A}$: 

$$\vec{A}=A\hat{n}=A(-\hat{\phi})=-a^2\hat{y}$$

También se tiene la siguiente definición de torque: 

$$\begin{align}
\vec{\tau}&=\frac{d\vec{L}}{dt}\\  \\
&=\frac{d}{dt}(J\dot{\phi}\hat{k})\\  \\
&=J\ddot{\phi}\;\hat{k}
\end{align}$$

Por lo tanto: 

$$\begin{align}
\vec{\tau}&=\vec{m}\times\vec{B}\\ \\
&=Ia^2(-\hat{\phi})\times(B_0\hat{x})\\  \\
&=Ia^2B_0(\sin(\phi)\hat{x}-\cos(\phi)\hat{y})\times B_0\hat{x}\\ \\
&=Ia^2B_0\cos(\phi)\;\hat{k}\\  \\
&=J\ddot{\phi}\hat{k}
\end{align}$$

También se puede hacer lo siguiente: 

$$\ddot{\phi}=\dot{\phi}\frac{d\dot{\phi}}{d\phi}=\frac{Ia^2B_0\cos(\phi)}{J}\tag{1}$$

Así, reemplazando $I$: 

$$\ddot{\phi}=\frac{a^2B_0\cos(\phi)}{J}\cdot\frac{-a^2B_0\dot{\phi}}{R}\cos(\phi)$$

Ocupando $(1)$: 

$$\begin{align}
\cancel{\dot{\phi}}\frac{d\dot{\phi}}{d\phi}&=-\frac{B_{0}^{2}a^4\dot{\phi}\cos^2(\phi)}{JR}\\  \\
&=-\left(\frac{a^4B_{0}^{2}}{JR}\right)\left(\frac{1+\cos(2\phi)}{2}\right)\\  \\
\implies\dot{\phi}(\phi)-\phi(0)&=-\left(\frac{a^4B_{0}^{2}}{JR}\right)\left(\phi+\frac{\sin(2\phi)}{2}\right)\\  \\
\implies\dot{\phi}(\phi)&=\omega_0-\frac{B_{0}^{2}a^4}{4JR}[2\phi+2\sin(2\phi)]
\end{align}$$

Reordenando: 

$$\dot{\phi}(\phi)=\omega_0-\frac{3}{5}\frac{(B_0a)^2}{mR}(2\phi-\sin(2\phi))$$

Por lo tanto, en $\phi=\pi$: 

$$\dot{\phi}(\phi=\pi)=\omega_0-\frac{6\pi a^2B_{0}^{2}}{5mR}$$ 
Entonces, por cada vuelta, $\dot{\phi}$ decrece en $\Delta\omega=\vert\dot{\phi}(\pi)-w_0\vert$. Por lo tanto, se va a detener luego de $n$ vueltas, con $n$ siendo: 

$$n=\frac{w_0}{\Delta w}$$
