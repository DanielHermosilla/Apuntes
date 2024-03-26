
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

#### Ejemplo 

Una compañia produce piezas de acero de largo $L_1<L_2<\dots<L_n$

- Di es la demanda para barras de largo Li.
- Ki : costo fijo para producir barras de largo Li
- ci : costo variable por producir una barra de largo Li
- Se puede satisfacer la demanda Di con barras de largo Di, Di+1,... Dn

Por lo tanto, nos definimos las siguientes variables: 

$$y_i=\begin{cases}
1&\text{Si produzco barras}\;L_i\\ \\
0&\text{Si no}\end{cases}$$

Y también, para representar la cantidad de barras: 

$$x_i=\text{Cantidad de barras}\;L_i$$

Otra variable que representa la cantidad de $D_i$ satisfecha por $L_j$: 

$$S_{ij}=\text{Cantidad de}\;D_i\;\text{satisfecha por}\;L_j$$

Por lo tanto, la **restricción** para satisfacer la demanda llegaría a ser: 

$$\begin{align}
\sum^{n}_{j=i}S_{ij}&\geq D_i\\  \\
X_i&=\sum^{i}_{k=1}S_{ki}\\  \\
X_i&\leq My_i
\end{align}$$

 