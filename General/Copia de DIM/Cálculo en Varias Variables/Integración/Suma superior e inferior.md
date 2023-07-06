
Sea $f:\mathbb{R}\subset\mathbb{R}^n\rightarrow\mathbb{R}$ una función [[Conjuntos compactos|acotada]] sobre el rectángulo $R$. Dada una [[Particiones en varias variables|partición]] $P$ que genera subrectángulos abiertos y disjuntos: $\lbrace R_1,R_2,\dots,R_n\rbrace$. Definimos su correspondiente suma inferior y suma superior, denotada por $L(f,P)$ y la suma superior denotada por $U(f,P)$ como las cantidades: 

$$L(f,P) = \sum^{n}_{i=1}m_iVol(R_i)$$ $$U(f,P) = \sum^{n}_{i=1}M_iVol(R_i)$$ Donde: 
- $m_i = \text{inf}\lbrace f(x)\;|\; x\in R_i\rbrace$  
- $M_i = \text{sup}\lbrace f(x)\;|\; x\in R_i\rbrace$  

Por ejemplo, el caso del $M_i$ de una [[Particiones en varias variables|partición]] cualquiera sería la siguiente:


![[IMG_8AF3D8F5965B-1.jpeg|center|450]]


De esto nos vamos a agarrar para poder formar una especie de [[Suma de Riemann|suma de Riemann]]. Entonces se puede ir refinando las [[Particiones en varias variables|particiones]] de a poco para obtener una aproximación al gráfico de la función. 