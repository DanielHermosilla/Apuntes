
Si definimos: 

$$\int^{}_{-R}f:=sup\lbrace L(f,p)\;|\;P\;\text{partición de R}\rbrace$$
$$\int^{-}_{R}f:=inf\lbrace U(f,p)\;|\;P\;\text{partición de R}\rbrace$$

Por lo tanto, decimos que $f$ es integrable sobre $R$ si: 

$$\int^{}_{-R}f=\int^{-}_{R}f$$ 
Análogo al curso de *Cálculo Diferencial e Integral* donde se define la [[Suma de Riemann|suma de Riemann]]. 

## Propiedades 

1) $\int^{}_{R}c=c\int^{}_{R}$ 
2) $\int^{}_{R}f\pm g=\int^{}_{R}f\pm\int^{}_{R}g$ 
3) $|\int^{}_{R}f|\leq\int^{}_{R}\;\text{(Desigualdad triangular)}$ 

En partícular: 

$$\int^{}_{R}c = cVol(R)$$ 
Es decir, si se tiene: 

$$L(f=1,P)=\sum^{n}_{j=1}1\;Vol(R_j) = Vol(R)$$ $$\implies\int^{}_{A}1 = Vol(A)$$ 
### Ejemplo

Consideremos $f:[0,1]^{2}\rightarrow\mathbb{R}$ definida por: 
$$f(x,y) = 0\;x\in[0,\frac{1}{2})$$ $$f(x,y) = 1\;x\in[\frac{1}{2},1]$$ 
Pruebe que $f$ es integrable y  se tiene que: 

$$\int^{}_{[0,1]^2}f = \frac{1}{2}$$ Es decir, se tiene la siguiente función: 

![[IMG_F5FF8C21E4FA-1.jpeg|center|450]]

Sea $P$ una [[Particiones en varias variables|partición]] de $[0,1]^2$ que genera [[Integral sobre rectángulos|subrectángulos]] abiertos disjuntos $\lbrace R_1,\dots,R_n\rbrace$. Supongamos que incluyen parte de la linea $x=\frac{1}{2}$ tienen todos ambos lados de tamaño $\epsilon$.

![[IMG_35D7D2A41B21-1.jpeg|center|450]]


Si no es el caso, realizamos un refinamiento que lo permita. Entonces para un rectángulo $R$ cualquiera se tiene: 

$$m_j=inf(f)_{x_j\in R_j} = 0\;\text{si existe}\;(x_j)\in R_j\;\text{tal que}\;x<\frac{1}{2}$$

$$m_j=inf(f)_{x_j\in R_j} = 0\;\text{si todos los}\;(x_j)\in R_j\;\text{son tales que}\;x\geq\frac{1}{2}$$

De la misma forma para la [[Suma superior e inferior|suma superior]]:

$$M_j=sup(f)_{x_j\in R_j} = 1\;\text{si existe}\;(x_j)\in R_j\;\text{tal que}\;x\geq\frac{1}{2}$$
$$M_j=sup(f)_{x_j\in R_j} = 1\;\text{si todos los}\;(x_j)\in R_j\;\text{son tales que}\;x<\frac{1}{2}$$

Por lo tanto, tenemos que si calculamos la [[Suma superior e inferior|suma inferior]] $L(f,p)$, los aportes son los [[Integral sobre rectángulos|rectángulos]] $R_{j}^{*}$  que están incluidos en la región $x\geq\frac{1}{2}$, es decir: 

$$L(f,P) =\sum^{}_{R_{j}^{*}}1\; Vol(R_{j}^{*})=\sum^{}_{R_{j}^{*}} Vol(R_{j}^{*})\leq Vol([\frac{1}{2},1]\times [0,1]) =\frac{1}{2}$$  
Ahora para los [[Integral sobre rectángulos|rectángulos]] $R_{j}^{**}$ que contienen parte de la linea $x=\frac{1}{2}$ se tiene que: 

