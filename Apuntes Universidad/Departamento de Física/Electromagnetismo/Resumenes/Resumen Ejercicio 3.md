
# Corrientes eléctricas

La corriente eléctrica se define como la carga en movimiento. Esta se define en ampere's, equivalente a $C/s$. 

Aun así, un tema más abstracto es aquel que hace referencia a la **densidad de corriente**, donde se consideran cantidades promediadas. 

Si definimos el aporte de cada electrón en una superficie es posible describir **la densidad de corriente superficial**, que está otorgada por la siguiente igualdad: 

$$\vec{J}=\rho\vec{V}$$

Donde se puede llegar a la corriente al integrar: 

$$I=\int_SJ\cdot da$$

Se dice que la corriente es estacionaria cuando $J$ no varía en el tiempo, vale decir, $\nabla\cdot J=0$. 

## Ley de Ohm 

Para hacer que las cargas fluyan es necesario *empujarlas*. Qué tan rápido se mueven dependen del material, aunque para la mayoría de estos son proporcionales a la fuerza por unidad de área: 

$$J=\sigma f$$

Para muchos casos, la fuerza que va a mover las cargas son las fuerzas **electromagnéticas**, vale decir, es posible expresar $J$ como: 

$$J=\sigma(E+v\times B)$$

Ordinariamente, la velocidad de las cargas es tán chica, que es posible ignorar el segundo término, así llegando a una fuerza **proporcional a la eléctrica**: 

$$J=\sigma E$$

Es contraintuitivo, ya que por lo general uno piensa que la carga eléctrica dentro del conductor es nula. Aun así, hace sentido ya que esa afirmación no corresponde a la **carga en movimiento**. 

A partir de la definición de $J$ es posible llegar a la Ley de Ohm, donde: 

$$V=IR$$

Aunque esa es la forma más general. Esto no considera las colisiones interna de los electrones y mucho menos la fuerza eléctrica. Aun así, es una aproximación bastante cercana. 

Dado todos los choques, el trabajo hecho por la fuerza eléctrica se convierte en calor dentro del resistor. Dado que el trabajo por unidad de carga es $V$ y la carga que fluye en el tiempo es $I$, entonces se llega que: 

$$P=VI=I^2R$$

Conocido como la **ley de Joule**. 

## Ley de Ohm macroscópica 

Si consideramos la definición más fundamental de $J$: 

$$J=\frac{I}{A}$$

Y además la fuerza de un campo eléctrico en un cable: 

$$E=\frac{V}{L}$$

Reemplazando en la ley de Ohm se llega que: 

$$R=\frac{V}{I}=\frac{LE}{AJ}=\frac{L}{A\sigma}$$

# Magnetostática 

Acordándonos que en electrostática se estudiaba el caso donde las cargas estaban en reposo, en la magnetostática se consideran las **fuerzas entre cargas en movimiento**. 

Por eso mismo, es importante el estudio de intensidades de corrientes, que habla sobre el flujo de carga en movimiento en un intervalo de tiempo. 

## Fuerza magnética 

Muchas veces se tienen casos donde se tienen fuerzas cuyo origen no se ha podido explicar dado que no viene de la naturaleza electrostática. 

Al saber que una carga estacionaría produce un **campo eléctrico** $E$, las cargas en movimiento producirán un **campo magnético** $B$. 

Una forma de ver cualitativamente el campo magnético es al ver como se comporta un compás al someterlo a un campo magnético.  

La forma más sencilla de saber la dirección del campo magnético es por la regla de la mano derecha, al poner el dedo gordo en dirección de la corriente: 

![[pngegg.png|center|450]]


Esto se puede generalizar aun más e incorporar el dedo índice para indicar la dirección de la **fuerza magnética** 

![[pngegg(1).png|center|425]]


Todo estas analogías vendrían a indicar en realidad que estas tres cantidades vectoriales forman una base entre ellas. 

>[!bug] Fuerza magnética 
>Se define la **fuerza de Lorentz** como el siguiente resultado ante una carga $Q$ moviéndose a una velocidad $v$ con un campo magnético $B$: 
>
>$$F_\text{mag}=Q(v\times B)$$
>
>Ante la presencia de la fuerza electrostática y magnética es posible escribir la fuerza neta como: 
>
>$$F=Q[E+(v\times B)]$$

Una implicación directa de la definición es que  **las fuerzas magnéticas no hacen trabajo**. Esto se ve mediante el siguiente razonamiento: sea $Q$ la carga que se mueve por una trayectoria $dl=v\;dt$, entonces, el trabajo llegaría a ser: 

$$\begin{align}
dW_\text{mag}&=F_\text{mag}\cdot dl\\  \\
&=Q(v\times B)\cdot v\;dt\tag{1}\\  \\
&=0
\end{align}$$

Lo importante es notar que en la ecuación $(1)$ se tiene un producto punto entre dos variables perpendiculares: la velocidad y $(v\times B)$. 

