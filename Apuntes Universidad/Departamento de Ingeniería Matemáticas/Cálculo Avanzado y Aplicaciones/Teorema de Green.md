
Sea $\Omega\subset\mathbb{R}^2$, se dirá lo siguiente: 

- $\Omega$ es conexo (o conexo por cáminos), si dado dos $(x,y)\in\Omega$ existe una [[Curvas|curva]] $C$ desde $x$ a $y$ tal que $C\in\Omega$.  

- Un [[Conjuntos|conjunto]] $\Omega$ es **simplemente conexo** si $\Omega^c$ es conexo. 

Por lo tanto, el *teorema de Green* plantea $\Omega\subseteq\mathbb{R}^2$, un [[Conjuntos|conjunto]] simplemente conexo y conexo, cuya [[Fronteras|frontera]] está dada por una curva $C$, regular y simple. 

Supongamos además que $C$ está recorrida en recorrido antihorario. 

Sea $F:A\subseteq\mathbb{R}^2\to\mathbb{R}^2$ una función de clase $C$ en $A$, y $\bar{\Omega}\subseteq A$. Además, $F=(P,Q)\iff P\hat{i}+Q\hat{j}$. Entonces: 

$$\oint_CF\cdot dr=\oint_CPdx+Qdy=\int\int_\Omega\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dxdy$$

Notemos que si el campo es [[Campos conservativos|conservativo]], la integral vale $0$. 

#### Ejemplo 

Sea $F(x,y)=(x^2-y^2,2x+y^2)$ y sea $C$ la circumferencia unitaria con centro en $(0,0)$ y recorrida en sentido antihorario. Calcular la [[Integral de línea|integral de línea]]. 

Sea $Q(x,y)=x^2-y^2\;\land\;P(x,y)=2x+y^2$. Por lo tanto: 

$$\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=2+2y\neq 0$$

Vale decir, el campo no es conservativo. Así, usando el teorema de Green: 

$$\int\int_\Omega2+2y\;dA$$

Ocupando [[Departamento de Ingeniería Matemáticas/Cálculo Diferencial e Integral/Aplicaciones de la integral/Coordenadas polares|coordenadas polares]], se llega que: 

$$\begin{align}
\oint F\cdot dr&=\int^{1}_{0}\int^{2\pi}_{0}(2+2r\sin\theta)r\;d\theta dr\\  \\
&=\int^{1}_{0}\
\end{align}$$