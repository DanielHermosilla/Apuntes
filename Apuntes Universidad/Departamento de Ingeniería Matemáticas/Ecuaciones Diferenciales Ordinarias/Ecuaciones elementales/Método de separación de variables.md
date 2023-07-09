
Son de la forma: 

$$y' = f(x)g(y)$$ 
Donde se tiene una **multiplicación**. 

O en el caso más general: 

$$y' = F(x,y)$$ 
Se llama separación de variables al hacer el siguiente paso, ya que se tiene la incognita $y$ y $x$ en los distintos lados de la igualdad: 

$$\frac{y'}{g(y)}=f(x)$$ 
Por lo tanto, [[Integral de Riemann|integrando]]: 

$$\int\frac{y'(x)}{g(y(x))}dx=\int f(x)dx + C$$ 
Haciendo cambios de variables, definiendo la variable $u = y(x)$ . 

$$\int\frac{dy}{g(y)}=\int f(x)dx + C$$

Por lo tanto, la forma implícita de la solución sería: 

$$G(y) = F(x) + C$$ 
### Ejemplo: Modelo de población 

Un modelo logístico que plantea lo siguiente: 

$$P' = \sigma P(1-P)$$ 
No esta escrito, pero la población depende del tiempo, siendo ésta la variable independiente:

$$P(t)$$

Entonces, reconociendo las componentes: 

$$f(t)=1\ \land\ g(P)=\sigma P(1-P)$$ 
Notemos que si existe una solución $y=cte$ que anule a $g$, es decir, $g(cte)=0$, será una solución especial de la EDO. En este caso, sería en $P=0\lor 1$. Estos casos especiales se hacen para **no dividir por cero**. 

Entonces, se ocupa el método de separación de variable: 

$$\frac{P'}{\sigma P(1-P)} = 1$$ 
$$\frac{1}{\sigma}\int\frac{P'}{P(1-P)}dt = \int 1dt$$ 
Entonces, el cambio de variable sería $P(t)$: 

$$\int\frac{dP}{P(1-P)} = t + c$$ 
Entonces se ocupa el **método de fracciones parciales**, donde: 

$$\frac{1}{P(1-P)} = \frac{A}{P}+\frac{B}{1-P}$$ 
$$1 = A + P(B-A)\implies A=1\ \land B=1$$ 
Por lo tanto:

$$\frac{1}{\sigma}[\ln(P)-\ln(1-P)] = t + c$$ 
Notar que es la integral de un logaritmo, recordando lo siguiente: 

$$\int\frac{1}{x}=\ln|x| + c$$ 
Y el $c$ se puede expresar como un logaritmo, con $ln(e^c)$. Entonces: 

$$\int\frac{1}{x}=\ln |x| + \ln K = K\ln(|x|)\ \ K>0$$ 
Sería una **solución implícita**. Falta despejar $P$.  

$$\implies\ln(\frac{P}{1-P})=\sigma t + \hat{c}$$ $$\frac{P}{1-P}=Ke^{\sigma t}\ \ \ \ K=e^{\hat{c}}> 0 $$
$$P=(1-P)Ke^{\sigma t}$$ $$\iff P=\frac{K}{K + e^{-\sigma t}}\ \ \ K>0$$

Ya con la solución hecha, hay que despejar $K$ y acordarnos de la hipótesis que $P\in (0,1)$. 

Para encontrar $K$ hay que asumir una [[Condición inicial|condición inicial]] donde asumiremos que $P(0)=P_0>0$. Notemos que la población en el instante $0$ vale $\frac{K}{K+1}$. Entonces, la variable $K$ nos dará el valor inicial. Entonces, volviendo a la [[Condición inicial|condición inicial]], $K=\frac{P_0}{1-P_0}$. 