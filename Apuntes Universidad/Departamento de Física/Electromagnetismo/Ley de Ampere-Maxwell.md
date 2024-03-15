
A pesar de haber llegado a

$$\begin{align}
\vec{\nabla}\cdot\vec{B}&=0\tag{1}\\  \\
\vec{\nabla}\times\vec{B}&=\mu_0\vec{J}\tag{2}\\  \\
\vec{\nabla}\cdot\vec{E}&=\frac{\rho}{\epsilon_0}\tag{3}g\\  \\
\vec{\nabla}\times\vec{E}&=-\frac{\partial\vec{B}}{\partial t}\tag{4}
\end{align}$$

Por la [[Inducción Electromagnética|inducción electromagnética]], la ecuación $(2)$ presenta una inconsistencia al juntarla con la [[Ecuación de continuidad|ecuación de continuidad]]. Por lo tanto, falta algo para que la [[Ley de Ampere en materiales|ley de Ampere]] sea consistente. De la ecuación de continuidad se debe cumplir que:

$$\begin{align}
0&=-\mu_0\frac{\partial\rho}{\partial t}+C\\  \\
C&=\mu_0\frac{\partial\rho}{\partial t}\\  \\
&=\mu_0\frac{\partial}{\partial t}(\epsilon_0\vec{\nabla}\cdot\vec{E})\\  \\
&=\vec{\nabla}\cdot\left(\mu_0\epsilon_0\frac{\partial \vec{E}}{\partial t}\right)
\end{align}$$

Por lo tanto, se postula la **versión corregida de la Ley de Ampere**, llamada la Ley de Ampere Maxwell: 

$$\vec{\nabla}\times\vec{B}=\mu_0\vec{J}+\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}$$

Así, es posible postular todas las leyes de Maxwell: 

$$\begin{align}
\vec{\nabla}\cdot\vec{B}&=0\tag{1}\\  \\
\vec{\nabla}\times\vec{B}&=\mu_0\vec{J}+\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}\tag{2}\\  \\
\vec{\nabla}\cdot\vec{E}&=\frac{\rho}{\epsilon_0}\tag{3}g\\  \\
\vec{\nabla}\times\vec{E}&=-\frac{\partial\vec{B}}{\partial t}\tag{4}
\end{align}$$

