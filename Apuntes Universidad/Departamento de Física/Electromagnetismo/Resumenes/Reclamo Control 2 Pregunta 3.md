
Estimada Valeria, 

Junto con saludar, me gustaría reclamar en la tercera pregunta del segundo Control. 

## Inciso A 

Antes que nada mencionar el error que tuve que fue penalizado correctamente. Al calcular el campo magnético en el espacio ocupé la Ley de Ampere donde establecí que 

$$\begin{align}
\oint B\;dl&=\mu_0I_\text{enc}\\  \\
B\cdot2\pi r&=\mu_oI_\text{enc}
\end{align}$$

Mi error subyace al haber considerado que el cable infinito tenía un radio, así, plantié erroneamente que: 

$$\begin{align}
K&=\frac{dI}{dl}\\  \\
\implies I_\text{enc}&=I\;2\pi R
\end{align}$$

Con $R$ siendo el radio del cable. Notemos que mi error fue muy estupido, porque pensé que la imagen del enunciado indicaba que se tenía la corriente $I$ multiplicada por su distribución de largo (que comunmente se le denomina $k$, de ahí subyace mi error de confundir $\hat{k}$ con $k$ 🥲). 

Así, juntando todo, llegué que la expresión para el campo eléctrico era 

$$B=\frac{I\mu_0R}{r}\;\hat{\theta}$$

Notemos que a pesar del error, se tiene un resultado muy parecido al de la pauta. Ambos difieren por una constante, de hecho, notemos que al buscar el lugar geométrico con campo nulo son equivalentes: 

> *Desarrollo de la pauta:*
> $$\begin{align}
0&=-\frac{\mu_0I}{2\pi(d-r)}+\frac{\mu_0I}{2\pi r}+\frac{\mu_0I}{2\pi(d + r)}\\  \\
&=\frac{\mu_0}{2\pi}\left(-\frac{1}{d-r}+\frac{1}{d}+\frac{1}{d+r}\right)\\  \\
&=-\frac{1}{d-r}+\frac{1}{r}+\frac{1}{d+r}
\end{align}$$

Por el otro lado en mi desarrollo se llega a lo siguiente: 

$$\begin{align}
0&=\frac{I\mu_0 R}{d-r}+\frac{I\mu_0R}{r}+\frac{I\mu_0R}{r+d}\\  \\
&=R\mu_0\left(\frac{1}{d-r}+\frac{1}{d}+\frac{1}{d+r}\right)\\  \\
&=\frac{1}{d-r}+\frac{1}{d}+\frac{1}{d+r}
\end{align}$$

Aquí cometí otro error pequeño que fue *"comerme un signo"*, básicamente se me olvido imponer el signo menos para el primer sumando. De tal forma, a pesar de haber tenido un buen planteamiento, llegué a un resultado distinto

Así, de los $4$ puntos correspondientes a la primera parte, se me otorgaron $2,8$. Siento que por estos dos errores chicos (error de signo y considerar el cable radial (que a priori no afecta los calculos como tal)) se me podría descontar un poco menos. 

## Inciso B 

Notemos que mi esquema de lineas se asimila al de la pauta:

![[Pasted image 20231213180047.png|center|400]]

![[Pasted image 20231213180113.png|center|400]] 


Se puede ver que la diferencia entre ambos esquemas subyacen en que dibujé mis lineas de campo como vectores, cuando en realidad había que hacerlo como líneas continuas (dado que $\vec{\nabla}\cdot\vec{B}=0$). Por el otro lado, la descripción que hice sobre el campo magnético es completa y da a entender que domino el tema. 

Considerando que mi único error fue haber puesto las líneas de forma discontinua, considero que se me podría asignar un poco más de puntaje que $0.3/1$. 

## Inciso c 

En este inciso no pude terminar mi desarrollo por temas de tiempo. No obstante, creo que a lo que yo llegué podría ameritar algo mas de $0.1$ puntos. 

Notemos que la pauta dice lo siguiente: 

>*Sobre el cable central consideramos el campo producido por los otros dos cables, con el cable central en $y$ como en la figura*: 
>
>$$\begin{align}
\vec{B_1}&=-\frac{\mu_0I}{2\pi(d-r)}\hat{i}\\  \\
\vec{B_3}&=\frac{\mu_0I}{2\pi(d+r)}\hat{i}\\ \\
I&=-I\hat{k}\\  \\
\implies\frac{\vec{F}}{L}&=\vec{I}\times\vec{B_1}+\vec{I}\times\vec{B_3}\tag{1}
\end{align}$$

Ahora, si vemos mi desarrollo, es posible ver que yo llegue a algo muy análogo: 

$$\begin{align}
\vec{B}&=\frac{I\mu_0R}{d-r}+\frac{I\mu_0R}{d+r}\;\hat{\phi}\tag{Error de arrastre}\\  \\
&=I\mu_0R\left(\frac{1}{d-r}+\frac{1}{d+r}\right)\hat{\phi}\\  \\
\implies\frac{\vec{F}}{L}&=I\int dl\times B\tag{2}
\end{align}$$

Notemos que también cometí un pequeño error dado que se me olvidó cancelar el diferencial de largo que pasé dividiendo para tener la fuerza por unidad de largo. No obstante, si se corrige esto, de $(2)$ se llega directamente a la expresión que se tiene en $(1)$. 

Considerando esto, siento haber planteado correctamente el problema e identificar el camino de éste. Sin embargo, por temas de tiempo no pude seguir con éste. 

Por lo anterior, creo poder rescatar algo más de puntaje en vez de tener únicamente $0.1/1$. A sabiendas que mi desarrollo está incompleto, creo poder obtener un poco más de $0.1$ puntos. 

## Recapitulación 

En el primer inciso cometí dos errores que llevaron a un error de arrastre: 
- Me equivoqué por una constante 
- Error de signo 

Por tales razones, creo poder obtener más de $2.8/4$ puntos dado que mi desarrollo muestra que dominaba la materia. 

Por el otro lado, en el segundo inciso fallé en poner las lineas de campo continua. Por tal error creo poder obtener una mayor asignación de puntaje que $0.3/1$. 

Por último, en la última parte hice un planteamiento correcto del problema e iba bien encaminado. Sin embargo, entregué el desarrollo incompleto que no alcancé a terminar por temas de tiempo. De haber *"matraqueado"* más se hubiera llegado a la respuesta o algo similar (considerando que venía teniendo un error de arrastre de signo del primer inciso). Así, creo merecer un poco más de $0.1/1$ puntos. 

Aprovecho de agradecer por la buena disposición por la recorrección, agradezco y reconozco mucho el esfuerzo. Que tengas un buen fin de semestre :) 
