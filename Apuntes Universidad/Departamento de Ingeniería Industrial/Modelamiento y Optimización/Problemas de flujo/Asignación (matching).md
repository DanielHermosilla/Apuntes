
Nuevamente, se separan en dos conjuntos de nodos, como en el [[Problema de Transporte|problema de transporte]]. 

- $\mathrm{V}=\mathrm{V}_1\cup \mathrm{V}_2$ donde $\mathrm{V}_1=\{\mathrm{i} \in \mathrm{V}: \mathrm{b}(\mathrm{i})=1\}$ y $\mathrm{V}_2=\{\mathrm{i} \in \mathrm{V}: \mathrm{b}(\mathrm{i})=-1\}$
- $|\mathrm{V}_1|=|\mathrm{V}_2|$
- $(i, j) \in A$ entonces $i \in V_1$ y $j \in V_2$

Por lo general, $V_1$ es el conjunto de trabajadores y $V_2$ es el conjunto de tareas. Por lo tanto, el par $(i,j)$ representa si $i$ puede hacer la tarea $j$. 

![[IMG_6221431BB0D3-1.jpeg|center|500]] 


La solución podría llegar a ser un emparejamiento de trabajadores tal que cada vertice incide en un sólo arco.  De tal forma, la relación es $1:1$,  la tarea necesita a **un trabajador** y las tareas deben tener una **única asignación**. 

Nuevamente, esto se resuelve con el [[Problemas de flujos|problema de flujo]], donde: 

$$\begin{aligned} & \min \sum_{(i, j) \in A} c_{i j} x_{i j} \\\\ & \sum_{\{j:(i, j) \in A\}} x_{i j}-\sum_{\{j:(j, i) \in A\}} x_{j i}=b(i) \quad \forall i \in V \\\\ & x_{i j} \leq u_{i j} \;\;\;\forall(i, j) \in A \\\\ & x_{i j} \geq 0 \;\;\;\forall(i, j) \in A\end{aligned}$$

Y las variables llegarían a ser 

- $x_{ij}$: Cuanto mando de $i$ a $j$
- $\sum_{j\in V_2}x_{ij}=s_1$
- $\sum_{i\in V_1}x_{i2}=d_2$ 

Por lo tanto, se puede formular de la siguiente forma: 

$$\sum_{j\vert (i,j)\in A}x_{ij}-\sum_{k\vert (k,i)\in A}x_{ki}=0$$

Sin embargo, los arcos que entran a $x_{ki}$ no existen, es un flujo constante hacia $V_2$. Así, se reduce a lo siguiente: 

$$\begin{align}
\sum_{j\vert (i,j)\in A}x_{ij}-\cancel{\sum_{k\vert (k,i)\in A}x_{ki}}&=0\\  \\
\sum_{j\vert j\in V_2(i,j)\in A}x_{ij}&=s_i
\end{align}$$

Así, poniendo en contexto el problema, la sumatoria debería ser igual a la demanda del nodo de destino. Por lo tanto: 

$$\sum_{i\in V_1(i,j)\in A}x_{ij}=d_j\;\;\;j\in V_2$$

Ahora, en el caso que se plantea para los nodos en $V_2$, es decir, al conjunto que le **llega flujo**. 

$$\sum_{j\vert (i,j)\in A}x_{ij}-\sum_{k\vert (k,i)\in A}x_{ki}=b_i\;\;\; i\in V_2$$

Por último, plantear que se puede hacer una especia de variable binaria donde

$$\sum_{j\in V_2}x_{ij}=1$$

Si existe un $j(i)$ tal que cumpla el trabajo. El resto valdría $0$. 