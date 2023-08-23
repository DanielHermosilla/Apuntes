
Se tienen $n$ cargas eléctricas y se quiere saber el trabajo de cada uno: 

![[IMG_7E2D81E7EA72-1.jpeg|center]]

Si vamos analizando el sistema partícula por partícula: 

$$\begin{align}
W_1&=0\\  \\
W_2&=q_2V_1\\  \\
W_2&=q_2\frac{q_1}{4\pi\epsilon_0r_{12}}\\  \\
W_3&=q_3\frac{q_1}{4\pi\epsilon_0r_{13}}+q_3\frac{q_2}{4\pi\epsilon_0r_{23}}
\end{align}$$

Por lo tanto, para el caso $n-esimo$ se podría resumir como: 

$$W_i=q_iV_i+\dots+q_iV_{i-1}=\sum^{i-1}_{j=1}q_iV_j$$

Y así para las otras cargas: 

$$\sum^{N}_{j=1}\frac{q_iq_j}{4\pi\epsilon_0r_{ij}}$$

Si sumamos toda la [[Trabajo y Energía en Electrostática|energía]]:

$$W=\sum^{N}_{i=1}W_i=\sum^{N}_{i=1}\sum^{i-1}_{j=1}\frac{q_iq_j}{4\pi\epsilon_0r_{ij}}$$ 
Esta sumatoria es horrible, entonces se puede tratar de ver [[matriz|matricialmente]]: 

$$\begin{vmatrix}
\times &  &  &  &  &  \\
\checkmark & \times &  &  &  &  \\
\checkmark & \checkmark & \times &  &  &  \\
\checkmark & \checkmark & \checkmark & \times &  &  \\
\checkmark & \checkmark & \checkmark & \checkmark & \times &  \\
\checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \times
\end{vmatrix}$$

Por lo tanto, en realidad la sumatoria sería: 

$$W=\frac{1}{2}\sum^{N}_{i=1}\sum^{N}_{j=1\; j\neq i}\frac{q_iq_j}{4\pi\epsilon_0r_{ij}}$$ 
Simplificando esto y definiendo $r_{ij}=\vert\vec{r_i}-\vec{r_j}\vert$: 

$$W=\frac{1}{2}\sum^{N}_{i=1}q_i\left(\sum^{N}_{j=1}\frac{q_j}{4\pi\epsilon_0r_{ij}}\right)$$

Pero, notemos que el término en el paréntesis es el potencial en $\vec{r_i}$ debido a todas las otras cargas, entonces, se puede llegar a la expresión final: 

$$\begin{align}
W&=\frac{1}{2}\sum^{N}_{i=1}q_i\cancelto{V(\vec{r_i})}{\left(\sum^{N}_{j=1}\frac{q_j}{4\pi\epsilon_0r_{ij}}\right)}\\  \\
W&=\frac{1}{2}\sum^{N}_{i=1}q_iV(\vec{r_i})
\end{align}$$


# Caso continuo 

Si asumimos una distribución continua con densidad de carga $\rho$, entonces se tendría lo siguiente: 

![[IMG_9659961E8C32-1.jpeg|center|400]]

Por lo tanto, el cálculo sería: 
$$\begin{align}
W&=\frac{1}{2}\int V(\vec{r})\;dq' \\  \\
&=\frac{1}{2}\int V(\vec{r''})\rho(\vec{r''})dZ'
\end{align}$$

De igual forma, si nos acordamos de la definiciónes de [[Trabajo del campo eléctrico|trabajo del campo eléctrico]], se pueden obtener varias equivalencias: 

$$\begin{align}
\vec{\nabla}\cdot\vec{E}&=\frac{\rho}{\epsilon_0}\\  \\
\vec{\nabla}\times\vec{E}&=0
\end{align}$$

Por lo tanto, el trabajo se llegaría a escribir como: 

$$W=\frac{\epsilon_0}{2}\int(\vec{\nabla}\cdot\vec{E})V\;dz$$

Y ahora, descomponiendo los términos de adentro: 

$$\begin{align} 
\vec{\nabla}\cdot(VE)&=V(\vec{\nabla}\cdot\vec{E})+\vec{E}\cdot(\vec{\nabla}V)\\  \\
&=\vec{\nabla}\cdot (V\vec{E})-\vec{E}\cdot (\vec{\nabla}V)\\ \\
\implies W&=\frac{\epsilon_0}{2}\int\vec{\nabla}\cdot (V\vec{E})\; dz-\frac{\epsilon_0}{2}\int\vec{E}\cdot (\vec{\nabla}V)\;dz\\  \\
&=\frac{\epsilon_0}{2}\oint_S(V\vec{E})\cdot d\vec{s}+\frac{\epsilon_0}{2}\int_V\vec{E}\cdot\vec{E}\; dz
\end{align}$$


Si resolvemos el primer sumando y asumiendo un volumen esférico con radio $R$, notemos que cuando todo diverge al infinito, los componentes escalan como: 

$$\begin{align}
V&\sim\frac{1}{R}\\  \\
\vert\vec{E}\vert&\sim\frac{1}{R^2}\\  \\
\vert d\vec{s}\vert&\sim R^2\\  \\
(V\vec{E})\cdot d\vec{s}&\sim\frac{1}{R}\to_{R\to\infty}0
\end{align}$$

Entonces, en realidad el trabajo llegaría a ser: 

$$W=\frac{\epsilon_0}{2}\int E^2\;dz$$ 
Donde $E^2=\vec{E}\cdot\vec{E}$ . Por ende, **existen dos formas de calcular la energía electrostática**: 

$$\begin{align*}
W&=\frac{1}{2}\int_{\text{Sólo la fuente}}\rho V\; dz\tag{1}\\ \\ 
W&=\frac{\epsilon_0}{2}\int_{\text{Todo el espacio}}E^2\;dz\tag{2}
\end{align*}$$


De aquí, se concluye que **la densidad de energía en el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] es**: 

$$\rho_e=\frac{\epsilon_0}{2}E^2$$

