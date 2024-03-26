
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

Dado que no es posible obtener muchos muestreos aleatorios para obtener estadísticos se pueden ocupar estimadores. 

>[!example]  Estimadores 
>
>Un estimador $\hat{\theta}$ de $\theta$ es una **regla** que asigna a cada posible resultado de una muestra un valor aproximado de $\theta$.  Un estimador también cae bajo la definición de [[Variable Aleatoria|variable aleatoria]].
>
>Un *estimador punto* de $\theta$ puede expresarse como $\hat{\theta}=h(Y_1,Y_2,\dots Y_n)$ y una *estimación puntual* de $\theta$ como $\hat{\theta}=h(y_1,\dots,y_n)$. En este caso, $h$ sería la regla o función y siempre es la misma. 
>
>Por ejemplo, el promedio muestral $(\bar{y}=\frac{1}{n} \sum_{i=1}^n y_i)$ es un **estimador** del promedio poblacional $(\mu)$, independiente de la muestra tomada. 


>[!example] Insesgamiento 
>
>Un estimador $\hat{\theta}$ es insesgado si el promedio o valor esperado de su distribución muestral es igual a $\theta$. Es decir: 
>
>$$E[\hat{\theta}]=\theta$$
>
>Formalmente, si $\hat{\theta}$ es insesgado, entonces $\text{Sesgo}[\hat{\theta}\;\vert\;\theta]=E[\hat{\theta}-\theta]=0$. 


El insesgamiento no siempre es la mejor alternativa, ya que se podría tener le caso que se tome como estimador $\hat\theta=y_1$ con sólo una única observación. Se tendría un estimador totalmente insesgado pero se estarían dejando $n-1$ muestras. 

De tal forma, se introduce la varianza del estimador. Mientras menor sea la varianza del estimador, mejor: 

$$
\operatorname{Var}[\bar{y}]=E\left[(\bar{y}-E[\bar{y}])^2\right]=E\left[\left(\frac{1}{n} \sum_{i=1}^n y_i-E[\bar{y}]\right)^2\right]=\frac{\sigma^2}{n}
$$

Otra forma de probar los estimadores es con el error cuadrático medio de los estimadores: 

$$
\operatorname{MSE}[\hat{\theta}]=E\left[(\hat{\theta}-\theta)^2\right]=\operatorname{Var}[\hat{\theta}]+(\operatorname{Sesgo}[\hat{\theta}])^2
$$

Lo que dice básicamente es, **usa el que tenga menor [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Varianza|varianza]]**. 