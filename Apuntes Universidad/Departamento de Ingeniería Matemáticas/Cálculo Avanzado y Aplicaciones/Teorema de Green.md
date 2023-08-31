
Sea $\Omega\subset\mathbb{R}^2$, se dirá lo siguiente: 

- $\Omega$ es conexo (o conexo por cáminos), si dado dos $(x,y)\in\Omega$ existe una [[Curvas|curva]] $C$ desde $x$ a $y$ tal que $C\in\Omega$.  

- Un [[Conjuntos|conjunto]] $\Omega$ es **simplemente conexo** si $\Omega^c$ es conexo. 

Por lo tanto, el *teorema de Green* plantea $\Omega\subseteq\mathbb{R}^2$, un [[Conjuntos|conjunto]] simplemente conexo y conexo, cuya [[Fronteras|frontera]] está dada por una curva $C$, regular y simple. Supongamos además que $C$ está recorrida en recorrido antihorario. 

>[!info]  
Sea $F:A\subseteq\mathbb{R}^2\to\mathbb{R}^2$ una función de clase $C$ en $A$, y $\bar{\Omega}\subseteq A$. Además, $F=(P,Q)\iff P\hat{i}+Q\hat{j}$. Entonces:  $$\oint_CF\cdot dr=\oint_CPdx+Qdy=\int\int_\Omega\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dxdy$$

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
&=\int^{1}_{0}\int^{2\pi}_{0}(2r+2r^2\sin\theta)\;d\theta dr\\  \\
&=\int^{1}_{0}\left[(2r\theta-2r^2\cos\theta)\bigg\vert^{2\pi}_{0}\right]dr\\  \\
&=\int^{1}_{0}4\pi r\;dr\\  \\
&=2\pi
\end{align}$$

#### Ejemplo 

Sea $C$ el cuadrado de vértices $(0,0),\;(1,0),\;(1,1),\;(0,1)$, recorrido en sentido antihorario. Sea $F(x,y)=(2x+y,xy)$. Calcular la integral de línea. 

Con el teorema de Green, notar que: 

$$\frac{\partial P}{\partial y}=1\;\land\;\frac{\partial Q}{\partial x}=y$$

Por lo tanto, se llega que el campo no es conservativo. Aplicando el teorema: 

$$\begin{align}
\oint F\cdot dr&=\int\int_Cy-1\;dA\\  \\
&=\int^{1}_{0}\int^{1}_{0}y-1\; dxdy\\  \\
&=\int^{1}_{0}y-1\;dy \\  \\
&=\frac{y^2}{2}-y\;\bigg\vert^{1}_{0}\\  \\
&=-\frac{1}{2}
\end{align}$$



## Teorema de Green generalizado 

Ahora, es posible extender el teorema para los casos donde el [[Conjuntos|conjunto]] no es conexo, como en el caso de un anillo: 

![[IMG_4CE96FB1CF1C-1.jpeg|center|450]]

Sin embargo, es posible hacer particiones del conjunto, para lograr que no sea conexo: 

![[IMG_D87C6F7FE17C-1.jpeg|center|450]]

Por lo tanto, es posible definir ahora la integral de línea del conjunto $\Omega$ como: 

$$\int\int_\Omega\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dxdy=\int\int_{C_1\cup C_2\cup C_3\cup C_4}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dxdy=$$

Pero ahora, si se hace lo equivalente con la otra mitad, donde nos definimos el otro conjunto como $\Omega'$, podríamos notar que $C_2'$ se cancela con $C_2$ al recorrer en sentido contrario y lo mismo con $C_3'$ y $C_3$. 

![[IMG_7AAA25B10C0D-1.jpeg|center|450]]

Por lo tanto, si se unieran ambos conjuntos, se tendría el siguiente diagrama: 

![[IMG_CFC809FBBB8B-1 1.jpeg|center|450]]

Por lo tanto, se tendría una curva que se recorre en sentido horario y otra en sentido antihorario. 

>[!info] 
>Sea $\Omega\subset\mathbb{R}^2$, un [[Conjuntos abiertos y cerrados|conjunto abierto]] no vacio, donde su [[Fronteras|frontera]] corresponde a [[Curvas|curvas]] [[Curva cerrada|cerradas]] [[Curva simple|simple]] seccionalmente suaves, todas recorridas en sentido antihorario disjuntas entre ellas, y $C_1,\dots,C_n\subset C_0$. 
>
>Además, sea $F:A\subseteq\mathbb{R}^2\to\mathbb{R}^2$ una función suave tal que: 
>$$F=P\hat{i}+Q\hat{j}\;\;\land\;\;\bar{\Omega}\subseteq A$$
>
>Entonces: 
>$$\begin{align}
>\int\int_{\Omega}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA&=\oint_{C_o}P\;dx + Q\;dy - \sum^{n}_{i=1}\oint_{C_i}P\;dx+Q\;dy
>\end{align}$$

#### Ejemplo 

Sea $C$ el cuadrado de vértices $(1,1),\;(-1,1),\;(-1,-1),\;(1,-1)$ recorrido en sentido antihorario. Calcular la integral: 

$$\int_C\left(\frac{-y}{x^2+y^2}\right)dx+\left(\frac{x}{x^2+y^2}\right)dy$$

Ocupando el teorema de Green extendido, nos definimos una circumferencia de radio $a$ en el origen.

![[IMG_81AB91872B43-1.jpeg|center|450]]

Por lo tanto, nos definimos $\Omega=[-1,1]\times [-1,1]\backslash\lbrace (x,y)\in\mathbb{R}^2\;\vert\; x^2+y^2<a\rbrace$. Si $F(x,y)=\left(P(x,y),Q(x,y)\right)$, entonces: 

$$\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}=0$$

Calculando la integral para la curva $C_1$, ocupando [[Departamento de Ingeniería Matemáticas/Cálculo Diferencial e Integral/Aplicaciones de la integral/Coordenadas polares|coordenadas polares]], se puede parametrizar como: 

$$C_1:r(t)=(a\cos t,a\sin t),\;t\in[0,2\pi]$$

Por ende, la integral sería: 

$$\begin{align}
\int_{C_1}Pdx+Qdy&=\int^{2\pi}_{0}\left(\frac{-a\sin t}{a^2\cos^2 t +a^2\sin^2 t},\frac{a\cos t}{a^2\cos^2 t+a^2\sin^2 t}\right)\cdot\left(-a\sin t,a\cos t\right)\;dt\\  \\
&=\int^{2\pi}_{0}\left(\frac{\cancel{a^2}\sin^2t}{\cancel{a^2}}+\frac{\cancel{a^2}\cos^2 t}{\cancel{a^2}}\right)\;dt\\  \\
&=\int^{2\pi}_{0}dt \\\\
&=2\pi
\end{align}$$

Así; 

$$\cancelto{0}{\int\int_{\Omega}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA}=\oint_{C_o}F\cdot dr - \cancelto{2\pi}{\oint_{C_1}F\cdot dr}$$

Por lo tanto, el resultado llegaría a ser, simplemente $2\pi$. 

#### Ejemplo: 

Calcular usando el teorema de Green, donde $F(x,y)=P\hat{i}+Q\hat{j}=\left(\frac{3xy}{x^2+y^2},\frac{2x-y}{x^2+y^2}\right)$ y $\Omega=\lbrace (x,y)\in\mathbb{R}^2\;\vert\; 1\leq x^2+y^2\leq 4\rbrace$.  