
Se define como la siguiente distribución, donde se separan los [[Evento|eventos]] entre unos y ceros. Es algo parecido a cosas *booleanas*: 

$$p_x(x) = \begin{cases}
1-p & \text{si}\ x=0 \\ 
p & \text{si}\ x=1 \end{cases} $$ 

En este caso, también se podría calcular la [[Esperanza|esperanza]]:

$$E[x] = 0 · (1-p) + 1 · p = p$$ 
Y la [[Varianza|varianza]]:

$$Var(x) = E[X^2]-E[X]^2$$ 
Por lo tanto, la [[Varianza|varianza]] sería: 

$$Var(X) = p(1-p)$$ 
Que se maximisa cuando $p=\frac{1}{2}$ 

Tipicamente se podría pensar un [[Espacio muestral|espacio muestral]] $\Omega$ y un [[Evento|evento]] dentro de este $A\subset\Omega$, entonces se puede definir la [[Variable aleatoria discreta|variable aleatoria]] $I_a$ que vale $1$ si el evento $A$ ocurre y $0$ en caso de lo contrario. 

## Gráfico 

Por lo tanto, gráficamente se vería de la siguiente forma: 

![[Bernoulli.png|center|500]]



### Ejemplo

Supongamos que 1 de cada 5 vehiculos tiene un accidente. Se puede definir la [[Variable aleatoria discreta|variable aleatoria]] como el siguiente: 

$$X =\begin{cases} 

1 & \text{Hay siniestro} \\ 
0 & \text{No hay siniestro}

\end{cases}$$ 
Por lo tanto, se sabe que $\mathbb{P}(X=1) = 0.2$ y $\mathbb{P}(X=0) = 0.8$.  

### Ejemplo 

Supongamos que se tienen 10 vehículos y $0.2$ es la probabilidad de siniestro de cada uno. Además, cada siniestro es [[Probabilidades/Probabilidad condicional e independencia/Independencia|independiente]]. En adición, se supone que los vehículos tienen un pago de $2\$$ a la aseguradora y $6\$$ es el costo de la aseguradora por siniestro. 

Se define la [[Variable aleatoria discreta|variable aleatoria]] $X$ el número de vehículos que tienen siniestros. El rango de $X$ sería $[0,10]$. Por otra parte, se define $A_i$ el [[Evento|evento]] que el vehiculo $i$ sufra un accidente.   

¿Cuál es la probabilidad de que la utilidad sea $2\$$? Es decir, $\mathbb{P}(X=3)$. Por ende, 

$$\mathbb{P}(X=3)=\sum_{i<j<k}\mathbb{P}(A_i,A_j,A_k,A_{l}^{c})\ \ \forall l\notin (i,j,k)$$ 
Es lo mismo que decir que: 

$$\sum_{i<j<k}(A_1,A_2,A_3,A_{4}^{c},\dots,A_{10}^{c})$$ 
Equivalente a tener $\begin{pmatrix} 10 \\ 3\end{pmatrix}$. Entonces, aplicando [[Probabilidades/Probabilidad condicional e independencia/Independencia|independencia]], se tiene que: 

$$\mathbb{P}(X=3) = \begin{pmatrix} 10 \\ 3\end{pmatrix} \mathbb{P}(A_1)·\mathbb{P}(A_2)·\mathbb{P}(A_3)·\mathbb{P}(A_{4}^{c})\dots\mathbb{P}(A_10))$$     
Esto se denomina como [[Distribución binomial]]. Por lo tanto, la [[Esperanza|esperanza]] del costo sería: 

$$E[\text{costo}] = E[6X] = 6E[X] = 6 · 10 · 0.2 = 12$$ 
