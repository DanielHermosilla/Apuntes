
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

