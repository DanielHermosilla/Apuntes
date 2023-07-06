
La [[Potencia eléctrica|potencia eléctrica]] que se distribuye para usos domiciliarios e industriales es casi universalmente una señal que tiene variación sinusoidal con el tiempo. Se denomina CA o AC. 

![[Captura de Pantalla 2023-01-09 a la(s) 18.10.31.png]]

Normalmente la [[Potencia eléctrica|potencia eléctrica]] es con una frecuencia de $50hz$, es decir, oscila con un período de $20$ milisegundos. El voltaje es caracterízado entre el máximo y mínimo de la [[onda]], es decir, lo que se conoce por voltaje *peak-to-peak*. 

Otra forma de expresar el voltaje es a través del valor eficaz. Es decir, la raíz cuadrada del promedio del cuadrado del valor instantáneo del voltaje. Básicamente, el valor absoluto del promedio del voltaje. Para el voltaje sinusoidal de amplitud $A$ se ocupá la formula típica de [[onda|ondas]]: $V(t)=A\sin \omega t$. 

Entonces: 

$$\bar{V(t)^2}=\frac{1}{2\pi}\int^{2\pi}_{0}(A\sin (\omega t))^2d(\omega t)=\frac{1}{2}A^2$$ 
Y por ende, el voltaje de valor eficaz sería: 

$$V_{rms}=\sqrt{\bar{V(t)^2}}=\frac{A}{\sqrt{2}}$$ 
Análogamente: 

$$I_{rms}=\sqrt{\bar{I(t)^2}}$$ 
Por lo tanto, el valor eficaz en la red de una casa sería de $220V$ pero su amplitud sería $A=311V$. 

También se puede hacer el análogo con la [[Potencia eléctrica|potencia]] disipada. Recordando la fórmula: 

$$P(t)=I^2R$$ 
Se ve que la potencia promedio disipada para una corriente alterna es $I(t) = A\cos (\omega t)$ es: 

$$\bar{P(t)}=\bar{I^2(t)}R = I^{2}_{rms}R$$ 
Acordando que la resistencia no varía en función del tiempo. Si lo relacionamos con la corriente continua, el voltaje promedio se comporta **igual** a que un sistema alterno. Por eso mismo, es mejor trabajar con valores RMS. 