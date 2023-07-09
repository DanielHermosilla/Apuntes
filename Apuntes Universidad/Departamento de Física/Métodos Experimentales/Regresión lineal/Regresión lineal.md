
A partir de la obtención de datos se puede trazar una **línea de tendencia**. Por lo tanto, se busca la **ecuación de la recta**. 

![[Captura de Pantalla 2022-12-14 a la(s) 14.52.29.png|center]]

Cabe mencionar el significado de $R^2$, que nos dirá que tan bien es la aproximación de nuestra recta. También nos dice la relación lineal entre las variables. Los valores van del 0 al 1. 

### Fórmulas necesarias 

#### Pendiente: 

$$a = \frac{\frac{\sum^{N}_{i=1}x_i y_i}{\sum^{N}_{i=1}} - \frac{\sum^{N}_{i=1} y_i}{N}}{\frac{\sum^{N}_{i=1} x_{i}^2}{\sum^{N}_{i=1} x_i} - \frac{\sum^{N}_{i=1} x_i}{N}} $$

#### Coeficiente de posición

$$ b = \frac{\sum^{N}_{i=1} y_i}{N} - a \frac{\sum^{N}_{i=1}x_i}{N}$$ 
#### Minimización del error (error cuadrático)

Se obtiene al comparar la relación entre la variable $a$ y $b$, donde se minimiza el error posible: 

![[Captura de Pantalla 2022-12-14 a la(s) 15.07.33.png|center|450]]

$$ \chi^2 = \sum^{N}_{i=1} (a x_i + b- y_i)^2$$
#### Promedio de la recta 

$$\langle y\rangle = \frac{1}{N}\sum^{N}_{i=1} y_i $$
####  $R^2$ 

$$ R^2 = 1 - \frac{\chi^2}{\sum^{N}_{i=1}(y_i - \langle y \rangle )^2} $$ 

