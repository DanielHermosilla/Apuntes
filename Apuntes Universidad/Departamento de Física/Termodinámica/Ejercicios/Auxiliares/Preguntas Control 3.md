
## Pregunta 1 

Una botella contiene $1$ kg en el congeladora. $-18\degree C$ en estado líquido. Al retirarla del congelador se observa que una parte se congela. 

- Determine el porcentaje de agua líquida y de hielo en el estado de equilibrio final. (Ignorar la posible dependencia de los calores específicos con la temperatura)

#### Solución 

Sabemos que $\Delta H=334 kJ$ y se libera $\Delta H x$, donde $x$ es el porcentaje de la masa de agua que se solidifica. Como ocurre en equilibrio, la temperatura final es $T_F=0$. 

Así, se tiene que: 

$$\begin{align}
x\Delta H&=Q_\text{agua}+Q_\text{hielo}\\  \\
x\Delta H&=c_A\Delta T(1-x)+c_H\Delta Tx\\  \\
x&=\frac{c_A\Delta T}{[\Delta H+(c_A+C_H)\Delta T]}\\ \\
&\approx 0.2
\end{align}$$

---

## Pregunta 2 

La ecuación de Clapeyron establece que el equilibrio de fases en transiciones de primer orden en el plano $P-T$ está dado por: 

$$\frac{dP}{dT}=\frac{h(T)}{T\Delta v}$$

Donde $h$ es la entalpía molar de transición y $\Delta v$ el cambio de volumen molar al pasar de una fase a otra. Para ello, considerar las siguientes consideraciones: 

- Considerar un intervalo de temperaturas reducidos, de modo que se puede ignorar la dependencia de $h$ con $T$. ($h$ constante). 

- Considerar el caso líquido-vapor, donde las condiciones son lejanas al punto crítico, de modo que se puede despreciar el volumen de la fase condensada frente al vapor 

- Suponga que el vapor se puede considerar un gas ideal. 

Demostrar que se tiene que: 

$$P(T)=P_0\exp(-h/RT)$$

Donde $P_0$ es una constante. 


#### Solución 

Como se puede considerar que es un gas ideal, se tiene que: 

$$\begin{align}
PV&=nRT\\  \\
Pv&=RT\\  \\
v&=\frac{RT}{P}
\end{align}$$

Así, reemplazando en la ecuación de Clapeyron: 

$$\begin{align}
\frac{dP}{dT}&=\frac{h}{T\Delta v}\\  \\
&=\frac{hP}{RT^2}
\end{align}$$

Por lo tanto, pasando multiplicando los diferenciales e integrando: 

$$\begin{align}
dP&=\frac{hP}{RT^2}dT\\  \\
\frac{1}{P}dP&=\frac{h}{RT^2}dT\\  \\
\ln P&=-\frac{h}{RT}+C
\end{align}$$

Ahora se puede elevar a exponencial: 

$$\begin{align}
P&=\exp(-h/RT)\exp(C)
\end{align}$$

Imponemos $\exp(C)=P_0$

$$P=\exp(-h/RT)\exp(C)$$

---

## Pregunta 3 

- Mostrar, usando Gibbs, que si se tiene una sustancia pura ésta no puede tener 4 fases de equilibrio (pensar en las restricciones y grados de libertad que tiene la sustancia)

- A partir de lo anterior, obtener la regla de la fases de Gibbs de forma general, para $c$ componentes químicos independientes y $f$ fases de equilibrio. 

#### Solución 

Para obtener la regla de Gibss, supongamos que se tienen $f$ fases y $C$ componentes en equilibrio. 

En este caso, vamos a asumir que $x_{ij}$ representa la fracción molar de los componentes donde $i$ representa el componente y $j$ la fase. Así, se tiene que: 

$$x_{1j}+x_{2j}+\dots+x_{cj}=1\tag{Fase j}$$


Notemos que para un compontente $C$ cualquiere se tendrían $f\cdot C$ grados de libertad. Esto se debe que para cada fase hay $C$ fracciones molares y para cada fracción molar se tiene un grado de libertad. 

Así, se tienen $f\cdot c - f+2$ grados de libertad. 

Con la condición de equilibrio se obtienen $f-1$ ecuaciones para cada componente $i$, por lo tanto, se llega que: 

$$\begin{align}
fc-f+2-fc+c\\  \\
\implies \tau=c-f+2
\end{align}$$

--- 

## Pregunta 4 

Encontrar una expresión para el coeficiente de Joule: 

$$\mu_j=\left(\frac{\partial T}{\partial V}\right)_E$$

En función de las variables de estado $(T,P,V)$ para un gas de Van Der Waals y un gas ideal. Además, calcular las variaciones de temperatura y entropía que sufrirían los gases en una expansión desde un volumen $V_1$ hasta un volumen $V_2=2V_1$. 

La ecuación de estado para un gas de Van Der Waals está dada por: 

$$P=\frac{RT}{v-b}-\frac{a}{v^2}$$


#### Solución 

Es posible calcular $\mu_J$ usando regla de la cadena y ecuaciones de estado: 

$$\begin{align}
\mu_J&=\left(\frac{\partial T}{\partial V}\right)_E=\left(\frac{\partial T}{\partial P}\right)_E\cdot\left(\frac{\partial P}{\partial V}\right)_E
\end{align}$$

Por lo tanto, calculando el primer término: 

$$\begin{align}
\left(\frac{\partial T}{\partial P}\right)_E&=-\left(\frac{\partial V}{\partial S}\right)_E\tag{1}
\end{align}$$

Esto es por la relación de Maxwell (sale directo del formulario). 

Ocupando que $C_p=T(\partial S/\partial T)_P$ se puede llegar a lo siguiente: 

$$\begin{align}
\frac{d}{dT}C_P&=\frac{d}{dT}\left(T\left(\frac{\partial S}{\partial T}\right)_P\right)
\end{align}$$

Como $C_P$ no depende de $S$, es posible aplicar la regla del producto: 

$$\frac{d}{dT}\left(T\left(\frac{\partial S}{\partial T}\right)_P\right)=\left(\frac{\partial S}{\partial T}\right)_P+T\frac{d}{dT}\left(\frac{\partial S}{\partial T}\right)_P$$


Ahora, como $C_p$ es constante, se llega a lo siguiente: 

$$-\left(\frac{\partial S}{\partial T}\right)_P=T\frac{d}{dT}\left(\frac{\partial S}{\partial T}\right)_P$$

Si dividimos por $-C_p$: 

$$\left(\frac{\partial S}{\partial T}\right)_P=-\frac{T}{C_P}\frac{d}{dT}\left(\frac{\partial S}{\partial T}\right)_P$$

Para llegar a una expresión útil, extendemos la definición de $(1)$: 


