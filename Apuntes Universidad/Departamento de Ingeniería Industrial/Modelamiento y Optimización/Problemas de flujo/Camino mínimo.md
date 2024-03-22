
Se tiene un [[Grafo|grafo]] y se quiere encontrar el caso especial de flujo a costo mínimo. La forma *más barata* de ir de $s$ a $t$.  Se tienen las siguientes variables: 

- Costo $c_{ij}$ por ir de $i$ a $j$ 
- Camino comienza en $s$ y termina en $t$. 
- $b(s)=1, b(t)=-1$ y $b(i)=0$ para $i\in V/\lbrace s,t\rbrace$

$$
\begin{aligned}
& \min \sum_{(i, j) \in A} c_{i j} x_{i j} \\
& \sum_{\{j:(i, j) \in A\}} x_{i j}-\sum_{\{j:(j, i) \in A\}} x_{j i}= \begin{cases}1 & \text { if } i=s \\
0 & \text { if } i \in V \backslash\{s, t\} \\
-1 & \text { if } i=t\end{cases} \\ \\
& x_{i j} \in\{0,1\} \\ \\
&\left(x_{i j}\right.\geq 0 \text { es suficiente })
\end{aligned}
$$

Leyendo la sumatoria en lenguaje natural, la primera sumatoria son los arcos que salen de $i$ y el segundo término serían los que entran a $i$. Se resuelve de la misma forma que cualquier [[Problemas de flujos|problema de flujo]]. 