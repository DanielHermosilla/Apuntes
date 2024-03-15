
# Electrostática 

La electrostática hace referencia a cualquier evento de la electrodinámica donde las cargas y partículas a analizar se mantienen en reposo. De ahí, el sufijo de *estática*. 

## Ley de Coulomb 

>[!danger] Ley de Coulomb 
>
>La ley de Coulomb es la ley fundamental de la electrostática, dado que relaciona la fuerza de interacción entre cargas eléctricas. Su forma y expresión tiene cierto símil con la fuerza de atracción gravitacional.  
>
>
$$\vec{F}=\frac{1}{4\pi\epsilon_0}\frac{qQ}{\vert\vert r-\vec{r'}\vert\vert^2}\cdot\frac{(\vec{r}-\vec{r'})}{\vert\vert \vec{r}-\vec{r}'\vert\vert}$$

Notar que la expresión del denominador corresponda a la **norma euclidiana**, por lo tanto, se puede simplificar a: 

$$\vec{F}=\frac{1}{4\pi\epsilon_0}\cdot\frac{qQ(\vec{r}-\vec{r'})}{(r^2+r^{'2})^{\frac{3}{2}}}$$ 
Todo esto, en dirección radial entre las cargas. 


```tikz 
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}

% Definimos las posiciones de las cargas
\coordinate (q) at (-2,0);
\coordinate (Q) at (2,0);

% Dibujo de las cargas
\fill[red] (q) circle (0.5cm) node[white] {$q$};
\fill[blue] (Q) circle (0.5cm) node[white] {$Q$};

% Fuerza de interacción
\draw[-stealth, thick, green!60!black] (q) + (0,0.5) -- (-1,0.5) node[midway,above] {$\vec{F}$};
\draw[-stealth, thick, green!60!black] (Q) + (0,0.5) -- (1,0.5) node[midway,above] {$\vec{F}$};

% Vector de posición
\draw[-stealth, thick, purple] (q) -- (Q) node[midway,below] {$\vec{r}-\vec{r'}$};

\end{tikzpicture}


\end{document}
```

## Principio de superposición 

Tanto para el cálculo de campos eléctricos y fuerzas, es fundamental definir el principio de superposición. Este establece que ante una distribución de cargas cualquiera (ya sea lineal, volumétrica, etc) se puede superponer las cargas.

Un ejemplo simple es el de la esfera; tomemos una partícula ubicada en $P$ y una superficie con densidad de superficie $\sigma$:
![[superposition.png|center|500]]Lo que nos representa la densidad $\sigma$ es la siguiente igualdad: 

$$\sigma=\frac{Q}{\text{Área}}$$

Por lo tanto, si se quisiera calcular la carga eléctrica en la superficie, se puede llegar a la siguiente igualdad: 

$$\int_A\sigma\;dA=Q$$

De tal forma, es posible calcular la fuerza de Coulomb ejercida por la superficie. 

<div style="page-break-after: always;"></div>

## Campo eléctrico 

>[!error] Campo eléctrico 
>
>El campo eléctrico para una carga puntual se define de la siguiente forma:
>
>$$\vec{E}(r)=\frac{1}{4\pi\epsilon_0}\cdot\frac{q}{r^2}\hat{r}$$ 
>
>Como su nombre lo indica, es un campo vectorial que representa la presencia de cargas eléctricas. De hecho, el flujo se ve representado por la siguiente ecuación: 
>
>$$\Phi_E=\int^{}_{S}E\cdot da$$

Notemos que los flujos se definen en función de una superficie, por eso la integral está en función de $S$, representando la superficie. De hecho, a partir de esta idea es donde nace la **ley de Gauss**. 
![[campoElectrico.png|center|650]]

## Ley de Gauss 

Para una superficie, se define el campo eléctrico como: 

$$\oint E\cdot dA=\frac{Q_{enc}}{\epsilon_0}$$

Vale decir, basta definir una superficie cualquiera para poder determinar su campo eléctrico. Notar que el $dA$ equivale a un diferencial de área, vale decir, $\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv=dA$, donde $\vec{F}$ es la parametrización de la superficie elegida. Por eso, **es recomendable saberse las diferenciales de áreas**: 

![[surface_portion.png|center|400]]
- **Esferas**: Ocupando coordenadas esféricas, se llega que: 

$$dA=r^2\sin(\theta)d\theta\;d\phi\;\;\;\;\;\;\;\theta\in[0,\pi]\;\land\;\phi\in [0,2\pi]$$

Esta superficie se debe ocupar cuando el campo eléctrico es radial. Si se tiene una esfera perfecta, el diferencial de área llegaría a ser únicamente $4\pi r^2$. 


![[esfera 1.png|center|250]]


- **Cilíndrica:** Aca la integral se divide en una suma de integrales, tanto para la tapa como para las superficies laterales, vale decir: 

$$\begin{align}\oint E\cdot dA&=\int_{\text{Superficie lateral}}E\cdot dA'+\int_{\text{Tapas}}E\cdot dA''\end{align}$$

En este caso, los diferenciales de área llegarían a ser: 

$$\begin{align}\oint E\cdot dA&=\int_{\text{Superficie lateral}}E\cdot R\;d\phi\;dz+\int_{\text{Tapas}}E\cdot r\;dr\;d\theta\end{align}$$

El cilíndro normalmente se ocupa en problemas bidimensionales, donde se tienen cables infinitos o cosas por el estilo. Si se tiene un cilindro perfecto el diferencial de área de la tapa llegaría a ser $\pi r^2$ y $2\pi rh$ para la superficie lateral.


![[cilindro.png|center|250]]


Al aplicar teoremas de divergencia se llega a la **ley de Gauss diferencial**, donde simplemente se ocupan operadores de divergencia y el *Teorema Fundamental del Cálculo*: 

$$\nabla\cdot E=\frac{1}{\epsilon_0}\rho$$

Acordándonos de la definición de divergencia, esto llegaría a ser **la suma de las derivadas parciales de cada componente del campo eléctrico**. 

## Potencial del campo eléctrico 

Supongamos que se tiene una carga puntual con su respectivo campo eléctrico. *¿Qué pasaría si la partícula se mueve de un punto $a$ hacia un punto $b$?*. Por lo general, se puede realizar su integral de línea: 

$$\int^{b}_{a}E\cdot dl$$

Sabemos que al ocupar coordenadas esféricas, se tiene que: 

$$dl = dr\;\hat{r}+rd\theta\;\hat{\theta}+r\sin\theta d\phi\;\hat{\phi}$$

Por ende, se llega que el producto punto es: 

$$E\cdot dl=\frac{1}{4\pi\epsilon_0}\frac{q}{r^2}dr$$

Entonces, realizando los cálculos de la integral: 

$$\begin{align}
\int^{b}_{a}E\cdot dl &=\frac{1}{4\pi\epsilon_0}\int^{b}_{a}\frac{q}{r^2}dr\\  \\
&=\frac{-1}{4\pi\epsilon_0}\frac{q}{r}\bigg\vert^{r_b}_{r_a}\\  \\
&=\frac{1}{4\pi\epsilon_0}\left(\frac{q}{r_a}-\frac{q}{r_b}\right)
\end{align}$$

Ahora, notar que si se tiene que el **camino es cerrado**, entonces trivialmente se llega que: 

$$\oint E\cdot dl=0\implies\nabla\times E=0$$

![[potencial.png|center|350]]



>[!danger] Potencial eléctrico 
>
>Sabemos que la integral de línea es independiente de su camino, por lo tanto, nos podemos definir un punto de referencia $O$ arbitrario y el punto de llegada $r$. De tal forma, se define el **potencial eléctrico** cómo: 
>
>$$V(r)=-\int^{r}_{O}E\cdot dl$$

Notar que el potencial eléctrico entre dos puntos $a$ y $b$ se define como $V(b)-V(a)$. Si esto lo conectamos con el teorema fundamental de gradientes, se llega a la siguiente igualdad: 

$$E=-\vec{\nabla} V$$

Notar que esto significa que **el campo eléctrico es el gradiente del potencial**. Hace mucho sentido si nos vamos a la definición de gradiente, que conecta el concepto de variación del campo eléctrico. 

Una observación importante es notar que $E$ es una cantidad vectorial, mientras que $\nabla V$ es escalar. La forma en que ambos se relacionan es al aprovecharse del Teorema de Stokes, que formula que para una integral de línea cerrada se tiene que $\nabla\times E=0$. Esto tiene varias implicancias importantes, donde se llega que: 

$$\frac{\partial E_x}{\partial y}=\frac{\partial E_y}{\partial x},\;\;\;\;\frac{\partial E_z}{\partial y}=\frac{\partial E_y}{\partial z},\;\;\;\;\frac{\partial E_x}{\partial z}=\frac{\partial E_z}{\partial x}$$

## Ecuación de Poisson y Laplace 

La ecuación de Poisson y de Laplace, en términos de la electrostática, nos da la relación entre el **campo eléctrico** y el **potencial eléctrico** mediante la **ley de Gauss**. 

>[!error] Ecuación de Poisson 
>
>De la ley de Gauss diferencial y el potencial eléctrico en trayectorias cerradas tenemos que: 
>
>$$\nabla\cdot E=\frac{\rho}{\epsilon_0}\;\;\;\land\;\;\;\nabla\times E=0$$
>
>Esto nos da una premisa de como ambos términos se podrían llegar a relacionar. Notemos que $\nabla\cdot E=\nabla\cdot(-\nabla V)=-\nabla^2V$. Por lo tanto, se llega que: 
>
>$$\nabla^2V=-\frac{\rho}{\epsilon_0}$$

Por el otro lado, aprovechando de la definición anterior, también se formula la **ecuación de Laplace**. 

>[!danger] Ecuación de Laplace
>
>En regiones donde no se tiene carga eléctrica, se cumple que: 
>
>$$\nabla^2V=0$$

Esto pareciera ser trivial dada la planteación de la ecuación de Poisson, pero es una conclusión útil. 

## Potencial para una distribución de cargas 

Notemos que anteriormente se definió el potencial en función del campo eléctrico. Aun así, por lo general lo más fácil sería encontrar primero el trabajo y luego calcular el campo eléctrico al tomar el gradiente. Por lo tanto, se va a **invertir la ecuación de Poisson** para encontrar una relación del potencial en función del radio. 

Antes que nada, partiendo por la definición de potencial, podemos poner el punto de referencia en el infinito y llegar a lo siguiente: 

$$\begin{align}
V(r)&=-\int^{r}_{\infty}E\cdot dl\\  \\
&=\frac{1}{4\pi\epsilon_0}\frac{q}{r}
\end{align}$$

Ahora, ocupando el principio de superposición para una carga volumétrica, se tiene que: 

$$V(r)=\frac{1}{4\pi\epsilon_0}\int\frac{\rho(r')}{\vec{(r-r')}}dS$$

