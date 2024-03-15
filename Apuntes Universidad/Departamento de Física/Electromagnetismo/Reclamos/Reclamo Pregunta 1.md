
En el final del documento se encontrará las fotos de mi desarrollo. De igual forma, para mejorar la claridad, voy a escribir mi desarrollo y enunciado de forma digital. Al final del documento, en la sección `Reclamo` estará mi reclamo. 

También mencionar que mi reclamo será en base a la pauta del auxiliar y el profesor. 
## Enunciado 

Dos varillas delgadas idénticas con una longitud $2a$ tienen cargas iguales $Q$ uniformemente distribuidas a lo largo de sus longitudes. Las varillas yacen a lo largo del eje $x$, con sus centros separados por una distancia $b>2a$. Calcule la magnitud de la fuerza ejercida por la varilla izquierda sobre la derecha. 
###  Desarrollo: 

Para calcular la fuerza **ejercida** por la varilla izquierda hay que fijarnos en el campo hecha por aquella barra. 

Sabemos que $\vec{F}=Q\vec{E}$

Por simetría, se tiene que el campo eléctrico va en $\hat{x}$

Notar que, la barra al tener logitud $2a$, me puedo definir su distribución de carga superficial como: 

$$\sigma_B=\frac{Q}{2a}$$

Antes de calcular el campo eléctrico me definiré mi vector $\vec{r}$ y $\vec{r'}$: 

$$\begin{align}
\vec{r'}&=x'\hat{x}\;\;\;\;x'\in [b,b+2a]\\  \\
\vec{r}&=x\hat{x}\;\,\;\; x\in [0,2a]
\end{align}$$

Notemos que desplazé mi punto de referencia en $-a\hat{x}$. Entonces: 

$$\begin{align}
\vec{E}(x)&=\frac{1}{4\pi\epsilon_0}\int^{b+2a}_{b}\frac{\vec{r}-\vec{r'}}{\vert\vert\vec{r}-\vec{r'}\vert\vert^2}\sigma_b\;dx'\\  \\
&=\frac{1}{4\pi\epsilon_0}\cdot\sigma_B\int^{b+2a}_{b}\frac{x-x'}{x^2+x'^2}\;dx'\\  \\
&=\frac{1}{4\pi\epsilon_0}\cdot\sigma_B\left[\int^{b+2a}_{b}\frac{x}{x^2+x'^2}dx'-\int^{b+2a}_{b}\frac{x'}{x^2+x'^2}dx'\right]
\end{align}$$

Por temas de claridad, $u=x'$

$$I_1=x\int^{b+2a}_{b}\frac{1}{x^2+u^2}du$$

Por formulario 

$$\begin{align}
I_1&=x\left[\frac{1}{x}\tan^{-1}(\frac{u}{x})\bigg\vert^{b+2a}_{b}\right]\\  \\
&=\tan^{-1}\left(\frac{b+2a}{x}\right)-\tan^{-1}\left(\frac{b}{x}\right)
\end{align}$$

Además, 

$$\begin{align}
I_2&=\int^{b}_{b+2a}\frac{u}{x^2+u^2}
\end{align}$$

Integrando por partes: 

$$\begin{align}
h&=u\implies dh=du\\  \\
v&=\frac{1}{x}\tan^{-1}\left(\frac{u}{x}\right)\implies dv=\frac{1}{x^2+u^2}
\end{align}$$

Así, 

$$\begin{align}
I_2&=\frac{u}{x}\tan^{-1}\left(\frac{u}{x}\right)\bigg\vert^{b}_{b+2a}-\int^{b}_{b+2a}\frac{1}{x}\tan^{-1}\left(\frac{u}{x}\right)\;du\\  \\
&=\frac{1}{x}\left[b\tan^1\left(\frac{b}{x}\right)+(b+2a)\tan^{-1}\left(\frac{b+2a}{x}\right)\right]+\frac{1}{x^2+u^2}\bigg\vert^{b+2a}_{b}
\end{align}$$

Volviendo a juntar las integrales 

$$\begin{align}
\vec{E(x)}&=\frac{\sigma_B}{4\pi\epsilon_0}\bigg[\tan^{-1}\left(\frac{b+2a}{x}\right)-\tan^{-1}\left(\frac{b}{x}\right)-\frac{2a}{x}\tan^{-1}\left(\frac{b+2a}{x}\right)\\ \\ 
&+\frac{1}{x^2+(b+2a)^2})-\frac{1}{x^2+b^2}\bigg]\end{align} $$

Por lo tanto, 

$$\vec{F}=Q\vec{E}$$

Y como 

$$\sigma_B=\frac{Q}{2a}$$

$$\begin{align}
\vec{F}(x)&=\frac{Q^2}{8\pi\epsilon_0}\left[\tan^{-1}\left(\frac{b+2a}{x}\right)\left(1-\frac{2a}{x}\right)-\tan^{-1}\left(\frac{b}{x}\right)+\frac{1}{x^2+(b+2a)^2}-\frac{1}{x^2+b^2}\right]\hat{x}\\  \\
x&\in(0,2a)
\end{align}$$

Notemos que, como ambas cargas son positivas la fuerza es de repulsión, es decir, la fuerza apunta en $-\hat{x}$.

## Imagen del desarrollo 

![[Pasted image 20231118183437.png|center]]

![[Pasted image 20231118183502.png|center]]

![[Pasted image 20231118183533.png|center]]

![[Pasted image 20231118183624.png|center]]

## Reclamo 

Estimado equipo docente, junto con saludar, agradezco de antemano la disposición de cada uno de ustedes por recibir mi reclamo y ser proactivos en este tema. 

Para tener consistencia con la corrección, me voy a fijar en la asignación de puntajes que se encuentra en la pauta de Alejandro. Voy a tratar de argumentar bajo aquella pauta por qué creo que merezco puntaje en ciertas secciones. 

Para todo lo relacionado a la asignación de puntaje para el cálculo del campo eléctrico estoy de acuerdo. Siento que la asignación es justa, considerando los errores que tuve. 

No obstante, me gustaría referirme al último ítem de fuerzas, 