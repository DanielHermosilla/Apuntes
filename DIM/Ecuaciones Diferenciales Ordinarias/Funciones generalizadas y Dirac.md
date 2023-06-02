
## Acción 

Si $f$ es [[Integral de Riemann|integrable]], tal que $f:\mathbb{R}\rightarrow\mathbb{R}$, se define la **acción** de $\psi$ sobre $f$ como: 

$$\psi [f]=\int^{\infty}_{-\infty}\psi(t)f(t)dt$$ 
## Dirac 

Se define $\delta$ tal que: 

$$\delta [f]=f(0)=\int^{\infty}_{-\infty}\delta(t)f(t)$$ 
Es decir, 

$$\begin{align}
\psi(0)&=+\infty \\
\psi(t)&=0&t\neq 0
\end{align}$$ 
Entonces, dirac en la [[Transformada de Laplace]] sería lo siguiente: 

$$\mathbb{L}[\delta](s)=\int^{\infty}_{0}\delta(t)e^{-st}dt = e^{-st}\bigg\vert_{s=0}=1$$ 
### Ejemplo 

$$\begin{align}
y'(t)&=\delta (t)&\backslash\mathbb{L}\\ 
s\mathbb{L}[y]-y(0^+)&=1
\end{align}$$ 
Si decimos $y(0)=1$, entonces $s\mathbb{L}[y]=2$

$$\implies L[y]=\frac{2}{3}\implies y(t)=2$$ 