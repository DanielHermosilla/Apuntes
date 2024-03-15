
Se tiene la siguiente sumatoria, con $n\in\mathbb{N}$ y $z\in\mathbb{C}$. Buscar radio de convergencia: 

$$\sum^{\infty}_{n=0}n!\;(z-i)^{n!}$$

Primero reescribimos: 

$$a_k=\begin{cases}k&\exists n\in\mathbb{N}\;\text{tal que}\;n!=k\\  \\
0&\text{si no}\end{cases}$$

Así: 

$$\begin{align}
\sum^{\infty}_{n=0}n!(z-i)^{n!}&=\sum^{\infty}_{k=0}a_k(z-i)^k\\  \\
\end{align}$$

Para calcular el radio $R$ lo hacemos por definición: 

$$\begin{align}
\lim_{k\to\infty}\sqrt[k]{a_k}&=\lim_{n\to\infty}\sqrt[n!]{n!}=1
\end{align}$$

Por lo tango, converge en $D(i,1)$