Por lo tanto, se obtiene el potencial en **función de la distribución de cargas**, sin tener que pasar por el cálculo del campo eléctrico. Notemos que esto es asumiendo un punto de referencia al infinito. Con lo anterior dicho, se cumple que: 

$$V(r')=\begin{cases}\frac{1}{4\pi\epsilon_0}\int\frac{\lambda(r')}{\vec{(r-r')}}dl&\text{Potencial de línea}\\  \\
\frac{1}{4\pi\epsilon_0}\int\frac{\sigma(r')}{\vec{(r-r')}}da&\text{Potencial de superficie}\end{cases}$$


## Condiciones de borde 

Notemos que al calcular un campo eléctrico siempre se tiene una especie de discontinuidad cuando se atraviesa a través de una superficie. De hecho, es posible saber como cambia el campo eléctrico ocupando la Ley de Gauss al imaginarnos un cilindro delgado que se extiende por los bordes de la superficie: 

$$\oint_SE\cdot da=\frac{1}{\epsilon_0}Q_{\text{enc}}=\frac{1}{\epsilon_0}\sigma A$$

Donde $A$ es el área superficiel del cilindro. Ahora, las tapas no contribuyen nada, ya que estamos asumiendo que es un cilindro muy delgado que solo cubre el pedazo de superficie. 

![[esfera 2.png|center|250]]

Al tener esto en mente, se llega que la discontinuidad es medible y su valor es: 

$$\Delta E = \frac{1}{\epsilon_0}\sigma$$

Por el otro lado, la componente tangencial a la superficie siempre es continuo **como también lo es el potencial**. Esto se debe que el potencial está definido como un gradiente del campo eléctrico, entonces una discontinuidad de un único punto no cambiaría su derivada parcial. 

## Trabajo y energía 

Sabemos que el trabajo por definición, es la cantidad de fuerza por el desplazamiento. En el contexto de electrostática la pregunta es la misma: *¿Cuanto trabajo se hará para mover. una carga del punto $a$ hasta el $b$?*. 

Sabemos que la fuerza de Coulomb se puede expresar en función del campo eléctrico, donde se tiene que $F=QE$. Sin embargo, lo que se busca acá es **la mínima fuerza** para mover la carga. Por lo tanto, acá se pueden hacer algunas igualdades ocupando la definición del potencial: 

$$\begin{align}
W&=\int^{b}_{a}F\cdot dl\\  \\
&=-Q\int^{b}_{a}E\cdot dl\\  \\
&=Q[V(b)-V(a)]\tag{Definición de potencial}
\end{align}$$

Notemos que, nuevamente, la respuesta es **independiente del cámino**, lo que hace ver que se tiene una **fuerza conservativa**. Si establecemos nuestro punto de referencia al infinito, se llega que: 

$$W=QV(r)$$

El sentido físico es que el potencial es la energía potencial por unidad de carga. 

![[trabajo.png|center|250]]

## Energía en una distribución puntual 

El caso anterior hizo el análisis para mover una única partícula desde dos puntos arbitrarios. Pero ahora, al extrapolarlo a tres cargas y ocupando la definición de potencial: 

$$W_3=\frac{1}{4\pi\epsilon_0}q_2\left(\frac{q_1}{(\vec{q_1}-\vec{q_3})}+\frac{q_2}{(\vec{q_2}-\vec{q_3})}\right)$$

Vale decir, el trabajo para implementar la tercera carga es $W_3$, pero el trabajo total es mucho mayor. Similarmente si se van añadiendo más cargas los términos aumentan considerablemente. Por regla general, el trabajo total para $n$ cargas es el siguiente: 

$$W=\frac{1}{4\pi\epsilon_0}\sum^{n}_{i=1}\sum^{n}_{j>i}\frac{q_iq_j}{(\vec{q_i}-\vec{q_j})}$$

Reordenando la sumatoria, se llega a lo siguiente: 

$$W=\frac{1}{2}\sum^{n}_{i=1}q_i\left(\sum^{n}_{j\neq i}\frac{1}{4\pi\epsilon_0}\frac{q_j}{(\vec{q_i}-\vec{q_j})}\right)$$

El término en el paréntesis representa **el potencial en un punto $r_i$ dada la presencia de todas las cargas**, entonces se puede llegar a concluir que el trabajo total es: 

$$W=\frac{1}{2}\sum^{n}_{i=1}q_iV(r_i)$$

 Para el caso continuo esto se llega a transformar en una integral sobre la densidad de carga: 

$$W=\frac{1}{2}\int\rho V\;dS$$

Ocupando integración por partes, la condición que $\nabla V=-E$ e imponiendo que no hay cargas externas fuera de la distribución de cargas, se puede simplificar al siguiente resultado: 

$$W=\frac{\epsilon_0}{2}\int E^2ds$$

Esto, si lo queremos ver en función de una partícula, se vería de la siguiente forma: 

![[trabajoContinuo-1.png|center|450]]

Notar que la fuerza de Coulomb es radial, por ende, no se considera su acción en la partícula. El que si se considera es el **campo eléctrico**. 

Un comentario final es la pregunta natural del lugar donde está almacenada esta energía. Hace mucho sentido, porque en mecánica casi siempre la energía *es almacenada* en el cuerpo en cuestión. En el contexto de la teoría de radiaciones decir que la energía **está localizada en el campo eléctrico**. 

## Conductores 

La propiedad básica de todo conductor es que uno o más electrones por átomo son libres para viajar. Un conductor perfecto tendría un cantidad ilimitada de cargas libres. En la vida real, lo más cercano a un conductor perfecto llegaría a ser los metales. 

![[conductor-1.png|center|200]]

A partir de esto, los conductores cumplen cinco propiedades fundamentales: 

- **El campo eléctrico es nulo dentro del conductor:** Existen dos formas simples y básicas para explicar esto. La primera, es que de ser cierto, las cargas libres se moverían, y ya no sería electro**estatica**. Otra explicación un poco más *científica* es que de existir campo eléctrico, haría que las cargas positivas y negativas se desplacen en sentido contrario. Estas cargas inducidas producen otro campo eléctrico con un dirección opuesta al original, haciendo que éste se cancele. 


![[polarizacion.png|center|100]]


- **La densidad de carga es nula dentro del conductor**: Suena contraintuitivo pero esto subyace de la ley de Gauss, donde $\nabla\cdot E=\rho/\epsilon_0$. Esto se debe al mismo argumento anterior: siguen habiendo cargas circulando pero estas se anulan entre sí, la *carga neta* llegaría a ser nula. 

- **La carga neta se encuentra en la superficie**: Dado las condiciones de borde, este llegaría a ser el único lugar restante para que circulen las cargas. 

- **Los conductores son equipotenciales**: Si tomamos dos puntos cualquiera dentro del conductor, podemos llegar que $V(a)=V(b)$. 

- **El campo eléctrico es perpendicular de la superficie, justo afuera del conductor**: Esto, nuevamente justificándose por la primera proposición, de lo contrario las cargas libres se moverían y no habría componente tangencial.



![[campoConductor 1.png|center|400]]



Ahora, para poder determinar el valor del campo eléctrico se puede usar la ecuación de condición de borde vista anteriormente: 

$$\vec{E}=\frac{\sigma}{\epsilon_0}\hat{n}$$

Dado esto, es posible obtener la densidad de carga en la superficie: 

$$\sigma=-\epsilon_0\frac{\partial V}{\partial n}$$

Ahora, *¿qué pasaría ante la acción de un campo externo?* Sabemos que el campo eléctrico es discontinuo en el borde, entonces, *¿se consideraría el campo por arriba de la superficie o por debajo?* En realidad, se considera el promedio de ambos campos, por la contribución que hace un pedazo de superficie por arriba del campo y por debajo. Entonces, si se quisiera calcular la fuerza por unidad de área se tendría lo siguiente: 

$$\vec{F}=\frac{1}{2\epsilon_0}\sigma\hat{n}$$


## Capacitadores 

Supongamos que tenemos dos conductores, uno con carga $+Q$ y otro con $-Q$. Dado que el potencial es constante dentro de un conductor, se puede hablar de la diferencia de potencial entre ellos: 

$$V=V_+-V_-=-\int^{(+)}_{(-)}E\cdot dl$$

Calcular el campo eléctrico entre ambos conductores muchas veces se puede llegar a complicar, por lo tanto, nos podemos aprovechar de la definición de campo eléctrico, que es **proporcional a la carga eléctrica**. Y como el campo eléctrico es proporcional, el potencial también lo es. Este constante de proporcionalidad se le llamará **capacitancia**. 

>[!error] Capacitancia 
>
>La capacitancia es una propiedad intrínseca de un objeto o sistema que cuantifica su capacidad para almacenar carga eléctrica. Está definida como la relación entre la cantidad de carga almacenada en un conductor y la diferencia de potencial o voltaje en ese conductor. La capacitancia es una medida de cuánta carga eléctrica puede almacenarse en un objeto por cada unidad de voltaje aplicado. Es una característica fundamental en componentes eléctricos como los condensadores. Está definida matemáticamente como: 
>
>$$C=\frac{Q}{V}$$

Notemos que por definición, $V$ es la diferencia de potencial del conductor positivo menos el negativo, por lo que la capacitancia siempre es **positiva**. 

Otra cosa importante es que la capacitancia es un valor asociado únicamente **a un material**, vale decir,  a un conductor único. Lo que se hace en este caso es simular un segundo conductor esférico de radio infinito que rodea al primer conductor. Esto no contribuiría nada con el campo eléctrico y su potencial sería nulo. 

Ahora, para poder cargar un capacitador se necesita realizar un trabajo para mover electrones de la placa positiva hasta la negativa. De hecho, habría que "*pelear*" contra el campo eléctrico que estaría empujando de vuelta a los electrones a su placa original. Si suponemos que a la mitad del proceso la carga de la placa positiva es $q$ y se quiere llegar a cargar una cantidad $Q$, se puede plantear lo siguiente: 

$$dW=\left(\frac{q}{C}\right)dq$$

Por lo tanto, se llegan a dos equivalencias para obtener el trabajo total para hacer un trabajo de $q=0$ a $q=Q$: 

$$W=\frac{1}{2}\frac{Q^2}{C}=\frac{1}{2}CV^2$$

Con $V$ siendo el potencial final del capacitador. 

## Expansión multipolar 

Si nos llegamos a poner en una posición muy lejana a una distribución de cargas, esto se llegaría a parecer como una carga puntual, y por lo tanto, una buena aproximación del potencial sería $(1/4\pi\epsilon_0)Q/r$ con $Q$ siendo la carga total. Sin embargo, cuando se quiere obtener mayor información es necesario partir por el ejemplo del dipolo eléctrico 

>[!error] Dipolo eléctrico 
>
>Un dipolo eléctrico consiste de dos cargas iguales pero con signo positivo $(\pm q)$ separados por una distancia $d$. 
>![[dipolo.png|center|450]]


Al hacer cálculos trigonométricos se llega que el potencial del dipolo a una distancia $r$ muy lejana equivale a: 

$$V(r)\approx\frac{1}{4\pi\epsilon_0}\frac{qd\cos\theta}{r^2}$$

Como era de esperar, decae más rápido que una carga puntual. Ahora, si llegamos a formar un cuadrupolo (dos dipolos formando un cuadrado) decaería por un factor $1/r^3$, un octopolo por $1/r^4$ y así sucesivamente. 

Ahora, si se quisiera hacer para una **distribución de cargas** el cálculo sería el siguiente: 

$$V(r)=\frac{1}{4\pi\epsilon_0}\int\frac{1}{\vec{(r-r')}}\rho(r')dS$$

Si nos definimos la siguiente integral, como **momento dipolar** (que no depende de $r$): 

$$p=\int r'\rho(r')dS=\sum^{n}_{i=1}q_ir_i'$$

Notemos que para un dipolo común y corriente (como el de la definición, donde se tiene dos cargas a una distancia $d$) el momento dipolar llegaría a ser $p=qd$. 

Entonces el potencial del dipolo se puede llegar a definir como: 

$$V_\text{dip}=\frac{1}{4\pi\epsilon_0}\frac{p\cdot\hat{r}}{r^2}$$ 

Ahora que se tiene el potencial definido, es posible obtener el campo eléctrico al sacar el gradiente, llegando a: 

$$E_\text{dip}(r,\theta)=\frac{p}{4\pi\epsilon_0r^3}(2\cos\theta\;\hat{r}+\sin\theta\;\hat{\theta})$$


## Polarización 

Cuando se tiene un átomo neutro y se le somete a una carga eléctrica experimenta un proceso llamado **polarización**. El núcleo de un átomo es considerado como positivo y los electrones negativos, entonces, ante una campo eléctrico, se llega a un estado de balance donde las cargas positivas y negativas estan repelidas la una con la otra. 

![[dipoloI.png|center|450]]



Por ende, el átomo ahora posee un pequeño momento dipolar **p**, que apunta a la misma dirección del campo eléctrico (En la figura se muestra con un ángulo para fines ilustrativos). Por lo general este momento dipolar es proporcional al campo eléctrico: 

$$p=\alpha E$$

La constante de proporcionalidad $\alpha$ se llama **polarizabilidad atómica** que depende de la estructura del átomo. 

## Polarización en materiales 

Ahora que sabemos como se comporta una molécula singular ante el efecto de un campo eléctrico, es posible analizar el comportamiento en materiales compuesto por muchas moléculas. De hecho, es de esperar que ante un campo eléctrico se tengan muchos momentos dipolares apuntando a la misma dirección del campo. Una forma conveniente de medir esto será la siguiente: 

$$P=\text{Momento dipolar por unidad de volumen}$$

Ahora, dado un dipolo singular $p$, es posible definir una integral para obtener el potencial del material: 

$$\begin{align}

V(r)&=\frac{1}{4\pi\epsilon_0}\frac{p\cdot\hat{r}}{(\vec{r}-\vec{r'} )^2}\\ \\ 
&=\frac{1}{4\pi\epsilon_0}\int^{}_{V}\frac{P(r')}{(\vec{r}-\vec{r'})^2}dS\\  \\
&=\frac{1}{4\pi\epsilon_0}\oint_S\frac{\sigma_b}{(\vec{r}-\vec{r'})}dA+\frac{1}{4\pi\epsilon_0}\int_V\frac{\rho_b}{(\vec{r}-\vec{r'})}\end{align}$$ 

Donde $\rho_b=-\nabla\cdot P$ es la densidad de carga volumétrica y $\sigma_b=P\cdot\hat{n}$ densidad de carga superficial. 

## Ley de Gauss en dieléctricos 

En los dieléctricos podemos definir un campo dada la polarización y el campo de su complemento (lo que se denomina carga libre $\rho_f$). Por lo tanto, en un dieléctrico la densidad de carga total se puede escribir como la suma de ambos: 

$$\rho=\rho_b+\rho_f$$

Ahora, por la Ley de Gauss tenemos lo siguiente: 

$$\epsilon_0\nabla\cdot E=\rho=\rho_b+\rho_f=-\nabla\cdot P+\rho_f$$

Por conveniencia se pueden juntar los términos divergentes: 

$$\nabla\cdot (\epsilon_0 E+P)=\rho_f$$

El término dentro del paréntesis se puede designar por la letra $D$ y se hace llamar como **desplazamiento eléctrico**. 

>[!error] Desplazamiento eléctrico 
>
>El desplazamiento eléctrico, denotado como $D$, es un vector que describe la cantidad de campo eléctrico libre de las influencias de las propiedades dielétricas del material en que está inmerso. Relaciona el campo eléctrico con la polarización del medio.
>![[desplazamientoElectrico.png|center|450]]
 Es especialmente útil en medios donde hay materiales dieléctricos, ya que refleja tanto el efecto del campo eléctrico externo como el de los dipolos inducidos en el material. 
>
>$$\begin{align}
>D&=\epsilon_0E+P\end{align}$$
>
>En términos de la Ley de Gauss se puede expresar como: 
>
>$$\nabla\cdot D=\rho_f$$
>
>O bien en su forma integral: 
>
>$$\oint D\cdot dA=Q_{f_\text{enc}}$$
>
>Donde $Q_{f_\text{enc}}$ es la **carga libre** total encerrada por el volumen.


## Susceptibilidad, permitividad y constante dieléctrica 

En muchas situaciones se tiene que el vector polarización es proporcional al campo eléctrico, de hecho, se cumple lo siguiente: 

$$P=\epsilon_0\chi_eE_\text{total}$$

La constante de proporcionalidad $\chi_e$ se llama **susceptibilidad eléctrica del medio**. Como su nombre lo indica, dependen de la estructura microscópica del medio. Los materiales que cumplen con cierta proporcionalidad se llaman **dieléctricos lineales** 

De hecho, a partir de esto se puede obtener una relación con el **desplazamiento eléctrico**: 

$$\begin{align}
\vec{D}&=\epsilon_0E+P\\  \\
&=\epsilon_0E+\epsilon_0\chi_eE\tag{Susceptibilidad eléctrica}\\  \\
&=\epsilon_0(1+\chi_e)E
\end{align}$$

Por lo tanto, $D$ **también es proporcional** al campo eléctrico. Por lo tanto definimos $\epsilon=\epsilon_0(1+\chi_e)$, llegando que: 

$$\vec{D}=\epsilon\vec{E}$$

La constante $\epsilon$ se llama **permitividad del material**. Por último, si se elimina el factor de la permitividad del vacio se tiene lo siguiente: 

$$\epsilon_r=1+\chi_e=\frac{\epsilon}{\epsilon_0}$$

Esto último se llama **permitividad relativa** o **constante dieléctrica** del material. Nuevamente cabe mencionar que al estar en función de $\chi_e$, éste depende de las propiedades del material. 