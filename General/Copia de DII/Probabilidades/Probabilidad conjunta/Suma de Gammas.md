
Sean $X\sim\text{Gamma}(s,\lambda)$ e $Y\sim\text{Gamma}(t,\lambda)$ variable [[Probabilidades/Probabilidad conjunta/Probabilidad conjunta continua/Independencia|independientes]], entonces, la distribución de $Z=X+Y$ llegaría a ser: 

Aplicando [[Convolución|convolución]]: 

$$f_Z(z)=\int_{-\infty}^{\infty}f_X(z-y)f_Y(y)dy$$ 
$$\begin{align}
&=\int_{0}^{z}\frac{\lambda e^{-\lambda (z-y)} (\lambda(z-y))^{s-1}}{\gamma (s)}\cdot\frac{\lambda e^{-\lambda y}(\lambda y)^{t-1}}{\gamma (t)}dy\\\\
&=\frac{\lambda^{s+t}e^{\lambda z}z^{s+t-1}}{\gamma(s)\gamma(t)}\frac{\int_{0}^{1}z^{s-1}(1-v)^{s-1}v^{t-1}z^{t-1}zdv}{\int_{0}^{1}(1-v)^{s-1}v^{t-1}dv}\\\\
&=\frac{\lambda\cdot e^{-\lambda z}(\lambda z)^{s+t-1}}{\gamma(s+t)}dy\\\\ 
&=\frac{Z\sim\text{Gamma}(s+t,\lambda)}{X\sim\text{Exp}(\lambda)\implies X\sim\text{Gamma}(1,\lambda)}

\end{align}$$ 