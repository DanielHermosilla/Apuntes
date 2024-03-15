
Sabemos que el [[Potencia eléctrica|potencial eléctrico]] se tenía que el [[Rotor|rotor]] era nulo, podiendo postular que se tiene un potencial eléctrico en el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]]. 

Ahora, para el [[Campo magnético|campo magnético]] se cumple que la [[Divergencia|divergencia]] es nula, pudiendo definir la siguiente equivalencia: 

$$\begin{align} 
\vec{\nabla}\cdot\vec{B}&=0\\ \\
\vec{\nabla}\cdot (\vec{\nabla}\times\vec{A})&=0\end{align}$$

Por lo tanto, es posible definir un $\vec{A}$ tal que: 

$$\vec{B}=\vec{\nabla}\times\vec{A}\iff\vec{\nabla}\cdot\vec{B}=0$$

Donde $\vec{A}$ es el potencial vectorial magnético. 

Dado $\vec{A}$ es un [[vectores|vector]] cualquiera, es posible definirla como $\vec{A}=\vec{A_0}+\vec{\nabla}\lambda$. La gracia de esto es poder escribir equivalencias en la [[Rotor y divergencia del campo magnético|ley de Ampere]]: 

$$\begin{align}
\vec{\nabla}\times\vec{B}&=\mu_0\vec{J}\\  \\
\vec{\nabla}\times (\vec{\nabla}\times\vec{A})&=\mu_0\vec{J}\\  \\
\vec{\nabla}(\vec{\nabla}\cdot\vec{A})-\nabla^2\vec{A}&=\mu_0\vec{J}
\end{align}$$

Entonces, la idea de esto, es tomar un $\lambda$ conveniente tal que se anule la ecuación, es decir: 

$$\vec{\nabla}\cdot\vec{A}=\vec{\nabla}\cdot\vec{A_0}+\nabla^2\lambda=0$$

Por lo tanto, se define una especie de *ecuación de Poisson* donde se cumple que: 

$$\nabla^2 A=-\mu_0\vec{J}$$ 
Por lo tanto, faltaría determinar el valor $\vec{A}$, que pareciera salir de: 

$$\vec{A}=\frac{\mu_0}{4\pi}\int\frac{\vec{J}(\vec{r}')}{\vec{r}}dz'$$

Donde $\vec{J}\to 0$ en el infinito. 

Como en electrostática, la [[Diferencia de potencial|diferencia de potencial]] se asociaba al trabajo por unidad de carga, lamentablemente en este caso, $\vec{A}$ **no tiene interpretación física**. 