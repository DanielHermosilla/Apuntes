
# Máquinas y Rendimiento 

El uso de las máquinas viene dado, históricamente, desde la necesidad de tener algun mecanismo **automatizado** con fines **bélicos**. Más que nada - extender las capacidades humanas como las catapultas. 

## Máquinas en la época preindustrial 

Algunos de los casos más notables vienen de la época preindustrial, donde se vieron inspiradas principalmente por el uso del agua. 

### La máquina de Thomas Newcomen 

Fue la **primera máquina de vapor automática** utilizada en aplicaciones prácticas. 

![[Pasted image 20231209232757.png|center|550]]

La caldera en rojo hace vapor de agua que se introduce a la cámara con el émbolo. Al tener el agua evaporándose el émbolo ira creciendo debido al contrapeso del lado derecho. Cuando termina la *"carrera"* del émbolo hacia arriba se cierra la válvula y se inyecta un chorro de agua fria **para condensar el vapor**. 

Lo importante del sistema es el último paso, donde ocurre la **condensación**. Esto hace que la presión atmosférica **empuje el pistón hacia abajo** y ocurra **trabajo mecánico** para levantar el contrapeso. 

Es importante notar que la presión que utilizaba **no era la del vapor**, si no la de la atmosféra. 

Esta máquina fue muy robusta e ineficiente. 

### La máquina de vapor de Watt 

La máquina de Watt marcó un antes y después histórico, pues se considera el inicio de la revolución industrial. Él trabajo mediante el modelo de Newcomen y lo trató de perfeccionar al ver la cantidad de energía que se desperdiciaba en calentar y enfriar el cilindro. 

Así, hace tres cambios importantes: 

- Colocó el condensador fuera del cilindro de trabajo. 
- Introducir la máquina de doble efecto. 
- Usar la presión **del vapor** para hacer trabajo 

![[Pasted image 20231209234152.png|center|550]]

Así, para entender la ilustración sería útil definirse un esquema del funcionamiento. En el tiempo $1$ el vapor de la caldera entra por la válvula superior de arriba mientras que el vapor anterior es expulsado por el condensador: 

![[Pasted image 20231209234333.png|center|325]] 

Al terminar esto el orden se invierte, el vapor ingresa de la cámara inferior y el vapor e expulsa hacia el condensador. 

![[Pasted image 20231209234448.png|center|350]] 

