
Nuevamente, se separan en dos conjuntos de nodos, como en el [[Problema de Transporte|problema de transporte]]. 

- $\mathrm{V}=\mathrm{V}_1\cup \mathrm{V}_2$ donde $\mathrm{V}_1=\{\mathrm{i} \in \mathrm{V}: \mathrm{b}(\mathrm{i})=1\}$ y $\mathrm{V}_2=\{\mathrm{i} \in \mathrm{V}: \mathrm{b}(\mathrm{i})=-1\}$
- $|\mathrm{V}_1|=|\mathrm{V}_2|$
- $(i, j) \in A$ entonces $i \in V_1$ y $j \in V_2$

Por lo general, $V_1$ es el conjunto de trabajadores y $V_2$ es el conjunto de tareas. Por lo tanto, el par $(i,j)$ representa si $i$ puede hacer la tarea $j$. 

![[IMG_6221431BB0D3-1.jpeg|center|500]] 


La solución podría llegar a ser un emparejamiento de trabajadores tal que cada vertice incide en un sólo arco. 

Nuevamente, esto se resuelve con el [[Problemas de flujos|problema de flujo]], donde: 

$$\begin{aligned} & \min \sum_{(i, j) \in A} c_{i j} x_{i j} \\\\ & \sum_{\{j:(i, j) \in A\}} x_{i j}-\sum_{\{j:(j, i) \in A\}} x_{j i}=b(i) \quad \forall i \in V \\\\ & x_{i j} \leq u_{i j} \;\;\;\forall(i, j) \in A \\\\ & x_{i j} \geq 0 \;\;\;\forall(i, j) \in A\end{aligned}$$

Y las variables llegarían a ser 

- $x_{ij}$: Cuanto mando de $i$ a $j$
- $\sum_{j\in V_2}x_{ij}=s_1$
- $\sum_{i\in V_1}x_{i2}=d_2$ 

Por lo tanto, se puede formular de la siguiente forma: 

$$\sum_{j\vert (i,j)\in A}x_{ij}-\sum_{k\vert (k,i)\in A}x_{ki}=0$$

Sin embargo, los arcos que entr
