

Es para resolver ecuaciones de la forma: 
$$
T(n)=pT(\frac{n}{q})+Cn^r
$$
Donde $p$, $q$, $C$ y $r$ son los parámetros del problema. 

Tiene como solución: 

$$

T(n) =

\begin{cases}

\Theta(n^r) & \text{ si } p<q^r\\

\Theta(n^r \log{n}) & \text{ si } p=q^r\\

\Theta(n^{\log_q{p}}) & \text{ si } p>q^r

\end{cases}

$$