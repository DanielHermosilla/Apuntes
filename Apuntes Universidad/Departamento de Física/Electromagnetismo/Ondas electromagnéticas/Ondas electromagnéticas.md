
Acordándonos de la [[onda electromagnética|ecuación de onda]], se tenía que: 

$$\frac{\partial^2f}{\partial z^2}=\frac{1}{v^2}\frac{\partial^2f}{\partial t}$$

Además, se tiene lo siguiente para funciones de onda: 

$$\begin{align}
g(z-vt)\tag{Desplazado hacia la derecha}\\  \\
h(z+vt)\tag{Desplazado hacia la izquierda}
\end{align}$$

Aun así, interesa estudiar la forma sinusoidal, donde se tiene que: 

$$f(z,t)=A\cos(k(z-vt)+\delta)$$

Donde $A$ es la amplitud y $\delta$ es la fase. Si dejamos $t=0$ es posible obtener el número de onda $k$ y longitud de onda $\lambda$: 

$$\begin{align}
k&=\frac{2\pi}{\lambda}\\  \\
\lambda&=\frac{2\pi}{k}
\end{align}$$

Y, cuando se trabajan con ondas monocromáticas se puede hacer una [[Transformada de Fourier|transformada de Fourier]], donde: 

$$\bar{f}(z,t)=\int^{\infty}_{-\infty}\bar{A}(k)e^{i(kx-wt)}dk$$

