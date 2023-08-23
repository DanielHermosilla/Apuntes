
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
W&=\frac{1}{#}
\end{align}$$