
## Información faltante 

Dentro de un sistema, es posible medir la cantidad de información que se dispone del sistema. Si nos definimos eventos dentro de un conjunto $\Omega$, donde cada evento $x_i$ tiene su probabilidad respectiva de aparició, se plantea el concepto de **incertidumbre promedio** como: 

$$I=K\sum^{\Omega}_{i=1}\mathbb{P}(x_i)\ln(\frac{1}{\mathbb{P}(x_i)})\;\;K\in\mathbb{R}$$

La elección de la constante $K$ es arbitraria, pero la más usual es $K=-1/\ln(2)$, que se denomina **información faltante de Shannon**: 

>[!info] 
>La información faltante de Shannon, medida en *bits*, se define como: 
>$$I_{\text{Shannon}}=-\sum^{\Omega}_{i=1}\mathbb{P}(x_i)\log_2(\mathbb{P}(x_i))$$

Notemos que la información faltante de Shannon nos dice la cantidad de consultas binarias necesarias para encontrar un evento. Ahora, como se tienen probabilidades, estas consultas son optimizadas para no ser únicamente binarias. Sin embargo, esta optimización no es posible cuando cada evento es equiprobable, en tal caso, se maximiza la información faltante: 

$$I_{max}=K\ln\Omega$$

>[!info] 
>La información faltante de Gibbs, se define como: 
>$$I_{\text{Gibbs}}=-k_B\sum^{\Omega}_{i=1}\mathbb{P}(x_i)\ln(\mathbb{P}(x_i))$$
>Donde $k_B$ es la constante de Boltzmann. 

## Entropía 

Se define ante un sistema macroscópico de muchos eventos, donde todos estos son equiprobables y las variables a describir son extensivas.

>[!info] 
>Se define la entropía como 
>
>$$S=k_B\ln\Omega$$

La entropía está contenida en el sistema y además es aditiva. Cada vez que dentro de un proceso ocurre un cambio en la entropía se puede afirmar que ocurre **pérdida de información**. 

Esto se puede interpretar como una medida de la falta de información que afecta a un observador externo cualquiera que conoce el estado de equilibrio macroscópico.


