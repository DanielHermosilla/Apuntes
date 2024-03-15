
# Propiedades de los gases 

## Factor de compresibilidad

El factor de compresibilidad $z$ de un gas real (no ideal) se define como el siguiente cociente: 

$$z(P,T)=\frac{Pv}{RT}$$

El factor de compresibilidad, en términos simples, es una medida que se utiliza para describir cómo se comporta un gas en condiciones de presión y temperatura diferentes a las condiciones estándar. El valor $z$ es un valor fijo que se mide y tabula para algún gas de interés. 

## Ecuaciones viriales

Si se analiza un gráfico de isoterma $z(P,T)$, se puede analizar que **el factor de compresibilidad son lentamente variables con la presión**. Vale decir, a cada temperatura es posible expresar $z$ como una serie de potencias de la presión, donde los coeficientes son funciones de la temperatura. Además se cumple que $z(P\to0,T)=1$, otorgando el primer término del desarrollo. Así, es posible escribir el factor de compresibilidad como: 

$$z(P,T)=1+B'(T)P+C'(T)P^2+D'(T)P^3+\dots$$

Esto se denomina **ecuación virial**. 

Otra forma de expresarlo es al aplicar la definición y fijarse en el volumen molar $v$. Mientras más presión, menor es el volumen molar y mayor es su recíproco $1/v$. Así, es posible expresar el factor de compresibilidad:

$$z(v,T)=1+\frac{B(T)}{v}+\frac{C(T)}{v^2}+\frac{D(T)}{v^3}+\dots$$

Notar que los coeficientes $B(T)$ y $C(T)$ son tabulados para algunos gases.

## Ecuación de Van der Waals 

La ecuación del gas ideal empezó a fallar a densidades elevadas de gas. A partir del siglo $XIX$ se han empezado a proponer diversos modelos para gases reales, entre ellos, se propuso la siguiente ecuación: 

$$\frac{P_\text{ef}v_\text{ef}}{RT}=1\tag{1}$$

Donde $P_\text{ef}$ y $v_\text{ef}$ llegarían a ser la presión y volumen **efectivos**. Así, el volumen efectivo $v_\text{ef}$ llegaría a ser el volumen **realmente disponible** a ser ocupado por las moléculas. En otras palabras, el volumen total menos el volumen propio: 

$$v_\text{ef}=v-v_\text{correción}$$

Pero se llega a otro problema; el volumen no está bien definido. Aquí es donde el modelo llega a considerar otros aspectos, como: 

- Las moléculas interactuan entre sí. 
- Existe transferencia de momentum al chocar con las paredes del recipiente

Así, con esto en consideración, se define también la corrección a la presión: 

$$P_\text{ef}=P_\text{real}+P_\text{correción}$$ 
**Las diferentes formas de expresar las correcciones son aquellas que dan a las distintas ecuaciones de estado.** 

Van der Waals propuso una corrección para el gas donde impone una constante $b$ a ser determinada para cada gas: 

$$v_\text{ef}=v-b$$

Por el otro lado, hizo el siguiente análisis con el siguiente modelo: 

![[Pasted image 20231106152027.png|center]]


Las moléculas (verdes) que van a chocar con la molécula de color naranjo la frenan por medio de fuerzas atractivas. El freno depende de la intensidad de atracción, que es **inversamente proporcional a $v$**. Por el otro lado, la cantidad de moléculas que chocan con la pared crecen con la densidad de partículas del gas, también **inversamente proporcional a $v$**. 

Así, la corrección depende del efecto de frenado y cantidad de partículas que lo experimentan, por lo que debe ser inversamente proporcional a $v\times v=v^2$. Por lo tanto, se propone la siguiente corrección: 

$$P_\text{corrección}=\frac{a}{v^2}$$

Donde $a$ es una constante arbitraria para cualquier gas. 

Así, la ecuación $(1)$ se puede escribir como: 

$$(P+\frac{a}{v^2})(v-b)=RT\tag{2}$$

### Presión envolvente 

Conceptualmente, corresponde a cómo cambia la presión en función del volumen. 

Si se estudia más a profundidad la ecuación de Van der Waals se puede evidenciar lo siguiente: 

- **Primera derivada de la presión**: Se despeja la presión en función de las otras variables: 

