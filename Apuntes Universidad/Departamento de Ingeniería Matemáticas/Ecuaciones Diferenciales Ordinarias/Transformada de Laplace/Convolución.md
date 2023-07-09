
Sean $f,g\in\mathbb{C}_\alpha$, luego se define la convolución entre $f$ y $g$ como: 

$$(f*g)(t)=\int^{t}_{0}f(s)g(t-s)ds$$ 

## Propiedad 

1. La convolución conmuta (solo respecto a la suma), asocia y distribuye para funciones en $\mathbb{C}_\alpha$. 

2. Se tiene que $\mathbb{L}[f*g](s) = L[f](s)\cdot\mathbb{L}[g](s)$ 

Esto se da por definición: 

$$\begin{align}
L[f*g](s)&=\int^{\infty}_{0}\left(\int^{t}_{\infty}f(u)g(t-u)du\right)e^{st}dt\\\\
&\text{Ocupando}\;\text{Fubini}\\\\ 
&=\int_{0}^{\infty}\int^{\infty}_{u}f(u)g(t-u)e^{-st}dt\;du\\\\
&=\int_{0}^{\infty}f(u)\int^{\infty}_{u}g(t-u)e^{-st}dt\;du\\\\
&=\int^{\infty}_{0}f(u)\int^{\infty}_{0}\mathbb{1}_{t<x<\infty}\;g(t-u)e^{-st}dt\;du\\\\ 
&=\int^{\infty}_{0}f(u)\mathbb{L}[\mathbb{1}_{t<x<\infty}\;g(t-u)](s)du\\\\ 
&=\int^{\infty}_{0}f(u)e^{-su}\;\mathbb{L}[g](s)du\\\\ 
&=\mathbb{L}[g](s)\int^{\infty}_{0}f(u)e^{-su}du\\\\ 
&=\mathbb{L}[g](s)\cdot\mathbb{L}[f](s)
\end{align}$$

