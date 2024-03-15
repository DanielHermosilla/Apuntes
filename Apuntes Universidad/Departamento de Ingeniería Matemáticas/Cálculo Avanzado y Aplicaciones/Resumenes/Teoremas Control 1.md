
>[!example] Teorema de Green 
>
>Sea $\Omega\subseteq\mathbb{R}^2$, un conjunto simplemente conexo y conexo, cuya **frontera** está dada por una curva $C$, regular y simple. Supongamos además que $C$ está recorrida en recorrido antihorario. 
>
>Además, sea $F:A\subseteq\mathbb{R}^2\to\mathbb{R}^2$ una función de clase $C^1$ en $A$, y $\bar{\Omega}\subseteq A$. Además, $F=(P,Q)\iff P\hat{i}+Q\hat{j}$. Entonces:  $$\oint_CF\cdot dr=\oint_CPdx+Qdy=\int\int_\Omega\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dxdy$$
>
 >**La extensión llegaría a ser**: 
 >
>Sea $\Omega\subset\mathbb{R}^2$, un [[Conjuntos abiertos y cerrados|conjunto abierto]] no vacio, donde su [[Fronteras|frontera]] corresponde a [[Curvas|curvas]] [[Curva cerrada|cerradas]] [[Curva simple|simple]] seccionalmente suaves, todas recorridas en sentido antihorario disjuntas entre ellas, y $C_1,\dots,C_n\subset C_0$. 
>
>Además, sea $F:A\subseteq\mathbb{R}^2\to\mathbb{R}^2$ una función suave tal que: 
>$$F=P\hat{i}+Q\hat{j}\;\;\land\;\;\bar{\Omega}\subseteq A$$
>
>Entonces: 
>$$\begin{align}
>\int\int_{\Omega}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA&=\oint_{C_o}P\;dx + Q\;dy - \sum^{n}_{i=1}\oint_{C_i}P\;dx+Q\;dy
>\end{align}$$


>[!example] Teorema de Gauss 
>
>Sea $D$ una región sólida acotada en $\mathbb{R}^3$, limitada por una superficie seccionalmente suave y **cerrada** $\Sigma$, y supongamos que $\vec{f}$ es un campo vectorial de clase $C^1$ en $D$ y $\hat{n}$ es la orientación de $\Sigma$ que apunta hacia el exterior. Entonces: 
>
>$$\int\int_{\Sigma}\vec{f}\cdot\hat{n}\;d\sigma=\int\int\int_{D}\text{div}\vec{f}(x,y,z)\;dx\;dy\;dz$$


>[!example] Teorema de Stokes 
>
>Sea $\Sigma$ una superficie orientable regular y con borde una curva $C$, curva cerrada simple. $\Sigma$ posee una normal $\hat{n}$ y es tal que la dirección de recorrido de la curva $C$ sea orientada positivamente con respecto a la normal $\hat{n}$, es decir, respeta la *regla de la mano derecha*. Sea $F:\Omega\subset\mathbb{R}^3\to\mathbb{R}^3$ , entonces: 
>
>$$\oint_C F\cdot dr=\int\int_\Sigma(\nabla\times\vec{F})d\Sigma$$


