
Sea $A\subseteq\mathbb{R}^d$ un conjunto [[Conjuntos abiertos y cerrados|acotado]], completamente incluido en un rectángulo cerrado $R$. Dada $f:A\rightarrow\mathbb{R}$, y $\bar{f}$ una extensión de $f$ al rectángulo $R$, diremos que $f$ es integrable sobre $A$ si $\bar{f}$ es [[Integral en varias variables|integrable]] sobre $R$. Acordándonos que $\bar{f}$ hace alusión a la función [[Extensión|extensión]]. En este caso, se define la integral de $f$ sobre $A$ como la cantidad: 

$$\int^{}_{A}f=\int^{}_{R}\bar{f}$$ 
Finalmente, se define el **volumen de A** como $vol(A) =\int^{}_{A}1$. 

A partir de esto, se puede saber si una función **es integrable**, no así calcular su valor numérico. 

### Observación 

Si $A\subseteq B$, entonces $Vol(A)\leq Vol(B)$. En efecto, si $R$ es el rectángulo que contiene a $B$, se sigue que la [[Extensión|extensión]] $\bar{1}_{a}\leq\bar{1}_{b}$, donde: 

$$ 
\bar{1}_{a}=\begin{cases} 
       1 & x\in A \\
      0 & x\notin A
   \end{cases}
$$
Así, 

$$Vol(A)=\int^{}_{A}1=\int^{}_{R}\bar{1}_{a}\leq\int^{}_{R}\bar{1}_{b}=\int^{}_{B}1_B=Vol(B)$$ 