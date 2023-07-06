
Se define con tres variables, siendo $N=\text{tamaño población}$, $k=\text{casos positivos o exitos}$ y $n =\text{tamaño de muestra}$ y $K=\text{numero de pasos positivos en la muestra}$. Por lo tanto, su fórmula es la siguiente: 

$$p_x(k)=\frac{\begin{pmatrix} K \\ k \end{pmatrix}\begin{pmatrix}N-K \\ n-k\end{pmatrix}}{\begin{pmatrix}N \\ n \end{pmatrix}}$$

## Esperanza 

$$E[X] = E[\sum_{i=1}^{n}y_i]$$ $$ E[X] = \sum_{i=1}^{n}E[Y_i]$$ $$E[X] = \frac{nk}{N}$$  
### Ejemplo 

Se tienen 50 vehículos y 10 siniestros. 8 son de la aseguradora.  ¿Cuantos vehículos son de la aseguradora? Se puede definir $X$ como el número de vehículos de la aseguradora, y se pregunta por $P(X=3) = \frac{\begin{pmatrix} 10 \\ 3 \end{pmatrix} \begin{pmatrix} 40 \\ 5 \end{pmatrix}}{\begin{pmatrix} 50 \\ 8 \end{pmatrix}}$.  

