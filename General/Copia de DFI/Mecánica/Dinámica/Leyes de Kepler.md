Notemos que si se tiene una [[Fuerzas centrales|fuerza central]], se puede llegar a la siguiente equivalencia, donde se tiene el siguiente barrido del área. 

![[IMG_1CDBBB5FE82E-1.jpeg]]

Notemos que el barrido del área se representa como: 

$$\vert\vec{r}\times d\vec{r}\vert= rdr\sin(\theta)$$ $$ds = \frac{1}{2}\vert\vec{r}\vert\vert d\vec{r}\vert\sin(\alpha)=\frac{1}{2}\vert\vec{r}\times d\vec{r}\vert$$
$$\frac{ds}{dt}=\frac{1}{2}\vert\vec{r}\times\frac{d\vec{r}}{dt}\vert=\frac{1}{2m}\vert\vec{r}\times m\vec{v}\vert$$ 

Notemos que se puede formar el área bajo la siguiente expresión:

$$\frac{1}{2}\vert\vec{r}\vert\vert d\vec{r}\vert\sin(\alpha)=dc$$ Donde $dc$ es el área. 

Si hacemos el *truco de mecánica* al dividir por $dt$: 

$$\frac{1}{2m}\vert\vec{r}\times\vec{p}\vert=\frac{dc}{dt}$$ 
Y además, notemos que $\vec{r}\times\vec{p}=\vec{l}$.  Por ende: 

$$\frac{dc}{dt}=\frac{1}{2m}\vert\vec{l_0}\vert=\frac{h}{2}$$ 

Entonces, esta ley se puede aplicar al movimiento en una elipse: 

![[IMG_B9AD03BADD60-1.jpeg|center]]

Por lo tanto, 

$$\begin{align}
\int dc&=\int\frac{h}{2}dt\\
\pi ab &=\frac{h}{2}T_0\\ 
T_0 &=\frac{2\pi ab}{h}
\end{align}$$ 
Además, sabemos que la ecuación del recorrido de una elipse es: 

![[ElipseRho.jpeg|center]]
$$\begin{align} 
\rho(\theta)&=\rho_0\frac{(1+e)}{(1-e\cos(\theta))}\\\\ 
\rho_1 &= \frac{1}{2}(\rho_0+\rho_1)\end{align} $$

Por lo tanto, donde $\theta$ corresponde al siguiente ángulo tranzado a partir de $\rho_0$ 

![[IMG_C5FE8BC58AE6-1.jpeg|center]] 

$$a=\frac{\rho_0}{(1-e)}$$ 
Y la expresión de $y$, llegaría a ser: 

$$\begin{align}
y &= \rho\sin(\theta)\\\\
&=\rho_0(1+e)\frac{\sin(\theta)}{(1+e\cos(\theta))}
\end{align}$$ 
Entonces, para encontrar $b$, hay que maximizar la expresión, se llega que el máximo ángulo $\theta$ es $\cos(\theta)=e$, y se llega a la siguiente figura si se le hace un zoom: 

![[IMG_CFF6A81E167F-1.jpeg|center]]

Además, notemos que: 

$$\begin{align}
a-\rho_0 &= \frac{\rho_0}{1-e}-\rho_0\\\\
&=\frac{\rho_0-(\rho_0-e\rho_0)}{1-e}\\\\
&=\frac{e\rho_0}{1-e}\\\\
&= ea
\end{align}$$

Por lo tanto, se llega a la siguiente equivalencia: 

![[IMG_D1C1C5C3D7D9-1 1.jpeg|center|600]]

Entonces, por pitágoras, se llega a lo siguiente: 

$$\begin{align}
T_{0}^{2} &= \frac{\rho_0(1+e)}{h^2}\\\\
&=\frac{h^2}{Gm}\frac{1}{h^2}\\\\
&=\frac{(2\pi)^2a^3}{GM} 
\end{align}$$

Es decir, el período al cuadrado de la órbita de la tierra es una constante equivalente al término hayado anteriormente. 