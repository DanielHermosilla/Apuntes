
El error estándar de un [[Estadísticos|estimador]] se da por su desviación estándar: 

$$
S . E(\bar{y})=\sqrt{\operatorname{Var}[\bar{y}]}=\sqrt{\frac{\sigma_y^2}{n}}=\frac{\sigma_y}{\sqrt{n}}
$$

Esto depende de un parámetro desconocido $\sigma_y$ donde hay que estimarlo antes de calcular el error estándar. Por ejemplo, la cuasivarianza es un estimador insesgado. 

Un estimador insesgado de $\sigma_y^2$ viene dado por:

$$
s_y^2=\frac{1}{n-1} \sum_{i=1}^n\left(y_i-\bar{y}\right)^2
$$

Luego,
$$
S . E .(\bar{y})=\sqrt{s_y^2 / n}
$$

