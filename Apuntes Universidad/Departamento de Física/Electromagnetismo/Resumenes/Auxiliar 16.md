
# Resumen 

El campo magnético puede producir corriente si: 

- Hay un movimiento relativo del circuito con respecto a $\vec{B}$

- $\vec{B}$ varía con respecto al tiempo. 

Así, se define la fuerza electromotriz como: 

$$\begin{align}
\epsilon&=\oint\frac{F_\text{mag}}{q}\cdot d\vec{l}\\  \\
&=\oint(\vec{v}\times\vec{B})\cdot d\vec{l}\\  \\
&=-\frac{d}{dt}\int\vec{B}\cdot d\vec{s}\\  \\
&=-\frac{d\Phi}{dt}
\end{align}$$

También, la variación del campo magnético produce un campo eléctrico: 

$$\begin{align}
\epsilon&=\int\vec{E}\cdot d\vec{l}\\  \\
&=-\frac{d}{dt}\int\vec{B}\cdot d\vec{s}\\  \\
\implies\nabla\times\vec{E}&=-\frac{\partial\vec{B}}{\partial t}\tag{Ley  de Faraday}
\end{align}$$


Por último se tiene la Ley de Lenz: 

>*"La naturaleza aborrece los cambios de flujo"*

Así, la fuerza electromotriz inducida generará una corriente inducida que se opondrá a los cambios de $\Phi_M$. 

<div style="page-break-after: always;"></div>

## Pregunta 1 


Una espira de radio $a$ se coloca en un campo magnético uniforme, como se muestra en la figura.

![[Pasted image 20231127192619.png|center]]

Si el campo magnético varía con respecto al tiempo de la forma $B(t)=B_0+bt$ con $B_0$ y $b$ constantes positivas, entonces: 

#### Encontrar el flujo magnético 

Por definición se sabe que el flujo magnético es: 

$$\Phi=\int\vec{B}\cdot d\vec{s}$$

Por lo tanto: 

$$\begin{align}
\Phi&=\int^{a}_{0}\int^{2\pi}_{0}\left[-(B_0+bt)\hat{z})\right]\cdot(ra\;d\phi dr\hat{z})\\  \\
&=-(B_0+bt)\cdot 2\pi\frac{r^2}{2}\bigg\vert^{a}_{0}\\  \\
&=-\pi a^2(B_0+bt)
\end{align}$$

#### Fuerza electromotriz inducida 

Nuevamente por definición se tiene que: 

$$\epsilon=-\frac{d\Phi}{dt}$$

Por lo tanto, derivando la expresión anterior: 

$$\epsilon=\pi a^2b$$

#### Corriente inducida y su dirección 

El enunciado nos dice cual es la resistencia equivalente. Entonces, usando la Ley de Ohm se puede llegar a la siguiente equivalencia: 

$$I=\frac{\epsilon}{R}$$

Así, reemplazando con el resultado anterior se llega que 

$$I=\frac{\pi a^2b}{R}$$

Por la Ley de Lenz, la corriente debería ir en sentido antihorario dado que $\vec{B}_\text{ind}$ produce un campo en $\hat{z}$ que a su vez provoca un campo neto $\Delta\vec{B}$ en $-\hat{z}$. 

#### Potencia disipada 

Ocupando otra vez la definición de potencia disipada: 

$$P=I^2R$$

Se llega a lo siguiente al reemplazar con los valores obtenidos: 

$$\begin{align}
P&=I^2R\\  \\
&=\left(\frac{\pi a^2b}{\cancel{R}}\right)^2\cancel{R}\\  \\
&=\frac{(\pi a^2b)^2}{R}
\end{align}$$

<div style="page-break-after: always;"></div>

## Pregunta 2 

Considere el circuito de la figura, el cual ilustra un toroide con dos bobinas. 

![[Pasted image 20231127195953.png|center|550]]

El toroide, que se compone de un material ferromagnético de permeabilidad $\mu$, posee una sección uniforme $S$, radio interior $a$ y radio exterior $b$. Si en el circuito de la izquierda se hace circular una corriente $I_1(t)$ determinar: 

#### Campo magnético en el punto medio del toroide 

Como se está trabajando con un material ferromagnético se generarán corrientes de magnetización, por lo tanto, se usará la ley de Ampere generalizada: 

$$\vec{H}=\frac{1}{\mu}\vec{B}\to\nabla\times\vec{H}=J_\text{libre}$$

Además, si analizamos la geometría y simetría de la figura, es directo ver que $\vec{H}$ va en la dirección de $\hat{\phi}$. 

Por lo tanto, se define el siguiente $\textbf{\textcolor{blue}{loop\;amperiano}}$: 

![[Pasted image 20231127200254.png|center|550]]

Donde se cumple que: 

$$\oint\vec{H}\cdot d\vec{l}=I_\text{libre}$$

Resolviendo la integral: 

