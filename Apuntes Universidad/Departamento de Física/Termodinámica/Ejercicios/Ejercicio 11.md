
## Suma de estados 

Ocupando la fórmula de la suma de los factores de Boltzmann para los estados accesibles del sistemas, la suma llegaría a ser: 

$$Z=e^{-\beta\epsilon}+e^{\beta\epsilon}$$

Donde: 

- $\beta=1/kT$
## Energía promedio 

La energía promedio se define como la derivada del logaritmo natural de $Z$ con respecto a $\beta$ multiplicado por $-1$. Así: 

$$\begin{align}
\langle E\rangle&=-\frac{1}{Z}\frac{\partial Z}{\partial \beta}=\frac{d(\ln Z)}{d\beta}
\end{align}$$

Así: 

$$\begin{align}
\frac{d\ln Z}{d\beta}&=-\frac{\epsilon e^{-\beta\epsilon}-\epsilon e^{\beta\epsilon}}{e^{-\beta\epsilon}+e^{\beta\epsilon}}\\  \\
\langle E\rangle &=-\frac{\epsilon e^{-\beta\epsilon}-\epsilon e^{\beta\epsilon}}{e^{-\beta\epsilon}+e^{\beta\epsilon}}\\  \\
&=-\epsilon\tanh(\beta\epsilon)
\end{align}$$

## Energía promedio positiva 

El signo de la energía promedio depende del valor de $\epsilon\beta$. Si $\epsilon\beta$ es grande, entonces la energía promedio va a tender a $-\epsilon$.

Por el otro lado, si la multiplicación es pequeña la energía va a tender a $0$ (lo que corresponde a una temperatura alta). 

Por ende, no es posible que se tenga energía promedio positiva ya que estará entre $0$ y $-\epsilon$. Esto se debe que a menor temperaturas el sistema va a tender a estar en el estado de menor energía mientras que a mayor temperatura la distribución es más uniforme. 

