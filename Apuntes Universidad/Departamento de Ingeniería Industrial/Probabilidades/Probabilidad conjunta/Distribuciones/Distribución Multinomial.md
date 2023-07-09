
Las [[Variable aleatoria continua|variables]] $X_1, X_2, \cdots, X_k$ siguen una distribución Multinomial$(N,q_1,q_2,\cdots, q_k)$ con parametros $N\in\mathbb{Z}_+$ y $q\geq 0$ tal que $\sum_{i=1}^{k} q_i=1$, y su [[PMF conjunto|PMF conjunta]] está dada por: 

$$\begin{align}P_{X_1,X_2,\dots,X_k}(x_1,x_2,\cdots,x_k)&=\frac{N!}{x_1!x_2!\dots x_k!}q_{1}^{x_1}q_{2}^{x_2}\cdots q_{k}^{x_k}\\\\
&= \begin{pmatrix}N\\x_1,x_2,\dots,x_k\end{pmatrix}q_{1}^{x_1}q_{2}^{x_2}\dots q_{k}^{x_k}\end{align}$$ 


Para $x_1, \dots, x_k$ tales que $\sum_{i=1}^{k}x_i=N$ 

### Propiedades 

Si $(X_1, X_2, \dots, X_k)$ distribuyen multinomial $(N,q_1,\dots, q_k)$, entonces: 

- $X_i \sim\text{Binomial}(N,q_1)$
- Para cualquier $S\subset\lbrace 1,2,\dots,k\rbrace$ se cumple que $\sum_{i \in S}X_i\sim\text{Binomial}(N,\sum_{i\in S}q_i)$ 
- $\text{Cov}(X_i, X_j) = -Nq_iq_j$ si $i\neq j$ 