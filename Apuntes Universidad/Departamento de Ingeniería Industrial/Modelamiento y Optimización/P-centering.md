
Corresponde a aquellos problemas de **[[Localización|localización]]** ($p$ lugares) al que para satisfacer la demanda hay que estar abierto (vale decir, se tiene que satisfacer **toda la demanda**). Las variables, por lo tanto, son **enteras**. Lo que se quiere minimizar es la **máxima distancia entre los consumidores**. 

En cuestión de variables se puede definir como: 

- $d_{ij}$: La distancia entre las localizaciones $i$ y $j$. 

- $x_{ij}$: Una indicatriz que determina si una persona va a demandar el servicio o no, es decir: 

$$x_{ij}=\begin{cases}1&\text{Si ocupa el servicio}\\  \\
0&\text{Si no}\end{cases}\;\land\;\sum^{}_{j\in J}x_{ij}=1$$

- $J$: El conjunto de posibles lugares a poner el servicio. 

- $y_j$: Una indicatriz si el lugar tiene espacio para hospedar (tiene *oferta*)

$$y_{j}=\begin{cases}1&\text{Si hay espacio}\\  \\
0&\text{Si no}\end{cases}\;\land\;\sum^{}_{j\in J}y_{j}=p$$

- $p$: La demanda total por los servicios 