Esto implica directamente que las fuerzas magnéticas **pueden** afectar la dirección de una partícula, no así cambiar sus velocidades. 

## Corriente sobre un cable 

Haciendo un recuerdo de la definición de corriente, se tenía la definición de flujo de carga que transcurre en un tiempo, es decir: 

$$I=\frac{dQ}{dt}$$

Ahora, extrapolando el concepto a un cable de corriente con densidad de carga $\lambda$ y una velocidad $v$: 


![[cable-1.png|center]]



Se puede llegar al siguiente cálculo: 

$$I=\lambda v$$

Dado que el segmento de largo $v\Delta t$ posee una carga $\lambda v\Delta t$, pasa en el punto $P$ en el intervalo $\Delta t$. De hecho, la corriente en realidad es un **vector** que se puede describir como: 

$$I=\lambda\vec{v}$$

Normalmente la notación vectorial no es necesaria, pero al trabajar con superficies es algo importante notar.

Por lo tanto, ocupando definición de fuerza magnética, se llega a lo siguiente para un cable conductor: 

$$\begin{align}
F_\text{mag}&=\int(v\times B)\;dq\\  \\
&=\int(v\times B)\lambda\;dl\\  \\
&=\int(I\times B)\;dl 
\end{align}$$

Que también, por conveniencia, se puede escribir de la siguiente manera: 

$$F_\text{mag}=\int I(dl\times B)$$

Y, cuando la corriente es constante, se tiene que: 

$$F_\text{mag}=I\int(dl\times B)$$


## Campo magnético 

El campo magnético ocurre en **flujos constantes de corrientes**. Esto es importante de tener en cuenta, dado que a partir de esa premisa se define la magnetostática. Esto, en términos matemáticos, llegaría a ser: 

$$\frac{\partial\rho}{\partial t}=0\iff\frac{\partial J}{\partial t}=0\implies\nabla\cdot J=0$$

Donde $J$ es un vector definido como la **densidad de corriente**: 

$$\vec{J}=\frac{I}{A}=\rho v$$

De hecho, si nos detenemos en la afirmación de antes, es posible decir que en realidad los modelos de la magnetostática y electrostática son casos muy particulares. Aun así, la magnetostática se tiene en muchos sistemas, incluyendo el sistema eléctrico de los hogares. 

