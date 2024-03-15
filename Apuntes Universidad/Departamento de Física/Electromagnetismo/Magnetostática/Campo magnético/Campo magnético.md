
En [[Fuerza electrostática|electrostática]] se tenía que la densidad superficial era constante, vale decir: 

$$\frac{\partial\rho}{\partial t}=0$$

En [[Magnetostática|magnetostática]] se llega que: 

$$\frac{\partial\vec{J}}{\partial t}=0$$

La fuente básica de $\vec{B}$ es un cable con [[Corriente eléctrica|corriente]]. Un esquema básico sería el siguiente: 

![[Captura de pantalla 2023-10-06 a la(s) 09.41.36.png|center]]

Por lo tanto, se postula la **ley de Biot-Savart**, donde. 

$$\begin{align}
\vec{B}(\vec{r})&=\frac{\mu_0}{4\pi}\int\frac{\vec{I}\times (\vec{r}-\vec{r'})}{\vert\vert\vec{r}-\vec{r'}\vert\vert^2}\;dl\\  \\
&=\frac{\mu_0 I}{4\pi}\int\frac{d\vec{l}\times(\vec{r}-\vec{r'})}{\vert\vert\vec{r}-\vec{r'}\vert\vert^2} 
\end{align}$$

Donde $\mu_0$ es la permeabilidad del espacio vacio. 

Otra cosa a notar es que el [[vectores|vector]] $\vec{B}$ en realidad no es el vector de campo magnético, si no más bien el **vector densidad de flujo magnético**. Sin embargo, ambas convenciones son aceptadas. Su unidad de medida es el Tesla $(T)$.  

#### Ejemplo: cable infinito con corriente 

Se tiene la siguiente configuración y se pregunta sobre el campo magnético sobre el punto $P$. 

![[Captura de pantalla 2023-10-11 a la(s) 08.39.26.png|center]]


Poniendo el origen en el eje $x$ donde parte la distancia $s$, es posible escribir la Ley de Biot-Savart en términos de $\theta$. 

![[Captura de pantalla 2023-10-11 a la(s) 08.41.06.png|center]]

Por lo tanto, se llega que: 

$$\begin{align}
d\vec{l}\times\hat{r}&=dl'\sin\alpha\;\hat{\xi}\tag{Dirección hacia adentro}\\  \\
&=dl'\cos\theta\;\hat{\xi}\\  \\
\frac{l'}{s}&=\tan\theta\\  \\
l'&=s\tan\theta\;\;\;\;\;\;(d\alpha)\\  \\
dl'&=\frac{s}{\cos^2\theta}d\theta
\end{align}$$

Por ende, 

$$\begin{align}
r\cos\theta&=s\\  \\
\implies\frac{1}{r^2}&=\frac{\cos^2\theta}{s^2}
\end{align}$$

Notemos que $\vec{B}$ va hacia afuera de la pantalla, por ende, aplicando la definición de la Ley de Biot-Savart: 

$$\begin{align}
B(s)&=\frac{\mu_0I}{4\pi}\int\left(\frac{s}{\cos^2\theta}d\theta\right)\cos\theta\cdot\frac{\cos^2\theta}{s^2}\\  \\
&=\frac{\mu_0I}{4\pi}\int\frac{1}{s}\cos\theta d\theta\tag{S es constante}\\  \\
B(s)&=\frac{\mu_0I}{4\pi}\cdot\frac{1}{s}\int\cos\theta d\theta
\end{align}$$

## Equivalencias 

Para corrientes $\vec{J}(r)$ y $\vec{K}(r)$ es posible también escribir la Ley de Biot-Savart: 

$$\begin{align}
\vec{B}(r')&=\frac{\mu_0I}{4\pi}\int\frac{\vec{J}\times\hat{r}}{r^2}dz'\\  \\
\vec{B}(r')&=\frac{\mu_0I}{4\pi}\int\frac{\vec{K}\times\hat{r}}{r^2}ds'
\end{align}$$

Notar que acá se ocupó la *notación Griffiths* para escribir la ley, donde $\hat{r}$ es la dirección del vector unitario, $r^2$ llegaría a ser el módulo de este vector al cuadrado. 

#### Ejemplo: campo magnético en una espira 

Se tiene la siguiente configuración: 

![[Captura de pantalla 2023-10-11 a la(s) 08.55.58.png|center]]

Hay que buscar el campo magnético a una altura $z$ de un anillo circular con corriente $I$. 

Notemos que por simetría, la única componente iría perpendicular al vector de posición en función del perímetro del anillo (fijarse en la figura). 

Haciendo trigonometría se llega fácilmente que el ángulo de arriba es $\theta$. Entonces, escribiendo la Ley de Biot-Savart: 

$$\begin{align}
\vert dl'\times\hat{r}\vert&=dl'\tag{Notación \textit{Griffiths}}\\  \\

\end{align}$$
Notar que se cumpel que $dl'\perp\hat{r}$. Entonces, tomamos sólo la proyección en $z$: 

$$\begin{align}
(dl'\times\hat{r})\cdot\hat{k}&=dl'\cdot\cos\theta
\end{align}$$

Es posible descomponer $r^2=R^2+z^2$. Entonces: 

$$\begin{align}
\vec{B}(p)&=\frac{\mu_0I}{4\pi}\int\frac{dl'\cos\theta}{r^2}\;\;\;\hat{k}\\  \\
&=\hat{k}\frac{\mu_0I}{4\pi}\frac{\cos\theta}{r^2}\cancelto{2\pi R}{\int dl'}\\  \\
\vec{B}(p)&=\frac{\mu_0I}{4\pi}\frac{R}{(R^2+z^2)^{3/2}}\hat{k}
\end{align}$$



