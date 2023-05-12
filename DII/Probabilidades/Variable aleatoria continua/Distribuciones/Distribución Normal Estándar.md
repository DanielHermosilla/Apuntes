
Se dice que una variable $Z(0,1)$ es una distribución normal estándar si cumple que su [[Función de Densidad de Probabilidad (PDF)|PDF]] es: 

$$f_z(z) = \frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}$$ 




## Densidad  

Esta definida sobre todos los reales, donde se cumple lo siguiente: 

![[Captura de pantalla 2023-05-12 a la(s) 09.12.40.png|center|500]]


Por lo tanto, 

$$F_z(z)=\phi(z)=\int_{-\infty}^{z}\frac{1}{2\pi}e^{-\frac{z^2}{2}}dz$$ 
$$\phi(z)=1-\phi(-z)$$ 
## Esperanza 

Dado que se tiene simetría, se tiene que: 

$$E[Z]=\int_{-\infty}^{\infty}\frac{z}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}dx$$ 
Como esta función de adentro es **impar**, se tiene que la esperanza es 0. 

Ahora, si se define la [[Variable aleatoria continua|variable aleatoria]] como $X = \sigma Z+\mu$ para algun $\sigma>0$, entonces la esperanza es equivalente a $\mu$. 

## Tabla normal 

Dado que no se puede calcular la [[Función de Densidad de Probabilidad (PDF)|CDF]], se puede ocupar una tabla normal, donde $z$ se forma con su **primer valor decimal** denominado por la fila y el **segundo valor decimal** con la columna. 

![[Captura de pantalla 2023-05-12 a la(s) 09.20.34.png|center|500]]

