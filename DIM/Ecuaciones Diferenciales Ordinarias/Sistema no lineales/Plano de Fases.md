
Los plano de fases se pueden hacer a partir de las direcciones de los [[vector propio|vectores propios]]. En este caso, analizando los [[Puntos críticos|puntos críticos]], se analiza la [[matriz Jacobiana]] y se miran los valores propios $\lambda_1$ y $\lambda_2$ . Entonces se divide en tres casos: 

1. $\lambda_1$ y $\lambda_2$ son reales y mismo signos, se trata de **nodo**. Va a ser un nodo estable si $\lambda_1 < 0$ y $\lambda_2 < 0$. Por el otro lado es inestable si $\lambda_1 > 0$ y $\lambda_2 > 0$. Las curvas son tangentes al [[vector propio]] asociado al [[valor propio]] menor en módulo. 

2. $\lambda_1$ y $\lambda_2$ son reales y diferentes signos, se trata de **punto silla**  Siempre es inestable, de hecho hay una dirección de inestabilidad del $v_1$ asociado a $\lambda_1 >0$, por el otro lado una dirección de estabilidad asociado a $v_2$ asociado a $\lambda_2 < 0$. 

3. $\lambda_1$ y $\lambda_2$ son complejos conjugados, se trata de **espiral**. Si la parte real es positiva es inestable y si es negativa es inestable. 

![[IMG_47A069221933-1.jpeg|center|500]]


### Formas topológicas 

Topológicamente todo esto se vería de la siguiente forma: 

- **Espirales**: 

![[IMG_58CCD3AC1FA2-1.jpeg|center|400]]

- **Nodos**: 

![[IMG_82657D097700-1.jpeg|center|400]]


- **Puntos sillas**: 

![[IMG_6E65B795690C-1.jpeg|center|400]]


## Análisis de estabilidad 

Notemos que la dirección de las trayectorias depende, en realidad, de las soluciones de la EDO. Por ejemplo, sean las siguientes soluciones de una EDO cualquiera: 

$$\begin{align}
\bar{x}&=c_1e^{\lambda_1t}\\\\
\bar{y}&=c_2e^{\lambda_2t}
\end{align}$$ 
Si se elevan ambas ecuaciones al valor propio contrario, se puede llegar a dividir: 

$$\begin{align}
\bar{x}&=c_1e^{\lambda_1t}\;\;\;\left(\right)^{\lambda_2}\\\\
\bar{y}&=c_2e^{\lambda_2t}\;\;\;\left(\right)^{\lambda_1}\\\\
\bar{x}=c_1e^{\lambda_1\lambda_2t}\;\;\;&\land\;\;\;\bar{y}=c_2e^{\lambda_2\lambda_1 t}
\end{align}$$

Por último, dividiendo, se llega que: 

$$\begin{align}
\bar{y}&= c\bar{x}^{\frac{\lambda_2}{\lambda_1}}\\\\
c&=\left(\frac{c_{2}^{\lambda_1}}{c_{1}^{\lambda_2}}\right)^{\frac{1}{\lambda_1}}
\end{align}$$ 
Por lo tanto, la siguiente relación permite ver los nodos del punto silla, donde nos definimos los puntos $P$ como $P=\bar{x}v_1 + \bar{y}v_2$:

![[IMG_9A7E23A74930-1.jpeg|center]]

Vale decir, se tendría una especie de plano oblicuo determinado por las direcciones de los vectores. Entonces, viendo la fórmula anterior, podemos volver a ponernos en casos: 

$$\bar{y}=c\bar{x}^{\frac{\lambda_2}{\lambda_1}}$$ 
1. Si $\lambda_1$ y $\lambda_2$ son de signos iguales y reales, $\bar{y}$ llega a ser una parábola. La concavidad viene determinada por $\frac{\lambda_2}{\lambda_1}$. Y se llega a la siguiente forma: 

![[IMG_234C005AC5D7-1.jpeg|center]]

Que depende de la constante $c$ la trayectoria. Ahora, para saber a que eje son tangentes las curvas depende exclusivamente si $\vert\lambda_2\vert > \vert\lambda_1\vert$. En el caso que $\vert\lambda_2\vert$ es mayor, entonces se tiene un gráfico como el de la figura de arriba. Del caso contrario, la curva sería tangente a $v_2$: 

![[IMG_B07CEE22CAC8-1.jpeg|center]]

En términos simple, va a ser tangente según el valor propio. El valor propio en valor absoluto que sea menor va a ser la recta tangente.