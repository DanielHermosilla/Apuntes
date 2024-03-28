
Dado que no se conoce el parámetro poblacional $\mu_y$ que se quiere estudiar, se puede decir que tán cerca está $\mu_y$ en un determinado rango, y decir que tán cerca está *probabilísticamente* $\bar{y}$ de $\mu_y$. La lógica detrás del intervalo de confianza es utilizar un intervalo tal que existe un cierto nivel de probabilidad que contenga a $\mu_y$. 

Se define de la siguiente forma: 

$$C(\bar{y})=\bar{y}\pm z_{1-\frac{\alpha}{2}}\cdot SE(\bar{y})$$ 
Donde $z$ es el valor que determina el investigador de confianza. 
#### Ejemplo 

Supongamos que $Y \sim N\left(\mu_y, \sigma_y^2\right)$, y que el parámetro $\sigma_y^2$ es conocido. Conocemos fácilmente la media muestral $\bar{y} \sim N\left(\mu_y, \frac{\sigma_y^2}{n}\right)$. Con esto podemos estandarizar $\bar{y}$, obteniendo:
$$
Z=\frac{\bar{y}-\mu_y}{\sqrt{\frac{\sigma_y^2}{n}}}=\frac{\bar{y}-\mu_y}{S E(\bar{y})}
$$

Podemos notar que encontramos un valor para $\mu_y=\bar{y}-Z \cdot S . E .(\bar{y})$. Con esto, podemos construir el intervalo de confianza de la media poblacional $\mu_y$ como:
$$
C(\bar{y})=\bar{y} \pm z_{1-\frac{\alpha}{2}} \cdot S E(\bar{y})
$$

Importante: $z_{1-\frac{\alpha}{2}}$ es el valor crítico (tabla) $z$ para el cual:
$$
P\left(z \leq z_{1-\frac{\alpha}{2}}\right)=1-\frac{\alpha}{2}
$$

