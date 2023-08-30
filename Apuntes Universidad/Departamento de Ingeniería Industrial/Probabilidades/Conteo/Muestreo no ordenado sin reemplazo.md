
El número de subconjuntos o combinaciones de $k$ elementos de un [[Conjuntos|conjunto]] de $n$ elementos: 

$$\begin{pmatrix}
n\\ 
k\\
\end{pmatrix} = \frac{n!}{(n-k)!k!}$$ 
O también equivalente a tener el **coeficiente binomial**: 

$$(a+b)^n = \sum_{k=0}^{n}\begin{pmatrix}n \\ k\end{pmatrix}x^{n-k}y^k$$ 
También sirve para obtener el número de combinaciones en que se pueden formar $r$ grupos de tamaños $n_1, n_2, \dots, n_r$ de un [[Conjuntos|conjunto]] de $n$ elementos. 

Corresponde al coeficiente multinomial. Corresponde a: 

$$\frac{n!}{k_1!\ k_2!\ k_3!\dots\ k_j!}$$ 

### Ejemplo

Se lanza un dado 18 veces, ¿cual es la probabilidad de que salgan exactamente 3 veces un número dado? 

$$\mathbb{P}(A) = \frac{|A|}{|\Omega|} = \frac{\begin{pmatrix}18 \\ 3^6\end{pmatrix}}{6^{18}}$$ 
## Propiedades 

- $\begin{pmatrix} n \\ k \end{pmatrix} = \begin{pmatrix} n \\ n-k \end{pmatrix}$

- $\sum_{k=0}^{n}\begin{pmatrix} n\\k\end{pmatrix} = 2^n$ 
- Para $0\leq k < n$ se tiene $\begin{pmatrix} n+1 \\ k + 1\end{pmatrix}$  = $\begin{pmatrix} n \\ k+1 \end{pmatrix} + \begin{pmatrix} n \\ k \end{pmatrix}$ 

- Identidad de Vandermonde: $\begin{pmatrix} x + y \\ n \end{pmatrix} = \sum_{k=0}^{n}\begin{pmatrix} 1 \\ k \end{pmatrix} \begin{pmatrix} y \\ n-k \end{pmatrix}$ 



### Ejemplo

Se tiene el [[Conjuntos|conjunto]] $A=\lbrace 1,2,3\rbrace$. ¿Cuántos subconjuntos (por ende sin repeticiones) de 2 elementos existen?. 

Solamente $\lbrace 1,2\rbrace , \lbrace 2,3\rbrace, \lbrace 1,3\rbrace$. 

Ahora si se extrapola a un [[Conjuntos|conjunto]] $A=\lbrace 1,2,\dots, n\rbrace$. ¿Cuantos subconjuntos de $k$ elementos existen? 

Sería lo mismo a tomar todas las posibilidades de un [[Muestreo aleatorio|muestreo ordenado]] sin reemplazo pero dividido por $k!$. 