
Se dice que una [[Variable aleatoria continua|variable aleatoria]] sigue una distribución normal $X(\mu,\sigma^2)$ si su [[Función de Densidad de Probabilidad (PDF)|PDF]] cumple que: 

$$f_x(x)=\frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$ 
### Ejemplo 

Se tiene que la altura de las personas siguen una distribución normal con media $1,70$mts y [[Desviación estandar|desviación estándar]] $0.15$mts. Determinar la probabilidad que una persona mida entre $1,65$ y $1,80$. 

Es decir, se tiene una distribución normal de la forma $X(1.7,0.15^2)$ y se pide encontrar $\mathbb{P}(1,65\leq X\leq 1.8)$ 

Es equivalente a tener $F_x(1.8)-F_x(1.65)$, pero como se vio anteriormente, es imposible calcular la CDF. Entonces, se podría hacer la transformación para hacerla una [[Distribución Normal Estándar|distribución normal estandar]], es decir: 

$$\mathbb{P}(\frac{1.65-1.7}{0.15}\leq\frac{X-1.7}{0.15}\leq\frac{1.8-1.7}{0.15})$$ 
$$ =\phi(\frac{1.8-1.7}{0.15})-\phi(\frac{1.65-1.7}{0.15})$$ 
Buscando en la tabla, se llega que $0.7454 - 0.6293$ 