
Las cargas eléctricas pueden ser positivas o negativas. Además, está **cuantizada**, es decir, son múltiplos entre sí: 

$$q=\pm Ne$$

Donde $e=1,6\times10^{-19}C$. El valor de $e$ está determinado por la carga de un electrón ($-e$) y de un [[Protones|protón]] $e$. 

El problema estándar es como estas cargas interactuan. Por lo tanto, primero se estudia el problema cuando las cargas fuertes están quietas. Es decir, **electrostática**. Si las cargas se movieran, los [[Departamento de Física/Métodos Experimentales/Circuitos eléctricos/Campo eléctrico|campos]] (o fuerzas) cambiarían, propagándose a la [[Rapidez de la luz|velocidad de la luz]] ($\approx 3\times 10^{8} ms^{-1}$. 

Por lo tanto, lo que se hace es el siguiente análisis: 

![[IMG_4DDF230A8A30-1.jpeg|center]]


Con simple suma de [[vectores]] se puede observar que: 

$$\begin{align}
\vec{r'}+\Delta\vec{r}&=\vec{r}\\  \\
\Delta\vec{r}&=\vec{r}-\vec{r'}
\end{align}$$

Por lo tanto, se postula la **ley de Coulomb**: 

$$\vec{F}=\frac{1}{4\pi\epsilon_0}\frac{qQ}{\vert\vert r-\vec{r'}\vert\vert^2}\cdot\frac{(\vec{r}-\vec{r'})}{\vert\vert \vec{r}-\vec{r}'\vert\vert}$$

Notar que: 

$$\frac{(\vec{r}-\vec{r'})}{\vert\vert \vec{r}-\vec{r}'\vert\vert}=\hat{r}$$

Es el vector unitario de $q$ a $Q$. Otras cosas a notar: 

- Si $qQ>0$,  $q$ y $Q$ tienen el mismo signo, es decir, las fuerzas es en la dirección en $\hat{r}$. 

- Si $qQ<0$, $q$ y $Q$ tienen distinto signo, fuerza en dirección $-\hat{r}$, es decir, es atractiva. 

- $\frac{1}{4\pi\epsilon_0}$ es una constante que depende del sistema de unidades, el $4\pi$ está ahí por conveniencia, y el $\epsilon_0$ es la **permeabilidad del vacio**, una constante. 

Por lo tanto, la versión *simplificada* de la **fuerza de Coulumb** sería la siguiente:

$$F=\frac{1}{4\pi\epsilon_0}\frac{qQ}{\varrho^2}\hat{r}$$

Si nos fijamos, se parece mucho a la [[Atracción gravitacional|atracción gravitacional]], de hecho, notemos que se pueden escribir como lo siguiente: 

$$\begin{align}
F_g&=\frac{Gm^2}{d^{2}}&\text{Fuerza de atracción} \\\\
F_c&=\frac{1}{4\pi\epsilon}\frac{e^2}{d^2}&\text{Repulsión}
\end{align}$$

Si vemos la escala de estas fuerzas, vale decir, $\frac{F_c}{F_g}$ el resultado es, aproximadamente, $10^{36}$ 