Por último, se obtuvo una innovación de poder transformar el movimiento lineal a uno circular. Así, se llega a la [siguiente animación](https://www.youtube.com/watch?v=Jktv9KP3eYc). Notemos que el mecanismo de transformamiento de momentum es **muy parecido al funcionamiento de una biela de una bicicleta**. 

## Rendimiento de las máquinas térmicas 

Para esta sección se considerará únicamente las máquinas cíclicas donde se cumple que el estado inicial es igual al estado final. Así, se cumple que: 

$$\begin{align}
\Delta E_\text{sistema}&=0\\  \\
\Delta S_\text{sistema}&=0
\end{align}$$

Una acotación es mencionar que el medio no mantiene un estado cíclico, permitiendo obtener la variación de entropía nula **en el sistema**. 

>[!quote] Enunciado de Kelvin-Plank 
>*"No es posible convertir íntegramente el calor en trabajo mecánico"* o, en otras palabras *"No es posible una máquina térmica cíclica interactúe con una sola fuente térmica"* 

Primero, veamos cómo se llega a la equivalencia entre ambos enunciados. Para que una máquina sea **cíclica** debe haber dos fuentes que puedan desencadenar el ciclo inicial y la segunda que haga volver al estado inicial. De tal forma, al no poder convertir el calor en trabajo mecánico, necesariemente se necesita interactuar con más de una fuente térmica. 

El argumento riguroso se puede ver mediante la siguiente figura: 

![[Pasted image 20231209235351.png|center|350]]

Supongamos que es posible extraer energía térmica ($Q_2$) de la fuente térmica a temperatura $T_2$ para que realice un trabajo $W'=-W>0$. Sabemos que por **conservación de energía** (recordando que $\Delta E_\text{sistema}=0$):  

$$\begin{align}
Q_2+W&=0\\  \\
\implies W'=-W&=Q_2
\end{align}$$

Ahora, como no hay creación de entropía en el sistema, la entropía **transferida** por la fuente caliente a la máquina en el ciclo estaría dada por: 

$$\Delta S_\text{sistema}=\frac{Q_2}{T_2}$$ 
Ahora, si el ciclo es irreversible, entonces se cumple que: 

$$\Delta S_\text{irreversible}\geq 0$$ 
Por lo tanto, la variación de entropía debería ser igual a la siguiente suma: 

$$\Delta S_\text{ciclo}=\frac{Q_2}{T_2}+\Delta S_\text{irreversible}=0$$

Notemos que la entropía irreversible es no negativa y la temperatura es siempre positiva. Entonces, para que se cumpla la igualdad se debería llegar a algo del siguiente estilo: 

$$\begin{align}
\frac{Q_2}{T_2}+\Delta S_\text{irreversible}&=0\\  \\
Q_2=-\frac{-\Delta S_\text{irreversible}}{T_2}&<0
\end{align}$$

Esto dice que el calor es negativo, vale decir, la fuente térmica **no podría entregar energía a la máquina**.  

No obstante, se cumple el proceso inverso, vale decir, que el trabajo mecánico pueda transformarse en calor (es el caso típico del roce). Se llegaría a la siguiente expresión para la entropía irreversible en tal caso: 

$$\Delta S_\text{irreversible}=\frac{W}{T_2}$$


## Máquina de Carnot 

Dada la demostración anterior, para cumplir el ciclo en las máquinas se debe cumplir que: 

$$\begin{align}
\Delta E_\text{sistema}=Q_1+Q_2+W&=0\\  \\
\Delta S_\text{sistema}=\frac{Q_1}{T_1}+\frac{Q_2}{T_2}+\Delta S_\text{irreversible}&=0
\end{align}$$

Donde la primera división corresponde a la entropía transferida a la máquina desde la fuente $1$ y la segunda desde la segunda fuente. Por el otro lado, $\Delta S_\text{irreversible}$ es la entropía generada al interior de la máquina. Así, el esquema *"real"* de las máquinas cíclicas llegar a ser la siguiente: 

![[Pasted image 20231210000703.png|center|350]] 

Como la máquina quiere funcionar como un motor, entonces se necesita que la fuente caliente entrege la energía térmica ($Q_2>0$). Por el balance de entropía, implica directamente que $Q_1$ debe ser negativo.  Así, se llegan a las siguientes conclusiones: 

- Al tener $Q_1/T_1<0$ la máquina debe ceder parte de la energía $Q_2$ 

- La máquina no puede convertir el $100\%$ de $Q_2$ en trabajo (contradicción del enunciado de Kelvin-Plank) 

- La máquina no puede funcionar sin fuente fría. 

- Al despejar $Q_1$ de la variación de entropía del sistema se tendría la *"energía malgastada"* por tener que descargar la fuente fria. Mientras más irreversible es el funcionamiento de la máquina, más entropía se genera. 

- Por el otro lado, mientras mayor es la temperatura de la fuente caliente, mejor se puede aprovechar la energía. 

- Se cumple lo mismo al revez, mientras más baja es la temperatura de la fuente fría, mejor se puede aprovechar la energía. 

Así, para calcular el rendimiento se define la relación $\eta$: 

$$\eta=\frac{\text{Beneficio}}{\text{Costo}}$$

En este caso, al definir $Q_2$ como *"lo que se tiene que pagar"* y $Q_1$ como *"lo que se pagó pero no se aprovechó"* se puede reescribir todo como: 

$$\begin{align}
\eta&=\frac{\text{Beneficio}}{\text{Costo}}\\  \\
&=\frac{W'}{Q_2}\\  \\
&=1-\frac{T_1}{T_2}-\frac{T_1\Delta S_\text{irreversible}}{Q_2}<1\tag{1}
\end{align}$$

Ahora, si se toma el límite con $\Delta S_\text{irreversible}=0$ se llega a lo siguiente (notar que es un límite teórico, ya que es físicamente inalcanzable tal límite): 

$$\eta_\text{Carnot}=1-\frac{T_1}{T_2}$$ 
Es un límite muy importante, ya que impone un límite teórico que funciona **independiente de cómo la máquina éste construida y diseñada**. Por eso mismo, no tiene un carácter predictivo, solamente establece el límite de lo innalcanzable. 

El rendimiento nulo se obtiene de $(1)$, que se denomina $\eta_\text{real}=0$. En tal caso, se llega a la conclusión que se obtiene esto al cortocircuitar las dos fuentes sin realizar trabajo (algo que parece obvio si tomamos la definición original de rendimiento que está en función del trabajo).

## Refrigerador 

Son máquinas frigoríficas que operan en el sentido inverso. El flujo de la energía se invierte, llegando que $Q_1>0$ y $Q_2<0$. Luego, al ser cíclico se llega que: 

$$Q_2=-Q_1\frac{T_2}{T_1}-T_2\Delta S_\text{irreversible}$$

Así, se define la eficiencia $E$ de forma análoga al rendimiento, donde se tenía una relación costo-beneficio: 

$$\begin{align}
E_\text{real}&=\frac{Q_1}{W}=\left(\frac{1}{T_2/T_1-1}\right)\left(1-\left[\frac{T_2\Delta S_\text{irreversible}}{W}\right]\right)\\  \\
E_\text{Carnot}&=\frac{1}{T_2/T_1-1}
\end{align}$$

Notemos que es posible tener eficiencias mayores que uno, lo que significa que no cuesta mucho trabajo extraer energía cuando las fuentes frias y calientes están a temperaturas parecidas. 

## Bomba térmica 

Una máquina frigorífica se puede usar para calentar un recinto, donde el usuario se encuentra dentro de la fuente caliente, de tal forma, el valor de interés del usuario es el de $-Q_2$. Al juntar la ecuación de eficiencia y el ciclo energético se llega a lo siguiente:

$$\begin{align}
E&=\frac{Q_1}{W}\tag{Eficiencia}\\  \\
0&=Q_1+Q_2+W\tag{Ciclo energético}\\  \\
\implies -Q_2&=W(1+E)
\end{align}$$

De tal forma, es interesante deducir que es posible disipar más energía que la consumida por la máquina. 

## Ciclo de Carnot 

El funcionamiento reversible de las máquinas térmicas y frigoríficas se pueden describir mediante el ciclo de Carnot, que se recorre en sentido **negativo** para el caso de un motor y **positivo** para el caso del refrigerador. 

### Ciclo de Carnot genérico 

Se dice que el ciclo de Carnot es genérico cuando su representación es en el plano $T-S$. Aquí, **la forma no depende de la susbtancia de trabajo o material que se llena la máquina**. Todos son de la misma forma: 

![[Pasted image 20231212223837.png|center|550]]

La forma de interpretarlo es la siguiente: 

1. Inicialmente la máquina parte de la fuente fría a temperatura $T_1$. La única forma de elevar la temperatura sin *"generar"* entropía es haciendo un proceso adiabático, donde se hace un calentamiento isentrópico (corresponde a la flecha apuntando hacia arriba) 

2. Luego, alcanzada la temperatura, la máquina cede energía $Q_2$ para que la máquina, a temperatura constante, incremente su entropía. 

3. Al haber transferido la energía, se hace un proceso similar al primero. 

4. Para cerrar el ciclo, la máquina debe ceder la energía sobrante $Q_1$ a la fuente fria. 

Notemos que es posible representarlo en un plano $P-V$ si la substancia de trabajo es un gas (acordándonos que el trabajo del gas es $-PdV$). 

## Máquinas asimilables a térmicas 

En muchos de los casos reales la energía proviene de un proceso externo, vale decir, son de combustión externa. La reacción química o nuclear ocurre afuera. Por ejemplo, las reacciones nucleares, a carbón, etc. 

### Motor a explosión 

Las máquinas donde la reacción química ocurre **dentro de la máquina** se les denomina de **combustión interna**. Los motores a explosión caben dentro de estos casos: 

![[Pasted image 20231212224743.png|center|600]]

Algunas cosas a considerar son las siguientes: 

1. El motor es un sistema abierto (por la inyección y expulsión), dado que intercambia materia con el medio. 

2. Existen reacciones químicas que no conservan el número de moles.

3. El funcionamiento es irreversible. 

Por lo tanto, el funcionamiento se describe mediante $5$ etapas y es posible representarlas en un plano $P-V$. 

1. **Inyección**: El émbolo retrocede permitiendo ingreso de mezclas o aire (motor de gasolina o Diesel respectivamente). Puesto que la válvula está abierta, se emula con expansión **isobárica** (a presión constante)

2. **Compresión**: Cuando el émbolo alcanza el tope inferior se cierra la válvula y se comprime, haciendo que se caliente el proceso. Modela un proceso **adiabático** (no hay transferencia de calor)

3. **Combustión**: Se pueden producir de dos modos: en el caso del motor a gasolina, salta una chispa que produce ignición y hace un calentamiento **isocórico** (volumen constante). Por el otro lado, el motor Diesel hace una ignición casi instantánea donde se emula un calentamiento **isobárico**. 

4. **Expansión**: Como consecuencia de lo anterior, la cámara es empujada hacia abajo y se forma expansión **adiabática** (no hay transferencia de calor)

5. **Expulsión**: Finalmente, se abre la válvula y el pistón sube expulsando los gases quemados de forma **isobárica** (presión constante). 

![[Pasted image 20231212225439.png|center|600]] 

El proceso verde, que encierra una área nula, representa la inyección y expulsión. Acordar que el área representa $PdV$, vale decir, el trabajo. 

## El computador como una máquina 

Los computadores al fin y al cabo son una máquina, y como toda máquina física, estás consumen energía y están sujetas a las leyes de la física. De tal manera, se instalan aspectos deseables de los computadores: 

- **Tamaño**: Mientras más reducido mejor, aumentar la densidad de componentes. 

- **Consumo de energía**: Mientras menor consumo de energía mejor. 

- **Tasa de procesamiento**: Mientras más procesamiento, mejor. 

### La tendencia de Moore 

Gordon Moore, uno de los cofundadores de Intel, observó en 1965 que la tendencia era que el número de componentes de un microprocesador se duplique cada dos años. Notemos que los componentes computacionales están hechos de transitores y por lo tanto, interesa ver como se van comprimiendo cada vez la cantidad de transiciones. Para tal aspecto, se han ido reduciendo el tamaño de estos 

![[Pasted image 20231212230218.png|center|550]]

La tendencia indica una reducción con el tiempo por la siguiente ecuación: 

$$c(t)=c_0\exp(-t/\tau_c)$$

Sin embargo, se espera que a $2040$ el tamaño de los transistores alcance un valor cercano a las distancias interatómicas, que es algo muy difícil de lograr. 

### La tendencia de Koomey 

En $2011$, Jonathan Koomey, et. al publicarón un trabajo sobre la eficiencia energética en los computadores. Nuevamente se ve una tendencia que el número de cálculos por unidad de energía utilizada se dobla cada año, teniendo el siguiente comportamiento: 

$$r=r_0\exp(t/\tau_p)$$

### El límite de Landauer 

Rolf Landauer se enfocó en el problema de la destrucción de la información, lo que ocurre inveitablemente al borrar un bit: 

![[Pasted image 20231212230716.png|center|600]] 

Si vemos tal caso, se llegaría que la diferencia de entropía sería $\Delta S=-k_B\ln2<0$. Aunque esto viola la segunda ley de la termodinámica, lo que llega al siguiente dilema: 

- O bien la segunda ley no se cumple dentro de las memorias 

- O bien no es posible borrar una memoria 

- O bien el sistema no está aislado 

Por la segunda ley, se concluye que el sistema no es aislado e implica que la entropía del medio aumenta en por lo menos la misma magnitud de reducción. Así, Landauer establece que: 

$$\Delta S_\text{1 bit}=k_B\ln 2$$

Es la entropía mínima al borrar un bit de memoria. La transferencia de entropía al medio, que se encuentra a temperatura $T>0$ involucra una transferencia térmica desde la memoria hacia el medio: 

$$Q_\text{1 bit}=T\Delta S_\text{1 bit}=k_BT\ln 2$$

$Q_\text{1 bit}$ representa la energía mínima necesaria para borrar un bit de memoría, que a temperatura ambiente es $10^{-21}J$. 

Notemos que procesar información también aniquila información, se puede ver bajo el siguiente ejemplo: 

![[Pasted image 20231212231229.png|center|600]] 


La operación suma, al ser totalmente irreversible, hace que sea imposible determinar la entrada $A$ y $B$, así, genera entropía. Por lo tanto, lo que postula Landauer se basa en la tendencia de Koomey, que expresa el requerimiento energético para que esta *"arrastre"* hacia el medio la entropía generada: 

$$j_0\exp(-t/\tau_P)=Q_\text{1 bit}$$

De donde: 

$$t=\tau_p\ln\left(\frac{j_0}{k_BT\ln 2}\right)$$

El límite, a temperatura ambiente, se alcanzaría hacia el $2060$. 

### Límites impuestos por consideraciones energéticas 

Si bien si se hace un análisis de la física clásica, pareciera existir operaciones reversibles que no involucran energía, la mecánica cuántica si establece límites. El principio de incertidumbre de Heisenberg establece que, dado una energía $E$ y un tiempo $t$: 

$$\begin{align}
\Delta E\Delta t&\geq\hbar/2\\  \\
\Delta t&\geq\frac{\hbar}{2\Delta E}
\end{align}$$

El término $\Delta t$ se interpreta como el tiempo mínimo de un proceso y $\Delta E$ la dispersión de energía asociada al proceso. Una cota es asimilar que $\Delta E\approx E$. Ahora, ocupando la relación de Einsten, donde $E=mc^2$: 

$$\Delta t\geq\frac{\hbar}{2mc^2}$$ 
El número de operaciones máximo por segundos sería el recíproco de $\Delta t$: 

$$\frac{1}{\Delta t}\leq\frac{2mc^2}{\hbar}$$ 
Suponiendo un computador de masa igual a $1kg$, se llega que: 

$$\frac{1}{\Delta t}\leq 10^{50}s$$

Así, un computador podría llegar a procesar una tasa máxima del orden de $10^{50}$ bits por segundo por kilo de CPU, lo que debe considerarse como límite inalcanzable. 

# Física estadística 

La física estadística trata de resolver la incógnita de sistemas donde la energía no está fija. Si bien existe *a priori* que existe un valor promedio para sistemas en equilibrio térmico, por lo general el intercambio térmico es aleatorio. De aquí subyace la pregunta principal: ***¿Cuál es la probabilidad de encontrar un sistema térmico en una configuración?*** 

## Probabilidad de una configuración 

En un sistema cualquiera se tiene lo siguiente: 

$$\text{Universo}=\text{Fuente}\;\cup\;\text{Sistema}$$

Así, se define la probabilidad de encontrar el sistema en su $i$-ésima configuración como: 

$$\mathbb{P}_i=\frac{\text{Casos favorables}}{\text{Casos posibles}}$$ 
Es posible, a partir de la definición de energía y entropía, llegar a la sigiuente variable aleatoria para la configuración $i-ésima$: 

$$X(i)=C\exp(-\frac{E_i}{k_bT})$$

$C$ es una constante que está en función de la temperatura. Sabemos que por definición de la variable aleatoría: 

$$\sum_{R_i}X(i)=1$$

Por lo tanto, es posible despejar $C$ bajo el siguiente procedimiento: 

$$\begin{align}
\sum_{R_i}X(i)&=1\\  \\
C\sum_{R_i}\exp(\frac{-E_i}{k_BT})&=1\\  \\
\sum_{R_i}\exp(-E_i/k_BT)&=Z(T)\tag{Cambio de variable}
\end{align}$$

Así, la probabilidad normalizada llegaría a ser: 

$$X(i)=\frac{\exp(-E_i/k_BT)}{Z}$$

De la misma forma, como $1/k_bT$ es una constante, se puede definir como $\beta$. Reescribiendo todo, la variable aleatoria quedaría como: 

$$X(i)=\frac{\exp (-E_i\beta)}{Z}$$

Esta distribución es conocida como la **distribución de Boltzmann**. 

Así, en el ámbito de la física estadística se tienen las siguientes equivalencias: 

- Promedios: la esperanza 

- Fluctuación: La [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Varianza|varianza]]: 

$$\text{Var}(X)=E[X^2]-E[X]^2$$

Notemos que la esperanza $E[X^2]$ llegaría a ser: 

$$\begin{align}
\bar{E^2}&=\frac{1}{Z}\sum_iE_{i}^{2}\exp(-\beta E_i)\\  \\
&=\frac{1}{Z}\sum_i\frac{\partial^2}{\partial\beta^2}\exp(-\beta E_i)\\  \\
&=\frac{1}{Z}\frac{\partial^2Z}{\partial\beta^2}
\end{align}$$

Donde $E_i$ es un elemento del rango $R_x$. 

Si se reemplaza todo, la varianza llega a ser la siguiente: 

$$\text{Var}(X)=\frac{\partial^2}{\partial\beta^2}(\ln Z)$$

- Desviación cuadrática media: La [[Desviación estandar|desviación estándar]] 

$$\sqrt{Var(X)}$$ 
Por la definición anterior de varianza, si se tiene $N$ elementos dentro del rango, entonces la desviación estándar llegaría a ser: 

$$\sigma(E_n)=N\cdot\text{Var}(X)$$ 
De aquí, se desprende que: 

$$\text{Var}(X)=\sqrt{N}\;\text{Var}(E_1)$$

Si se toma el cuociente entre ambos, se llega a una relación del orden $N^{-1/2}$. Esto significa, básicamente, que la varianza del sistema disminuye al crecer el sistema en razón $N^{-1/2}$. 

## Entropía y función de Helmholtz

Dado que la entropía y función de Helmholtz dependen de la suma de estados, es posible dejarlo como una variable aleatoria. 

La función de Helmholtz fue originalmente definida como $F=E-TS$. No obstante, se quiere trabajar con la esperanza de la energía, así, $F=\mathbb{E}[E]-TS$. De la probabilidad disjunta se tenía que: 

$$\mathbb{P}=\frac{\Omega_F(E_0-E_i)}{\Omega_U}\tag{1}$$ 
Donde $E_0$ es la energía total del universo. Puesto que la energía de la fuente es $E_0-\mathbb{E}[E]$, la del sistema es $\mathbb{E}[E]$ y $\Omega_U=\Omega_F\Omega_S$: 

$$\begin{align}
\Omega_U&=\Omega_F(E_0-\mathbb{E}[E])\cdot\Omega(\mathbb{E}[E])\;\;\;/k_B\ln()\\  \\
S_U&=S_F(E_0-\mathbb{E}[E])+S(\mathbb{E}[E])
\end{align}$$

Si se toma el logaritmo natural de $(1)$ se puede escribir también: 

$$\begin{align}
k_B\ln(\mathbb{P})&=S_F([E_0-\mathbb{E}[E]]+[\mathbb{E}[E]-E_i])-S_F(E_0-\mathbb{E}[E])-S(\mathbb{E}[E])
\end{align}$$

Ahora, como $\mathbb{E}[E]-E_i$ es pequeño se puede hacer un Taylor en torno a $E_0-\mathbb{E}[E]$:

$$k_B\ln(\mathbb{P})=\frac{\mathbb{E}[E]-TS(\mathbb{E}[E])}{T}-\frac{E_i}{T}$$

Ahora, si lo dejamos en función de la función de Helmoltz queda de la siguiente forma: 

$$\mathbb{P}=\exp(\beta F)\exp(-\beta E_i)$$

También es posible dejar la función de Helmotz en función de la suma $Z$: 

$$F=-k_BT\ln(Z)$$ 
Por último, la entropía en función de la suma de estados: 

$$S=\frac{\mathbb{E}[E]}{T}+k_B\ln(Z)$$

# Teoría cinética de los gases 

La teoría cinética consiste en determinar el comportamiento de los gases en términos de la cantidad de moléculas que se encuentran a una cierta velocidad. 

Se consideran que las moléculas son puntuales e independientes. 

## Partícula encerrada en una caja 

Considerando una partícula libre en una caja de volumen $V$ que sólo tiene energía cinética. Está caracterizada por tres coordenadas y tres velocidades. La energía asociada se expresa en función de esas seis variables bajo la distribución de Boltzmann $E=E(\vec{x},\vec{v})=mv^2/2$. Así, aplicando la definición de CDF: 

$$\begin{align}
Z_1&=\int_{\text{vol},\vec{v}\;\in\;V,\mathbb{R}^3}\exp(-\beta m\vec{v^2}/2)\;dx\;dv\\  \\
&=\int_{\text{vol}\in V}dx\int_{\vec{v}\in\mathbb{R}^3}\exp(-\beta m\vec{v^2}/2)\;dv
\end{align}$$

La primera integral es simplemente el volumen del sistema, se denominará $Z_V$. La segunda se puede calcular al al notar que $v^2=v_{x}^{2} + v_{y}^{2} + v_{z}^{2}$, pudiendo separarse en tres integrales iguales, lo que es equivalente a tener una de ellas elevada al cubo: 

$$\begin{align}
Z_E&=\int_{\vec{v}\in\mathbb{R}}\exp(-\beta m\vec{v^2}/2)dv\\  \\
&=\left[\int^{\infty}_{-\infty}\exp(-\beta mv_{x}^{2}/2)\;dv_x\right]^3\\  \\
&=\left(\frac{2\pi}{m\beta}\right)^{3/2}
\end{align}$$

Así, la suma de estados para una partícula libre encerrada en una caja de volumen $V$ llegaría a ser: 

$$Z_1=V\left(\frac{2\pi k_BT}{m}\right)^{3/2}=V\left(\frac{2\pi}{m\beta}\right)^{3/2}$$ 
La energía cinética se calcula al obtener la esperanza, arrojando que: 

$$\mathbb{E}[E_1]=\frac{3}{2}k_BT\;\;\land\;\;\mathbb{E}[v^2]=\frac{3k_BT}{m}$$ 
Notar que la fluctuación relativa (varianza) llegaría a er: 

$$\text{Var}(E)=(k_BT)^{1/2}$$ 
## Distribución de velocidades de Maxwell-Boltzmann 

Ahora se quiere determinar la probabilidad en función de las seis coordenadas (la posición y velocidad). La PDF llegaría ser de la siguiente forma: 

$$P(\vec{x},\vec{v})=\frac{1}{Z}\exp\left(-\frac{mv^2}{2k_BT}\right)$$

La probabilidad de encontrar la partícula en un volumen $V$ siempre es la misma, por lo tanto, sólo interesa encontrar la velocidad, que llegaría a ser la siguiente: 

$$P(\vec{v})=\frac{1}{Z_E}\exp\left(-\frac{mv^2}{2k_BT}\right)dv=f_1(\vec{v})dv$$

Notemos que $f_1(v)$ es la **distribución de Maxwell-Bolztmann**, que puede ser reescrita como: 

$$f_1(\vec{v})=\left(\frac{m}{2\pi k_BT}\right)^{3/2}\exp\left(-\frac{mv^2}{2k_BT}\right)$$ 
Finalmente, si se considera un gas ideal con $N$ partículas independientes que no interactuan entre ellas, entonces el número de moléculas con velocidades $\vec{v}$ llegaría a ser simplemente $Nf_1$ (multiplicar la variable aleatoria $N$ veces). 

Por lo general la forma más fácil de trabajar con esta distribución es con coordenadas esféricas.

### Velocidad más probable 

Sea $M\sim\text{Maxwell-Boltzmann}$, entonces, al aplicar condición de primer orden en la PDF se llega que la **velocidad más probable es**: 

$$v_{MP}=1,414\left(\frac{k_BT}{m}\right)^{1/2}$$ 
### Esperanza 

La esperanza de la distribución llegaría a ser: 

$$\mathbb{E}[M]=1,596\left(\frac{k_BT}{m}\right)^{1/2}$$ 
### Esperanza cuadrática 

La esperanza al cuadrado, que llegaría a ser útil para el cálculo de la varianza, llegaría a ser: 

$$\mathbb{E}[M^2]=1,732\left(\frac{k_BT}{m}\right)^{1/2}$$ 
## Teorema de equipartición de energía 

Es posible considerar un sistema donde la energía depende cuadráticamente de $N$ variables: 

$$E(x_1,x_2,\dots,x_N)=\sum^{N}_{i=1}a_ix_{i}^{2}$$ 
Con $a_i$ constantes positivas. La constante $Z_i$ de la suma sobre estados se obtiene facilmente al integrar sobre un estado: 

$$Z_i=\int^{\infty}_{-\infty}\exp(-\beta a_ix_{i}^{2})\;dx_i=\left(\frac{\pi}{\beta a_i}\right)^{1/2}$$ 
Ahora, como las distribuciones de energía son independientes, entonces $Z=Z_1Z_2\dots Z_n=\pi^{N/2}/[/\beta a_1)(\beta a_2)\dots(\beta a_N)]^{1/2}$. Ahora, al utilizar la esperanza, la energía esperada es: 