$$\begin{align}
\oint\vec{H}\cdot d\vec{l}&=\oint(H(r)\hat{\phi})\cdot(r\;d\phi\;\hat{\phi})\\  \\
&=2\pi rH
\end{align}$$

Por el otro lado, la carga libre: 

$$\begin{align}
I_\text{libre}&=\int\vec{J}\cdot d\vec{s}\\  \\
&=-N_1I_1(t)
\end{align}$$

Juntando todo se llega que: 

$$H(r)=-\frac{N_1I_1(t)}{2\pi r}$$

Así, el campo magnético en el toroide es: 

$$\vec{B}(r)=-\mu\frac{N_1I_1(t)}{2\pi r}\;\hat{\phi}$$

Y en el centro llegaría a ser: 

$$\vec{B}\left(\frac{a+b}{2}\right)=-\mu\frac{N_1I_1(t)}{\pi(a+b)}\;\hat{\phi}$$


#### Flujo magnético enlazado por la espira del segundo circuito 

Como no se tiene información de $S$ (a priori no se podría asumir que es una circumferencia perfecta al ser un toroide) se va a asumir que el radio transversal es lo suficientemente chico para poder imponer que: 

$$B(r)\approx B(r_\text{centro})$$

Por lo tanto: 

$$\begin{align}
\Phi&=\iint\vec{B}\cdot d\vec{s}\\  \\
&=\iint\left(\vec{B}(r_\text{centro})\right)\cdot (ds\;\hat{\phi})\\  \\
&=-\mu\frac{N_1I_1(t)}{\pi(a+b)}S
\end{align}$$

#### Fuerza electromotriz inducida entre A y B 

Notar que las espiras del sigundo circuito están *conectadas en serie*. Así: 

$$\begin{align}
\epsilon_{AB}&=N_2\epsilon\\  \\
&=N_2\left(-\frac{d\Phi}{dt}\right)\\  \\
&=\mu\frac{N_1N_2S}{\pi(a+b)}\;\frac{dI_1}{dt}
\end{align}$$

<div style="page-break-after: always;"></div>

## Pregunta 3 

Un loop rectangular de ancho $w$ y largo $l$ se mueve con velocidad constante $\vec{v}$ alejándose de un cable delgado infinito en el que circula una corriente $I$, como se muestra en la figura.

![[Pasted image 20231127211045.png|center]]

Si la resistencia total del loop es $R$ y considerando el instante en que la parte más cercana del loop al cable se encuentra a una distancia $r$, determine: 

#### Flujo magnético a través del loop 

Se sabe por ley de Ampere que el flujo magnético producido por el cable es 

$$B(y)=\frac{\mu_0I}{2\pi y}$$

Si ocupamos ley de la mano derecha, el campo magnético iría en $-\hat{z}$. 

Aplicando la definición de flujo magnético se tiene lo siguiente: 

$$\begin{align}
\Phi&=\int\vec{B}\cdot d\vec{s}\\  \\
&=\int\left(-\frac{\mu_0I}{2\pi y}\hat{z}\right)\cdot(dx\;dy\;\hat{z})\\  \\
&=-\frac{\mu_0I}{2\pi}\int^{l}_{0}\int^{r+w}_{r}\frac{dy}{y}\;dx\\  \\
&=-\frac{\mu_0I}{2\pi}\;l\;\ln\left(\frac{r+w}{r}\right)
\end{align}$$

Notar que lo importante de esta parte es notar que **el campo magnético depende de $\hat{y}$**. Por lo tanto, no es *directa* la integral de superficie. 

#### Fuerza electromotriz inducida y corriente inducida 

Primero notar que el loop se mueve en $\hat{y}$ con una velocidad $v$. Por lo tanto, la variable logarítmica del flujo tiene dependencia del tiempo. Así: 

$$\begin{align}
\epsilon&=-\frac{d\phi}{dt}\\  \\
&=\mu_0\frac{I}{2\pi}\;l\;\frac{d}{dt}\left[\ln\left(\frac{r+w}{r}\right)\right]\\  \\
&=\mu_0\frac{I}{2\pi}\;l\;\frac{r}{r+w}\left[\frac{r-(r+w)}{r^w}\right]\cdot\frac{dr}{dt}\tag{Regla de la cadena}\\  \\
&=-\frac{\mu_0I\;l}{2\pi}\frac{w}{r(r+w)}\cdot v
\end{align}$$

Para obtener la corriente inducida se ocupa nuevamente la ley de Ohm 

$$\begin{align}
I&=\frac{\epsilon}{R}\\  \\
&=-\mu_0\frac{I\;l}{2\pi R}\frac{vw}{r(r+w)}
\end{align}$$


También es posible calcularlo al ocupar la segunda definición de la fuerza electromotriz, que se llega a lo mismo: 

$$\epsilon=\oint(\vec{v}\times\vec{B})\cdot d\vec{l} $$

La dirección de la intensidad de corriente es horario, puesto que se opone a la fuerza electromotriz. El signo negativo indica el sentido horario. 