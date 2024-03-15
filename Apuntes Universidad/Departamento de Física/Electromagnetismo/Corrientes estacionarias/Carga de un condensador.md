
Asumamos que se tiene un [[Condensadores|condensador]] donde existe $Q=0$ en $t=0$. Por lo tanto, *¿cual sería la carga en el tiempo?* *¿La corriente en el tiempo?* *¿El potencial?*.  

Ocupando las leys de Kirchoff, sabemos que $\sum V=0$. Entonces, se puede llegar a plantear: 

$$V_0-\frac{Q}{C}-RI=0$$

Como cargamos el condensador, $dQ/dt>0$. Además, esta diferencial es la definición de corriente. Ocuparemos esto para juntar ambas ecuaciones: 

$$V_0-\frac{Q}{C}-R\frac{dQ}{dt}=0$$

Esta es una [[Aplicaciones a EDOs a coeficientes constantes|ecuación diferencial]], entonces resolviendo esto se llega que: 

$$Q(t)=V_0C(1-e^{\frac{-t}{RC}})$$


```functionplot
---
title: Carga del condensador en el tiempo
xLabel: Tiempo
yLabel: Carga eléctrica
bounds: [0,10,0,1.5]
disableZoom: true
grid: false
---
q(x)=1-2.37^(-x*1/1.5)
```


Ahora, resolviendo para la energía entregada por la batería, se tiene que: 

$$E_B=\frac{V_{0}^{2}}{R}\cdot RC=CV_{0}^{2}$$ 
Por último, la energía almacenada en el condensador llega a ser: 

$$E_C=\frac{1}{2}V_{0}^{2}C$$

