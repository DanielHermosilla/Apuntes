
### Integración por partes 

Sea la siguiente integral $\int_{0}^{1}xe^{2x}dx$ 

Entonces; 

- $u = x\implies du = 1$ 
- $v = \frac{1}{2}e^{2x}\implies dv = e^{2x}$ 

Por lo tanto, sabemos que lo siguiente es válido: 

$$\int u dv = uv -\int vdu$$ 
Entonces, 

$$\int_{0}^{1}xe^{2x}dx = \frac{xe^{2x}}{2}\bigg\vert_{0}^{1} - \int_{0}^{1}\frac{1}{2}e^{2x}$$ 
Desarrollando hasta el final se llega que: 

$$ = \frac{1}{4}e^2 + \frac{1}{4} $$ 

### Cambio de variable 

Se puede ocupar una sustitución de una variable dentro de la integral, reemplazando por el [[Derivada|diferencial]] por el diferencial respectivo del cambio de variable. 

### Integración en varias variables 

Para integrar en varias variables se puede ocupar **el teórema de Fubini** donde nos deja conmutar el orden de las integrales manteniendo los límites.  

Normalmente para evaluar los límites de integración en lugares que no corresponden a rectángulos hay que determinar los límites de la región, por ejemplo: 

$$\int\int_D x dxdy$$ $$D = \lbrace (x,y)\in\mathbb{R}^2\big\vert x^2\leq y \leq 2x\rbrace $$ 
Sería un gráfico parecido al siguiente: 

![[GraficoIntegral.png|center|500]]

Por lo tanto, los límites de integración serían los siguientes: 

$$\int_{0}^{2}x\int_{x^2}^{2x} 1\ dydx$$ 