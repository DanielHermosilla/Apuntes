
Consisten en los siguientes polinomios: 

$$\text{EDO's de orden superior} = \begin{cases}
y'' + a_1y' + \bar{a_0}y = Q & \text{No homogeneo} \\
y'' + a_1y' + \bar{a_0}y = 0 & \text{Homogeneo} \end{cases}$$

Todos se pueden reducir a su [[polinomio característico]], es decir, $P(D) = D^2 + \bar{a_1}D + a_0$, donde $D$ equivale al operador derivada. Por ejemplo: 

$$y''' + y'' + y' + y = x \rightarrow P(D) = D^3 + D^2 + D + 1$$ 
O por ejemplo, el polinomio característico de: 

$$y'' + 2y' + y = 0 \rightarrow P(D) = D^2 + 2D + 1$$ 
En este caso, los operadores diferenciales se pueden factorizar: 

$$P(D) = (D+1)(D+1)$$ 
Por lo tanto, una ecuación de orden dos, se puede factorizar en dos factores, de orden tres en tres y sucesivamente. 

Por lo tanto, sea el siguiente [[polinomio característico]]: 

$$P(D) = D^2 + \bar{a_1}D + \bar{a_0}$$ $$\iff p(\lambda) = \lambda^2 + \bar{a_1}\lambda + \bar{a_0},\ \ \lambda\in\mathbb{C}$$ 
Las raices del polinomio se les llamaran **valores característicos**. 

Si se consiguen estos valores se podrían escribir como: 

$$p(\lambda) = (\lambda - \lambda_1)(\lambda - \lambda_2)$$ 
Si lo llevamos al caso del operador $D$, queda como: 

$$P(D)f = (D-\lambda_1)o(D-\lambda_2)f$$ $$ = (D - \lambda_1)(f' - \lambda_2 f) = D(f' - \lambda_2 f) - \lambda_2(f' - \lambda_2 f)$$ $$ = f'' - (\lambda_1 + \lambda_2)f' + \lambda_1\lambda_2f = (D^2 - (\lambda_1 + \lambda_2)D + \lambda_1\lambda_2)f = P(D)f$$ 
En efecto se podría comprobar que en este caso, la composición si es conmutativa. 

## Edo homogenea

Es decir, el caso de: 
$$y'' + a_1y' + \bar{a_0}y = 0 \ \ \  \text{Homogeneo}$$ 
Si se describe con el operador $D$ se llega que: 

$$(D-\lambda_1)(D-\lambda_2)y = 0$$ 
Si se reemplaza $(D-\lambda_2)y$ por $z$ se llega que: 

$$(D-\lambda_1)z = 0$$$$(D-\lambda_2)y = z$$ 
Por lo tanto, se llega que: 

$$z' -\lambda_1 z = 0$$ $$y' - \lambda_2 y = z(x)$$ 
Esto se resuelve con **factor integrante**. Es decir, 

$$(ze^{-\lambda_1 x})' = 0$$ 
Con $z = C_1 e^{\lambda x}\ \ \ C_1\in\mathbb{C}$ 

Entonces $y' - \lambda_2 y = z = C_1e^{\lambda_1 x}$$ 
$$(ye^{-\lambda_2 x})' = C_1 e^{(\lambda_1 - \lambda_2)x}$$ 
$$ye^{-\lambda_2 x} = C2 + C1\int e^{(\lambda_1 - \lambda_2)x}\ \ \ C_2 \in\mathbb{C}$$ 

$$ y = C_2 e^{\lambda_2 x} + C_1 e^{\lambda_2 x}\int e^{(\lambda_1 - \lambda_2)x}$$ 
Entonces: 

$$y = \begin{cases}
\frac{C_1}{\lambda_1 - \lambda_2}e^{\lambda_1 x} + C_2 e^{\lambda_2 x} & \lambda_1\neq\lambda_2\ \land\ \lambda_1 , \lambda_2\in\mathbb{R} \\\\ 
C_1 xe^{\bar{\lambda}x} + C_2 e^{\bar{\lambda}x} & \lambda_1 = \lambda_2 \ \land\ \lambda_1 , \lambda_2\in\mathbb{R}\\ \\
\bar{C_1}e^{\sigma x}\cos(\omega x) + C_2e^{\sigma x}\sin(\omega x)& \lambda_{1,2} = \sigma\pm i\omega\ \ \  \text{Complejos conjugados de parte real y parte imaginaria}\end{cases}$$   
### Ejemplo 

Sea la siguiente ecuación: 

$$y'' + 2y' + y = 0$$ 
Aplicando el polinomio característico: 

$$\lambda^2 + 2\lambda + 1 = 0$$ $$\implies (\lambda + 1)^2 = 0\ \ \ \lambda_1 = \lambda_2 = -1$$ 
Entonces, la solución sería: 

$$y_h = \alpha e^{-x} + \beta xe^{-x}$$ 
### Ejemplo 

Este ejemplo se asimila mucho a un oscilador armónico: 

$$y'' + k^2y = 0$$ 
Su polinomio característico sería: 

$$\lambda^2 + k^2 = 0$$ $$\implies\lambda=\pm ik$$ 
Donde $\sigma = 0, w = k$. Entonces, la solución sería: 

$$y_h = \alpha\cos(kx) + \beta\sin(kx)$$ 
### Ejemplo 

Sea el siguiente polinomio característico: 

$$(\lambda - (\sigma + i\omega))(\lambda-(\sigma - iw)) = ((\lambda - \sigma)^2+\omega^2)$$ 
Entonces, la EDO que corresponde sería: 

$$\left[ (D-\sigma)^2 + \omega \right]y = \left[D^2 - 2\sigma D + \sigma^2 + \omega^2\right]y$$ 
Se podría prensar que es un resorte amortiguado es decir: 

$$y'' - 2\sigma y' + (\sigma^2 + \omega^2)y = 0$$ 
## Ejemplos gráficos de las soluciones 

Para $e^x$ se dice que se tiene una solución **sobre-amortiguado**. 

```functionplot
---
title: Función críticamente sobreamortiguada
xLabel: x
yLabel: y
bounds: [0,5,0,1]
disableZoom: true
grid: true
---
y =  exp(-x)

```

Para $e^{-x}\cos(x)$ se tiene una solución **subamortiguado**, donde se tiene una oscilación acotada por $\pm e^{-x}$ 

```functionplot
---
title: Función críticamente subamortiguada
xLabel: x
yLabel: y
bounds: [0,5,-1,1]
disableZoom: true
grid: true
---
y =  exp(-x)cos(x)
h = exp(-x)
z = -exp(-x)
```


Por último, para el caso $xe^{-x}$ se tiene una solución **críticamente amortiguada**. 

```functionplot
---
title: Función críticamente amortiguada
xLabel: x
yLabel: y
bounds: [0,5,0,1]
disableZoom: true
grid: true
---
y = x * exp(-x)
```