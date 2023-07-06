Sea $A$ una [[matriz]] cualquiera, denominaremos como polinomio carácteristico al siguiente cálculo: 

$$ P(\lambda) = det (A - \lambda I) $$ 
Si nos acordamos de la definición de [[valores y vectores propios]], donde $v$ es [[vector propio]] si $v \neq 0$ y existe un [[escalares|escalar]] $\lambda \in \mathbb{K}$ tal que $Av = \lambda v$, podemos concluir que $\lambda$ es [[valor propio]] solo si existe solución no nula de la ecuación 

$$ (A - \lambda I)v = 0 $$

Es decir, cualquier solución no nula de la ecuación es un [[vector propio]] de $A$ con [[valor propio]] $\lambda$. 

Notemos que los valores propios son únicos, no así los vectores propios, por lo tanto, por cada valor propio $\lambda$ introduciremos el concepto de [[subespacios propios|subespacio propio]] donde se determinará el [[Espacios vectoriales|espacio vectorial]] de cada [[vectores|vector]] asociado a $\lambda$.  

### Cálculo de [[valor propio|valores propios]] a partir del polinomio característico 

Como sabemos que los valores propios son escalares que necesitan ser valores reales, al calcular el polinomio característico de una matriz estamos calculando, en realidad, el polinomio cuyas raíces nos darán los valores propios. 

#### Ejemplo

Sea $A \in M_{2,2}$ la siguiente matriz: 

$$ \begin{bmatrix} 4 & -5 \\ 2 & -3 \end{bmatrix} $$

Entonces, el polinomio característico sería:

$$ P(\lambda) = \det \begin{bmatrix} 4 - \lambda  & -5 \\ 2 & -3 - \lambda\end{bmatrix} = -(4- \lambda)(3+ \lambda) + 10 = -2 - \lambda + \lambda^2$$ 
Por lo tanto, los valores propios serían $\lambda$ = 2 y $\lambda = -1$. Para calcular los vectores propios habría que calcular los subespacios propios. Por lo tanto: 

1. Espacio propio para $\lambda = 2$:

$$ W_2 =  Ker \begin{bmatrix} 2  & -5 \\ 2 & -5\end{bmatrix} = \begin{bmatrix} 2  & -5 & | \enspace 0\enspace\\ 2 & -5 & |\enspace 0\enspace\end{bmatrix} = \langle\lbrace\begin{pmatrix} \frac{5}{2} \\ 1 \end{pmatrix} \rbrace \rangle$$
2. Espacio propio para $\lambda = -1$:

$$ W_{-1} = Ker \begin{bmatrix} 5  & -5 \\ 2 & -2\end{bmatrix} = \begin{bmatrix} 5  & -5 & | \enspace 0\enspace\\ 2 & -2 & |\enspace 0\enspace\end{bmatrix} = \langle\lbrace\begin{pmatrix} 1 \\ 1 \end{pmatrix} \rbrace \rangle$$

