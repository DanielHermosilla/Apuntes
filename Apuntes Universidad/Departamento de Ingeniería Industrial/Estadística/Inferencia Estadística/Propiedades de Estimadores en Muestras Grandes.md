
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
>
>Esto es **una forma de probar inconsistencia** (*pero hay más*).


Esto, en su forma lógica, se dice de la siguiente forma: 

$$\hat{\theta}\;\text{insesgado}\;\land\;p\lim(Var(\hat{\theta}))=0\iff p\lim(\hat{\theta})=\theta\iff\hat{\theta}\;\text{estimador consistente}$$

>[!cite] Teorema: Ley de los Grandes Números (LLN)
>Sea $\lbrace X_i\rbrace^{n}_{i=1}$ una muestra i.i.d, con $E[X_i]=\mu<\infty$ y $Var[X_i]=\sigma^2<\infty$. Luego, $X=\frac{1}{n}\sum^{n}_{i=1}X_i$ es un estimador consistente de $\mu$. 

>[!example] Convergencia en distribución 
>Sea $X_n$ una secuencia de variable aleatorias con $X_n\sim F_n(\cdot)$ y $X$ una variable aleatoria con distribución $f(\cdot)$. Si para cada $x$ tenemos que $f(x)$ es continua y $f_n(x)\to_{n\to\infty}f(x)$, entonces decimos que $X_n$ converge en distribución a $X$, y se escribe $X_n\to_d X$. 
>
>- Por ejemplo, la distribución *t-student* converge a una Normal Estándar cuando los grados de libertad crece al infinito. 


## Propiedades para operar con límites 

#### Slutsky: Parte 1 

Si $X_n$ es una variable aleatoria tal que: 

- $p\lim X_n=c$
- $g(X_n)$ es una función continua y diferenciable 
- $g(X_n)$ no depende de $n$

Entonces: 

$$p\lim g(X_n)=g(p\lim X_n)$$

Además, si $X_n$ y $Y_n$ son dos variables aleatorias con ímites de probabilidad $\theta$ y $\mu$ respectivamente, entonces: 

1. $p\lim(X_n\pm Y_n)=\theta\pm\mu$
2. $p\lim(X_n\cdot Y_n)=\theta\cdot\mu$
3. $p\lim\left(\frac{X_n}{Y_n}\right)=\frac{\theta}{\mu}$
4. En general, $p\lim (g(X_n, Y_n))=g(\theta, \mu)$ 

#### Slutzky: Parte 2 


Sea $X_n$ una variable aleatoria tal que: 

- $X_n\to X$
- $g(X_n)$ es una función continua y diferenciable. 
- $g(X_n)$ no depende de $n$

Entonces: 

$$g(X_n)\to_d g(X)$$

Si $X_n\to_dX$ y $p\lim Y_n=\theta$, entonces $g(X_n, Y_n)\to_d g(X_n,\theta)$ y también: 

1. $X_n\cdot Y_n\to X_n\cdot\theta$
2. $X_n+Y_n\to X_n+\theta$
3. $\frac{X_n}{Y_n}\to_d\frac{X_n}{\theta}$

# Teorema del Límite Central 

Corresponde a una expansión de la Ley de los Grandes Números. 

>[!example] Teorema del Límite Central 
>Sea $\lbrace X_i\rbrace^{n}_{i=1}$ una muestra i.i.d, con $E[X_i]=\mu<\infty$ y $Var[X_i]=\sigma^2<\infty$. Luego: 
>
>$$\sqrt{n}(\bar{X_n}-\mu)\to_d N(0,\sigma^2)$$
>
>Equivalente a tener: 
>
>$$\frac{\bar{X_n}-\mu}{\sigma/\sqrt{n}}\to_d N(0,1)$$


De esto se puede decir que $\sqrt{n}(\bar{X_n}-\mu)$ se aproxima a una Normal *independiente de la distribución de la que proviene cada variable aleatoria*. 


### Relación con intervalos asintóticos 

Supongamos que se tiene una variable aleatoria $A$ que converge a otra $B$, pero no se sabe la distribución de $B$. Entonces por el CLT se puede transformar en $\sqrt{n}(B-\mu)$ tal que la distribución límite de $\sqrt{n}(B-\mu)$ tiene una media y varianza conocida. Luego, se puede descomponer la distribución de $B$

