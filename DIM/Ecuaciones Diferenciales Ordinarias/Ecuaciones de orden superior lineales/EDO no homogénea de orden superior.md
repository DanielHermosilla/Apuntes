
Es decir, algo de la forma: 

$$y'' + \bar{a_1}y' + \bar{a_0}y = \bar{Q(x)}$$ 
Por lo tanto, lo que postula LaGrange es encontrar la solución **no-lineal** obtenida de las soluciones [[EDO de orden superior lineal|EDO homogénea]]. Es decir: 

$$y_p = \alpha(x)y_1 + \beta(x)y_2$$ 
Es una [[combinación lineal|combinación no lineal]]. 

## Método de variación de parametros 

Aplicando la EDO de Lagrange: 

$$(\alpha(x) y_1 + \beta(x) y_2)'' + \bar{a_1}(\alpha(x) y_1 + \beta(x) y_2)' + \bar{a_0}(\alpha(x) y_1 + \beta(x) y_2) = \bar{Q(x)}$$ 
Pero, si nos fijamos en el segundo término, se tiene que: 

$$(\alpha(x) y_1 + \beta(x) y_2)' = (\alpha ' y_1 + \beta ' y_2) + (\alpha y_1' + \beta y_2')$$ 
Pero se impone que $\alpha ' = \beta ' = 0$, ya que de lo contrario sería una ecuación nueva para $\alpha ', \beta '$. 

Lo mismo ocurre para $(\alpha y_1 + \beta y_2)$. 

Entonces, el primer término terminaría siendo: 

$$(\alpha(x) y_1 + \beta(x) y_2)'' = (\alpha_1' y_1' + \beta ' y_2') + (\alpha y_1 '' + \beta y_2 '')$$ 
Pero, nuevamente, $(\alpha y_1 '' + \beta y_2 '') = 0$ pues es solución del sistema homogéneo. Y el factor restante lo dará el **determinante de la [[Matriz Wronskiana]]**. Sea $(\alpha_1' y_1' + \beta ' y_2') = \bar{Q}$. 

Entonces, 

$$\begin{bmatrix}

y_1(x) & y_2(x) \\ 
y_1'(x) & y_2'(x)

\end{bmatrix}
\begin{bmatrix}

\alpha' \\ 
\beta'

\end{bmatrix}
=
\begin{bmatrix}

0 \\ 
Q'

\end{bmatrix}$$

Donde $\alpha ' = \frac{-y_2 \bar{Q}}{W}$ y $\beta' = \frac{y_1\bar{Q}}{W}$. Por último, basta integrar para obtener $\alpha$ y $\beta$, es decir: 

$$\alpha = \int\frac{-y_2\bar{Q}}{W}\ \land\ \beta = \int\frac{y_1\bar{Q}}{W}$$ 
Juntando todo esto, la solución general llegaría a ser: 

$$y_p = -y_1\int\frac{-y_2\bar{Q}}{W} dx +  y_2 \int\frac{-y_1\bar{Q}}{W}dx$$ 
### Ejemplo 

Sea la siguiente función 

$$y'' + k^2y = \sin(\omega_0 x)$$ 
Por lo tanto, la solución [[EDO de orden superior lineal|homogénea]] sería: 

$$y_h = \alpha\cos(kx) + \beta\sin(kx)$$ 
Por lo tanto, la [[Matriz Wronskiana]] llegaría a ser: 

$$W = \begin{bmatrix}
\cos(kx) & \sin(kx)\\ 
k\sin(kx) & k\cos(kx)
\end{bmatrix}$$ 
Con el valor del determinante siendo $W=k$. Por lo tanto, la solución no homogénea sería: 

$$y_p = -cos(kx)\int\frac{\sin(\omega_0 x)\sin(kx)}{k}dx + \sin(kx)\int\frac{\sin(\omega_0 x)\cos(kx)}{k}dx$$ 
Ocupando las fórmulas:
- $\sin(\alpha \pm \beta)=\sin(\alpha)\cos(\beta)\pm\cos(\alpha)\sin(\beta)$ 
- $\cos(\alpha\pm\beta)=\cos(\alpha)\cos(\beta)\mp\sin\alpha\sin\beta$ 

Entonces, 

$$\frac{1}{2}\left[ \cos(\alpha-\beta) -\cos(\alpha + \beta)\right] = \sin(\alpha)\sin(\beta)\ \land \ \frac{1}{2}\left[\sin(\alpha-\beta) + \sin(\alpha + \beta)\right] = \sin(\alpha)\cos(\beta)$$ 
Por lo tanto, la función queda como: 

$$y_p = \frac{-\cos(kx)}{2k}\int\left[ \cos(\omega_0 - k)x - \cos(\omega_0 + k)x \right] + \frac{\sin(kx)}{2k}\int\left[ \sin(\omega_0 - k)x + \sin(\omega_0 + k)x \right] - \frac{\cos(kx)}{2k}\left[\frac{1}{\omega_0 - k}\sin((\omega_0-k)x)-\frac{1}{\omega_0 + k}\sin(\omega_0 + k)x\right] + \frac{\sin(kx)}{2k}\left[\frac{-1}{\omega_0-k}\cos((\omega_0-k)x)-\frac{1}{\omega_0 + k}\cos((\omega_0 + k)x)\right]$$ 

Resolviendo todo esto queda: 

$$y_p = \frac{2}{|\omega_{0}^2 - k_{0}^{2}|}$$ 
Algo de la forma 

```functionplot
---
title: Solución de la ecuación
yLabel: y
bounds: [-2,2,0,20]
disableZoom: true
grid: true
---
y =  2/abs(x)

```