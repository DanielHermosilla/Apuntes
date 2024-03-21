
Es un valor calculado como una función de la [[Departamento de Ingeniería Industrial/Estadística/Inferencia Estadística/Muestreo Aleatorio|muestra aleatoria]] y permite caracterizar los datos: 

- **Promedio muestral**: 

$$
\bar{y}=\frac{1}{n} \sum_{i=1}^n y_i
$$

- **Desviación estándar**: 

$$
s_y=\sqrt{\frac{\sum\left(y_i-\bar{y}\right)^2}{n-1}}=\sqrt{\frac{\left(\sum y_i^2\right)-n \bar{y}^2}{n-1}}
$$

- **Covarianza**: 

$$
s_{x y}=\frac{\sum_{i=1}^n\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)}{n-1}=\frac{\left(\sum_{i=1}^n x_i y_i\right)-n \bar{x} \bar{y}}{n-1}
$$

- **Correlación**: 
$$
r_{x y}=\frac{s_{x y}}{s_x \cdot s_y}
$$

Los otros llegarían a ser la mediana, moda, skewness, etc. 

Cada estadístico es una **función de la muestra aleatoria obtenida** y por lo tanto, **también es una variable aleatoria**. De hecho, cada estadístico también tiene una distribución de probabilidad. 