$$\mathbb{E}[E]=\frac{N}{2}k_bT$$ 
Se llama el **teorema de equipartición de la energía**: 

>*A cada grado de libertad cuadrático le corresponde una energía promedio de $k_BT/2$*

### Éxitos del teorema de equipartición 

El teorema tiene éxito en las moléculas **monoatómicas** dado que tienen sólo tres grados de libertad. La energía promedio por mol llegaría a ser $3N_Ak_BT/2$ y su capacidad térmica llegaría a ser $3/2 R$: 

$$c_V=\left(\frac{\partial\mathbb{E}[E]}{\partial T}\right)_V=\frac{3}{2}R$$

Otro éxito se encuentra en moléculas **diátomicas rígidas**, vale decir, aquellas donde hay un enlace químico fuerte. La molécula, además de las tres traslaciones puede rotar, aunque el momento de inercia de cada molécla se anula de modo que hay sólo cinco grados de libertad. 

$$c_V=\left(\frac{\partial\mathbb{E}[E]}{\partial T}\right)_V=\frac{5}{2}R$$

![[Pasted image 20231215121538.png|center|500]] 

No obstante, el modelo falla en moléculas flexibles o aquellas no colineales. De hecho, los grados de libertad en las moléculas más complejas tienen estados internos que no son cuadráticos y también que la distribución de Maxwell-Boltzmann es una aproximación. Por esto mismo, para un sólido de $N_A$ átomos el teorema se cumple bajo algunas suposiciones. 

