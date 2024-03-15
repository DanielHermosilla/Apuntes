
Existen tres tipos de respuestas de un material a un [[Campo magnético|campo magnético]]: 

- **Paramagnético** Los $\vec{m}$ del material se orientan **paralelos** a $\vec{B}$

- **Diamagnético**: Los $\vec{m}$ se orientan **anti-paralelo** a $\vec{B}$

- **Ferreomagnético**: Hay $\vec{m}$ permanente, $\vec{m}$ depende de la historia del material. 

## Campo magnético de un objeto magnetizado 

Es posible imaginar un [[Sistema macroscópico|sistema macroscópico]] con [[Momento dipolar magnético|dipolo magnético]]. 

![[Captura de pantalla 2023-10-23 a la(s) 09.18.56.png|center]]

Por lo tanto, se define $\vec{A}(r)$: 

$$\vec{A}(r)=\frac{\mu_0}{4\pi}\frac{\vec{m}\times\vec{(r-r')}}{(r-r')^2}$$

Por lo tanto, el potencial del dipolo magnético, para el sistema macroscópico, ocupando la definición de la [[Fuerza de un dipolo magnético|fuerza de un dipolo magnético]] [[Sistema macroscópico|macroscópico]]: 

$$\vec{A}(r)=\frac{\mu_0}{4\pi}\int\frac{\vec{M}(\vec{r'})\times(r-r')}{(r-r')^2}$$

La idea es poder expandir $1/(r-r')^2$ y usar identidades vectoriales, integración por partes, etc: 

$$\vec{A}(\vec{r})=\frac{\mu_0}{4\pi}\int_V\frac{1}{(r-r')}(\vec{\nabla}\times\vec{M})dz'+\frac{\mu_0}{4\pi}\oint_S\frac{1}{(r-r')}(\vec{M}\times\hat{n})\;da$$

Se puede definir, por lo tanto,  la [[Corriente eléctrica|corriente]] de magnetización como: 

$$\begin{align}
\vec{J_m}&=\vec{\nabla'}\times\vec{M}(\vec{r})\\  \\
\vec{K_m}&=\vec{M}\times\hat{n}
\end{align}$$

Donde $\vec{J_m}\equiv\vec{J_b}$ y $\vec{K_m}\equiv\vec{K_b}$. De tal forma, el [[Campo magnético|campo magnético]] llegaría a ser: 

$$\vec{B}=\vec{\nabla}\times\vec{A}$$

