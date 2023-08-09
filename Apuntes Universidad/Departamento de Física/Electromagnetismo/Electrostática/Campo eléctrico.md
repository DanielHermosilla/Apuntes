
Si nos fijamos en la [[Ley de Coulomb]], ésta se puede escribir como: 

$$\vec{F}=\frac{1}{4\pi\epsilon_0}\frac{qQ}{\vert\vert r-\vec{r'}\vert\vert^2}\cdot\frac{(\vec{r}-\vec{r'})}{\vert\vert \vec{r}-\vec{r}'\vert\vert}$$

Todo esto se puede poner en función de la carga de prueba, es decir: 

$$\vec{F}=Q\left[\frac{1}{4\pi\epsilon_0}\frac{q}{\vert\vert r-\vec{r'}\vert\vert^2}\cdot\frac{(\vec{r}-\vec{r'})}{\vert\vert \vec{r}-\vec{r}'\vert\vert}\right]$$

Entonces, se define el campo eléctrico como un campo [[vectores|vectorial]] definido en todo el espacio: 

$$\vec{E}(\vec{r})=\frac{1}{4\pi\epsilon_0}\frac{q}{\vert\vert r-\vec{r'}\vert\vert^2}\cdot\frac{(\vec{r}-\vec{r'})}{\vert\vert \vec{r}-\vec{r}'\vert\vert}$$

Haciendo aritmética simple, se puede relacionar las fuerzas y el campo eléctrico de la siguiente forma: 

$$\vec{F}(\vec{r})=Q\vec{E}(\vec{r})$$

Por lo tanto, la unidad de medida, o forma de verlo, es fuerza por unidad de carga.

### Ejemplo: Cargas puntuales 

Se tiene la siguiente configuración: 

![[IMG_B22B0FB3B139-1.jpeg|center|500]]

La carga eléctrica total, por el [[Principio de superposición|principio de superposición]] llegaría a ser: 

$$\vec{E}=\vec{E_1}+\vec{E_2}$$

Además, notamos lo siguiente: 

$$\begin{align}
\vec{r}&=z\hat{k}\\  \\
\vec{r_2'}&=\frac{d}{2}\hat{i}\\  \\
\vec{r_1'}&=-\frac{d}{2}\hat{i}
\end{align}$$

Por lo tanto, la suma de campos vectoriales sale por la [[Ley de Coulomb]]: 

$$\vec{E}=\frac{1}{4\pi\epsilon}\frac{q}{\vert\vert z\hat{k}+\frac{d}{2}\hat{i}\vert\vert^3}(z\hat{k}+\frac{d}{2}\hat{i})+\frac{1}{4\pi\epsilon}\frac{q}{\vert\vert z\hat{k}-\frac{d}{2}\hat{i}\vert\vert^{3}}(z\hat{k}-\frac{d}{2}\hat{i})$$

Además notamos que: 

$$\vec{E}=\cancelto{0}{E_x\hat{i}}+\cancelto{0}{E_y\hat{j}}+E_z\hat{k}$$ 
Pero, la forma más simple es hacerlo con geometría: 

![[IMG_C4C906F5EF52-1.jpeg|center|500]]

Donde la distancia puede salir con [[Teorema de Pitágoras|pitágoras]] y se hace una descomposición de [[vectores]]. Finalmente se llega que: 

$$E_z=\frac{1}{4\pi\epsilon}\frac{2qz}{\left(z^2+\frac{d^2}{4}\right)^{\frac{3}{2}}}$$

### Ejemplo: Distribución lineal de cargas 

Se tiene una distribución uniforme de carga lineal entre $-L$ y $L$ en el eje x, con densidad uniforme. La densidad llegaría a ser $\lambda = \frac{C}{m}$. 

![[lineal 1.jpeg|center|500]]

Por lo tanto, la carga total llegaría a ser: 

$$q=\int^{L}_{-L}\lambda dx=2L\cdot\lambda$$

Para ver el campo eléctrico, se tiene una **integral de linea**, entonces: 

$$\vec{E}(\vec{r}=z\hat{k})=\frac{1}{4\pi\epsilon}\int^{L}_{-L}\frac{(\lambda dx')}{\vert\vert z\hat{k}-x'\hat{i}\vert\vert^3}(z\hat{k}-x'\hat{i})$$

Los vectores de posición se sacan a través del siguiente análisis: 
   
![[IMG_E4A8ABDBCEF2-1.jpeg|center|550]]

Por lo tanto, la integral sería doble, una en $\hat{k}$ y $\hat{i}$. Pero por simple geometría sabemos que la [[Integral de Riemann|integral]] en $\hat{i}$ es 0. De hecho se puede ver que: 

$$E_x=\frac{-\lambda}{4\pi\epsilon_0}\int^{L}_{-L}\frac{x'}{(z^2+x'^2)^{\frac{3}{2}}}dx'$$

```functionplot
---
title: Campo en x
xLabel: x
yLabel: z
bounds: [-3, 3, -3, 3]
disableZoom: true
grid: true
---
f(x)=x/((0.4^2+x^2)^(3/2))
```


Como es impar, va a ser cero. Pero, para el eje $\hat{k}$: 

$$E_z=\frac{\lambda z}{4\pi\epsilon_0}\int^{L}_{-L}\frac{dx'}{(z^2+x'^2)^{\frac{3}{2}}}=\frac{\lambda 2L}{4\pi\epsilon_0}\frac{1}{z(z^2+L^2)^{\frac{1}{2}}}\hat{k}$$

Analizando los límites, por ejemplo si $z\to\infty$, se puede ver que se llega a lo siguiente: 

$$\lim_{z\to\infty}E_z=\frac{\lambda 2L}{4\pi\epsilon_0}\cdot\frac{1}{z^2}$$

### Ejemplo: Distribución de carga superficial 

Se tiene un disco con densidad superficial $\sigma=\frac{c}{m^2}$ y radio $R$

![[IMG_3C141247250C-1.jpeg|center|500]]


Se sabe que la carga es: 

$$q=\pi r^2\sigma=\int^{2\pi}_{0}\int^{R}_{0}\sigma ds$$

Donde $ds=rd\phi dr$. Por lo tanto, escribiendo el campo eléctrico: 

$$\vec{E}=\frac{1}{4\pi\epsilon_0}\int^{2\pi}_{0}\int^{R}_{0}\frac{\sigma ds'}{\vert\vert z\hat{k}-r\hat{r}\vert\vert^3}(z\hat{k}-r\hat{r})$$

Sabiendo el cambio de variable de $ds$, entonces la integral llegaría a ser: 


$$\vec{E}=\frac{1}{4\pi\epsilon_0}\int^{2\pi}_{0}\int^{R}_{0}\frac{\sigma r\;d\phi\; dr}{\vert\vert z\hat{k}-r\hat{r}\vert\vert^3}(z\hat{k}-r\hat{r})$$

Si pasamos esto a coordenadas normales se llega que $\hat{r}=\cos\phi\hat{i}+\sin\phi\hat{j}$. Ahí se llegaría que la integral estaría en tres dimensiones:

$$\vec{E}=\frac{1}{4\pi\epsilon_0}\int^{2\pi}_{0}\int^{R}_{0}\frac{\sigma r\;d\phi\; dr}{\vert\vert z^2-r^2\vert\vert^{\frac{3}{2}}}(z\hat{k}-r(\cos\phi\hat{i}+\sin\phi\hat{j}))$$

Notar que $\hat{i}$ y $\hat{j}$ se anulan por ser funciones sinusoidales. La integral a calcular sería la del eje en $z$. 

$$E_z=\frac{\sigma z}{4\pi\epsilon_0}\int^{2\pi}_{0}\int^{R}_{0}\frac{r\;dr\;d\phi}{(z^2+r^2)^{\frac{3}{2}}}=\frac{\sigma}{2\epsilon_0}\left(\frac{z}{\vert z\vert}-\frac{z}{(z^2+R^2)^{\frac{1}{2}}}\right)\hat{k}$$