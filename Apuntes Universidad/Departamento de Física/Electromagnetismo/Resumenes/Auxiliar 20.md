
# Pregunta 1 

En un medio lineal caracterizado por una merbealidiad $\mu$ y permitividad $\epsilon$, el campo eléctrico de una onda plana toma la forma: 

$$\vec{E}(x,y,z,t)=Re\lbrace\;E_0\exp(iay+ibz-i\omega t)\;\rbrace$$
# Pregunta 2 

Una onda electromagnética tiene una frecuencia de $100MHz$ y se propaga en el vacío. El campo magnético viene dado por

$$\vec{B}(z,t)=B_0\cos(kz-\omega t)\;\hat{x}$$

Donde $B_0=10^{-8}T$

## Encontrar la frecuencia angular, longitud de onda y dirección de propagación 

Para la dirección de propagación, notemos que en una onda monocromática siempre se tiene algo de la siguiente forma: 

$$(\vec{k}\cdot\vec{r}-\omega t)$$

Si hacemos el análisis del producto punto: 

$$\begin{align}
\vec{K}\cdot\vec{r}&=Kz\\  \\
&=k\hat{z}\cdot z\hat{z}\tag{Dirección propagación}
\end{align}$$

Así, sabemos que la propagación va en $\hat{z}$. 

Ahora, para la frecuencia angular, sabemos que la relación entre $\omega$ y $f$ es: 

$$\omega=2\pi f=2\pi 100MHz=628,32M\frac{\text{rad}}{s}$$
Y, para la longitud de onda, se usa que: 

$$c=\lambda f=\frac{\omega}{k}\implies\lambda = 3m$$
## Encontrar el campo eléctrico 

Notemos que para encontrar $\vec{E}$ no hay corrientes libres (se ésta trabajando en el vacio). Y, usando la siguiente ecuación de Maxwell: 

$$\nabla\times\vec{B}=\mu_0\vec{J}+\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}$$

Pero, al no haber corrientes libres: 

$$\nabla\times\vec{B}=\cancelto{0}{\mu_0\vec{J}}+\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}$$

Otra cosa a notar es la siguiente relación: 

$$\begin{align}
\mu_0\epsilon_0&=\frac{1}{c^2}\\ \\
\implies\mu_0\epsilon_0\frac{\partial\vec{E}}{\partial t}&=\frac{1}{c^2}\frac{\partial\vec{E}}{\partial t}
\end{align}$$

Ahora, analizando el rotor $\nabla\times\vec{B}$: 

$$\begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
\partial_x & \partial_y & \partial_z \\
B_x(z) & 0 & 0
\end{bmatrix}=\frac{\partial B_x}{\partial t}\hat{y}=-B_0K\sin(Kz-\omega t)\;\hat{y}$$ 
Faltaría *"conectar"* ambas ecuaciones. Si integramos con respecto al tiempo para despejar $\vec{E}$:  

$$\begin{align}
\vec{E}(z,t)&=-B_0c(ck)\;\int\;dt\sin(kz-\omega t)\;\hat{y}\\  \\
&=-B_0c(ck)\frac{1}{\omega}\cdot\cos(kz-\omega t)\;\hat{y}
\end{align}$$

Por último, sabemos que se cumple la siguiente relación: 

$$c=\lambda f=\frac{\omega}{k}$$

Así, la ecuación queda: 

$$\begin{align}
\vec{E}(z,t)&=B_0c(\cancelto{\omega}{ck})\cos(kz-\omega t)\;\hat{y}\\ \\
&=-cB_0\cos(kz-\omega t)\;\hat{y}\\  \\
&=-3\cos(kz-\omega t)\;\hat{y}
\end{align}$$

## Vector de Poynting e intensidad de onda 

Para el vector de Poynting ocupamos la definición: 

$$\begin{align}
\vec{S}&=\vec{E}\times\vec{H}\\  \\
&=\frac{1}{\mu_0}\vec{E}\times\vec{B}\\  \\
&=-\frac{cB_{0}^{2}\cos^2(kz-\omega t)}{\mu_0}\;(\hat{y}\times\hat{x})\\  \\
&=\frac{cB_{0}^{2}\cos^2(kz-\omega t)}{\mu_0}\;\hat{z}\\  \\
&=3\times 10^8m/s (10^{-8}T)^2\frac{1}{4\pi\times 10^{-7}T \frac{m}{A}}\cos^2(kz-\omega t)\;\hat{z}\\  \\
&=2.4\times 10^{-2}\cos^2(kz-\omega t)\;\hat{z}\;\frac{W}{m^2}
\end{align}$$

Y, sabemos que la intensidad de onda es un promedio temporal (sobre un período). Por lo tanto: 

