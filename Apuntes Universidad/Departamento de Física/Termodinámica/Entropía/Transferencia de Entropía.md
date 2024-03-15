
## Transferencia de entropía cuasiestática 

Antes de presentar la transferencia cuasiestática, es importante mencionar el siguiente razonamiento al aplicar la **aproximación de Taylor**. Si aplicamos una aproximación con [[Derivadas parciales|derivadas parciales]], podemos llegar que: 

$$\begin{align}
df=\left(\frac{\partial f}{\partial x}\right)dx+\left(\frac{\partial f}{\partial y}\right)dy
\end{align}$$

Ahora, muchas veces se cumple con aproximaciones de Taylor que: 

$$\begin{align}
df&=A(x,y)dx + B(x,y)dy
\end{align}$$

Si restamos ambas ecuaciones se llega que: 

$$\begin{align}
df&=\left[(\frac{\partial f}{\partial x})-A\right]dx+\left[(\frac{\partial f}{\partial y})-B\right]dy
\end{align}$$

Si definimos $A$ y $B$ como las siguientes variables: 

$$\begin{align}
A&=\left(\frac{\partial f}{\partial x}\right)\\  \\
B&=\left(\frac{\partial f}{\partial y}\right)
\end{align}$$


Por conclusión se llega que: 

$$\begin{align}
\left(\frac{\partial A}{\partial y}\right)&=\left(\frac{\partial B}{\partial x}\right)
\end{align}$$

A partir de esto, es posible definir la transferencia cuasiestática de [[Entropía|entropía]]. Podemos considerar el siguiente sistema: 

![[Pasted image 20230929103730.png|center]]

Por la [[Primera ley de la termodinámica|primera ley de Termodinámica]], sabemos que: 

$$\begin{align}
dE&=q_\text{rev}+w_\text{rev}\tag{1}
\end{align}$$

Por condición de [[Reversibilidad|reversibilidad]], tenemos dos implicancias importantes: 

$$\text{Reversibilidad}\implies\begin{cases}w=-PdV\\  \\
\text{No se crea entropía}\end{cases}$$

Reemplazando en la ecuación $(1)$: 

$$\begin{align}
dE&=q-PdV
\end{align}$$

Si la energía la ponemos en función de la [[Entropía|entropía]] y el volumen, entonces: 

$$\begin{align}
dE&=\left(\frac{\partial E}{\partial S}ds\right)+\left(\frac{\partial E}{\partial V}dV\right)\\  \\
dE&= TdS+\left(\frac{\partial E}{\partial V}\right)dV\\  \\
dE-dE&=\left[q-Tds\right]+\left[-p-(\frac{\partial E}{\partial V})\right]dV\\  \\
\text{Imponer}\;dV&=0\\  \\
\implies q-Tds&=0
\end{align}$$

Por lo tanto, la variación de entropía se define como: 

$$\begin{align}
dS&=\frac{q}{T}\\  \\
P&=-\left(\frac{\partial E}{\partial V}\right)
\end{align}$$

Además, sabiendo que la ecuación de la entropía se define como: 

$$\begin{align}
S-S_0&=Nk\ln V+\frac{3}{2}Nk\ln E\;\;\;\;\;\;\;\;\;\frac{\partial}{\partial V}\\ \\
E&=\frac{3}{2}NkT\\  \\
0&=\frac{Nk}{V}+\frac{3}{2}\frac{Nk}{E}\left(\frac{\partial E}{\partial V}\right)\\  \\
&=\frac{Nk}{V}+\frac{3}{2E}Nk\left(-P\right)
\end{align}$$

Finalmente, nos definimos entonces, **la entropía transferida reversiblemente por el medio al sistema** como: 

$$dS_\text{reversible}=\frac{q_\text{reversible}}{T}$$

## Estados inicial y final no necesariamente próximos 

Podemos imaginar una función continua en el plano $P-V$: 


```functionplot
---
title: Plano P-V
xLabel: V
yLabel: P
bounds: [0,5,0,10]
disableZoom: true
grid: false
---
f(x)=x^5/(x+3x^2)+2-sin(8x)-x
```

