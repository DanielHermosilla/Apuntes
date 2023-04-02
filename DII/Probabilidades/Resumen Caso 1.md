#### Axiomas y Propiedades: 
1. Ley uniforme discreta: $$\mathbb{P}(A)=\frac{|A|}{|\Omega|}$$
2. Resta 
$$\mathbb{P}(A\backslash B)=\mathbb{P}(A)-\mathbb{P}(A\cap B)$$
3. Inclusión-exclusión 
$$\mathbb{P}(A\cup B) = \mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$$
4. Aditividad disjunta 
$$\mathbb{P}(\bigcup_{i=1}^{n}A_i) =\sum_{i=1}^{n}\mathbb{P}(A_i)$$
#### Probabilidad condicional 
1.  Probabilidad condicional 
$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$
2. Regla de la cadena: 
$$P(B\cap A)= P(B|A)P(A)$$
3. Definición independencia 
$$P(A\cap B)=P(A)\; ·\;P(B)$$
4. Definición independencia condicional: 
$$P(A\cap B\vert C) = P(A\vert C)\ P(B\vert C)$$
5. Ley de Bayes 
$$P(A\vert B) = \frac{P(B\vert A)P(A)}{P(B)}$$
6. Ley de Probabilidades Totales: Si $A_1, A_2, A_3, \dots$ es una particion de $\Omega$,
$$ P(B) = \sum_{i=1}^{\infty}P(B\cap A_i) = \sum_{i=1}^\infty P(B\vert A_i)P(A_i)$$
#### Conteo 
1. Muestreo ordenado con reemplazo: 
$$n\ ·\ n\ ·\ n\ \dots = n^k$$
2. Muestro ordenado sin reemplazo: 
$$n \ ·\ (n-1)\ \dots\ (n-k+1) = \frac{n!}{(n-k)!}=P_{k}^{n}$$
3. Muestreo no-ordenado sin reemplazo 
$$\begin{pmatrix}
n\\ 
k\\
\end{pmatrix} = \frac{n!}{(n-k)!k!}$$
4. Muestro/conteo no-ordenado con reemplazo:
$$\begin{pmatrix}n+k-1\\k\end{pmatrix} = \begin{pmatrix}n + k - 1 \\ n-1\end{pmatrix}$$