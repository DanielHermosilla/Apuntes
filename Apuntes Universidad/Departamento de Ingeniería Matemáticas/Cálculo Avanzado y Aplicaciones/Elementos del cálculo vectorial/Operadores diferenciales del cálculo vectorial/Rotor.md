
Sea $\vec{F}=F_1\hat{i}+F_2\hat{j}+F_3\hat{k}$ un [[Campos escalares y vectoriales|campo vectorial]] de clase $C^1$, se define el rotor como: 

$$\text{rot}\;\vec{F}=\left(\frac{\partial F_3}{\partial y}-\frac{\partial F_2}{\partial z}\right)\hat{i}+\left(\frac{\partial F_1}{\partial z}-\frac{\partial F_3}{\partial x}\right)\hat{j}+\left(\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\right)\hat{k}$$

Pareciera ser algo azaroso, pero en realidad se puede describir utilizando el **producto cruz** entre la función y su [[Divergencia|divergencia]]:

$$\text{rot}\;\vec{F}=\nabla\times\vec{F}=\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
F_1 & F_2 & F_3
\end{vmatrix}$$

