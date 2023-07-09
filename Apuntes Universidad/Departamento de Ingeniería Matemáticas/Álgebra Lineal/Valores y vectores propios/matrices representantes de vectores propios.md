Sea $L: K^n \rightarrow K^n$ una [[transformaciones lineales|transformación lineal]] y $A$ la [[matriz representante]] de $L$ con respecto a la [[Base|base]] canónica $B$. Además, supongamos que existe la siguiente base de [[vector propio|vectores propios]]: $B' = \lbrace v_1 \dots , v_n \rbrace$. Entonces, *¿cuál es la matriz representante de L con respecto a B'?*

Por la definicione de [[valores y vectores propios]] podemos definir a la matriz representante de la siguiente forma: 

$$ M_{B'B'}(L) = \begin{bmatrix} \alpha_1 & 0 & \dots & 0 \\ 0 & \alpha_2 & \dots & 0 \\ \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & 0 & \alpha_n \end{bmatrix} $$ 
Además, se tiene el siguiente diagrama: 

![[Captura de Pantalla 2022-11-28 a la(s) 20.17.08.png|center]]

Entonces, $A = PDP^{-1}$.

Es decir, una [[transformaciones lineales|transformación lineal]] se puede expresar a partir de sus bases canónicas y la [[matriz]] con los valores propios. Esto nos otorga mucha información, pues nos podemos percatar que los [[valor propio|valores propios]] se comportan similar a una homotecia. 


#concepto 