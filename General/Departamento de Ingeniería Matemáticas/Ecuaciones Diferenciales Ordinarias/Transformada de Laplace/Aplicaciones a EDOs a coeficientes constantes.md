
Supongamos tenemos la ecuación: 

$$P(D)y(t)=Q(t)$$ 
Con $P(D)=\sum^{n}_{k=0}a_kD^k$. Entonces tomemos una [[Transformada de Laplace|transformación de Laplace]] a ambos lados de la ecuación: 

$$\mathbb{L}[\sum^{n}_{k=0}a_ky^{(k)}]=\mathbb{L}[Q]$$ 
Trabajando el lado izquierdo: 

$$\begin{align}

\mathbb{L}[\sum^{n}_{k=0}a_ky^{(k)}](s)&=\sum^{n}_{k=0}a_k\mathbb{L}[y^{(k)}]\\\\
&\text{Notemos que}:\\\\
\mathbb{L}[y^{(k)}]&=s^k\mathbb{L}[y](s)-R_k(s)\;\;\; R_k\;\text{es un polinomio que depende de CI} \\\\ 
\sum^{n}_{k=0}a_k\mathbb{L}[y^{(k)}]&=\mathbb{L}[y](s)\sum^{n}_{k=0}a_ks^k - \sum^{n}_{k=0}a_kR_k(s)\\\\

\end{align}$$

Notar que $\sum^{n}_{k=0}a_ks^k$ es el polinomio característico y el otro sumando es un polinomio que depende de las condiciones iniciales. 

Llamando $P(s)=\sum^{n}_{k=0}a_kS^k$, entonces: 

$$R(s)=\sum^{n}_{k=0}a_kR_k(s)$$  Queda como: 

$$\begin{align}
P(s)\mathbb{L}[y](s)-R(s)&=\mathbb{L}[Q](s)\\\\
\implies\mathbb{L}[y](s)&=\frac{R(s)}{P(s)}+\mathbb{L}[Q](s)\cdot P^{-1}(s)
\end{align}$$

Tomando [[Antitransformada|antitransformadas]]: 

$$y(t)=\mathbb{L}^{-1}\left[\frac{R}{P}\right]+\mathbb{L}^{-1}\left[\mathbb{L}[Q]\cdot P^{-1}\right]$$ 
Supongamos existe $G$ tal que: 

$$\begin{align}
\mathbb{L}[G]&=P^{-1}\\\\
\mathbb{L}[Q]\cdot P^-1 &= \mathbb{L}[Q]\cdot\mathbb{L}[G]\\\\
&=L[Q*G]
\end{align}$$

Es decir, se llega a una [[Departamento de Ingeniería Matemáticas/Ecuaciones Diferenciales Ordinarias/Transformada de Laplace/Convolución|convolución]], entonces $y$ satisface: 

$$y(t)=\mathbb{L}^{-1}\left[\frac{R}{P}\right] + Q*G$$ 
Donde $\frac{R}{P}$ es una descomposición en fracciones parciales. 