>[!error] Ley de Biot-Savart 
>El campo magnético para una corriente que sigue una trayectoria rectilinea se define como: 
>
>$$B(r)=\frac{\mu_0}{4\pi}\int\frac{I\times\widehat{(r-r')}}{(r-r')^2}dl'=\frac{\mu_0}{4\pi}I\int\frac{dl\times(\widehat{r-r'})}{(r-r')^2}$$


Donde $\mu_0$ es la permeabilidad del vacio. 

Ahora, el análogo para cargas superficiales y volumétricas llegaría a ser: 

$$\begin{align}
B(r)&=\frac{\mu_0}{4\pi}\int\frac{K(r')\times(\widehat{r-r'})}{(r-r')^2}da\tag{Corriente volumétrica}\\  \\
B(r)&=\frac{\mu_0}{4\pi}\int\frac{J(r')\times(\widehat{r-r'})}{(r-r')^2}d\tau\tag{Corriente superficial}
\end{align}$$

## La divergencia y rotor del campo magnético 

Para los cables infinitos se tienen campos magnéticos que constituyen un rotor no nulo. De hecho, si se llega a calcular para el cable infinito, se cumple que: 

$$\oint B\cdot dl=\oint\frac{\mu_0I}{2\pi s}dl=\frac{\mu_0I}{2\pi s}\oint dl=\mu_0 I$$

Notemos que no depende del radio $s$ del cable, de hecho, para todo *loop* que cierra el campo magnético se tiene la misma respuesta. Si se tuviera un conjunto de cables se llegaría a algo similar: 

$$\oint B\cdot dl=\mu_0I_\text{enc}$$

Ahora, aplicando la definición de $J$, donde: 

$$I_\text{enc}=\int J\cdot da$$

Se llega a través el teorema de Stokes que: 

$$\int(\nabla\times B)\cdot da=\mu_0\int J\cdot da$$

Y, por lo tanto, se llega a la conclusión que: 

$$\nabla\times B=\mu_0J$$

Esto, sin embargo, aplica solo para un *"puñado"* de cables infinitos, lo que no es algo tan realista. Sin embargo, es posible llegar a una conclusión similar ocupando la Ley de Biot-Savart al sacar su rotor: 

$$\nabla\times B=\frac{\mu_0}{4\pi}\int\nabla\times\left(J\times\frac{\widehat{r-r'}}{(r-r')^2}\right)d\tau$$

Estos cálculos pueden ser simplificados y llegar a la misma conclusión de antes para los cables infinitamente largos. 

>[!error] Ley de Ampere 
>Se dice que el rotor del campo magnético se define como: 
>
>$$\nabla\times B=\mu_0J$$

Esa llegaría a ser su forma diferencial, aunque es fácil notar que su forma integral se define a través del teorema de Stokes: 

$$\int(\nabla\times B)\cdot da=\oint B\cdot dl=\mu_0\int J\cdot da$$

Notemos que el sentido físico de $\int J\cdot da$ es la corriente total pasando por cierta superficie, lo que se puede redefinir como $I_\text{enc}$ (la corriente encerrada por un *"loop"* amperiano). Por lo tanto, la equivalencia más importante a destacar es: 

$$\oint B\cdot dl=\mu_0I_\text{enc}$$


Notar que se debe ocupar un camino que vaya **en sentido del campo magnético**, de lo contrario, la integral de línea no haría sentido. 

### Comparación de la Magnetostática y Electrostática 

Ambos tienen una relación muy similar entre ellos, principalmente porque se calculan con integrales superficiales. 

La diferencia más notoria es que **la electrostática tiene trabajo asociado pero la magnetostática no**. 

Al comparar los campos hechos por ambos, se llega a lo siguiente

$$\text{Campo eléctrico}=\begin{cases}\nabla\cdot E=\frac{1}{\epsilon_0}\rho\\\  \\
\nabla\times E=0\end{cases}$$

Por el otro lado, para el campo magnético: 

$$\text{Campo magnético}=\begin{cases}\nabla\cdot B=0\\\\ 
\nabla\times B=\mu_0J\end{cases}$$


## Potencial magnético 

A pesar que el rotor no sea nulo para el campo magnético, es posible introducir un vector nuevo tal que: 

$$B=\nabla\times A$$

Este vector $\vec{A}$ no es arbitrario, de hecho, se aprovecha que $\vec{\nabla}\cdot B=0$ para poder relacionarlo con la Ley de Ampere: 

$$\begin{align}
\nabla\times B&=\nabla\times(\nabla\times A)\tag{Definición de A}\\  \\
&=\nabla(\nabla\cdot A)-\nabla^2A\tag{Rotor de divergencia}\\  \\
&=\mu_0J\tag{Ley de Ampere}
\end{align}$$

Dado esto, es posible definir $A$ por conveniencia un vector tal que $\nabla\cdot A=0$. Es posible demostrar que esto siempre se cumple al resolver una ecuación de Poisson. Con esta condición, se llega a lo siguiente: 

$$\nabla^2A=-\mu_0J$$

Esta otra ecuación de Poisson tiene solución, que de hecho, se puede expresar de la siguiente forma: 

$$\begin{align} 
A(r)&=\frac{\mu_0}{4\pi}\int\frac{J(r')}{(r-r')}d\tau\\  \\
&=\frac{\mu_0I}{4\pi}\int\frac{1}{(r-r')}d\tau\tag{Corriente lineal}\\  \\
&=\frac{\mu_0}{4\pi}\int\frac{K}{(r-r')}da'\tag{Corriente superficial}
\end{align}$$



## Condiciones de borde 

Al igual que el campo eléctrico sufría una discontinuidad ante una superficie, el campo magnético tiene una discontinuidad en una **corriente superficie**. Sólo por esta vez, lo que se ve afectado es **el componente tangencial**. 

Si se ocupa la Ley de Ampere para obtener el campo tangencial :


![[Captura de pantalla 2023-10-30 a la(s) 09.55-PhotoRoom(1).png|center]]

Claramente aquí no se cumple que: 

$$\oint B\cdot dl=0$$

De hecho, bajo la imagen anterior, se cumpliría que: 

$$\begin{align}
\oint B\cdot dl&=(B^{\parallel}_{\text{arriba}}-B^{\parallel}_{\text{abajo}})l\\  \\
&=\mu_0I_\text{enc}\\  \\
&=\mu_0Kl\end{align}$$

De forma equivalente, se tiene que: 

$$B^{\parallel}_{\text{arriba}}-B^{\parallel}_{\text{abajo}}=\mu_0K$$

Por lo tanto, **la discontinuidad es de $\mu_oK$.

Al igual que el potencial eléctrico, **el potencial magnético si es continuo ante cualquier borde** 

## Expansión multipolar del vector potencial 

Sabemos que, dado que la divergencia del campo magnético es nula, el campo magnético de un monopolo es nulo. Sin embargo, es posible hacer la expansión para conseguir el potencial magnético en forma dipolar: 

$$A_\text{dip}(r)=\frac{\mu_0}{4\pi}\frac{m\times\hat{r}}{r^2}$$

Donde $m$ es el **momento dipolar**, descrito como: 

$$m=I\int da=Ia$$

Así, ocupando la definición de potencial, es posible escribir **el campo magnético dipolar**: 

$$B_\text{dip}(r)=\nabla\times A=\frac{\mu_0m}{4\pi r^3}(2\cos(\theta)\hat{r}+\sin(\theta)\hat{\theta})$$