Podriamos tomar una [[Integral de línea|integral de línea]] que nos defina el [[Trabajo macroscópico|trabajo]] desde el inicio hasta el final. Por lo tanto, se tiene que: 

$$\begin{align}
dS&=\frac{q_A}{T}\\  \\
S_F-S_I&=\int^{f}_{a}\frac{q_A}{T}\\  \\
&=\int^{f}_{b}\frac{q_b}{T}
\end{align}$$

Entonces, el calor para el punto $A$ y el punto $B$ se define como: 

$$\begin{align}
Q_a&=\int^{f}_{a}q_a\\  \\
Q_b&=\int^{a}_{b}q_b\\  \\
Q_a&\neq Q_b\\  \\
\Delta S_A&=\Delta S_B
\end{align}$$


A partir de esto se postulo el [[Teorema de Clausius]], lo que ayudó a definir la [[Entropía|entropía]] dado que no depende del proceso: 

$$\oint\frac{q}{T}=0$$

#### Ejemplo 

Un bloque de masa $m=200g$ se calienta reversiblemente de $T_1=30^\degree C$ a $T_2=60^\degree C$. Calcular $\Delta S_{C_u}$. Como dato, $c_p=0.385kJ/kg-K$. 

Sabemos que: 

$$\begin{align}
C_P&=mc_p\\  \\
&=77 J/K
\end{align}$$

Como el proceso es reversible e isobárico de $T_1$ a $T_2$, entonces: 

$$q_{C_u}=C_pdT$$

Por ende, la entropía sería: 

$$\begin{align}
dS_{C_u}&=C_p dT\\  \\
\Delta S_{C_u}&=\int\frac{q_{C_u}}{T}\\  \\
&=C_p\ln(T_2/T_1) \\\\
&=7,3\;J/K
\end{align}$$

Notar que no importa si es reversible o irreversiblemente, ya que es una función de estado. Pero, entonces, *¿Dónde está la diferencia?* 

![[Pasted image 20231003144430.png|center]]

Notemos que en el **reversible** tenemos: 

$$\begin{align}
dS_\text{medio}&=\frac{-q_{C_u}}{T}
\end{align}$$

Pero, **como es reversible**, entonces, 

$$dS_\text{sistema}=\frac{q_{C_u}}{T}$$ 
Para el sistema se tendría: 

$$\Delta S= c_p m\ln(\frac{T_2}{T_1})$$

Equivalente en el medio pero distinto signo. Por lo tanto, $\Delta S_\text{Universo}=0$. 

Sin embargo, en el reversible **en vez de ser igualdades se tienen desigualdades**. 

#### Ejemplo 

Se tiene un cuenco de agua sobre una superficie térmica caliente. Es un proceso irreversible y se emula usando dos procesos **reversibles**. 

- Uno para el agua 
- Otro para la fuente térmica 

![[Pasted image 20231003145444.png|center]]

Para el agua, de masa $1kg$ y $c_p=4,19 kJ/K$, cuando se calienta de $T_1=0$ a $T_2=100$ entonces se cumple que: 

$$\begin{align}
q_a&=mc_pdT\\  \\
Q_a&=\in tmc_pdT\\  \\
Q_a&=mc_p(T_2-T_1)\\  \\
Q_a&= 419kJ>0
\end{align}$$

Ahora, el análisis para el medio, que es la fuente térmica, inventamos un proceso donde la fuente a $T_2$ cede calor $Q_a$ al agua. Para imponer que van a ceder calor, imponemos que $Q_F=-Q_A=-C_p(T_2-T_1)$. 

Para la fuente, entonces: 

$$\begin{align}
ds&=\frac{q_q}{T_q}\\  \\
&=-\frac{q_a}{T_2}
\end{align}$$

Dado que por definición, la temperatura de la fuente es constante. Entonces: 

$$\begin{align}
\Delta S_F&=\frac{-Q_a}{T_2}\\  \\
&=\frac{-C_p(T_2-T_1)}{T_2}
\end{align}$$

