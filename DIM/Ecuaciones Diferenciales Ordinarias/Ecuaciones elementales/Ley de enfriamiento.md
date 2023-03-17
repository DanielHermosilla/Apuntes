
Postulado por *Isaac Newton*, donde ocurre un intercambio de calor entre dos cuerpos, por ejemplo el oceano y la atmósfera. 

Para ver como variaba la temperatura del oceano, él miraba el signo de la [[Derivada|derivada]]. Si se tuviera que $T_1(x)$ es la temperatura caliente de la atmósfera y $T_2(x)$ es la del oceano, la derivada se podría modelar de la siguiente forma: 

$$T_{2}^{'}(t)=\sigma\;(T_1(t)-T_2(t))$$ 
Donde $\sigma$ corresponde a la **constante de intercambio** calórico océano-atmósfera y el restando corresponde a la **gradiente de temperatura**. 

En este caso, nuestra incógnita sería $T_{2}^{'}$. 

Esto sería una [[Ecuación diferencial lineal de primer orden|ecuación diferencial ordinaria]], ya que tenemos una igualdad, una incógnita que corresponde a una [[Derivada|derivada]] y ordinaria ya que tiene una variable independiente que correspondería a $t$ (tiempo). 

Si nos fijamos en las [[Ecuación diferencial lineal de primer orden|ecuaciones diferenciales lineales de primer orden]] se tienen los elementos necesarios; una constante ($\sigma$), una derivada única ($T_{2}^{'}(t)$), etc. 

### Solución 

Dejaremos al lado derecho lo que depende de la atmósfera: 

$$ T_{2}^{'} + \sigma\; T_2 = \sigma\; T_1(t) $$

Se puede catalogar una EDO lineal no homogénea (ya que no está igualado a $0$), de coeficiente constantes y de orden 1. 

Si no estuviera el segundo término se podría ocupar [[Integrales de primera especie|integral directa]] ya que llegariamos a lo siguiente: 

$$T_{2}^{'} = \sigma\; T_1(t)$$ $$\implies T_2 = \int\sigma T_1 + c, \ \ c\in\mathbb{R}\ \text{constante arbitraria}$$
Esté método se llama **integración directa**. 

De no ser tal caso, se tendría que buscar dos funciones multiplicadas que al derivarla nos de la solución.  

Es decir, buscar un valor $f$ tal que: 

$$(f·T_2)' = f\;T_{2}^{'} + f'\;T_2$$ 
Donde $\sigma f = f'\implies f = e^{\sigma t}$. 

Por lo tanto, volviendo a la ecuación original y multiplicando por $e^{\sigma t}$. 

$$[e^{\sigma t}\;T_{2}^{'} + \sigma\;e^{\sigma t}T_2] = \sigma\; T_1e^{\sigma t}$$

Y nos podríamos fijar que la igualdad izquierda es el resultado de la multiplicación de una derivada, entonces: 

$$(T_2e^{\sigma t})' = \sigma\; T_1(t)e^{\sigma t}$$ 
Y por lo tanto se ocupa la **integración directa**: 

$$T_2\;e^{\sigma t} = \int\sigma\; T_1e^{\sigma t} + C$$ 
Por lo tanto, 
$$T_2(t) = c\;e^{-\sigma t} + \sigma\; e^{-\sigma t}\int T_1(s)e^{\sigma s} ds\ \ ,\ c\in\mathbb{R}$$ 
Por lo tanto, tenemos lo siguiente: 

$$T_2(t) = \text{Solución homogénea (no depende de }T_1) + \text{Solución particular o forzante (depende de }T_1)$$ 
Esto llegaría a ser la **solución general**, ya que depende de una constante arbitraria. 

Ahora, uno podría plantear una posible ecuación de la temperatura atmosférica ocupando ecuaciones sinusoidales: 

$$T_1(t)=A\sin(\omega t) + D\ \ ,\;\omega>0$$ 
Y también vamos a tener a la función que encontramos en la EDO, que para terminos prácticos se va a reducir a la solución homogénea suamdo con la particular. 

$$T_2(t) = T_H + T_P$$ 
Notemos que $T_P$ es una oscilación periódica, esto se llama **solución permanente**, no así en $T_h$, ya que puede tender 0 cuando $t\rightarrow\infty$ (transiente). 

Acordemonos que se necesita una [[Condición inicial|condición inicial]] para poder determinar la constante $c$. 

Por lo tanto;

$$T_p = \sigma De^{-\sigma t}\int e^{\sigma t} + A\sigma e^{-\sigma t}\int\sin (\omega t)e^{\omega t}$$


Si se desarrollan ambas integrales (la segunda se podría hacer por partes o por [[Integración con variable compleja|integración por variable compleja]], se llega a lo siguiente: 

$$T_p = \frac{A\omega}{\sqrt{\omega^2 + \sigma^2}}[\frac{\sigma}{\sqrt{\omega^2 + \sigma^2}}\sin\omega t - \frac{\omega}{\sqrt{\sigma^2 + \omega^2}}\cos\omega t]$$ 
Considerando que son dos funciones sinusoidales, se puede hacer lo siguiente: 

$$\frac{A\omega}{\sqrt{\omega^2 + \sigma^2}}[\sin\phi - \cos\phi]$$ 
Con $\phi$ siendo la **fase**. Por lo tanto, la solución de la solución permanente es: 

$$T_p = A\frac{\omega}{\sqrt{\omega^2 + \sigma^2}}\;\sin(\omega t - \phi)$$ 