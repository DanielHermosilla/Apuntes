
Por lo general, se puede definir la siguiente [[transformaciones lineales|transformación]] para algunas funciones termodinámicas: 

$$f(x,y)\to f-\left(\frac{\partial f}{\partial x}\right)x$$

Por lo tanto, es posible reescribir la energía cuando está en función de la [[Entropía|entropía]] y el volumen: 

$$E\to E-\left(\frac{\partial E}{\partial V}\right)V$$

Esto es equivalente a lo siguiente, por definición: 

$$E\to E+PV=H$$

Análogamente, si se hace sobre $S$, se llega a la **energía libre de Helmholtz**: 

$$E\to E-TS$$

Si combinamos ambas, se llega a **energía libre de Gibbs**: 

$$E+PV-TS=G$$

Es posible llegar que: 

$$\begin{align}
H&=E+PV\\  \\
dH&=(dE)+d(PV)\\  \\
&=(TdS-PdV)+PdV+VdP\\  \\
&=TdS+VdP 
\end{align}$$

Si desarrollamos para cada variable: 

$$\begin{align}
dE&=TdS-PdV\\  \\
dH&=TdS+VdP\\  \\
dF&=-PdV-SdT\tag{Energía libre de Helmholtz}\\  \\
dG&=VdP-SdT
\end{align}$$


Acordándonos que las [[Derivadas parciales|derivadas parciales]] cruzadas sirven para encontrar relaciones: 

$$\begin{align}
dE&=TdS-PdV\\  \\
&=\left(\frac{\partial E}{\partial S}\right)dS+\left(\frac{\partial E}{\partial V}\right)dV\\  \\
&=\frac{\partial}{\partial V}\left((\frac{\partial E}{\partial V})\right)\\  \\
&=\left(\frac{\partial T}{\partial V}\right)\\  \\
&=\frac{\partial}{\partial S}\left(-P\right)
\end{align}$$

Esto, básicamente nos dice que: 

$$\left(\frac{\partial T}{\partial V}\right)=-\left(\frac{\partial P}{\partial S}\right)$$

Análogamente: 

$$\begin{align}
\left(\frac{\partial T}{\partial P}\right)&=\left(\frac{\partial V}{\partial S}\right)\\  \\
\left(\frac{\partial P}{\partial T}\right)&=\left(\frac{\partial S}{\partial V}\right)\\  \\
\left(\frac{\partial V}{\partial T}\right)&=-\left(\frac{\partial S}{\partial P}\right)
\end{align}$$