
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

Así, es posible encontrar un valor para $\mu_y$ donde se obtiene que $\mu_y=\hat{\theta}-Z\cdot\frac{\sigma^2}{n}$. Por lo tanto, para encontrarlo bajo un intervalo de confianza $\alpha$, se consigue el valor crítico de la distribución Normal tal que $P(z\leq z_{1-\frac{\alpha}{2}})$. Así, la fórmula general para el intervalo de confianza llegaría a ser: 

$$C(\hat{\theta})=\hat{\theta}\pm z_{1-\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}$$ 
Ahora, para el caso donde $\sigma$ es desconocido, es posible utilizar la **cuasi-varianza muestral**. Sin embargo, hay que tener en cuenta que no es posible computar 

$$C(\hat{\theta})\neq\hat{\theta}\pm z_{1-\frac{\alpha}{2}}s_y$$

Ya que $s_y$ es una **variable aleatoria**. Para saber la distribución de $\hat{\theta}$ es posible utilizar una aproximación parecida a la anterior, donde se normaliza bajo la siguiente fórmula: 

$$T=\frac{\hat{\theta}-\mu_y}{s_y/\sqrt{n}}\sim t_{n-1}$$

Así, el intervalo queda definido como: 

$$C(\hat{\theta})=\hat{\theta}\pm t_{n-1, 1-\frac{\alpha}{2}}\cdot\frac{s_y}{\sqrt{n}}$$

Ahora, para el caso que no se conoce la distribución de la población hay que ocupar **distribuciones asintóticas**. 

## Estimadores en muestras grandes 

Para los casos donde se tienen muestras muy grandes es posible observar que la calidad del estimador va mejorando proporcionalmente a $n$. 

>[!quote] Convergencia en Probabilidad 
>Sea $X_n$ una secuencia de variables aleatorias indexadas por tamaño muestral $n$. La variable aleatoria **converge en probablidad a una constante $c$** si para todo $\epsilon>0$, se tiene que: 
>
>$$\lim_{n\to\infty}P(\vert X_n-c\vert>\epsilon)=0$$
>
>La intuición dice que mientras $n$ crece, la masa muestral se centra en torno a $c$. 


Un ejemplo de convergencia en probabilidad es tener la variable aleatoria $X_n$ que toma valores $0$ y $n$ con probabilidad $1-1/n$ y $1/n$. Luego: 

$$p\lim X_n=0\cdot p\lim(1-1/n)+n\cdot p\lim(1/n)=0\cdot 1+n\cdot 0=0$$

>[!quote] Consistencia 
>Si $X_n$ tiene media $\mu_n$ y varianza $\sigma^{2}_{n}$ tal que los límites ordinarios de $\mu_n$ y $\sigma^{2}_{n}$ son $c$ y $0$ respectivamente, entonces $X_n$ converge en probabilidad a $c$. Luego, un **estimador consistente** $\hat{\theta}$ si $p\lim\hat{\theta}=\mu$, donde $\mu$ debe ser constante. 

También es posible decir que se tiene un estimador consistente para el caso en que $X_n$ es un estimador insesgado y su varianza converge en $0$. 

>[!example] Ley de los Grandes Números (LLN)
>Sea $\lbrace X_i\rbrace^{n}_{i=1}$ una muestra idéntica e independientemente distribuida, con $E[X_i]=\mu$ y $\text{Var}[X_i]=\sigma^2$. Luego $\bar{\theta}=\frac{1}{n}\sum^{n}_{i=1}X_i$ es un estimador consistente de $\mu$. Por lo tanto, **la ley sólo funciona en distribuciones muestrales**. 

Donde $\lbrace X_i\rbrace^{n}_{i=1}$ corresponde a la variable aleatoria de la muestra. 

Además, se tienen las siguientes proposiciones: 

- Si $X_n$ es una variable aleatoria tal que $p\lim X_n=c$, $g(X_n)$ es continua y diferenciable y $g(X_n)$ no depende de $n$, entonces: 

$$p\lim g(X_n)=g(p\lim X_n)$$

- Si tenemos una variable aleatoria $H_n$ que, a medida que aumenta $n$ (*"grados de libertad"*), converge a otra distribución, entonces se dirá que hay una **convergencia en distribución**: 

