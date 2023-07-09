
Sabiendo que el exponencial se puede definir con la siguiente igualdad: 

$$e^{i\alpha} = \cos\alpha + i\sin\alpha$$ 
Entonces al tener una función sinusoidal, se podría ocupar un cambio de variable compleja para resolver una [[Integral en varias variables|integral]]. 

### Ejemplo 

Sea la siguiente integral: 

$$\int\sin(\omega t)e^{\sigma t}$$ 
Por lo tanto, se podría hacer lo siguiente al hacer el cambio de variable: 

$$Im\int e^{(\sigma + i\omega)}t = Im[\frac{1}{\sigma + i\omega}e^{(\sigma + i\omega)t}]$$ 
Entonces, para llegar a la forma $a + bi$ se hace una conjugación 

$$\frac{1}{\sigma + i\omega}\;\frac{\sigma - i\omega}{\sigma - i\omega} = \frac{\sigma - i\omega}{\sigma^2 + \omega^2} = \frac{\sigma}{\sigma^2 + \omega^2} - i\;\frac{\omega}{\sigma^2 + \omega^2}$$ $$\implies Im(\frac{\sigma}{\sigma^2 + \omega^2}-i\frac{\omega}{\sigma^2 + \omega^2})(\cos(\omega t) + i\sin(\omega t))e^{\sigma t}$$ 
Factorizando el $\frac{1}{\sigma^2 + \omega^2}$ y desarrollando, tenemos: 

$$e^{\sigma t}\frac{1}{\sigma^2 + \omega^2}[\sigma\sin(\omega t)-\omega\cos(\omega t)]$$ 