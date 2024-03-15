
## Definiciones termodinámicas 

>[!danger] Sistema físico 
>Se entiende por *sistema físico* como una región del espacio bajo estudio, con todo lo que contiene. Su frontera se clasificará mediante la sigla $\Sigma$. 
>
>Para efectos del curso, no se analizará la frontera bajo su definición matemática *per se*, aunque podría ser útil a futuro. 
>
>Se dice que un sistema es **aislado** cuando el sistema no interactua con otros sistemas. 

>[!error] Medio 
>
>Se entiende por tal conjunto de todos los otros sistemas que interactúan de manera apreciable bajo el estudio. 

>[!danger] Universo local 
>
>Es básicamente el conjunto del sistema y el medio. Es trivial notar que el sistema es subconjunto del medio, y así, el universo se llegaría a definir como: 
>
>$$U=M\cup S$$

Se entenderá como definición de magnitud como aquella propiedad de un sistema que puede ser expresada cuantitativamente. Por lo mismo, se definirán las magnitudes **extensivas** e **intensivas**. 

>[!example] Magnitud extensiva 
>Se entiende como magnitud extensiva aquellas que están asociadas a la **masa**. Por ende, son aquellas que **están contenidas dentro del sistema**. Lo más importante de estas magnitudes es que, al estar asociados a un volumen y masa, tienen una densidad y son aditivas. Algunos ejemplos particulares son: 
>
>- La densidad de masa 
>
>- La densidad de carga $\Phi$
>
>- La energía 
>
>- Número de partículas 
>
>- Momentum 
>

>[!example] Magnitudes intensivas 
>
>Son aquellas magnitudes que se diferencian de las extensivas. No están asociadas a un sistema y no son transportables. 

>[!example] Estado 
>Se dice que un sistema se encuentra en un estado si es posible proveer un listado suficiente de **magnitudes físicas**, haciendo alusión a que el resto de las magnitudes pueden ser derivadas a partir de estas. 

## Segunda Ley de la Termodinámica 

Esta ley trata, fundamentalmente, sobre la reversibilidad e irreversibilidad de los sistemas macroscópicos. 

Como introducción es importante definir la noción de tiempo para sistemas termodinámicos. 

![[Captura de pantalla 2023-10-17 a la(s) 14.14.54.png|center]]

Dado el sistema esbozado, es fácil decir en la primera situación que el sistema se encuentra en $t=t_1$. Sin embargo, si sólo se pudiera ver la segunda situación, sería difícil o imposible determinar en que tiempo se está. 

Lo mismo ocurre en la situación del lanzamiento de un proyectil: dado un lanzamiento con una velocidad dada, es posible determinar su posición de caida y el tiempo que éste demora en caer. No así al revés, vale decir, a partir de la posición de caída determinar el tiempo de vuelo o velocidad inicial. 

Por lo general, en un sistema aislado con una ligadura, **siempre se cumple que** 

$$\Omega_2=\Omega_1+\text{Nuevas configuraciones accesibles}$$

A partir de esto, bajo una equivalencia, es posible decir que para un sistema aislado ocurre que: 

$$S_2\geq S_1\tag{Sistema aislado}$$

Esto da a conocer la **segunda Ley de la Termodinámica**, que puede ser planteada de las siguientes formas equivalentes: 

- En un sistema aislado, la entropía nunca decrece 
- La entropía se puede crear, pero no se puede aniquilar. 
- Puesto que el universo local es un sistema asilado, la entropía del universo local nunca decrece 

### Reversibilidad e irreversibilidad física 

Es importante hacer la distinción entre los procesos reversibles e irreversibles, pues es una hipótesis **muy importante** para que se llega a cumplir la sucesión de eventos de implicancias: 

$$A\implies B$$

>[!example] Reversibilidad 
>
>Un sistema aislado experimenta un **proceso reversible** si y solo sí es capaz de regresar por sí mismo al estado original. Esto en teoría es posible en la teoría microscópica, pero en base a la estadística es algo **muy improbable** 

Sabemos, por probabilidad, que para que un sistema pueda retornar a su estado inicial, **debe tener la misma cantidad de configuraciones iniciales y finales**: 

$$P_\text{retorno}=\frac{\Omega_1}{\Omega_2}$$

Por ende, es verídico decir que **en los procesos reversibles la entropía final es la misma que la inicial**: 

$$\text{Reversible}\iff\Omega_1=\Omega_2\iff S_1=S_2$$

Recíprocamente, en los procesos irreversibles se crea entropía. 

### Sistema que interactua con el medio 

Es importante hacer la distinción en la segunda Ley con los sistemas que interactuan en los medios con un universo local aislado. 

La segunda ley plantea que **la entropía del universo no decrece**. Sin embargo, es posible que ocurran ambiguedades que no necesariamente violen este principio. 

Acordándonos de la definición de universo, como $\text{Universo}=\text{Sistema}\cup\text{Medio}$, entonces es posible estar bajo la siguiente situación: 

$$S_U(1)\leq S_U(2)\tag{Segunda ley}$$