$$H_n\to_{d}H^*$$

Un gran ejemplo de esto, es la $t$ student que converge a una Normal Estándar a medida que aumentan sus grados de libertad. 

- Por el otro lado, si $X_n\to_{d}X$ y $g(X_n)$ es una función continua y diferenciable que no depende de $n$, entonces: 

$$g(X_n)\to_{d}g(X)$$

Esto es conocido como **continuos mapping problem**. 

>[!example] Teorema del Límite Central 
>Sea $\lbrace X_i\rbrace^{n}_{i}$ una muestra independiente e indenticamente distribuida con una media y varianza constante. Así, se tiene que: 
>
>$$\sqrt{n}(\bar{X_n}-\mu)\to_{d} N(0,\sigma^2)$$
>
>Equivalente a tener: 
>
>$$\frac{(\bar{X_n}-\mu)}{\sigma/\sqrt{n}}\to_{d}N(0,1)$$
>
>Por lo demás, se tiene que: 
>
>$$\bar{X_n}\to_{a}N(\mu,\frac{\sigma^2}{n})$$

Se dirá que un estimador es **asintóticamente eficiente** si la varianza de la distribución asintótica excede $\text{Var}[\theta]/n$. 

Así, a modo de resumen, la forma de escribir intervalos de confianza es la siguiente: 

$$\text{IC}=\begin{cases}\hat{\theta}\pm z_{\alpha/2}\cdot\frac{\sigma}{\sqrt{n}}&\text{Si se conoce la distribución y varianza}\\  \\
\hat{\theta}\pm t_{n-1, 1-\alpha/2}\cdot\frac{s_y}{\sqrt{n}}&\text{Si se conoce la distiribución}\\  \\
\hat{\theta}\pm z_{1-\alpha/2}\cdot\frac{s_y}{\sqrt{n}}&\text{No se conoce distribución, pero n grande}
\end{cases}$$


## Test de Hipótesis 

Se ocupa para rechazar una posible hipótesis, por ejemplo, la media de una muestra es $\mu_0$. Por ende, se definen dos hipótesis: 

- **Hipótesis Nula** ($H_0$)
- **Hipótesis Alternativa $(H_1)$

Para realizarlo se siguen tres pasos: 

1. Obtención de los datos 
2. Calcular el estadístico de interés 
3. Obtener la conclusión (por ejemplo, si $\bar{X_n}$ es demasiado grande, entonces se rechaza $H_0$ en favor de $H_1$)

El test de significancia sólo permite desacreditar una hipótesis pero no confirmarla. 

1. Error tipo $I$: 

$$P(\text{Rechazar hipótesis nula}\;\vert\;\text{La hipótesis nula es verdadera})$$

2. Error tipo $II$:

$$P(\text{No rechazar hipótesis nula}\;\vert\;\text{Dado que la hipótesis alternativa es verdadera})$$

Así, se define la significancia como $\alpha$, la probabilidad del error tipo $I$, y poder como $1-\beta$-, la probabilidad del error tipo $II$.

Se define el estadístico del test para aceptar o rechazar la hipótesis nula como: 

$$T(X)=\frac{\bar{X_n}-\mu_0}{\sigma/\sqrt{n}}$$

Por lo tanto, la región que permite rechazar la hipótesis nula se define como $T(X)>c$. Esta distribución corresponde a aquella cuando la hipótesis alternativa es verdadera. 

Así, se define **$p$-valor** como: 

$$\text{p-valor}=P(\vert\;t\;\vert>\vert\;t^*\;\vert\;\vert H_0)$$

Entonces, se define como la probabilidad de observar un valor $t$ mayor a $t^*$ cuando la hipótesis $H_0$ es verdadera.

Es decir, **el mínimo nivel de probabilidad de rechazar la hipótesis nula, dada que es verdadera**. 

Así, para hacer un test de hipótesis se hace lo siguiente: 

1. Se define la hipótesis nula $H_0$ y la alternativa $H_1$. 

2. Asumiendo que la nula es verdadera, se calcula el valor del test estadístico. 

$$t=T(X)=\frac{\bar{X_n}-\mu_0}{\sigma/\sqrt{n}}$$






