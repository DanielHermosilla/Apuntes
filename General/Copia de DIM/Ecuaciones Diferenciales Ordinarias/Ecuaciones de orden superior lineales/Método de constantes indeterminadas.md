
Acordándonos de las [[EDO de orden superior lineal]] y [[EDO de coeficiente variables]], a partir de una ecuación de orden superior: 

$$y^{(n)} + \bar{a_{n+1}}y^{(n-1)} + \dots + \bar{a_1}y' + \bar{a_0}y = \bar{Q}(x)$$ 
Donde se busca primero la solución homogénea con el [[polinomio característico]], y se encuentra una [[Base|base]] linealmente [[dependencia|independiente]]:

$$\langle e^{\lambda_1x},xe^{\lambda_1x},\dots,e^{\sigma x}\cos(\omega x),xe^{\sigma x}\cos(\omega x),\dots,e^{\sigma x}\sin(\omega x), xe^{\sigma x}\sin(\omega x),\dots,\rangle = H$$ 
Entonces, si se busca una solución partícular ($\bar{Q}$) para la homogénea, se buscaban anuladores, donde:

$$\bar{Q} = e^{\lambda_0 x}\ \dots\ (D-\lambda_0)e^{\lambda_0 x} = 0$$
$$\bar{Q} = xe^{\lambda_0 x}\dots (D-\lambda_0)^2 xe^{\lambda_0 x} = 0$$ $$\bar{Q} = (A_0 + A_1x + A_2x^2 + A_3x^3 + \dots + A_kx^k)e^{\lambda_0 x},\ (D \lambda_0)^{k+1}\bar{Q}=0$$ 
Por lo tanto, si se tiene una solución de la siguiente forma: 

$$\bar{Q(x)} = q(x)e^{\lambda_0x}\;\ \exists\lambda_0\in\mathbb{C}$$ 
Con $q$ un polinomio de grado $k$. Esto se obtiene al ir anulando las exponenciales.

Entonces, lo que propone *Euler* es aplicar un anulador a la ecuación diferencial, es decir: 

$$(D-\lambda_1)^{m_1}(D-\lambda_2)^{m_2}\dots(D-\lambda_l)^{m_l}y = q(x)e^{\lambda_0x}\;\;\;\;\ \backslash\;(D-\lambda_0)^{k+1},\;\ k=\text{Grado de q}$$ 
Entonces lo que se va a hacer es agregar una solución a la EDO y **se va a convertir en una EDO homogenea**. 

$$(D-\lambda_0)^{k+1}(D-\lambda_1)^{m_1}(D-\lambda_2)^{m_2}\dots(D-\lambda_l)^{m_l}y = 0$$ 
Es decir, se van a agregar las siguientes soluciones: 

$$e^{\lambda_0 x} + xe^{\lambda_0 x} + x^2e^{\lambda_0 x} + \dots x^ke^{\lambda_0 x}$$ 
Por lo tanto, la solución particular llegaría a ser: 

$$y_p \in \langle e^{\lambda_0 x} + xe^{\lambda_0 x} + x^2e^{\lambda_0 x} + \dots x^ke^{\lambda_0 x}\rangle $$
$$y_p = e^{\lambda_0x}(C_0 + C_1x +\dots + C_kx^k)\;\;C_0,\dots,C_k\ \text{a determinar}$$ 
Si $\lambda_0\neq \lambda_i$ se llaman casos resonantes, es decir, **todas las soluciones llegan a ser nuevas**. 

## Caso resonante 

Cuando $\lambda_0 = \lambda_i$, entonces se llega a aumentar la multiplcidad de las soluciones: 

$$(D-\lambda_0)^{k+1}(D-\lambda_1)^{m_1}(D-\lambda_2)^{m_2}\dots(D-\lambda_l)^{m_i + k + 1}y = 0$$

En este caso, se tienen algunas soluciones, pero se agregan algunas, como: 

$$\langle x^{m_i}e^{\lambda_i x}, x^{m+1}e^{\lambda x}, \dots, x^{m_1 + k}e^{\lambda x}\rangle$$

Por ende, $y_p = x^{m_i}e^{\lambda_0 x}(C_0 + C_1x + \dots + C_k x^k)$ 

### Ejemplo 

$$(D-1)^2(D+2)^3y = (1+x^2)e^{-x}$$ 
Aquí se tendría que: 

1. $\lambda_1 = 1,\;\ m_1=2$ 
2. $\lambda_2 = -2,\;\ m_2 = 3$ 

Y por último, $\lambda_0 = -1$, por lo tanto, es **no resonante**. 

$$y_h\in\langle e^x, xe^x, e^{-2x}, xe^{-2x}, x^2e^{-2x}\rangle$$ 
Para anular el lado derecho se habría que anular el lado derecho por $(D+1)^3$. 

Entonces se agregan tres soluciones, donde $y_p = e^{-x}(C_0 + C_1x + C_2x^2)$ con $C_0, C_1, C_2$ son constantes a determinar. 

### Ejemplo 

$$(D-1)^2(D+2)^3y = (1+x^2)e^{-2x}$$ 
Aquí se tendría que: 

