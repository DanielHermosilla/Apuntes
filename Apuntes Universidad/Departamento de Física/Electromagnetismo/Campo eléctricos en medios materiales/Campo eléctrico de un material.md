
Suponiendo que se tiene un material [[Dipolo inducido|polarizado]] que tiene su respectivo vector polarización $\vec{p}=\frac{\sum^{N}_{i=1}\vec{p_i}}{\text{Vol}}$. Por lo tanto, la pregunta a resolver es, dado un $\vec{p}$ para el material, *¿cuál sería el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] producido por el material dieléctrico?*. 

Aplicando la definición del [[Trabajo del campo eléctrico|trabajo]] del campo eléctrico eléctrico: 

$$\begin{align}
V(\vec{r})&=\frac{1}{4\pi\epsilon_0}\int\frac{\rho(\vec{r})dz'}{\vert\vec{r}-\vec{r'}\vert}\\  \\
&=\cancelto{0}{V_{\text{Monodipolo}}}+V_{\text{Dipolo}}+ O\left((\frac{r'}{r})3\right)\\  \\
&=0
\end{align}$$

Donde $O$ representa el orden de la expansión de Taylor. Se puede concluir que sólo es necesario saber $V_{\text{Dipolo}}$ para calcular el campo producido. Por lo tanto: 

$$\begin{align}
V_{\text{Dipolar}}(\vec{r})&=\frac{1}{4\pi\epsilon_0}\;\frac{\vec{p}\cdot\hat{r}}{r^2}
\end{align}$$

Para todo el material se puede [[Integral de superficie|integrar]]: 

$$\begin{align}
V_{\text{Dipolar}}(\vec{r})&=\frac{1}{4\pi\epsilon_0}\;\int_{\text{Volumen material}}\frac{\vec{p}\cdot\hat{r}}{r^2}\;dz'
\end{align}$$


Haciendo muchos cálculos vectoriales se llega que: 

$$V(\vec{r})=\frac{1}{4\pi\epsilon_0}\int\frac{\frac{1}{p}\cdot\hat{n}}{r}+\frac{1}{4\pi\epsilon_0}\int\frac{-\vec{\nabla}\cdot\vec{-p}}{r}dz$$

Desarrollando aun más: 

$$V(\vec{r})=\frac{1}{4\pi\epsilon_0}\int_{S=\partial v}\frac{\rho_p}{r}da+\frac{1}{4\pi\epsilon_0}\int_V\frac{\rho}{r}dz$$

