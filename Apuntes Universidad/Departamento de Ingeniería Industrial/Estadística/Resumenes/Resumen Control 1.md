
>[!example] Inferencia estadística 
>Consiste en el aprendizaje de **una población dada en base a una muestra particular**. Lo más importante es saber; *¿Cómo se hace la inferencia? ¿Qué tan precisa es la aproximación?*

Por lo general, se trata de buscar **un parámetro ($\mu$)** a partir de una **muestra** extraída de la población. 

>[!example] Muestreo aleatorio 
>Supongamos que se tiene una población con una pdf $f(y,\theta)$, con $\theta$ el parámetro poblacional de interés. 
>
>Se definirá como **muestreo aleatorio** a $Y_1, Y_2, \dots, Y_n$ variables aleatorias **independientes** (asumiendo, justamente, que las muestras son obtenidas de forma aleatoria) y que vienen de la misma pdf.
>
>Estas muestras, definidas como $\lbrace y_1, y_2, \dots, y_n\rbrace=Y_i$ son **independientes e idénticamente distribuidas**. 
>

## Estadísticos

Se definirán como estadísticos a aquellos valores que son calculados a partir de la muestra aleatoria y permite caracterizar los datos. Cada estadístico tiene su *"contraparte"* poblacional que corresponde a los **estimadores**. 

Notar que los estadísticos son **funciones sobre el muestreo aleatorio**, haciendo que estos también sean variables aleatorias. De hecho, **los estadísticos tienen una distribución muestral** (para el caso que se toman muchas muestras aleatorias). Aun así, es muy poco común tener la oportunidad de acceder a una **distribución muestral** (conjunto de observaciones). 

### Propiedades de los estimadores 

Se dice que un estimador $\hat{\theta}$ de $\theta$ es una **regla** que se le asigna a cada posible resultado de una muestra un valor aproximado de $\theta$.  Se pueden expresar de las siguientes maneras: 

$$\begin{align}
\hat{\theta}=h(Y_1,\dots,Y_n)&\;\;\;\text{Estimador punto (sobre distribuciones muestrales)}\\  \\
\hat{\theta}=h(y_1,\dots, y_n)&\;\;\;\text{Estimador puntual (sobre una única muestra)}
\end{align}$$

>[!example] Insesgamiento 
>Un estimador $\hat{\theta}$ es insesgado si su esperanza es igual al parámetro que se busca $E[\hat{\theta}]=\theta\iff E[\hat{\theta}-\theta]=0$.
>

Esta claro que, para ver la esperanza del estimador, hay que ocupar **distribuciones muestrales**.

- **Promedio muestral**: Se busca la esperanza del estimador, donde se asume que $y_i$ corresponde a una muestra: 

$$\begin{align}
E[\bar{y}]&=E\left[\frac{1}{n}\sum^{n}_{i=1}y_i\right]\\  \\
&=\frac{1}{n}\sum^{n}_{i=1}E[y_i]
\end{align}$$

Notemos que la esperanza de una muestra es, justamente, el promedio poblacional. Así: 

$$\begin{align}
&=\frac{1}{n}\cdot n\cdot \mu_y\\  \\
&=\mu_y
\end{align}$$

Por lo tanto, se concluye que el estimador para el promedio muestral es **insesgado**. 