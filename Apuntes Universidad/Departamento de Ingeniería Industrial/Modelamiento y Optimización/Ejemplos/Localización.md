
Se quiere satisfacer una demanda que está geográficamente distribuida y se quiere ver donde poner los servicios para atender las personas. Existen tres variantes de este problema: 

- P-mediana 

- P-centering 

- Cobertura

Por lo tanto, nos definimos las siguientes variables: 

$$\begin{align}
I&=\text{Conjunto de demandas}\\  \\
J&=\text{Posibles lugares para establecerse}\\  \\
d_{ij}&=\text{Costo para ir de}\;i\;\text{a}\;j\\  \\
p&=\text{Número de servicios a instalar} 
\end{align}$$

## Enunciado p-mediana 

Dónde poner $p$ servicios para minimizar la suma de los costos de las distancias de atender $i$. 

Por lo tanto, se define las siguientes variables binarias: 

$$\begin{align}
y_j&=\begin{cases}
1&\text{Si pongo servicio en}\;j\\  \\
0&\text{Si no} 
\end{cases}\\  \\
x_{ij}&=\begin{cases}
1&\text{Si demanda en}\;i\;\text{se atiende en}\; j\\  \\
0&\text{Si no} 
\end{cases}\\  \\
J_i&=\;\text{Donde ya existen servicios}
\end{align}$$

Por lo tanto, instalar $p$ servicios se puede expresar como: 

$$\begin{align}
\sum^{}_{j\in J}y_i&=p
\end{align}$$

Por el otro lado, $x_{ij}\leq y_j\;\;\forall i\in I,\;\forall j\in J$. Así, $x_{ij}\leq y_j$ que representa que la demanda de que se atienda en un lado es menor o igual a que si pone el servicio en ese mismo lado. 

Por último, 

$$\sum_{j\in J}x_{ij}=1\;\;\;\;\;\forall i\in I$$