$$\begin{align}
I&=\vert\langle\vec{S}\rangle\vert_T\\  \\
&=\frac{1}{T}\int^{T}_{0}\;(2.4\times 10^{-2}\frac{W}{n^2})\hat{z}\;\cos^2(kz-\omega t)
\end{align}$$

Recordando que $T=1/f=2\pi/\omega$. La integral sobre $\cos^2$ sobre un período es igual a $1/2$. Así: 

$$\begin{align}
I&=\frac{1}{2}\left(2.4\times 10^{-2}\frac{W}{m^2}\right)\\  \\
&=1.2\times 10^{-2}\frac{J}{m^2}
\end{align}$$

# Pregunta 3 

La intensidad promedio de luz solar en la superficie terrestre es de $1.35\times 10^3\;W/m^2$. 

## Calcular la amplitud del campo eléctrico y magnético en la superficie de la Tierra 

Es posible escribir de la definición de $\vec{S}$: 

$$\begin{align}
I&=\frac{1}{2}\epsilon_0cE_{0}^{2}\\  \\
\implies E&=\sqrt{\frac{2I}{\epsilon_0 c}}\\  \\
&=1012.17\;\frac{V}{m}
\end{align}$$


Y, para ondas monocromáticas se tiene la relación: 

$$B_0=\frac{E_0}{c}$$

Así, reemplazando: 

$$\begin{align}
B_0&=3.37\times 10^{-6}\;T
\end{align}$$

## Potencia total irradiada por el sol a la distancia que está la tierra 

Por enunciado nos dicen que la distancia del Sol a la Tierra es $1.49\times 10^{11}m$. Así: 

$$\begin{align}
P_\text{sol}&=I4\pi d^2\\  \\
&=3.8\times 10^{26}W
\end{align}$$


## Potencia total recibida por la Tierra 

El Sol ve a la Tierra como un círculo de radio $R_T$. Así: 

$$\begin{align}
P_\text{tierra}&=I\cdot\pi R_{t}^{2}\\  \\
&=1.73\times 10^{17}\;W
\end{align}$$



# Pregunta 4 

La figura a continuación muestra una fibra óptica rodeada por un material de bajo índice de refracción, conocido como revestimiento. Encuentre el máximo ángulo de incidencia $\theta$, para que los rayos que inciden en la cara frontal del núcleo quedan atrapados dentro de él. Para esto considere que el aire tiene un índice de refracción igual a $1$. 

![[Pasted image 20231201094125.png|center]]

El indice de refracción de los tejidos de los mamíferos se puede medir utilizando un método de revestimiento de fibra óptica basado en la sustitución del revestimiento habitual por el tejido en estudio y utilizando el principio de reflexión interna total. Si se utiliza como fuente de luz un láser $He-Ne$, con una longitud de onda $632 nm$, un núcleo hecho de cuarzo fundido con índice de refracción $n_q=1457$ a $632nm$, y el semiángulo del cono de luz emergente de la salida de la fibra óptica es de $23,8\degree$. 

## Encontrar índice del refracción del tejido 

Ocupando la Ley de Snell en $P_1$: 

$$\begin{align}
n_a\sin(\theta_i)&=n_1\sin(\theta_t)\tag{1}
\end{align}$$

Por el otro lado, en $P_2$: 

$$n_1\sin(\theta_i')=n_2\sin(\theta_t')\tag{2}$$


Notar también que $\theta_t=90\degree-\theta_i'$. Así, de la Ley de Snell en $P_1$: 

$$\begin{align}
\sin(\theta_i)&=\sin(90\degree-\theta_i')\\  \\
\cos(\theta_i')&=\frac{n_a}{n_1}\sin(\theta_i)\tag{3}
\end{align}$$

Ahora, desde $(2)$: 

$$\sin(\theta_t')=\frac{n_1}{n_2}\sin(\theta_i')$$

Para que no haya una onda en el revestimiento, el ángulo $\theta_t'=90\degree$. Así, habría **reflexión total interna**. Así: 

$$\begin{align}
1&=\frac{n_1}{n_2}\sin(\theta_i')\\  \\
\implies\sin(\theta_i')&=\frac{n_2}{n_1}
\end{align}$$

Notar que $\forall\;\theta_i'>\theta_c'$ hay reflexión total interna. Así: 

$$\begin{align}
\cos(\theta_i')&\leq\cos(\theta_c')=\sqrt{1-\sin^2(\theta_c')}=\sqrt{1-\left(\frac{n_2}{n_1}\right)^2}
\end{align}$$

Ocupando $(3)$: 

$$\frac{n_a}{n_1}\sin(\theta_i)\leq\sqrt{1-\left(\frac{n_2}{n_1}\right)^2}$$

Así, despejando todo 

$$\sin(\theta_i)=\sqrt{n_{1}^{2}-n_{2}^{2}}$$

