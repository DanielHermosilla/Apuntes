
Diferentes agentes pueden tener distintas actitudes al riesgo. 

Se definen los **aversos al riesgo**, que son aquellos que su utilidad marginal decrece según la riqueza.

Los **neutrales al riesgo**, cuya utilidad marginal es constante según la riqueza. 

Por último, los **amanetes del riesgo** son aquellos cuya utilidad marginal es creciente según la riqueza.

Matemáticamente se pueden definir segun desigualdades. Para el caso de la persona **neutral al riesgo** la utilidad marginal sería, para $x>y$: 

$$u(y+1)-u(y)=u(x+1)-u(x)$$

Que es equivalente a tener una función de **utilidad** [[Sistema no lineales|lineal]]: 

$$\lambda\in (0,1),\;\;\;u(\lambda w+(1-\lambda)w')=\lambda u(w)+(1-\lambda)u(w')$$

Esto, gráficamente se vería de la siguiente forma: 


```functionplot
---
title: Agente neutral al riesgo
xLabel: X
yLabel: Y
bounds: [0,10,0,10]
disableZoom: true
grid: true
---
f(x)=x
```

Sin embargo, para una persona amante del riesgo se tendría una función convexa y cóncava para los aversos al riesgo: 


```functionplot
---
title: Agentes aversos y amantes del reisgo
xLabel: X
yLabel: Y
bounds: [0,5,0,10]
disableZoom: true
grid: true
---
g(x)=-x^(2)+3x+9.5
f(x)=x^2
```
