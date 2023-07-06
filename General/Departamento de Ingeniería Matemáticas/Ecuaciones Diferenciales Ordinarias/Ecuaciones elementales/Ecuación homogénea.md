
Son las del siguiente orden: 

$$y' = h(\frac{y}{x})$$ 
Se ocupa el [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Cambio de variable|cambio de variable]] equivalente a $z = \frac{y}{x}\ \implies\ \text{EDO en}\; Z$. Entonces, se llega a la igualdad $xz(x) = y\implies xz(x)' + z(x) = y' = h(z(x))$ . Entonces, se llega a lo siguiente: 

$$xz' + z = h(z)$$
$$z' = \frac{1}{x}(h(z)-z)$$ 
Esa es una EDO de [[Método de separación de variables|separación de variables]]. Al terminar con la EDO se deshace el [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Cambio de variable|cambio de variable]]: 

$$y = xz$$ 
### ejemplo

Se tiene la siguiente EDO: 

$$y' = (\frac{y}{x})^2$$ 
Se hace un [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Cambio de variable|cambio de variable]] con $z = \frac{y}{x}$ y se llega a: 

$$xz' + z = z^2$$
$$\iff z' = \frac{1}{x}(z^2-z)$$ 
Es una [[Método de separación de variables|separación de variable]] donde hay que considerar las soluciones constantes $z=0\ \land\ z=1$ y se llega la siguiente integral:

$$\int\frac{dz}{z(z-1)} = \int\frac{1}{x} + C$$ 
Se hace sumas parciales, donde: 

$$-\ln|z| + \ln|z-1| = \ln k|x|\ \ \ \ k>0$$ $$\implies z - 1 = \pm kxz$$ $$\implies z = \frac{x}{1 \mp kx}$$ 