No obstante, dada la definición de universo, es posible separar la entropía en dos elementos: 

$$S_\text{Sistema}(1)+S_\text{Medio}(1)\leq S_\text{Sistema}(2)+S_\text{Medio}(2)$$ 
Y esto da la libertad a conducir que: 

$$S_\text{Medio}(2)=S_\text{Medio}(1)+\Delta S\;\;\;\;\;\Delta S>0$$

Esto da para la interpretación que un sistema *puede disminuir su propía entropía* a costa del medio. 

También, por el otro lado, es posible hacer el análisis para **sistemas cíclicos**. Podemos asumir que se tiene un sistema de tres estados, donde realiza un proceso irreversible, vale decir; 

$$S_U(1)\leq S_U(3)$$

Sin embargo, el sistema retorna al estado original. *¿Cómo es posible?*. Notemos que se tiene, por segunda ley que: 

$$\Delta S_U=\Delta S_\text{irr}>0$$

Entonces, desglosando la definición de universo, se cumple que: 

$$\Delta S_\text{ciclo}+\Delta S_\text{medio}=\Delta S_U=\Delta S_\text{irr}$$

Dado que en un proceso cíclico la entropía es nula, entonces se establece que: 

$$\Delta S_\text{medio}=\Delta S_U=\Delta S_\text{irr}$$

De aquí se concluye que **un sistema que interactúa con el medio puede disminuir su entropía**, siempre cuando la entropía del ambiente aumente en igual magnitud. 

## Energía: trabajo y calor 

Antes de definir el trabajo para sistemas macroscópicos, es necesario imponer condiciones generales que subyacen de la definición del proceso cuasiestático. 

>[!example] Proceso cuasiestático 
>
>Se define un proceso cuasiestático como aquel en que tanto el estado inicial, final y todos los estados intermedios **son de equilibrio**. Esto es una idealización. 

A partir de esto, existen diferencias notables entre el trabajo cuasiestático y no cuasiestático. 

- En los procesos cuasiestáticos los estados intermedios son de equilibrio, por lo tanto, variables como la presión $P$ mantienen un valor constante y que no varía en el tiempo. 


Notemos, de la definición fundamental de trabajo, que se tiene lo siguiente: 

$$W=\int\vec{F}\cdot dl$$

Ahora, si vemos la fuerza que el medio ejerce sobre un sistema, es posible acordar la definición de presión, que es definida como fuerza por unidad de área. Luego, se tiene que $F=PA$. Puesto que un sistema se desplaza una cantidad $dx$ ante el impacto, de forma paralela a la fuerza, se llega que: 

$$w=Fdx=PAdx$$

Notemos que la variación del volumen es negativo a $Adx$, de hecho, cuando se le ejerce presión a un embolo este reduce su volumen. Entonces, se llega a la conclusión principal que 

$$w=-PdV$$

Notar que a través de esto, es posible describir un proceso cuasiestático por medio de la presión y el volumen, al estar todas las variables en equilibrio. Luego; 

- Cualquier punto en el plano $PV$ es un estado de equilibrio.

- Todo estado de equilibrio es un punto del plano $PV$

- Un proceso cuasiestático se representa como una curva continua en el plano $PV$. 

Una conclusión más fundamental aun, es que **el área bajo la curva del plano $PV$ representa el inverso aditivo del trabajo.** 

![[Captura de pantalla 2023-10-17 a la(s) 14.45.33.png|center]]


### Trabajo cíclico 

Si nos fijamos en un proceso cíclico, donde el estado inicial es igual al final, es posible elegir arbitrariamente el punto de inicio y final tal que estos puedan unir el proceso. 

Sin embargo, algo a notar a partir de la conclusión anterior, es que el área bajo la curva representa el inverso aditivo del trabajo. Si se llegase a tener un proceso cíclico, entonces se estaría barriendo el área bajo la curva en sentido horario y en sentido antihorario. Esto es importante notar, ya que una parte del trabajo se anularía. 

### Calor 

El concepto físico del calor que es el actual nace del experimento de Joule, que consiste en verificar si esta variable posee masa, volumen y si puede ejercer trabajo. De esto se llego a un resultado fundamental: 

1. Una unidad de trabajo mecánico produce siempre el mismo aumento de temperatura del agua. Entonces existe una relación definida entre trabajo y calor. 

2. La unidad de energía para calentar el agua es siempre constante. 

Por lo tanto, el calor se define como *energía que pasa de un cuerpo a otro y es causa de que se equilibren las temperaturas*.

## Primera ley de la termodinámica 

A partir del concepto del trabajo y calor, se pudo consolidar la primera ley de la termodinámica, concepto que es un axioma. Esta plantea que la energía siempre se conserva. En términos termodinámicos es equivalente a decir que: 

- La energía del universo local es constante. 

- En un sistema aislado, la energía es constante. 

- La energía no se puede crear ni destruir. 

Notemos que, en términos matemáticos, es posible dejar todo esto en función de un sistema que evoluciona entre estados. De tal manera, es posible escribir lo siguiente: 