## Colisiones con las paredes del recipiente 

Ahora, considerar la situación donde el recipiente contiene un gas con un pequeño orificio por el cual las moléculas pueden escapar. Se determinará la tasa de escape por unidad de área y tiempo. 

![[Pasted image 20231215124105.png|center|550]] 


El área se denominará $A$ y se considerará un cilindro oblicuo imaginario de longitud $v\Delta t$, donde $v$ es una velocidad molecular cualquiera y $\Delta t$ un intervalo temporal. El cilíndro está inclinado a una altura $\theta$, por lo que el volumen llegaría a ser: 

$$\Delta V=Av\Delta t\cos\theta$$ 
Además, se define la *densidad de partículas* como: 

$$n=\frac{N}{V}$$ 
Por lo que el volumen de moléculas en el volumen de cilindro lelgaría a ser: 

$$\Delta N=n\Delta V=nAv\Delta t\cos\theta$$ 
### Efusión 

Ahora, para considerar la probabilidad que la molécula choque contra el sector cilíndrico se considerarán las siguientes condiciones: 

$$\text{Estar dentro del cilíndro}\;\land\;\text{Moverse en torno a}\;\vec{v}$$ 
Luego, la probabilidad de choque llegaría a ser el número de partículas en el volumen por la probabilidad que sus velocidades se encuentren en torno a $\vec{v}$. Si $\Delta N$ es la variable aleatoria que representa la PDF de esto: 

