
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

$$T_2(t) = \text{Solución homogénea (no depende de }T_1) + \text{Solución particular (depende de }T_1)$$ 