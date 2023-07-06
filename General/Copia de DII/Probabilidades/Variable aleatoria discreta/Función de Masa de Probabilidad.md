
Sea $X$ una [[Variable aleatoria discreta|variable aleatoria discreta]] con rango $R_x$, entonces la **función de masa de probabilidad** de $X$ se define como la función: 

$$p_x(x) = \mathbb{P}(X=x)$$ 
Para todo $x\in R_x$. 

Notar que se podría definir la PMF sobre todos los valores reales, es decir, incluyendo los $x\notin R_x$ 

$$p_x(x) = \begin{cases}
\mathbb{P}(X=x) & \text{si}\ x\in R_x. \\ 
0 & \text{si no}
\end{cases}$$ 

## Propiedades 

1. $0\leq p_x(x)\leq 1\ \forall x$ 
2. $\sum_{x\in R_x}p_x(x) = 1$
3. Para todo $A\subset R_x, \mathbb{P}(X\in A) = \sum_{x\in A}p_x(x)$ 

## Ejemplo 

Se lanza una moneda dos veces y se pregunta por el número de caras, es decir, $X = \text{cantidad de caras}$. Se sabe que $\Omega = \lbrace (c,c),(c,s),(s,c),(s,s)\rbrace$ y el rango es $R_x = \lbrace 0,1,2,3\rbrace$. Entonces: 

- $P_x(0) = \mathbb{P}(\lbrace(s,s)\rbrace) = \frac{1}{4}$ 
- $P_x(1) = \mathbb{P}((c,s),(c,s)) = \frac{1}{2}$ 
- $P_x(0) = \mathbb{P}(\lbrace(c,c)\rbrace) = \frac{1}{4}$ 

Si ahora la moneda es tal que la probabilidad de caras es "$p$" y se lanzan $k$ monedas. Entonces: 

- $P_x(k) = \mathbb{P}(x=k) = \mathbb{P}(1-p)^{k-1}$ 