$$L(f,P)=\sum^{}_{R_{j}^{**}}1\; Vol(R_{j}^{**})\geq Vol([\frac{1}{2},1]\times [0,1]) -\sum^{}_{R_{j}^{**}}Vol(R_{j}^{**}) = \frac{1}{2} -\epsilon$$

Análogamente, tenemos que  la [[Suma superior e inferior|suma superior]]: 

$$U(f,P)=\sum^{}_{R_{j}^{*}}1\;Vol(R_{j}^{*}) +\sum^{}_{R_{j}^{**}}1\;Vol(R_{j}^{**}) =\frac{1}{2} +\epsilon$$ 
En resumen, obtenemos que al combinar ambas variables: 

$$U(f,P)-\epsilon\leq\frac{1}{2}\leq L(f,P)+\epsilon$$ 
El problema es que se ocupó una [[Particiones en varias variables|partición]] específica en vez de una arbitraria, por lo tanto, ocupamos un refinamiento arbitrario a partir de esta [[Particiones en varias variables|partición]]. Entonces, la refinación quedaría como: 

$$U(f,P')-\epsilon\leq\frac{1}{2}\leq L(f,P'')+\epsilon$$ 
Como las [[Particiones en varias variables|particiones]] son independientes del valor $\epsilon$, al tomar ínfimo y supremo sobre el conjunto de las [[Particiones en varias variables|particiones]] $[0,1]^2$; definimos:

$$\int^{-}_{[0,1]^2}f-\epsilon\leq\frac{1}{2}\leq\int^{}_{-[0,1]^2}f+\epsilon$$ 
Como $\epsilon$ es arbitrario, se tiene que: 

$$\int^{-}_{[0,1]^2}\leq\frac{1}{2}\leq\int^{}_{-[0,1]^2}f$$ 
Pero recuerde que siempre se tiene: 

$$\int^{}_{-[0,1]^2}f\leq\int^{-}_{[0,1]^2}f$$ 
Así, 

$$\int^{}_{-[0,1]^2}f=\int^{-}_{[0,1]^2}f=\int^{}_{[0,1]^2}f=\frac{1}{2}$$

### Ejemplo 

Sobre $R=[0,1]^2\in\mathbb{R}^2$, sea: 
$$f(x,y)=1\;x\in\mathbb{Q}$$ $$f(x,y)=0\;x\notin\mathbb{Q}$$ 
Sea $P$ una [[Particiones en varias variables|partición]] arbitraria del [[Integral sobre rectángulos|rectángulo]] de $[0,1]^2$ que genera subrectángulos abiertos disjuntos $(R_j)_{j=1}^{*}$. Luego; 

$$m_j=0\;\land\;M_j=1$$ 
Es decir, independiente del [[Integral sobre rectángulos|rectángulo]] que tome, se va a tener que el supremo va a ser igual a 1. Análogo con el ínfimo. Por lo tanto: 

$$U(f,P)=1\;\land\;L(f,P)=0$$ 
## Teorema 

Sea $f:\mathbb{R}\subset\mathbb{R}^n\rightarrow\mathbb{R}$ una [[Funciones escalares|función escalar]] [[Conjuntos compactos|acotada]], con $R$ un [[Integral sobre rectángulos|rectángulo]] de $\mathbb{R}^n$. Entonces $f$ es [[Integral en varias variables|integrable]] sobre $R$ si y sólo si el conjunto de discontinuidades de $f$ tiene [[Medida nula|medida nula]]. En particular, toda función [[Continuidad en varias variables|continua]] sobre $R$ es [[Integral en varias variables|integrable]]. Es decir, cada conjunto es integrable si tienen una [[Fronteras|frontera]] de [[Medida nula|medida nula]]. 

En particular si $f$ es [[Continuidad en varias variables|continua]] sobre el rectángulo $R$ entonces $f$ es [[Integral en varias variables|integrable]] sobre ese conjunto. 