$$\begin{align}
P&=\frac{RT}{v-b}-\frac{a}{v^2}\\  \\
\frac{dP}{dv}&=-\frac{RT}{(v-b)^2}+2\frac{a}{v^3}=0\\  \\
\frac{RT}{v-b}&=2\frac{a(v-b)}{v^3}
\end{align}$$

Si se reemplaza esto en $(2)$ se llega a lo siguiente: 

$$\begin{align}
P_\text{envolvente}&=2\frac{a(v-b)}{v^3}-\frac{a}{v^2}\\  \\
&=\frac{a}{v^2}-\frac{2ab}{v^3}
\end{align}$$

Así, esta curva representa el lugar geométrico de los puntos **donde se anula la primera derivada**. La presión envolvente se anula si $v=2b$ y tiende a cero si $v\to\infty$. 

Si lo vemos con valores simples, para un gas con $a=2$ y $b=3$: 


```functionplot
---
title: Presión envolvente
xLabel: Volumen
yLabel: Presión envolvente
bounds: [0,5,-10,10]
disableZoom: true
grid: true
---
f(x)= 2/x^2 - 12/x^3
```

Notemos que es posible graficar una variedad de gases y tienen un comportamiento similar: 


```functionplot
---
title: Presión envolvente
xLabel: Volumen
yLabel: Presión envolvente
bounds: [0,5,-10,10]
disableZoom: true
grid: true
---
f(x)= 2/x^2 - 12/x^3
g(x) = 10/x^2 - 20/x^3
h(x) = 1/x^2 - 2/x^3
y(x) = 5/x^2 - 80/x^3
```

- **Segunda derivada**: El máximio de la curva corresponde a pedir que se anule la derivada, así: 

$$\frac{dP_\text{envolvente}}{dv}=-\frac{2a}{v^3}-6\frac{ab}{v^4}=0$$

Esto se anula para $v=3b$, comúnmente denominado como **volumen crítico**. Así, se define la **presión y temperatura crítica**, vale decir, los límites físicos a partir donde un gas deja de existir. 

>[!example] Presión crítica 
>Es el valor de la presión envolvente en el volumen crítico $v_c=3b$: 
>
>$$P_c=a/27b^2$$

>[!example] Temperatura crítica 
>Es el valor de le temperatura evaluada en $v_c=3b$ y $P_c=a/27b^2$: 
>
>$$RT_c=\frac{8a}{27b}$$
>

Notemos que de aquí se puede llegar a algo importante; dado que la temperatura y presión crítica **son medibles**, entonces es posible definir las constantes en función de ellas: 

$$\begin{align}
a&=\frac{27R^2T_{c}^{2}}{64P_c}\\  \\
b&=\frac{RT_c}{8P_c}
\end{align}$$

### Isotermas 

- Si $T>T_c$ las isotermas en el plano $P-V$ son univaluadas, es decir, solo tienen un valor único. Hace sentido, por que el sufijo "crítico" hace alusión al valor máximo. 

- Si $T=T_c$ la isoterma también sigue siendo univaluada, pero es el punto de inflexión en el volumen crítico 

- Si $T<T_c$ las isotermas $P-V$ decrecen. hasta un mínimo, luego crecen a un máximo, y luego decrecen hasta cero. 



# Equilibrio entre fases 

>[!example] Fases 
>Se definira como fase a una porción de materia con propiedades homogéneas, vale decir, que no dependen de las coordenadas.
>
![[imagen-removebg-preview.png|center]] No confundir con el concepto de especies químicas 


## Transiciones de fase de primer orden 

En una transición de fase cualquiera se pueda saber, empíricamente, que la mezcla puede estar en varios estados. Sin embargo, la entropía de fases es distintas. Se va a decir que la transición de fase es de **primer orden*** si la entropía es discontinua con respecto a un parámetro intensivo. 

Un ejemplo clásico, si se considera la presión atmosférica constante, existe sólamente hielo cuando $T\leq 273K$ y solamente líquido cuando $T\geq 273$ que es de mayor entropía. De tal forma la entropía es una función discontinua de la temperatura. 

Por lo tanto, por contradicción, se define las trancisiones de segundo orden como aquellas que la entropía es continua. 
## Calor latente 

Ahora, nuevamente bajo el mismo ejemplo, se sabe que para fundir hielo es necesario poder calentarlo. Si la trancisión llegase a ser reversible, debería satisfacer que: 

