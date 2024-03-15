
Se puede tener una fuente de cargas eléctricas y, por ende, un [[Potencia eléctrica|potencial eléctrico]].

![[Captura de pantalla 2023-08-30 a la(s) 09.49.25.png|center]]

Sabemos que el potencial eléctrico está en función de: 

$$V(\vec{r})\sim\frac{1}{\vert\vec{r}-\vec{r'}\vert}$$

Si se hace una expansión: 

$$\begin{align}
\vert\vec{r}-\vec{r'}\vert&=r^2+r^{'2}-2rr'\cos\alpha\\  \\
&=r^2\left(1+(\frac{r'}{r})^2-2\frac{r'}{r}\cos\alpha\right)\tag{Teorema del coseno}
\end{align}$$

Luego, si se hace una **expansión de Taylor**: 

$$\begin{align}
\frac{1}{\vert r-r'\vert}=\frac{1}{r}\cdot\frac{1}{\left(1-2(\frac{r'}{r})\cos\alpha+\cancel{(\frac{r'}{r})^2}\right)^{\frac{1}{2}}}
\end{align}$$

Luego, si la fuente de carga $r'<<r$, notar que: 

$$\frac{1}{(1+x)^{\frac{1}{2}}}\sim 1-\frac{1}{2}x+\sigma(x^2)$$

Por lo tanto, aplicando lo mismo a la expresión que tenemos: 

$$\frac{1}{\vert r-r'\vert}\sim(\frac{1}{r})(1+\frac{r'}{r}\cos\theta+\sigma((\frac{r'}{r})^2)$$

Entonces, calculando el potencial del [[Departamento de Física/Métodos Experimentales/Circuitos eléctricos/Campo eléctrico|campo eléctrico]], se tiene que: 

$$V(\vec{r})=\frac{1}{4\pi\epsilon_0}\cdot\frac{1}{r^2}\hat{r}\cdot\int\vec{r'}\rho(\vec{r})dz$$

Esto es el potencial dipolar, donde $\hat{r}=\frac{r'}{r}$. Ahora, podriamos definir el **momento dipolar** como: 

$$\vec{p}=\int\vec{r'}\rho(\vec{r'})dz$$

Y se puede escribir el [[Trabajo del campo eléctrico|potencial]] dipolar en función del **momento dipolar**: 

$$V_{dip}(\vec{r})=\frac{\vec{p}\cdot\hat{r}}{4\pi\epsilon_0\cdot r^2}$$

>[!info] 
>
>Esto lo que dice, básicamente, es que al hacer una expansión de Taylor del trabajo eléctrico se obtiene los términos que representa un **monopolo**, **dipolo**, etc. 
>
>$$V\approx\frac{1}{4\pi\epsilon_0}\frac{1}{r}+\frac{1}{4\pi\epsilon_0}\frac{\vec{p}}{r^2}\hat{r}+\dots$$
>
>Donde el primer término corresponde al monopolo, el segundo al dipolo, y así sucesivamente. Notar que el dipolo está en función de $\vec{p}$, lo que se denomina **momento dipolar**: 
>
>$$\vec{p}=\int_N\rho(\vec{r}')\vec{r}'\;dz\;\iff\;\vec{p}=\sum^{N}_{i=1}q_i\vec{r_i'}$$

## Campo eléctrico  

Para calcular el campo eléctrico de un dipolo, donde se eligen coordenadas tal que $p$ es el origen y apunta en dirección $z$, entonces, sacando el [[Gradiente y plano tangente|gradiente]] del potencial para obtener el [[Departamento de Física/Métodos Experimentales/Circuitos eléctricos/Campo eléctrico|campo eléctrico]]: 

![[Captura de pantalla 2023-09-04 a la(s) 09.00.59.png|center|400]]


Se obtienen los siguientes campos eléctricos, a sabiendas que se están en [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Coordenadas esféricas|coordenadas esféricas]]:

$$\begin{align}
E_r&=-\frac{\partial V}{\partial r}=\frac{2p\cos\theta}{4\pi\epsilon_0 r}\\  \\
E_\theta&=-\frac{1}{r}\;\frac{\partial V}{\partial \theta}=\frac{p\sin\theta}{4\pi\epsilon_0 r^3}\\  \\
E_\phi&=-\frac{1}{r\sin\theta}\;\frac{\partial V}{\partial \phi}=0
\end{align}$$
## El sentido físico 

Si se hace el mismo análisis para la misma imagen anterior, nos podemos definir $d$ como la distancia entre las cargas puntuales y $\theta$ el ángulo entre ellas, entonces: 

$$V(\vec{r})=\frac{1}{4\pi\epsilon_0}\frac{qd\cos\theta}{r^2}$$

Haciendo despresaciones y cálculos parecidos a la parte anterior. Y por ende, el $\vec{p}$ se puede definir, para cargas puntuales, como: 

$$\vec{p}=\sum^{N}_{i=1}q_i\cdot\vec{r_i'}$$