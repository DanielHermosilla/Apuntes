 
Se dice que se tiene una distribución binomial con $n\in\mathbb{Z}_{+}, p\in [0,1], R_x = \lbrace 0,1,\dots,n\rbrace$. 

Entonces: 

$$p_x(k)=\begin{pmatrix} n \\ k \end{pmatrix}p^k(1-p)^{n-k}$$ 
## Esperanza 

La [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Esperanza|esperanza]] de esto sería: 

$$E[X] = \sum_{k=0}^{n}k·\begin{pmatrix} n \\ k \end{pmatrix}p^k(1-p)^{n-k}$$ 
Con cambios de variable y sacando constantes afuera: 

$$ E[X] = np\sum_{j=0}^{n-1}\frac{(n-1)!}{(n-j-1)!j!}p^j(1-p)^{n-1-j}$$ 
Dado que se tiene una [[Función de Masa de Probabilidad|PMF]], entonces la suma es 1. 
$$E[X] = np · 1$$  
Otra forma más simple es considerar una distribución de Bernoulli, donde $Y=1$ si el evento $i$ cumple y $0$ si no. Entonces 

$$E[X] = E[Y_1 + Y_2 + \dots + Y_n]$$
$$\iff E[Y_1] + E[Y_2] + E[Y_3] + \dots E[Y_n]$$ $$\implies E[X] = np$$ 
## Varianza 

Para calcular la [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Varianza|varianza]] sería: 

$$Var(x) = E[X^2] + E[X]^2$$ 
Primero, se calcula el primer término: 

$$E[X^2] = \sum_{k=0}{n}k^n\begin{pmatrix}n \\ k \end{pmatrix}p^k(1-p)^{n-k}$$ 
$$E[X^2] = \sum_{k=1}^{n}\frac{(k-1)!n!}{(n-1)!(n-k)!}p^k(1-p)^{n-k} + \sum_{k=1}^{n}\frac{n!}{(k-1)!(n-k)!}p^k(1-p^{n-k})$$ 
La segunda suma es conocida, que es $np$, por el otro lado, sacando constantes hacia afuera y haciendo cambios de índices: 

$$ = n(n-1)p^2\sum_{j=0}^{n-2}\frac{(n-2)!}{j!(n-2-j)!}p^j(1-p)^{n-2-j} + np$$ 
Y la sumatoria que se obtiene es la suma de una [[Función de Masa de Probabilidad|PMF]], entonces: 

$$ Var(x) = np(1-p)$$ 