$$dS=\frac{q}{T}$$

Como la transición ocurre a una temperatura fija y $\Delta S=S_\text{agua}-S_\text{hielo}$ entonces: 

$$\begin{align}
\Delta S&=\int dS\\  \\
&=\int\frac{q_P}{T}\\  \\
&=\frac{Q_\text{transición}}{T}\\ \\
&=\frac{\Delta H_\text{transición}}{T}
\end{align}$$

De esta forma el $Q_\text{transición}$ se denomina como **calor latente de transición**, y como ocurre a presión constante, el calor coincide con la definición de entalpía $\Delta H$. Recordando que la entalpía se definia como: 

$$H=U+PV$$

Con $U$ siendo la energía interna, $P$ la presión y $V$ el volumen. Claramente si la presión es constante, $\Delta P=0\implies \Delta H=\Delta U$. 

## Transición líquido-vapor a temperatura constante 

En los sistemas líquido-gas ocurre un fenómeno muy peculiar al estar encerrados dentro de un émbolo a temperatura constante: 


![[imagen-removebg-preview(1).png|center]]


Al pulsar el émbolo, lo que uno esperaría es que la presión aumente dentro del gas.  No obstante, la disminución forzada del volumen conduce que una parte del vapor pase a fase líquida, de modo que la presión sigue siendo constante. Así, **la transición ocurre a presión constante**. Lo anterior se generaliza por la siguiente frase: 

>"Fijar la temperatura implica fijar la presión de la transición"

Esto nos conduce a la implicancia que si dos fases coexisten en el equilibrio no se puede fijar independientemente la presión o la temperatura. 

## Transición líquido-vapor a presión constante 

Ahora consideramos el calentamiento isobárico desde la fase líquida hasta la del vapor:

![[imagen-removebg-preview(2).png|center]]


También se sabe que calentar el sistema por debajo de la temperatura de ebullición $T_e$ el sistema permanecerá en fase líquida. Al alcanzar la temperatura de ebullición el liquido se empieza a evaporar y coexiste el líquido y vapor. En tal momento, **el calentamiento no aumenta la temperatura del sistema**. Después. que todo el líquido se evapora el calentamiento vuelve a aumentar con la temperatura del sistema. Luego, ocurre el mismo fenómeno de antes; al fijar presión también se fija la temperatura de transición. 

Dado que el proceso es isobárico (la presión del sistema no cambia) se puede plantear lo siguiente: 

$$\begin{align}
\Delta E&=Q_\text{transición}-P\Delta V\\  \\
\Delta (E+PV)&=Q_\text{transición}\\  \\
\Delta H &= Q_\text{transición}
\end{align}$$

Análogo lo que se había llegado anteriormente. Esto se llama **entalpía de transición**. 

## Curvas en el plano P-T 

De lo discutido anteriormente se puede desprender que al hacer transiciones de fase solo se puede fijar o bien la temperatura o la presión. Por lo general, se expresa la presión en función de la temperatura, llamado la **curva de equilibrio de fases**. Los puntos del plano P-T que están fuera de la curva consisten en estados **de una sola fase**. Un ejemplo es el plano para el agua: 

![[Pasted image 20231112154637.png|center|500]]



## Transición líquido-vapor en el plano P-V: punto crítico 

Es conveniente señalar las siguientes observaciones al trabajar en el plano $P-V$: 

1. Para cada gas existe una temperatura $T_c$, llamada crítica, por encima del cual es imposible licuarlo. De este modo, las isotermas $T>T_c$ representan siempre estados del gas como fase única. 

2. Bajo $T_c$, a presión baja, la sustancia se encuentra en la fase gaseosa. Esta fase se llama vapor. Si se aumenta la presión a temperatura constante se alcanza un valor al cual el vapor se empiza a condensar, coexistiendo vapor y líquido. En estas condiciones el vapor se llama *vapor saturado* y el líquido llega a nombrarse *líquido saturado*. 

3. Cuando todo el vapor se condensa, un intento de reducir el volumen se traduce en un **gran aumento de presión**, dada a la escasa comprensibilidad del líquido. 

