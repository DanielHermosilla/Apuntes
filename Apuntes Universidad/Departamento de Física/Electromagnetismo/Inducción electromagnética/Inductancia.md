
Podemos suponer dos espiras en el espacio: 

![[Pasted image 20231113092807.png|center]]


Sabemos que por [[Inducción Electromagnética|inducción electromagnética]] se tiene que:: 

$$\Phi_2=\int_{S_2}\vec{B_1}\cdot d\vec{s}$$

Además, al inducir la corriente, se induce una [[Fuerza electromotriz|fuerza electromotriz]] en la espira de arriba:

$$\epsilon=\frac{-d\Phi_2}{dt}$$

De tal forma, la espira de abajo se *"comunica"* con la de arriba al ir induciendo un [[Campo magnético|campo magnético]] variable.  Por ley de Biot-Savart: 

$$\begin{align}
\vec{B_1}&=\frac{\mu_0}{4\pi}I\int\frac{d\vec{l}\times\hat{r}}{(r-r')^2}
\end{align}$$

Notemos que el campo es proporcional con I, vale decir, $\vert\vec{B}\vert\sim I$. Por lo tanto, esta constante de proporcionalidad se denominará $M$. Así: 

$$\Phi_2=M_{21}I_1$$

Análogamente: 

$$\Phi_1=M_{12}I_2$$

Se puede llegar a demostrar que: 

$$\Phi_2=\left(\frac{\mu_0}{4\pi}\oint\oint\frac{d\vec{l_1}\cdot d\vec{l_2}}{(r-r')}\right)I_1$$

Y también se define la inductancia mutua: 

$$M_{21}=M_{12}\equiv M\tag{Inductancia mutua}$$

En resumen, se tienen las siguientes igualdades: 

$$\begin{align}
\Phi_2&=MI_1\\  \\
\Phi_1&=MI_2\\  \\
\epsilon_2&=-\frac{d\Phi_2}{dt}=-M\frac{dI_1}{dt}\\  \\
\epsilon_1&=-\frac{d\Phi_1}{dt}=-M\frac{dI_2}{dt}
\end{align}$$


También se define la autoinductancia como el flujo inducido por la espira en sí misma: 

$$\Phi=LI$$

Donde $L$ es la autoinductancia. Así, la expresión para la [[Fuerza electromotriz|fuerza electromotriz]] llegaría a ser: 

$$\epsilon=-\frac{d\Phi}{dt}=-L\frac{dI}{dt}$$

