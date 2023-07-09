
Asumimos que la demanda de cada cliente es i.i.d. Si queremos garantizar con probabilidad $0.95$ las galletas van a alcanzar. *¿Cuál deberia ser el stock?*

Tenemos $X_i$ independientes, entonces: 

$$
P\left( \sum^{n}_{i=1}X_{i}\leq Q \right)=0.95
$$

Para sacar la **media**, dividimos por $n$ y restamos por $\mu$

$$\begin{align}
P\left( \frac{\sum^{n}_{i=1}X_{i}}{n}-\mu\leq \frac{Q}{n}-\mu \right)\\\\ 
P\left(  \frac{\frac{\sum^{n}_{i=1}X_{i}}{n}}{\sqrt{\frac{\sigma^2}{n}}}-\mu\leq \frac{\frac{Q}{n}-\mu}{\sqrt{\frac{\sigma^2}{n}}} \right)
\end{align}


$$