4. El punto crítico corresponde a la cúspide de la campana. La zona interior es aquella donde convive el líquido y vapor y **la isoterma crítica** $T_c$ es tangente a la cúspide de la campana. La presión en ese punto se llama presión crítica $P_c$ y el volumen molar se llama volumen crítico $v_c$. Esto se llama punto crítico debido que: 

- En el punto crítico desaparece la diferencia entre vapor y líquido 
- El volumen molar el líquido y vapor son iguales. 
- Se anula la entalpía de evaporación 
- Se anula la tensión superficial. 

![[Pasted image 20231112155403.png|center|500]]

## Ecuación de Clapeyron 

El equilibrio entre dos fases consiste en que **cada componente químico *le da lo mismo* estar en un sistema u otro**. 

En el equilibrio se debe cumplir que el número de moléculas que abandona el líquido para pasar al vapor debe ser igual al número que recorre por el camino inverso. Luego: 

$$\left(\frac{\partial E}{\partial N}\right)_{V,S}\bigg\vert_\text{líquido}=\left(\frac{\partial E}{\partial N}\right)_{V,S}\bigg\vert_\text{vapor}$$

Esto coincide con la **definición de potencial químico**, así: 

$$\mu_\text{líquido}=\mu_\text{vapor}$$

Ahora, ocupando la ecuación de Euler donde $\mu=g$ se concluye que la condición de equilibrio para una sustancia en dos fases diferentes es: 

$$g_1(P,T)=g_2(P,T)$$

Es decir, **en equilibrio se deben igualar las funciones de Gibss molares**. 

Una forma alternativa de llegar a la misma conclusión anterior es al hacer el siguiente desarrollo:

$$\begin{align}
G&=E+PV-TS\\  \\
dG&=VdP-SdT\\  \\

\end{align}$$

Si la transición ocurre a presión y temperatura constante se tiene que $dG=0$, lo que significa que la funcion de Gibbs molares para ambas fases son iguales. Sea: 

 $$g_i(P,T)=\frac{G_i(P,T)}{\nu_i}$$

Donde $\nu_i$ es el número de moles de la fase $i$. Además, sea $x$ la fracción molar de la sustancia en fase $1$ y $x-1$ la fracción molar en la segunda fase. Por lo tanto, la función de Gibbs molar del sistema completo llegaría a ser: 

$$g=xg_1(P,T)+(1-x)g_2(P,T)$$

Si la presión y temperatura es constante, se llega que $g_1=g_2$. 

>"Durante la transición las funciones de Gibbs molares de ambas fases son iguales" 

### Ecuación de Clapeyron en transiciones de primer orden 

Ahora, podriamos considerar una curva en el plano $P-T$ y dos puntos próximos sobre ellas: $(P,T)$ y $(P+\Delta P, T+\Delta T)$. 

![[Pasted image 20231112161419.png|center|450]]

La idea es poder derivar la pendiente de la curva. Sabemos que la ecuación de Gibbs molar deben ser iguales para todos los puntos de la curva. Así, se puede armar un sistema de ecuación: 

$$g_1(P+\Delta P,T+\Delta T)-g_1(P,T)=g_2(P+\Delta P,T+\Delta T)-g_2(P,T)$$

Al restar y hacer el desarrollo de Taylor la ecuación queda como: 

$$v_1\Delta P-s_1\Delta T=v_2\Delta P-s_2\Delta T$$

Así, la pendiente de equilibrio de fases llega a ser: 

$$\begin{align}
\frac{\Delta P}{\Delta T}&=\frac{dP}{dT}\\  \\
&=\frac{s_2-s_1}{v_2-v_1}\\  \\
&=\frac{\Delta s}{\Delta v}
\end{align}$$

Donde $\Delta s$ y $\Delta v$ son los cambios de entropía y volumen molar en transición de fase. Luego, $\Delta s=h/T$ donde $h(T)$ es la **entalpía de transición**. Así, se postula la **ecuación de Clapeyron**: 

$$\frac{dP}{dT}=\frac{h(T)}{T\Delta v}\tag{Ecuación de Clapeyron}$$

De aquí se desprenden dos cosas importantes: 

- **Líquido-vapor**: El vapor <u>siempre</u> tiene mayor volumen que el líquido, luego $\Delta v>0$ y la pendiente de la curva es siempre positiva. 

- **Sólido-líquido**: Al igual que antes, por lo general el líquido tiene mayor volumen que el sólido y la curva tiene pendiente positiva. 