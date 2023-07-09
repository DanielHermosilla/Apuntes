
Si la [[Fuerzas centrales|fuerza central]] se define como $\vec{F_c}=f(\rho)\hat{\rho}$. Esto, al ser una fuerza, tiene asociado un [[Departamento de Física/Mecánica/Energía/Trabajo|potencial]], recordando que por definición es $\vec{F}\cdot d\vec{r} = -dV$. Entonces 

$$f(\rho)\hat{\rho}\cdot(dp\hat{\rho}+\rho d\theta\hat{\rho})=f(\rho)d\rho$$ 
$$\implies V=-\int f(\rho)d\rho + C$$ 

Notemos que la energía potencial en función de $\rho$ queda de la siguiente forma 

$$V^*(\rho)=V(\rho)+\frac{mh^2}{2\rho^2}$$ 

### Ejemplo

Si tenemos la fuerza gravitatoria, se llega que: 

$$\vec{F_c}=\frac{-GM_tm}{\rho^2}\hat{\rho}$$ 
Entonces, su potencial es: 

$$V=\int\frac{GM_tm}{\rho^2}d\rho
$$ 
Por lo tanto, 

$$V= -\frac{GM_tm}{\rho}$$ 

Esto es equivalente a tener un gráfico de la forma: 

```functionplot
---
title: Potencial de la fuerza de gravitación
xLabel: x
yLabel: t
bounds: [-0.05,10,-1,1]
disableZoom: true
grid: true
---
y =  -1/x

```

Entonces, como sabemos que la energía mecánica total se conserva, tenemos que: 

$$\frac{1}{2}mv^2 - \frac{GM_tm}{\rho}=E_0$$ 

$$\iff\frac{1}{2}mv_{0}^{2}-mgR_t = E_0$$ 
Donde $R_t$ es el radio de la tierra. 