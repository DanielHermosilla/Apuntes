
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
\end{align}