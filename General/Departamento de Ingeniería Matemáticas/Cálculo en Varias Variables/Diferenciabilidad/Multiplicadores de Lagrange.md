## Teorema (Lagrange)

Sea $f,g$  una [[Funciones escalares|funciones escalares]] y de clase $C^1\in\mathbb{R}^n$. Definimos el conjunto de restricciones $S =\lbrace x\in\mathbb{R}^n\;|\;g(x)=0\rbrace$. Supongamos que $\bar{x}$ es [[Máximos y mínimos|mínimo o máximo local]] para $f$ sobre el conjunto $S$ y que $\nabla g(\bar{x})\neq\vec{0}$. Entonces, existe $\lambda\in\mathbb{R}$ tal que: 


$$\nabla f(\bar{x}) = \lambda\nabla g(\bar{x})$$ 
Al [[escalares|escalar]] $'\lambda'$ se le llama multiplicador de Lagrange. 

## Observación 

Este resultado se puede extender para incluir varias restricciones a la vez, es decir, $g:\mathbb{R}^n\rightarrow\mathbb{R}^p$ con $p<n$, luego: 

$$\nabla f(\bar{x})=\lambda_1\nabla g_1(\bar{x}) + \dots + \lambda_p\nabla g_p(\bar{x})$$ 
Donde $g(x) = (g_1(x),\dots,g_p(x))$. 

$\lambda_j$ son [[Multiplicadores de Lagrange|multiplicadores de Lagrange]] y $g_j$ son las funciones componentes de $g$. Lo anterior vale siempre que los [[vectores]] $\nabla g_j(\bar{x})$ sean [[dependencia|linealmente independientes]]. 

### Ejemplo 

Optimizar $f(x,y) = x$ sobre el conjunto $S=\lbrace (x,y)\in\mathbb{R}^2\;|\; x^2 + y^2 = 3\rbrace$. Es decir, encontrar el [[Máximos y mínimos|máximo y mínimo de la función.]] 

En este caso tenemos que: 

$$f(x,y) = x\;\land\;g(x,y)=x^2 + y^2 - 3$$ 
Luego, el Lagrangeano de nuestro problema es: 

$$L(x,y,\lambda) = f(x,y) + \lambda g(x,y)$$ 
De aquí se puede optimizar como antes en la sección de [[Máximos y mínimos|máximos y mínimos]]. Por ende, sacamos el [[vector gradiente]] de $L$. 

Note que $\nabla L(x,y,\lambda) = (\frac{\partial f}{\partial x} + \lambda\frac{\partial g}{\partial x}\;,\; + \frac{\partial f}{\partial y} + \lambda\frac{\partial g}{\partial y}\;,\; g(x,y))$  

En nuestro caso, tenemos que: 

$$\nabla L(x,y,\lambda) = (1 + 2\lambda x\;,\; 4\lambda y\;,\; x^2 + 2y^2-3)$$ 
Los [[Puntos críticos|puntos críticos]] son tales que: 

1) $1 + 2\lambda x = 0\implies x=\frac{-1}{2\lambda}$

2) $4\lambda y=0\implies y = 0$  

3) $x^2 + 2y^2 - 3 = 0\implies x\pm\sqrt{3}$ 

Por ende, los [[Puntos críticos|puntos críticos]] serían: 

1) $(x_1,y_1) = (-\sqrt{3},0)$ 
2) $(x_2,y_2) = (\sqrt{3},0)$

De acá, queda pensar; *¿Cómo sabemos si es máximo o mínimo?*  

## Teorema 

Sea $\bar{x}\in S=\lbrace x\;|\;g_i(x)=0\rbrace$. Supongamos que $\lbrace\nabla g_1(\bar{x}), \nabla g_2(\bar{x}),\dots,g_p(\bar{x}))\rbrace$ es un conjunto [[dependencia|linealmente independiente]]. Entonces existe un $\lambda\in\mathbb{R}^p$ tal que: 

$$\nabla L(\bar{x},\lambda) = \vec{0}$$ 
Si además, se tiene $h^T H_xL(\bar{x},\lambda)\;\;h>0\;\;\forall h\neq\vec{0}$, con $H_x$ siendo la [[Matriz Hessiana|matriz Hessiana]], entonces $\bar{x}$ sería un [[Máximos y mínimos|mínimo local.]] 

Mientras que, si se tiene lo mismo: $h^T H_xL(\bar{x},\lambda)\;\;h<0\;\;\forall h\neq\vec{0}$ entonces $\bar{x}$ es un [[Máximos y mínimos|máximo local]]. 

Del ejemplo anterior, tenemos que la [[Matriz Hessiana|matriz Hessiana]] sería: 

$$H_{(x,y)}L(x,y,\lambda) = \begin{bmatrix}

2\lambda & 0\\ 
0 & 4\lambda
\end{bmatrix} $$ 
Tenemos para $(x,y) = (-\sqrt{3},0)$, que $\lambda_1 = \frac{\sqrt{3}}{6}$. Así, la [[Matriz Hessiana|matriz Hessiana]] sería: 

$$H_{(-\sqrt{3},0)}L(-\sqrt{3},0,\lambda) = \begin{bmatrix}

\frac{\sqrt{3}}{3} & 0\\ 
0 & \frac{2\sqrt{3}}{3}
\end{bmatrix} $$

Luego, el [[determinante]] de la [[Matriz Hessiana|matriz]] daria positivo, entonces, es un [[Máximos y mínimos|mínimo local]] de $f$. 

Ahora, para $(x,y) = (\sqrt{3},0)$, $\lambda_2 = -\frac{\sqrt{3}}{6}$. Luego, la [[Matriz Hessiana|matriz Hessiana]] sería: 

$$H_{(\sqrt{3},0)}L(\sqrt{3},0,\lambda) = \begin{bmatrix}

-\frac{\sqrt{3}}{3} & 0\\ 
0 & -\frac{2\sqrt{3}}{3}
\end{bmatrix} $$

Nuevamente, se tiene un [[determinante]]  positivo, pero su traza (suma de las diagonales) es negativo, entonces es máximo local sobre $S$. 