$$dE=q+w$$

Es decir, la variación de energía corresponde al **calor** y **trabajo**. Ahora, lo que podría llegar a ocurrir en el caso **cuasiestático** es que se llege a la siguiente igualdad: 

$$dE=q-PdV$$


## Temperatura absoluta 

En este capítulo se trata de ver como la energía es distribuida entre dos sistemas en equilibrio térmico. 

A través de repetidos experimentos se pudo percatar que dos sistemas ante una interacción térmica tienden a llegar a la misma temperatura. De hecho, la energía se llega a distribuir entre ellos. 

Por la primera Ley de la termodinámica, se debe cumplir que: 

$$E_A+E_B=E_o$$

Por el otro lado, la segunda Ley establece que la entropía del universo debe estar representada como: 

$$S_U=S_A(E_A)+S_B(E_B)$$

Si expresamos $E_B$ en función de $E_A$: 

$$S_U=S_A(E_A)+S_B(E_B=E_o-E_B)$$

Si se deriva todo respecto a $A$, dejando el volumen constante, se llega a lo siguiente: 

$$\frac{\partial S}{\partial E}\bigg\vert_A=\frac{\partial S}{\partial E}\bigg\vert_B\tag{Condición de equilibrio}$$

De aquí se desprende que, para que un sistema esté en equilibrio, deben compartir la propiedad: 

$$\left(\frac{\partial S}{\partial E}\right)_V$$

De aquí nace la **definición de la temperatura absoluta**, que plantea que: 

$$\frac{1}{T}=\left(\frac{\partial S}{\partial E}\right)_V$$

Es posible también plantear el recíproco correctamente: 

$$T=\left(\frac{\partial E}{\partial S}\right)_V$$

Notemos que la entropía **siempre es creciente**, entonces la temperatura **siempre es positiva**. Es una definición directa que sale de la derivada parcial. 

### Capacidad térmica 

Por el otro lado, se establece una medida cuantitativa para cada material para cuantificar su almacenamiento. 

#### Capacidad térmica a volumen constante 

Se postula que un sistema tiene una capacidad térmica $C_V$ si su proceso de transferencia térmica, a volumen constante, se escribe como: 

$$C_V=\left(\frac{q_V}{\Delta T}\right)$$

Notemos que para un proceso cuasiestático se tiene que: 

$$\Delta E=q_v+\cancelto{0}{w_v}$$

Al tener que el volumen es constante, entonces $PdV=0$. 

Además, se cumple que: 

$$\lim_{\Delta T\to 0}\left(\frac{\Delta E}{\Delta T}\right)=\left(\frac{\partial E}{\partial T}\right)$$

Por definición de derivada. Por lo tanto, es posible poner que: 

$$C_V=\left(\frac{\partial E}{\partial T}\right)$$

#### Capacidad térmica a presión constante 

Análogo al proceso anterior, se define como: 

$$C_P=\left(\frac{q_P}{\Delta T}\right)$$

En este caso no se cumple que el trabajo se va a cero, sin embargo, ocupando la misma igualdad se tiene que: 

$$q_P=\Delta E+P\Delta V$$

Luego, es posible reescribir la capacidad térmica como: 

$$C_P=\left(\frac{\Delta E}{\Delta T}\right)+\left(\frac{P\Delta V}{\Delta T}\right)$$

Nuevamente, al tomar el límite de $\Delta T\to 0$, se llega que: 

$$C_P=\left(\frac{\partial E}{\partial T}\right)+P\left(\frac{\partial V}{\partial T}\right)$$
### Calor específico 

El concepto de calor específico llegaría simplemente a ser la capacidad térmica por unidad de masa, vale decir; 


$$\begin{align}
c_v&=\frac{C_V}{M}\\  \\
c_p&=\frac{C_P}{M}
\end{align}$$

### Transferencia reversible de entropía 

Es posible imaginar una situación donde se tiene un sistema que interactúa con el medio a través de un proceso reversible. Esto implicaría directamente que no se crea entropía: 

![[Captura de pantalla 2023-10-17 a la(s) 15.12.28.png|center]]

Dado el desarrollo de la energía $E(S,V)$ en series de Taylor, es posible llegar que: 

$$dE=TdS+\left(\frac{\partial E}{\partial V}\right)_SdV$$

Donde la temperatura se obtuvo al ocupar la definición de temperatura. 

Ahora, al estar en un proceso reversible, también se sabe que: 

$$\begin{align}
dE&=q_\text{rev}+w_\text{rev}\\ \\
&=q_\text{rev}-PdV\end{align}$$

Si se restan ambas ecuaciones se llega que: 

$$(TdS-q_\text{rev})+\left[\left(\frac{\partial E}{\partial V}+P\right]\right)dV=0$$

Esto es una identidad, por lo tanto, eligiendo convenientemente $dV=0$ se llega que: 

$$dS_\text{rev}=\frac{q_\text{rev}}{T}$$

Puesto que no se crea entropía, es posible decir que la entropía transferida por el sistema al medio es igual y de signo contrario. 