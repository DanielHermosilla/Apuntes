
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

### Estadísticos

Se definirán como estadísticos a aquellos valores que son calculados a partir de la muestra aleatoria y permite caracterizar los datos. Cada estadístico tiene su *"contraparte"* poblacional que corresponde a los **estimadores**. 

Notar que los estadísticos son **funciones sobre el muestreo aleatorio**, haciendo que estos también sean variables aleatorias. De hecho, **los estadísticos tienen una distribución muestral** (para el caso que se toman muchas muestras aleatorias). 