1. $\lambda_1 = 1,\;\ m_1=2$ 
2. $\lambda_2 = -2,\;\ m_2 = 3$ 

Pero, $\lambda_0 = -2$, es decir, se tiene un caso **resonante**. Entonces se multiplica por $(D+2)^3$ y se agregan las soluciones: 

$$y_p = x^3e^{-2}(C_0 + C_1x + C_2x^2)$$ 
## Caso complejo 

Es decir, $\lambda_0 = \sigma_0 + i\omega_0$. Por lo tanto, $e^{\lambda_0 x} = e^{\sigma x}(\cos(\omega_0 x) + i\sin(\omega_0x))$. Por lo tanto, el lado derecho podría ser: 

1. $\bar{Q} = q(x)e^{\sigma_0x}\cos(\omega_0 x)$ 
2. $\bar{Q} = q(x)e^{\sigma_0 x}\sin(\omega_0 x)$ 

El anulador de la exponencial compleja sería $(D-(\sigma_0 + i\omega_0))^{k+1}(D-(\sigma_0 - i\omega_0))^{k+1}$. Si se juntan las dos, llega a ser real, y termina siendo: $((D-\sigma_0)^2 + \omega_{0}^{2})^{k+1}\bar{Q}=0$ 

### Caso no resonante: 

$$y_p = e^{\sigma_0 x}\cos(\omega_0 x)(C_0 + C_1x + \dots + C_kx^k) + e^{\sigma_0x}\sin(\omega_0 x)(D_0 + D_1x + \dots + D_kx^k)$$ 
### Caso resonante 

Se tiene que $\sigma_0 + i\omega_0 = \sigma_0 \pm \omega_i$ 
$$y_p = x^{m_i}\left[e^{\sigma_0 x}\cos(\omega_0 x)(C_0 + C_1x + \dots + C_kx^k) + e^{\sigma_0x}\sin(\omega_0 x)(D_0 + D_1x + \dots + D_kx^k)\right]$$
Donde aparece un factor de resonancia 

## Ejemplo 

Oscilador con amortiguamiento $a>0, b>0$. Es decir: 

$$y'' + ay' + by = A\sin(\omega_0 t)$$ 
Entonces, $\lambda_0 = \pm\ i\omega_0$  y $k=0$. Por lo tanto, el anulador llegaría a ser $(D^2 + \omega_{0}^{2})$. 

$$y_p = C\cos(\omega_0 t) + D\sin(\omega_0 t)$$ 
En el caso no resonante,  es decir, $\lambda_0 = \lambda_1\lor\lambda_2$ que a lo más tienen multiplicidad 1. Entonces, aparece: 

$$y_p = t(C\cos(\omega_0t) + D\sin(\omega_0 t))$$ 
Ahora, si buscamos las soluciones homogeneas: 

$$\lambda^2 + a\lambda + b = 0\implies\lambda_{1,2} = -\frac{a}{2}\pm\sqrt{(\frac{a}{2})^2-b}$$ 
Para *hacer más entretenido* el ejemplo, modifiquemos el oscilador: 

$$y'' + ay' + by = A\sin(\omega_0 t)e^{\sigma_0t}$$ 
Entonces, 

$$y_p = e^{-\sigma_0 t}(C\cos(\omega_0 t) + D\sin(\omega_0 t)$$ 
Y por el otro lado, 

$$y_p = e^{\sigma_0t}t(C\cos(\omega_0t) + D\sin(\omega_0 t))$$ 
Y de nuevo, buscando soluciones homogeneas de la misma forma que antes, 

$$\lambda^2 + a\lambda + b = 0 \implies \lambda_{1,2} = -\frac{a}{2}\pm\sqrt{(\frac{a}{2})^2-b}\ \implies \omega_0=\sqrt{b-(\frac{a}{2})^2}\;\;\;\;\;\text{Hay resonancia}$$


### ejemplo 

Se tiene la siguiente ecuación 

$$(D+1)(D-2)y =xe^x,\ \lambda_1 = -1, m_1 = 1,\ \lambda_2 = 2, m_2 = 1\ \lambda_0 = 1, k = 1$$ 
Por lo tanto, la solución homogenea es: 

$$y_h\in\langle e^{-x}, e^{2x}\rangle\ \land\ y_p=e^x(C_0 + C_1x)$$ 
Reemplazando, 

$$(D+1)(D-2)e^x(C_0 + C_1x)$$ $$(D+1)(e^xC_1 - 2e^x(C_0 + C_1x))$$ $$(D+1)(e^x(C_1-2C_0)-2C_1xe^x)$$ $$(D+1)(e^x(C_1 - 2C_0)-2e^xC1x)$$ $$e^x(C_1 - 2C_0) - 2C_1(x+1)e^x + e^x(C_1-2C_0) - 2C_1xe^x$$ 
Y reagrupando: 

$$e^x(-4C_0) + xe^x(-4C_1) = 0·e^x + xe^x$$ 
Por ende, se llega a lo siguiente: 

$$\begin{cases}
-4C_0 = 0\\-4C_1 = 1\end{cases}\implies C_0 = 0, C_1=-\frac{1}{4}$$ 