$$\Delta N_\text{colisiones}=(nAv\Delta t\cos\theta)f_1(\vec{v})v^2\sin\theta$$

Es posible reemplazar $f_1$ por $f_2(v)=4\pi v^2f_1(\vec{v})$, por lo que se puede escribir: 

$$\Delta N_\text{colisiones}=\frac{nA\Delta t}{4\pi}\cos\theta vf_2(v)\sin\theta$$

Para obtener $\Delta N$ colisiones, vale decir, el número total de partículas que chocan contra el sector de área $A$ en un tiempo $\Delta t$, entonces hay que integrar con respecto a las coordenadas esféricas. Así, se llega que la tasa de efusión es: 

$$\begin{align}
J_N&=\frac{dN_\text{efusión}}{dA\;dt}\\  \\
&=\frac{\Delta N_\text{colisiones}}{A\Delta t}\\  \\
&=\frac{1}{4}n\bar{v}\\  \\
&=\frac{P}{\sqrt{2\pi mk_BT}}
\end{align}$$

### Presión colisional 

Ahora se calculará la fuerza y por ende la presión ejercida por las moléculas que chocan contra la superficie. Acá, se considerará la siguiente figura: 

![[Pasted image 20231215125854.png|center|550]] 


Donde la partícula colisiona elásticamente con la pared. rebota con un ángulo $\theta$. Al aplicar la definición anterior de efusión es posible determinar que la presión llegaría a ser: 

