
Cuando se consideran las interacciones intramoleculares y ya no se aproximan las moléculas como [[Partícula|partículas]], se define el **gas de Van der Waals**: 

$$\left(P+\frac{a}{v^2}\right)\left(v-b\right)=RT$$

Para interpretarlo; el $(v-b)$ en el plano $PV$, la constante $b$ es un desplazamiento horizontal: 


```functionplot
---
title: Gas de Van Der Waals
xLabel: V
yLabel: P
bounds: [0,10,0,10]
disableZoom: true
grid: true
---
f(x)=1/(x-2)
g(x)=1/x
```

En el caso del gráfico, la función roja es un gas ideal y la azul un gas de Van Der Walas. 

Por el otro lado, la constante $a$ hace dar cuenta del potencial atractivo de las moléculas, muy similar al [[Diferencia de potencial|potencial eléctrico]]. 

Por ende, se define el **coeficiente de Joule** como: 

$$\mu_s=\left(\frac{\partial T}{\partial V}\right)_E$$

Y también la **propiedad cíclica**: 

$$\left(\frac{\partial T}{\partial V}\right)_E\cdot\left(\frac{\partial V}{\partial E}\right)_T\cdot\left(\frac{\partial E}{\partial T}\right)_V=1$$

Y por último, las ecuaciones $TdS$: 

$$\begin{align}
TdS&=C_vdT+T\left(\frac{\partial P}{\partial T}\right)_VdV\tag{Entropía en funcion de T y V}\\  \\
TdS&=C_pdT-T\left(\frac{\partial V}{\partial T}\right)_PdP\tag{Entropía en función de T y P}
\end{align}$$

#### Ejemplo: Coeficiente de Joule 

Encuentre una expresión para el coeficiente de Joule en función de las variables de estado (T,P,V) para un gas de van der Waals y un gas ideal, además calcule las variaciones de temperatura y entropía que sufrirían estos gases en una expansión desde un volumen $V_1$ hasta un volumen $V_2 = 2V_1$ 


Por lo tanto, sabemos que: 

$$\begin{align}
dE&=TdS-PdV\\  \\
&=c_VdT+T\left(\frac{\partial P}{\partial T}\right)_VdV-PdV\\  \\
&=c_VdT+\left[T\left(\frac{\partial P}{\partial T}\right)-P\right]dV
\end{align}$$

Si asumimos volumen constante, entonces $dE=c_VdT$. Por el otro lado, se podría decir que: 

$$\left(\frac{\partial E}{\partial T}\right)_V=c_v$$

Por el otro lado, si la temperatura es constante: 

$$\begin{align}
dE&=\left[T(\frac{\partial P}{\partial T})-P\right]dV\\  \\
\left(\frac{\partial E}{\partial V}\right)_T&=T\left(\frac{\partial P}{\partial T}\right)-P
\end{align}$$

Ocupando un teorema que sólo es válido cuando se pueden escribir todas las variables en funciones de las otras... 

$$\frac{1}{\left(\frac{\partial V}{\partial E}\right)_T}=T\left(\frac{\partial P}{\partial T}\right)_V-P$$