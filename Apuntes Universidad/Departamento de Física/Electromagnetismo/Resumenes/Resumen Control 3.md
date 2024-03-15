
# Inducción Electromagnética 

Podriamos suponerque tenemos dos *loops* de un cable. Sabemos que si hacemos pasar una corriente $I_1$ por un loop de cable se produce un campo magnético $B_1$ que interactua con el segundo loop: 

![[Pasted image 20231125092946.png|center|450]]


Si se quisiera calcular el campo magnético tendríamos que darnos cuenta de una cosa fundamental:

- El campo magnético es **proporcional a la corriente producida** 

Así, para poder calcular las líneas de campo que pasan por el segundo loop se postula la siguiente ecuación: 

$$\begin{align}
\Phi_2&=\int B_1\cdot da_2\\  \\
\Phi_2&=M_{21}I_1 
\end{align}$$

Acá se define una variable nueva denominada **inductancia mutua**, que actúa como una constante de proporcionalidad: 

>[!danger] Inductancia mutua $M$
>
>En el contexto del electromagnetismo, sabemos que el campo magnético ($\vec{B}$) generado por una corriente es proporcional a esa corriente. Sin embargo, cuando tenemos múltiples circuitos en proximidad, la relación entre sus campos magnéticos y corrientes se vuelve más intrincada.
>
>La inductancia mutua es, esencialmente, una medida de cómo la corriente en un circuito puede afectar la corriente inducida en otro circuito cercano. Su magnitud y signo revelan la dirección y la fuerza de esta influencia magnética entre los circuitos. Esta conceptualización resulta fundamental en el diseño y análisis de sistemas electromagnéticos complejos, proporcionando una herramienta valiosa para entender y optimizar la transferencia de energía y la interacción magnética en dispositivos electrónicos y sistemas de comunicación.
>
>Es posible expresarla gracias al teorema de Stokes y el **vector potencial**. Su resultado final se expresa como sigue: 
>
>$$M_{21}=\frac{\mu_0}{4\pi}\oint\oint\frac{dI_1\cdot dI_2}{(\vec{r}-\vec{r'})}$$
>
>Este valor se conoce como la **fórmula de Neumann**. 
>
>Algunas cosas interesantes a considerar son las siguientes: 
>
>- $M$ es una cantidad geométrica que está relacionado a la forma y tamaño de los distintos loops. 
>  
>  - Se tiene una especie de simetría donde $M_{21}=M_{12}$


Ahora, saliéndonos de la magnetostática, podríamos suponer que se hace variar la corriente del primer loop. La ley de Faraday dice que un campo que varía va a inducir una fuerza electromotriz, determinada por la siguiente ecuación: 

$$\upvarepsilon_2=-\frac{d\Phi_2}{dt}=-M\frac{dI_1}{dt}\tag{Ley de Lenz}$$

El resultado más importante a notar aca subyace de la última igualdad: **al variar la corriente del primer loop se induce una corriente en el segundo loop a pesar de no existir ninguna conexión física entre ellas**. De hecho, una corriente alterna no sólo induce una fuerza electromotriz en loops cercanos, si no también en sí misma: 

$$\Phi=LI$$

Así, se introduce a la constante de proporcionalidad **$L$** como **inductancia propia** o simplemente **inductancia**. Así, **la fuerza electromotriz propiamente inducida** se define como: 

$$\upvarepsilon=-L\frac{dI}{dt}$$ 

La inductancia al igual que la capacitancia es intrínsecamente una cantidad positiva. La ley de Lenz impone un signo menos que dice que la dirección de la fuerza electromotríz va en sentido opuesto a la corriente del cable: cuando se trata de alterar la corriente de un cable se debe *peliar* contra la fuerza electromotriz propia. 

## Ecuaciones de Maxwell 

Anteriormente por la electrostática y magnetostática se llegaron a ecuaciones fundamentales a través de la Ley de Gauss y Ampere respectivamente. Al combinar todas las ecuaciones y ocupar la de la continuidad se llega a las siguientes igualdades: 

$$\begin{align}
\nabla\cdot E&=\frac{1}{\epsilon_0}\rho\tag{Ley de Gauss}\\  \\
\nabla\cdot B&=0\\  \\
\nabla\times E&=-\frac{\partial B}{\partial t}\tag{Ley de Faraday}\\  \\
\nabla\times B&=\mu_J\tag{Ley de Ampere}
\end{align}$$


Resulta que al aplicar la segunda ecuación con la primera **se llega a una inconsistencia**. De hecho, al aplicar la Ley de Ampere a una intensidad de corriente variable se llega que el campo depende de la superficie elegida. Así,  **Maxwell arregló la Ley de Ampere al ocupar la ecuación de la continuidad**. Se llega a lo siguiente: 

$$\nabla\times B=\mu_0J+\mu_0\epsilon_0\frac{\partial E}{\partial t}$$

Así, se llega a la gran conclusión que **un campo eléctrico variable produce un campo magnético**. Este término extra se llama **corriente de desplazamiento**. 

$$J_d\equiv\epsilon_0\frac{\partial E}{\partial t}$$


## El vector de Poynting 

Anteriormente en electrostática se había llegado que el trabajo necesario para tener una distirbución de carga estática es: 

$$W_e=\frac{\epsilon_0}{2}\int E^2\;d\tau$$

Nuevamente, si ahora lo relacionamos con el concepto de la **corriente autoinducida**, el trabajo necesario para mover las cargas que van en contra de una fuerza electromotriz es: 

$$W_m=\frac{1}{2\mu_0}\int B^2\;d\tau$$

Con esto se llega que **la energía total en un campo electromagnético es**: 

$$u=\frac{1}{2}\left(\epsilon_0E^2+\frac{1}{\mu_0}B^2\right)$$

Si juntamos esto con la definición de fuerza electromagnética se llega a la definición del vector de Poynting: 

>[!error] Vector de Poynting 
>Vector utilizado para describir la dirección y flujo de energía electromagnética en un campo electromagnético. Subyace principalmente del siguiente desarrollo: 
>
>$$S=E\times B$$
>
>Donde se llega a su definición fundamental: 
>$$S=\frac{1}{\mu_0}(E\times B)$$
>
>Donde $S\cdot da$ se define como la energía por unidad de tiempo a través de una superficie. 


A partir de esto es razonable preguntarse sobre la proposición de magnetostática: 

>*"El campo magnético no hace trabajo"*

Sin embargo, todas las situaciones en la vida real involucran cargas en movimiento, donde se produce una fuerza electromotriz por una variación de campo magnético. El trabajo del campo magnético que conocemos en realidad es un trabajo hecho por la **variación del campo**. 

# Ondas electromagnéticas 

Como introducción al tema es importante preguntarse: *¿qué es en realidad una onda?* Es un concepto muy abstracto cada vez que se trata de ahondar, pero se puede describir facilmente en palabras como: 

>*"Una perturbación de un medio continuo que se propaga con una forma regular a velocidad constante"*

Aunque la definición cae un poco corta: en presencia de absorción la onda va a disminuir su amplitud, o que las frecuencias son distintas a medida que van en distintas dimensiones y así sucesivamente. 

Una onda se puede expresar matemáticamente por la siguiente función matemática: 

$$f(z,t)=f(z-vt,0)=g(z-vt)$$

Donde $g(z)=f(z,0)$, vale decir, **la forma original de la onda**. Así, la función $f$ se lee como el punto de la onda en función del tiempo $t$ y posición $z$: 

![[Pasted image 20231126210820.png|center|550]]

De hecho, es natural preguntarse por qué una cuerda tiene un comportamiento al de una onda. Esto nace principalmente de la segunda Ley de Newton cuando una tensión es sacada del equilibrio: 

$$\Delta F=T\sin\theta'-T\sin\theta$$

Donde $\theta'$ es el ángulo que hace la cuerda en la dirección de $z$ en el punto $z+\Delta z$. 

![[Pasted image 20231126211120.png|center|520]]


Al hacer un análisis trigonométrico y una expansión en series de Taylor se llega a la siguiente igualdad: 

$$\frac{\partial^2f}{\partial z^2}=\frac{\mu}{T}\frac{\partial^2f}{\partial t^2}$$

Esa ecuación diferencial es la motivación a lo que se le conoce como **la ecuación fundamental de la onda**, que para cada perturbación se cumple que: 

$$\frac{\partial^2 f}{\partial z^2}=\frac{1}{v^2}\frac{\partial^2f}{\partial t^2}\tag{Ecuación de onda}$$

Donde $v$ es la velocidad. 

## Ondas sinusoidales 

De todas las formas posibles de onda, la más importante y representativa es la sinusoidal: 

$$f(z,t)=A\cos[k(z-vt)+\delta]$$

![[Pasted image 20231126211452.png|center|540]]


De esta ecuación es importante reconocer y definir algunos elementos: 

- **Amplitud ($A$)**: La máxima distancia de la posición de equilibro con el *peak* de la onda. 

- **Fase ($\delta$)**: Es el argumento del coseno, el término $\delta$ es conocido como **constante de fase** que representa el desplazamiento horizontal de la onda. 

- **Número de onda ($k$)**: Representa una relación aritmética con la longitud de onda ($\lambda$):

$$\lambda=\frac{2\pi}{k}$$

- **Período ($T$)**: Se define como el tiempo en hacer una oscilación: 

$$T=\frac{2\pi}{kv}$$

- **Frecuencia**: Es el inverso del período - el número de oscilaciones por unidad de tiempo: 

$$f=\frac{1}{T}=\frac{v}{\lambda}$$

- **Frecuencia angular ($\omega$)**: Es la convención más utilizada para hablar de frecuencia, dado que representa el número de radianes recorridos por unidad de tiempo: 

$$\omega=2\pi f=kv$$


De hecho, es más conveniente escribir la onda sinusoidal en términos de la frecuencia angular: 

$$f(z,t)=A\cos(kz-\omega t+\delta)$$


Por último notar el signo que acompaña a la frecuencia angular. Cuando viaja hacia la izquierda le acompaña un signo positivo y viceversa. 

## Ondas electromagnéticas en el vacio 

Notemos que de las ecuaciones de Maxwell se puede llegar a la ecuación de onda al manipularlas. De hecho, para el campo magnético y eléctrico se tiene lo siguiente: 

$$\begin{align}
\nabla^2E&=\mu_0\epsilon_0\frac{\partial^2E}{\partial t^2}\\  \\
\nabla^2B&=\mu_0\epsilon_0\frac{\partial^2B}{\partial t^2}
\end{align}$$

Por lo general, la ecuación de onda sinusoidal del campo eléctrico y magnético van en direcciones contrarias. Así, se tienen cosas del siguiente estilo: 

$$\begin{align}
E(z,t)&=E_0\cos(kz-\omega t+\delta)\hat{x}\\  \\
B(z,t)&=\frac{1}{c}E_0\cos(kz-\omega t+\delta)\hat{y}
\end{align}$$

![[Pasted image 20231126215826.png|center|550]]


## Energía en ondas electromagnéticas 

Al igual que en el capítulo anterior, se introduce el concepto de **vector de Poynting** pero para las ondas electromagnéticas. La definición es la misma pero se reemplaza el campo eléctrico y magnético por la definición de onda: 

$$\begin{align}
S&=\frac{1}{\mu_0}(E\times B)\\  \\
S&=c\epsilon_0E^2\cos^2(kz-wt+\delta)\hat{z}\\  \\
S&=cu\hat{z}
\end{align}$$

De hecho, otro resultado interesante de esto es que las ondas electromagnéticas **también tienen un momentum asociado**. La densidad de momentum para cualquier densidad de campo se define como: 

$$g=\frac{1}{c^2}S$$

Así, haciendo el cálculo análogo que se hizo en la parte anterior, se llega que: 

$$g=\frac{1}{c}u\hat{z}$$


## Presión de radiación 

Dado que las ondas poseen energía, es posible calcular el valor promedio que hace una onda por período y extrapolarlo a $S$ y $g$ (dado que ambos dependen de la energía $u$)

$$\begin{align}
\langle u\rangle&=\frac{1}{2}\epsilon_0E_{0}^{2}\\ \\
\langle S\rangle&=\frac{1}{2}c\epsilon_0E_{0}^{2}\;\hat{z}\\  \\
\langle g\rangle&=\frac{1}{2c}\epsilon_0E_{0}^{2}\;\hat{z}
\end{align}$$

Estos valores se obtienen al saber que en un ciclo el valor promedio del coseno es $1/2$. Así, se puede definir la **intensidad** como la energía promedio por una onda: 

$$I=\langle S\rangle=\frac{1}{2}c\epsilon_0E_{0}^{2}$$ 
Cuando una onda de luz es absorbida, transfiere su momentum a la superficie. Así, también se puede definir la presión de radiación promedio en un tiempo $\Delta t$ como: 

$$\begin{align}
P&=\frac{1}{A}\frac{\Delta p}{\Delta t}
\\  \\
&=\frac{I}{c}\end{align}$$

Donde $\Delta p=\langle g\rangle Ac\Delta t$. 