$$P=\left(\frac{N}{V}\right)k_BT$$

Que coincide con la expresión del gas ideal. 

## Propiedades de transporte 

A partir de ahora se considerarán modelos con colisiones entre moléculas: 

![[Pasted image 20231215184217.png|center|450]] 

Si se consideran que las moléculas tienen forma esférica, su sección transversal sería $2\pi r^2$. Así, dada la figura, las moléculas chocaran si están dentro de un cilíndro de radio $2r$ con sección de área $\sigma=4\pi r^2$. 

![[Pasted image 20231215184350.png|center|520]] 

Así, se definira el camino libre del medio $\lambda$ como la distancia recorrida por una molécula entre dos colisiones sucesivas con otras moléculas y el tiempo medio entre colisiones $\tau$ de forma análoga. 

Si suponemos una densidad de partículas $n=N/V$, en un tiempo $t$ la molécula habrá barrído un volumen $vt$. Entonces, chocará con todas las moléculas que se encuentren entre $\sigma vt$ y el número de colisiones será $n\sigma vt$. Así, se puede obtener $\tau$ como: 

$$\tau=\frac{1}{n\sigma\bar{v}}$$ 
También se puede definir la frecuencia de colisiones por unidad de volumen: 

$$\lambda=\frac{1}{n\sigma}$$



