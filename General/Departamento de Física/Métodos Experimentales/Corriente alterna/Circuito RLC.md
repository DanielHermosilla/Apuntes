Si al circuito ahora se le agrega un resistor, se deja de tener una relación etérnamente sinusoidal. Ahora la energía se va disipando progresivamente de forma térmica por el efecto Joule. 

![[Captura de Pantalla 2023-01-09 a la(s) 19.45.33.png|center]]

Si se considera a $E$ como la energía total y $\Delta E$ como la pérdida de energía por ciclo, entonces se dfine el factor de calidad $Q^*$ como:

$$Q^*=2\pi\frac{E}{\Delta E}$$ 
Por lo tanto, a frecuencias altas se funciona como un [[Circuito RL|circuito RL]]: 

$$ Z = R + i\omega L + \frac{1}{i\omega C}$$ 
A frecuencias bajas, se comporta como un [[Circuito RC|circuito RC]]: 

$$|Z| = \sqrt{R^2 + (\omega L - 1/\omega C)^2}$$ 

También existe el concepto de **resistencia crítica**, donde la forma de oscilación va variando según el valor de la resistencia. A $R_{crítica}$ se obtiene lo llamado *"underdamped"*. Tiene que ver más que nada con el decaimiento. 

![[Captura de Pantalla 2023-01-09 a la(s) 19.52.03.png|center]]

Además, la intensidad se puede modelar de la siguiente forma: 

$$|I_0(\omega)| = \frac{V_0}{\sqrt{R^2 + (\frac{L}{\omega})^2(\omega^2 - \omega_{0}^2)^2}}$$ 
Esta expresión tiene un máximo en $\omega = \omega_0$ 

## Ancho de la curva de resonancia 

Por último, se define el **ancho de la curva de resonancia** como la intensidad máxima obtenida en función de la frecuencia, determinada por la siguiente ecuación: 

$$\Delta\omega=\frac{R}{2L}$$ 
![[Captura de Pantalla 2023-01-09 a la(s) 19.55.30.png|center]]