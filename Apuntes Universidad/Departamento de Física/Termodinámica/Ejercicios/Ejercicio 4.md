
Considere la entropía de un sólido de $N$ átomos con $m$ defectos de red: 

$$S(m)=mk_b\left[\ln(\frac{N}{m})+1\right]$$

Donde la energía total de la red es proporcional al número de defectos, $E=\epsilon\cdot m$. 

Encontrar la energía del sólido en función de la temperatura absoluta del sistema, $E(T)$. 

### Solución 

Por lo general, la definición de la temperatura absoluta es la siguiente: 

$$\frac{1}{T}=\left(\frac{\partial S}{\partial E}\right)_V$$

Por lo tanto, expresando la energía en función de la entropía: 

$$T=\frac{\partial E}{\partial S}$$

Notemos que la energía se relaciona con la entropía por el término $m$, entonces: 

$$\frac{\partial E}{\partial m}=\epsilon$$

Y por el otro lado, si derivamos la entropía en función de $m$ podremos relacionar ambos términos por regla de la cadena: 

$$\frac{\partial S}{\partial m}=\ln(\frac{N}{m})k_b$$


Por lo tanto: 

$$\frac{\partial S}{\partial E}=\frac{\partial S}{\partial m}\cdot\frac{\partial m}{\partial E}$$ 
$$\frac{\partial S}{\partial E}=\ln(\frac{N}{m})k_b\cdot\frac{1}{\epsilon}$$

Luego, 

$$T=(\ln(\frac{N}{m})k_b\cdot\frac{1}{\epsilon})^{-1}$$

Usando la definición de la energía, $m=E/\epsilon$: 

$$T=(\ln(\frac{N\epsilon}{E})k_b\cdot\frac{1}{\epsilon})^{-1}$$
$$\frac{T}{\epsilon}=(\ln(\frac{N\epsilon}{E})k_b)^{-1} $$

$$\frac{\epsilon}{T}=ln(\frac{N\epsilon}{E})k_b$$

$$e^{\frac{\epsilon}{Tk_b}}=\frac{N\epsilon}{E}$$

$$E(t)=\frac{N\epsilon}{e^{\frac{\epsilon}{Tk_b}}}$$