
# Pregunta 1 

## Calcular la resistencia entre los electrodos 

Anteriormente se había llegado que: 

$$\vec{J}(r)=\frac{K}{r^2}\hat{r}$$

Así, para calcular la resistencia se ocupan las siguientes fórmulas: 

$$\begin{align}
V&=IR\tag{1}\\  \\
J&=\frac{dI}{dA}\tag{2}
\end{align}$$

La diferencia de potencial es fija $(V_0)$, por lo tanto: 

$$R=\frac{V_0}{I}$$ 
Calculando la intensidad de corriente para $a<r<b$: 

$$\begin{align}
I&=\int^{}_{}J(r)dA\\  \\
&=\int^{}_{}\frac{K}{r^2}dA\\  \\
&=K\int^{2\pi}_{0}\int^{c}_{a}\frac{1}{r}\;dr\;d\theta\\  \\
&=K\int^{2\pi}_{0}\ln\left(\frac{a}{c}\right)d\theta\\  \\
&=2K\pi\ln\left(\frac{a}{c}\right)
\end{align}$$
