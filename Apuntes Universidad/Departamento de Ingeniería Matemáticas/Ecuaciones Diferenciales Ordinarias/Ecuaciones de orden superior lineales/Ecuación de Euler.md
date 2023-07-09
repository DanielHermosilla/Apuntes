
Sea la siguiente solución a coeficientes variables: 

$$x_ny^{(n)} + x^{n+1}y^{(n-1)} + \dots + xy' + y = 0$$ 
Se hace el cambio de variable $z(t) = y(e^t),\;\;\; x=e^t\implies t = ln(x)$ 

Entonces: 

$$z' = y'e^t=xy',\;\; z'' = y''e^{2t} + y'e^t = x^2y'' + xy'$$ 
Donde se llega que $x^2y' = z'$, $x^"y''=z''-z'$, y así sucesivamente. Si esto se reemplaza en la ecuación diferencial, queda una EDO de orden n en $z$ a coeficientes constantes. 

### Ejemplo 

$$x^2y'' + xy' + y = x$$ 
Entonces, el cambio de variable sería: 

$$z(t) = y(e^t)$$ $$z' = xy'\;\; , \;\; z'' = x^2y'' + z'$$ 
Y, al reemplazar arriba queda: 

$$z'' - z' + z' + z = e^t$$ $$\iff z'' + z = e^t$$ 
Aquí queda una ecuación de coeficientes constantes, donde: 

$$\lambda^2 + 1 = 0 \implies\lambda\pm i$$ 
Entonces, $z_h = A\cos(t) + B\sin(t)$. Por el otro lado, para sacar la partícular, se ocupa el [[Método de constantes indeterminadas|método de constantes indeterminadas]], donde $z_p = ce^t$ en el caso no resonante. Entonces, 

$$z_p'' + z_p = 2ce^t = e^t$$ 
$$\implies z_p = \frac{1}{2}e^t$$ 
Por lo tanto, la solución sería $$z = A\cos(t) + B\sin(t) + \frac{1}{2}e^t$$ 
Y, volviendo a la variable original, se llega que: 

$$y = A\cos(\ln(x)) + B\sin(\ln(x)) + \frac{1}{2}x$$ 