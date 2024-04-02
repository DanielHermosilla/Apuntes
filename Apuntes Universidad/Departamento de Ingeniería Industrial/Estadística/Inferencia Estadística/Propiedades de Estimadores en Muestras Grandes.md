
La calidad de un [[Estadísticos|estimador]] depende de su distribución muestral. Para algunos estimadores es posible conocer su distribución muestral, sin embargo, en la mayoría de los casos no se conoce.  **Cualquier proceso de estimación meojra conforme aumenta el tamaño muestral**. 

Las propiedades en muestras grandes dan muchas propiedades, que también ayuda a descartar estimadores insesgados que no mejorar conforme aumenta $n$. 

Recordando que la calidad del estimador depende del comportamiento de la distribución muestral. También sabemos que **mientras mayor sea el tamaño muestral** mejor será la estimación. Esto también ayuda para determinar que tan bien funcionan los estimadores insesgados. 

>[!example] Convergencia en Probabilidad 
>
>Sea $X_n$ una secuencia de [[Variable Aleatoria|variable aleatorias]] indexadas por el tamaño muestral $n$. La variable aleatoria **converge en una probabilidad** a una constante $c$ si, para todo $\epsilon>0$, se tiene que: 
>
>$$
\lim _{n \rightarrow \infty} \operatorname{Pr}\left\{\left|X_n-c\right|>\varepsilon\right\}=0$$
 Cuando eso sucede, decimos que $X_n\to_p c$ o $p\lim X_n=c$

La intuición detrás de ello significa que conforme *n* crece al infinito, toda la masa de distribución muestra se concentra a un punto $c$. 

>[!example] Consistencia 
>Si $X_n$ tiene media $\mu_n$ y varianza $\sigma^{2}_{n}$ tal que los límites de aquellos parámetros son $c$ y $0$ respectivamente, entonces $X_n$ converge en probabilidad a $c$ y por tanto, $p\lim X_n=c$. Luego $\hat{\theta_n}$ es un **estimador ocnsistente** del parámetro poblacional. 
>
>Se puede tener inconsistencia si: 
>
>- $\hat{\theta}$ converge a una constante distinta de $\theta$
>- $\hat{\theta}$ converge a una variable aleatoria. 


Así, se establece la diferencia entre ser insesgado y la consistencia, ya que el insesgamiento es para muestras finitas

>[!cite] Teorema 
>Si $X_n$ es un estimador insesgado de $\theta$ y su varianza converge en probabilidad a $0$ cuando $n\to\infty$, entonces $p\lim X_n=\theta$ y por lo tanto, $X_n$ es un estimador consistente de $\theta$. 









