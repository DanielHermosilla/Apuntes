
Es de la siguiente forma: 

$$y' + a(x)y = q(x)y^n\ \ \ n\neq 1,\; n\neq 0$$ 
Entonces el [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Cambio de variable|cambio de variable]] es $z(x)=y^{1-n}$, entonces se tiene $(y^{1-n})' = (1-n)\; y^{-n}\; y'$ 

Y la ecuación llega a quedar, al multiplicarla por $(1-n)y^{-n}$: 

$$(1-n)y'y^{-n} + a(x)(1-n)y^{1-n} = (1-n)q(x)$$ 
Y reemplazando por el cambio de variable: $$z' + (1-n)a(x)z = (1-n)q(x)$$ 
Es una [[Ecuación diferencial lineal de primer orden|EDO de primer orden.]] 

Al terminar, se deshace el cambio de variable donde: 

$$y = z^{\frac{1}{1-n}}$$ 
### Ejemplo 

La ecuación de crecimiento logístico: 

$$P' = \sigma P(1-P)$$
$$P' - \sigma P = -\sigma P^2$$ 
Se puede aplicar una EDO de Bernoulli de n=2. Por lo tanto, el cambio de variable es: 

$$z=P^{1-2}=\frac{1}{P}$$

Entonces, dividiendo la ecuación principal por $\frac{1}{P^2}$: 

$$-\frac{P'}{P^2} + \sigma\frac{1}{P} = \sigma$$ $$\implies Z' + \sigma Z = \sigma$$ 
Es una [[Ecuación diferencial lineal de primer orden|EDO lineal]], entonces se hace el procedimiento: 

$$(ze^{\sigma t})' = \sigma e^{\sigma t}$$ $$ze^{\sigma t} = e^{\sigma t} + C$$
$$z = 1 + ce^{-\sigma t}$$ 
Entonces se vuelve hacia atrás con el cambio de variable:

$$P=\frac{1}{1 + ce^{-\sigma t}}$$ 