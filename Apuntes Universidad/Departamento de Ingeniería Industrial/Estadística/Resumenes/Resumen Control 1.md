
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

- **Varianza muestral**: La varianza muestral **es sesgada**. Se tiene que se define de la siguiente forma: 

$$\begin{align}
S_{n}^{2}=\frac{1}{n}\sum^{n}_{i=1}\left(X_i-\bar{X}\right)^2
\end{align}$$

Donde $\bar{X}$ corresponde al promedio muestral. Notemos lo siguiente: 

$$\begin{align}
E[S_{n}^{2}]&=E\left[\frac{1}{n}\sum^{n}_{i=1}\left(X_i-\mu-\bar{X}+\mu\right)^2\right]\\  \\
&=E\left[\frac{1}{n}\sum^{n}_{i=1}\left((X_i-\mu)-(\bar{X}-\mu)\right)^2\right]\\  \\
&=E\left[\frac{1}{n}\sum^{n}_{i=1}\left((X_i-\mu)^2-2(X_i-\mu)(\bar{X}-\mu)+(\bar{X}-\mu)^2\right)\right]\\  \\
&=E\left[\frac{1}{n}\sum^{n}_{i=1}(X_i-\mu)^2\right]-2E\left[\frac{1}{n}\sum^{n}_{i=1}(X_i-\mu)(\bar{X}-\mu)\right] +E\left[\frac{1}{n}\sum^{n}_{i=1}(\bar{X}-\mu)^2\right]\\  \\
&=\frac{1}{n}\sum^{n}_{i=1}\text{Var}(X_i)-\frac{2}{n}E\left[(\bar{X}n-\mu n)(\bar{X}-\mu)\right]+(\bar{X}-\mu)^2\\  \\
&=\sigma^2-2E[(\bar{X}-\mu)^2]+(\bar{X}-\mu)^2\\  \\
&=\sigma^2-2E[(\bar{X}-\mu)^2]+E[(\bar{X}-\mu)^2]\\  \\
&=\sigma^2-\text{Var}(\bar{X})\\  \\
&=\sigma^2-\sigma^2/n\neq\sigma^2
\end{align}$$

El sesgo llegaría a ser: 

$$E[S^{2}_n -\sigma^2]=\frac{-\sigma^2}{n}$$

A diferencia, se ocupa la **cuasi-varianza** para corregir el sesgo: 

$$s_{y}^{2}=\frac{1}{n-1}\sum^{n}_{i=1}(y_i-\bar{y})^2$$

Sin embargo, **no siempre ser insesgado implica ser un buen estimador**. También es importante conocer la varianza muestral (error). Mientras menor sea ésta, mejor. 

>[!example] Eficiencia 
>Se dice que un estimador $\hat{\theta}$ de $\theta$ es eficiente si, **dentro de todos los estimadores insesgados es el de menor varianza.**
>

>[!example] Error Cuadrático Medio 
>Poniendo en perspectiva el sesgo y la eficiencia, es posible medir la precisión de un estimador mediante la siguiente fórmula: 
>
>$$\text{MSE}[\hat{\theta}]=E[(\hat{\theta}-\theta)^2]=\text{Var}[\hat{\theta}]+(\text{Sesgo}[\hat{\theta}])^2$$

>[!example] Error Estándar 
>El error estándar de un estimador es la raiz cuadrada de su desviación estándar: 
>
>$$\text{S.E}(\hat{\theta})=\sqrt{\text{Var}[\hat{\theta}]}=\sqrt{\frac{\sigma^{2}_{\theta}}{n}}=\frac{\sigma_\theta}{\sqrt{n}}$$
>
>Se tiene la división por $n$ donde este es el tamaño de la muestra que representa $Y$. Sin embargo, notemos que el error está en función de un parámetro desconocido ($\sigma^{2}_{y}$), por ende, es posible es posible ocupar el estimador de la **cuasi-varianza**: 
>
>$$\text{S.E}(\hat{\theta})=\sqrt{\frac{s^{2}_{\theta}}{n}}=\frac{s^{}_{\theta}}{\sqrt{n}}$$

Puesto que el error estándar está íntimamente relacionado con la varianza del estimador, es posible decir que el error estándar nos dirá la **eficiencia del estimador**. Sin embargo, **no es posible deducir que tán cercano está $\hat{\theta}$ del parámetro a evaluar**. 

Para poder decir que tan cerca se está del parámetro, es posible definir **intervalos de confianza**, que nos dirá la **probabilidad que el parámetro está contenido en un determinado rango en torno al estadístico**. 


## Intervalos de confianza 

A forma de introducción, es posible definirnos una variable aleatoria de una población que distribuye Normal $Y\sim N(\mu_y, \sigma^{2}_y)$, **con el parámetro $\sigma^{2}_{y}$ conocido (luego se relajará la condición)**. Luego es posible estandarizar su estadístico, pues se sabe que $\hat{\theta}\sim N(\mu_y,\frac{\sigma^{2}_{y}}{n})$. Así: 

$$Z=\frac{\hat{\theta}-\mu_y}{\sqrt{\sigma^{2}_{n}/n}}=\frac{\hat{\theta}-\mu_y}{\text{S.E}(\hat{\theta})}$$

 