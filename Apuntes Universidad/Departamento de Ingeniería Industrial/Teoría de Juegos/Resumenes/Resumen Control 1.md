
La teoría de juegos es el estudio de interacciones estratégicas, donde las decisiones de los agentes influyen en el resultado del *juego*. Si se quisiera definir de forma formal, es la **rama de las matemáticas** que estudia las decisiones de **agentes que quieren maximizar beneficios**. 

## Formalidades técnicas 

Antes de definir los teoremas y aplicaciones de la teoría de juegos, es importante conocer los dos conceptos fundamentales que equivalen a las variables de cada juego. 

>[!tip] Jugadores 
>Son los agentes participantes del juego, por lo general se van a tener $n\geq 2$. 

>[!tip] Estrategias 
>Para un jugador $i$ se va a representar con $S_i$ el conjunto de estrategias de $i$. Un elemento representativo de $S_i$ será $s_i\in S_i$. 
>
>Por consecuencia, se representará como $S=S_1\times S_2\times\dots S_n$ el conjunto de todas las jugadas posibles-
>
>Las jugadas de los jugadores opuestos a $i$ se representaran con un $-i$. En este caso, $S_{-i}=S_1\times S_2\times S_n$ representaría el conjunto de jugadas de todos los jugadores excepto $i$. 

Por lo tanto, una jugada $s\in S$ se le llamará un **perfil de estrategias**, equivalente a un vector con todas las jugadas de cada jugador: 

$$s=\begin{pmatrix}
s_1 \\
s_2 \\
\vdots \\
s_n
\end{pmatrix}$$

Notemos que el perfil de estrategias tiene la misma cantidad de dimensiones que de jugadores. 

>[!tip] Pagos 
>Se representarán los pagos de un jugador $i$ como una función de utilidad $U(s)=U(s_1,s_2,\dots,s_n)$ que dependen de las decisiones de todos los jugadores. 

Durante el transcurso del curso, lo normal será **maximizar** la función de utilidades en función del conjunto de jugadas $S_{-i}$. Cuando no se tiene certeza absoluta del perfil de estrategias se ocupa el concepto de **utilidad esperada**, haciendo alusión al concepto de **esperanza** de Probabilidades. 

###  Dominancia estricta 

>[!important] Estrategia **estrictamente** dominada 
>Una estrategia es **estrictamente dominada** si existe una otra estrategia que da mayores pagos para cualquier juego de los otros jugadores.
>
>Para un jugador $i$, una estrategia $s_i\in S_i$ es **estrictamente dominada** si existe una estrategia $s_{i}^{'}\in S_i$ tal que: 
>
>$$u_i(s_i,s_{-i})<u_i(s_{i}^{'},s_{-i})\;\;\;\forall s_{-i}\in S_{-i}$$

Algo a considerar es que **los jugadores racionales no juegan estrategias estrictamente dominadas**. Esto se llama *conocimiento común de racionalidad*. 

#### Ejemplo: Dominancia estricta 

Se tiene el siguiente juego, donde las estrategias del Jugador $1$ corresponde a $(U,\; M,\; D)\in S_1$ y $(L,\; M,\; R)\in S_2$ para el Jugador $2$. 


|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(4,3)$ | $(5,1)$ | $(6,2)$ |
| **M** | $(2,1)$ | $(8,4)$ |$(3,6)$   |
| **D** | $(3,0)$ | $(9,6)$ | $(2,8)$ |


Se asume que todos los jugadores son racionales y todos saben entre sí que son racionales. 

Por lo tanto, notemos que el Jugador $1$ no tiene estrategias estrictamente dominadas, esto se puede ver al notar la mejor jugada ante una estrategia del Jugador $2$. El análisis se hace por el método de **dominancia estricta**, a diferencia de **mejor respuesta**. 

- Comparando $U$ con $M$: 

|       |          **L**           |          **M**           |          **R**           |
|:-----:|:------------------------:|:------------------------:|:------------------------:|
| **U** | $(\textcolor{red}{4},3)$ |         $(5,1)$          |         $(\textcolor{red}{6},2)$          |
| **M** |         $(2,1)$          |   $(\textcolor{red}{8},4)$            |   $(3,6)$   |


$U$ domina en dos jugadas, sin embargo, $M$ domina en una. 

- Comparando $U$ con $D$: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(5,1)$ | $(\textcolor{red}{6},2)$ |
| **D** | $(3,0)$ | $(\textcolor{red}{9},6)$ | $(2,8)$ |


Nuevamente, $U$ no es la mejor jugada. 

- Comparando $M$ con $D$: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **M** | $(2,1)$ | $(8,4)$ |$(\textcolor{red}{3},6)$   |
| **D** | $(\textcolor{red}{3},0)$ | $(\textcolor{red}{9},6)$ | $(2,8)$ |


Lo mismo en este juego. Por lo tanto, no hay estrategia estrictamente dominada para el Jugador $1$. 

Aun así, notemos que para el Jugador $2$ si existen estrategias estrictamente dominadas:

- Comparando $L$ con $M$: 

|       |           **L**           |           **M**           |
|:-----:|:-------------------------:|:-------------------------:|
| **U** | $(4,\textcolor{blue}{3})$ |          $(5,1)$          |
| **M** |          $(2,1)$          | $(3,\textcolor{blue}{6})$ |
| **D** |          $(3,0)$          |          $(9,\textcolor{blue}{6})$          |


Aquí se puede ver que no hay estrategía estrictamente dominada. 

- Comparando $M$ con $R$: 

|       |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(5,1)$ | $(6,\textcolor{blue}{2})$ |
| **M** | $(8,4)$ | $(3,\textcolor{blue}{6})$ |
| **D** | $(9,6)$ | $(2,\textcolor{blue}{8})$ |


En este caso **$M$** **está estrictamente dominada por $R$**. 

- Comparando $L$ con $R$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,\textcolor{blue}{3})$ | $(6,2)$ |
| **M** | $(2,1)$ | $(3,\textcolor{blue}{6})$ |
| **D** | $(3,0)$ | $(2,\textcolor{blue}{8})$ |


Acá tampoco hay una estrategia dominada. 

Como el segundo Jugador es racional, no va a jugar $M$, entonces esa estrategia se eliminaría. La tabla quedaría de la siguiente forma: 


|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,3)$ | $(6,2)$ |
| **M** | $(2,1)$ | $(3,6)$ |
| **D** | $(3,0)$ | $(2,8)$ |


Ahora, para el Jugador $1$, notemos lo siguiente: 

- Comparando $U$ con $M$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(\textcolor{red}{6},2)$ |
| **M** | $(2,1)$ | $(3,6)$ |


Aquí, notemos que $M$ **está estrictamente dominada** por $U$. 

- Comparando $M$ con $D$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **M** | $(2,1)$ | $(\textcolor{red}{3},6)$ |
| **D** | $(\textcolor{red}{3},0)$ | $(2,8)$ |


Aquí no hay una estrategia estríctamente dominada. 

- Comparando $U$ con $D$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(\textcolor{red}{6},2)$ |
| **D** | $(3,0)$ | $(2,8)$ |


En este caso $U$ **domina a D**. Por lo tanto, se eliminarían dos estrategias. 

Por ende, se llega a la siguiente tabla: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,3)$ | $(6,2)$ |


A partir de aquí es claro ver que el Jugador $2$ va a jugar $L$, por ende, la solución llegaría ser $(U,L)$. 

#### Ejemplo: Mejor respuesta 

Muchas veces, comparar estrategia por estrategia puede llegar a ser muy tedioso. En este caso, se tenía una matriz $3\times 3$, pero en el caso de una matriz $n\times n$ se tendría que hacer las siguiente cantidad de comparaciones por jugador: 

$$\sum^{n}_{i=1}\;(N-i)=\frac{N(N-1)}{2}$$

Si consideramos las comparaciones del jugador $2$, serían $N(N-1)$ comparaciones en total. Esto, **solamente para la primera tanda de estrategias estrictamente dominadas**. Si siguieramos bajo la misma lógica, y suponiendo el peor caso (una eliminación por tanda), se repetiría el proceso: 

$$\sum^{n}_{i=1}(N-i)(N-(i-1))=\frac{N^2(N+1)}{2}+\frac{N^3-N^2}{6}$$

Esto quiere decir que, bajo este método, **el peor caso es $\Theta(N^3)$**, algo completamente ineficiente. 

De aquí es donde se introduce el método de **mejor respuesta**, que se enfoca en encontrar la estrategia óptima ante una posible jugada del otro jugador. Viéndolo con el mismo juego con el Jugador 1: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(5,1)$ | $(\textcolor{red}{6},2)$ |
| **M** | $(2,1)$ | $(8,4)$ |$(3,6)$   |
| **D** | $(3,0)$ | $(\textcolor{red}{9},6)$ | $(2,8)$ |


Por **mejor respuesta** se elimina la estrategia $M$, quedando con la siguiente matriz: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(4,3)$ | $(5,1)$ | $(6,2)$ |
| **D** | $(3,0)$ | $(9,6)$ | $(2,8)$ |


Ahora, para el Jugador $2$: 

|       |  **L**  |  **M**  |  **R**  |
|:-----:|:-------:|:-------:|:-------:|
| **U** | $(4,\textcolor{blue}{3})$ | $(5,1)$ | $(6,2)$ |
| **D** | $(3,0)$ | $(9,6)$ | $(2,\textcolor{blue}{8})$ |


Se eliminaría la estrategia $M$, quedando con la siguiente tabla: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,3)$ | $(6,2)$ |
| **D** | $(3,0)$ | $(2,8)$ |


Ahora, nuevamente, analizando para el Jugador $1$: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(\textcolor{red}{4},3)$ | $(\textcolor{red}{6},2)$ |
| **D** | $(3,0)$ | $(2,8)$ |


Se elimina $D$, quedando con la siguiente matriz: 

|       |  **L**  |  **R**  |
|:-----:|:-------:|:-------:|
| **U** | $(4,3)$ | $(6,2)$ |


Y aquí se llega **a la misma situación anterior**, donde trivialmente se llega al equilibrio $(U,L)$. Notemos que en este caso, se hicieron $3$ comparaciones en vez de $9$. 

#### Ejemplo: Elecciones políticas 

Se tiene el siguiente modelo, donde cada bloque representa la posición política de un candidato. 

| **Izquierda** |     |     |     | **Centro** |     |     |     |     | **Derecha** |
|:-------------:|:---:|:---:|:---:|:----------:|:---:|:---:|:---:|:---:|:-----------:|
|      $$1$$      | $2$ | $3$ | $4$ | $$5$$       | $6$ | $7$ | $8$ | $9$ |    $$10$$     |


Un candidato $i$ puede elegir posicionarse en cualquier lugar del espectro. El pago que se llevaría corresponde al porcentaje de población que logra captar. Por ejemplo, en el siguiente juego se tienen los siguientes pagos.

| **Izquierda** |     |     |     | **Centro** |     |     |     |     | **Derecha** |
|:-------------:|:---:|:---:|:---:|:----------:|:---:|:---:|:---:|:---:|:-----------:|
|               |     |  $$\textcolor{red}{X}$$   |     |            |  $$\textcolor{blue}{Y}$$   |     |     |     |             |
|     $$\textcolor{red}{1}$$     | $\textcolor{red}{2}$ | $\textcolor{red}{3}$ | $\textcolor{red}{4}$ |   $$\textcolor{blue}{5}$$    | $\textcolor{blue}{6}$ | $\textcolor{blue}{7}$ | $\textcolor{blue}{8}$ | $\textcolor{blue}{9}$ |   $$\textcolor{blue}{10}$$    |


En este caso, el candidato $X$ se llevaría el $40\%$ de los votantes, mientras $Y$ se llevaría $60\%$. *¿Existe una estrategía estrictamente dominada?*

Si se viera el caso más extremo, donde $s_X=1$, bastaría con que $s_Y=2$ para maximizar sus utilidades. De hecho, $\forall s_Y\in S_Y\;\vert\;s_y\neq 1$ se cumple que $s_Y$ tendrá más utilidades que $X$. 


| **Izquierda** |     |     |     | **Centro** |     |     |     |     | **Derecha** |
|:-------------:|:---:|:---:|:---:|:----------:|:---:|:---:|:---:|:---:|:-----------:|
|      $$\textcolor{red}{X}$$       |    $$\textcolor{blue}{Y}$$   |     |     |            |     |     |     |     |             |
|     $$\textcolor{red}{1}$$     | $\textcolor{blue}{2}$ | $\textcolor{blue}{3}$ | $\textcolor{blue}{4}$ |   $$\textcolor{blue}{5}$$    | $\textcolor{blue}{6}$ | $\textcolor{blue}{7}$ | $\textcolor{blue}{8}$ | $\textcolor{blue}{9}$ |   $$\textcolor{blue}{10}$$    |


Aquí se obtiene que $u_X=10\%$ pero $u_Y=90\%$. Si el jugador $Y$ decidiera jugar $s_Y=1$, se tendría que $u_X=50\%$ y $u_Y=50\%$. Por ende, $s=(1,1)$ sería una estrategia estrictamente dominada. 

Si se sigue con la misma lógica, se llega que **los candidatos se van a querer posicionar lo más al centro posible**. De hecho, hay cuatro posible predicciones para $S_1\times S_2$, que llegaría a ser el conjunto de tuplas  $\lbrace (5,5),\;(5,6),\;(6,5),\;(6,6)\rbrace\in S_1\times S_2$. 

Este ejemplo es conocido como **el teorema del votante mediano**, que explica de una forma idealista como se comportan las elecciones en escenarios reales. 

A partir del segundo ejemplo, se puede llegar a deducir una definición de lo que llegaría a ser **la mejor respuesta**. 

>[!tip] Mejor respuesta
>Para un jugador $i$, una estrategia $s_i\in S_i$ es una **mejor respuesta** a la jugada $s_{-i}\in S_{-i}$ de los otros jugadores si: 
>
>$$u_i(s_i,s_{-i})\geq u_i(s_{i}',s_{-i}),\;\;\forall s_{i}'\in S_i$$
>
>O de forma equivalente, se tiene que $s_i$ es una mejor respuesta si cumple que: 
>
>$$\max_{s_{i}'\in S_i}\;u_i(s_{i}',s_{-i})$$
>
>Ahora, si las estrategias tendrían asociadas una probabilidad a ellos, se puede decir que se tiene **una mejor respuesta** a la creencia $p$ sobre las acciones de los otros jugadores si: 
>
>$$E[u_i(s_i,p)]\geq E[u_i(s_i',p)]\;\;\forall s_{i}'\in S_i$$
>
>De forma equivalente, se tiene que $s_i$ es una mejor respuesta ante una creencia $p$ si se cumple que: 
>
>$$\max_{s_{i}'\in S_i}\;E\left[u_i(s_{i}',s_{-i})\right]$$

### Equilibrio de Nash 

El equilibrio de Nash es un concepto ampliamente utilizado para referirse a los puntos de **indiferencia** de los jugadores. 

>[!tip] Equilibrio de Nash 
>Un perfil de estrategias $s^*=(s_1^*,s_2^*,\dots,s_n^*)$ es un **equilibrio de Nash** para cada jugador $i$ si se cumple que: 
>
>$$u_i(s_{i}^{*},s_{-i}^{*})\geq u_i(s_{i}{'},s_{-i}^{*})\;\;\forall   s_{i}^{'}\in S_i$$
>
>Esto quiere decir que **cada jugador está jugando su mejor respuesta** frente al resto de los jugadores. 

Algunas consecuencias del equilibrio de Nash son: 

- Nadie se arrepiente de la estrategia que elige 

- Creencias autocumplidas 

- Nunca se tiene una estrategia estrictamente dominada en el perfil de estrategias.  

## Competencia de Oligopolios 

Los oligopolios son aquellos mercados donde existen pocas firmas que compiten por un producto. Normalmente las firmas son tomadoras de decisiones, vale decir, ellas deben decidir cuanto producir y a qué precio vender. 

Las decisiones de los productores de los oligopolios se pueden dividir al tomar decisiones en la **producción** o en los **precios de venta**. Los juegos a continuación cumplen el requisito económico de *citrus paribus*, para evitar mayores complicaciones. 
### Competencia Cournot 

Corresponde a la competencia por cantidad producida. Para el caso más simple, primero se verá el caso de $2$ jugadores para luego extrapolarlo a $n$ jugadores. 

>[!quote] Competencia Cournot 
>La competencia Cournot es un modelo económico que describe una estructura de mercado en la cual varias empresas compiten en cantidad, y no en precio. Fue desarrollado por el economista francés Antoine Augustin Cournot en 1838. Los productos que se producen son **homogéneos** y las firmas **buscan maximizar beneficios**. 

Por lo tanto, la estrategia consiste en que cada firma elige una cantidad de producción $S_i=\mathbb{R}_+$. Claramente, la producción conlleva costos, que será modelada por el costo marginal $c(q)=c\cdot q$ (se asumirá un costo marginal constante para las dos firmas). 

Dado que se tiene un modelo simplificado, se asumirá también que el precio de mercado cumple los requisitos de ser una función lineal, por lo tanto, la función será de la forma $p(q_1,q_2)=a-b(q_1+q_2)$ y se tiene el sigiuente gráfico: 

![[cournot_graph2 1.png|center]]

Por lo tanto, si se quiere calcular los beneficios de las firmas, se calculan los ingresos: 

$$\begin{align}
\Pi_1(q_1,q_2)&=(p-c)q_1=[a-b(q_1+q_2)-c]q_1=pq_1-cq_1\\  \\
\Pi_2(q_1,q_2)&=(p-c)q_2=[a-b(q_1+q_2)-c]q_2=pq_2-cq_2
\end{align}$$

Para encontrar el equilibrio de Nash de las firmas, necesario es **derivar y maximizar en función de las cantidades** en la función de pagos: 

$$\begin{align}
\frac{\partial\Pi_1(q_1,q_2)}{\partial q_1}&=a-2bq_1-bq_2-c=0\\  \\
\frac{\partial^2\Pi_1(q_1,q_2)}{\partial q_{1}^{2}}&=-2b<0
\end{align}$$

Por ende, considerando todas las variables, se llega al siguiente gráfico: 
![[ingresosMax.png|center]]
Donde lo más importante a rescatar es la parábola de ingresos y la recta vertical de maximización de ingresos. Si nos fijamos, estos dos parámetros dependen de $Q=q_1 + q_2$, por ende, la maximización de ingresos está en función de la cantidad producida por ambas firmas. 

De aquí, las mejores respuestas llegarían a ser: 

$$\begin{align}
BR_1(q_2)&=\frac{a-c}{2b}-\frac{q_2}{2}\\  \\
BR_2(q_1)&=\frac{a-c}{2b}-\frac{q_1}{2}
\end{align}$$

Y se tendría el siguiente gráfico de mejores respuestas: 

![[cournot_graph 1.png|center]]

Donde es importante notar que **ambas pendientes son negativas**. Vale decir, mientras una firma produzca más, la otra producirá menos. Es decir, ambos se comportan de forma sustitutas entre sí. 

El equilibrio de Nash se daría **en el cruce de las mejores respuestas**, vale decir: 

$$q_1^*=q_2^*=\frac{a-c}{3b}$$

Lo que hace sentido si se mira el gráfico. En el cruce de ambas respuestas, ninguna firma presionaría por producir más. Si se evalúa esto en la función de la demanda, el precio sería: 

$$p^*=\frac{a+2c}{3}$$

![[equilibrioCournot.png|center]]

No obstante, si se hace el análisis con el mercado de los monopolistas, donde ellos producen cuando la cantidad es igual al costo marginal, se puede ver que las firmas al coludirse y producir como monopolistas **maximizan su beneficio**: 

![[CournotMonopolio.png|center]]

Vale decir, ambas firmas generarían mayores beneficios al producir en la línea morada. Esto se produce al haber un **intercambio de información** entre ambos agentes, y por ende, una **colusión**. 

La forma de reducir la colusión es reducir las barreras de entradas, que produce una mayor entrada de firmas. De hecho, el problema de maximización sería el siguiente: 

$$\text{n firmas}=\begin{cases}
a-b\sum^{n}_{i=1}q_i&\text{Precios}\\  \\
a-b\sum^{n}_{j=1}q_j-c& \text{Cantidades}\\  \\
\frac{a+nc}{n+1}&\text{Precio de}\;\textbf{equilibrio}\\  \\
\frac{a-c}{b(n+1)}&\text{Cantidad de}\;\textbf{equilibrio}
\end{cases}$$

Notemos que es exactamente el mismo problema de antes pero con sumatorias, que arrastra el $n$-ésimo término al maximizar utilidades. 

Una conclusión de esto, que nos servirá como guia para la paradoja de Bertrand, es que cuando se tienen **muchas** firmas, el comportamiento converge a una competencia perfecta: 

$$\lim_{n\to\infty}p^*=c$$


### Competencia Bertrand 

Esta competencia, a diferencia de la competencia Cournot, es una competencia por precios. 

>[!quote] Competencia Bertrand 
>La competencia Bertrand es un modelo económico de competencia de precios entre empresas. Fue formulada por Joseph Bertrand en 1883. A diferencia del modelo de Cournot, que se basa en la competencia de cantidades, Bertrand se enfoca en la competencia de precios. En este modelo las empresas mantienen un **costo fijo** de producción. 

Por lo tanto, en esta competencia cada firma elige su precio, vale decir, $S_i\in\mathbb{R}_+$. Por el otro lado, el costo marginal de ambas firmas es el mismo y constante. Se va a suponer que si tienen el mismo precio, entonces se comparte la demanda equitativamente, donde: 

$$Q(p)=1-p$$

Es la función de demanda, donde $p$ es el precio mínimo del mercado. Por lo tanto, la demanda para la Firma $1$ sería: 

$$q_1(p_1,p_2)=\begin{cases}
1-p_1&\text{si}\;p_1<p_2\\  \\
0&\text{si}\;p_1>p_2\\  \\
\frac{1-p_1}{2}&\text{si}\; p_1=p_2
\end{cases}$$

Por lo tanto, los pagos respectivos de cada firma sería: 

$$\begin{align}
\Pi_1(p_1,p_2)&=q_1(p_1,p_2)(p_1-c)\\  \\
\Pi_2(p_1,p_2)&=q_2(p_1,p_2)(p_2-c)
\end{align}$$

Notar que no es posible encontrar la mejor respuesta porque la función cantidad **no es una función continua**. Pero, aun así, es posible ponerse en casos donde $p_M$ es el precio del monopolista: 

$$BR_1(p_2)=\begin{cases}
p_1>p_2&\text{si}\;p_2<c\\  \\
p_1\geq p_2&\text{si}\; p_2=c\\  \\
p_2-\epsilon&\text{si}\;p_M\geq p_2>c\\  \\
p_M&\text{si}\;p_2>p_M
\end{cases}$$


Ahora, si analizamos los casos: 

- Si $p_2<c$ entonces la segunda firma se iría a pérdidas, entonces no sería equilibrio de Nash. 

- Por el otro lado, si $p_1\geq p_2$, basta con que la Firma 1 eliga $p_1'=p_2-\epsilon$ y captura todo el mercado. 

Por lo tanto, **no hay equilibrio de Nash vendiendo a un precio menor al costo** y tampoco hay **cuando cada firma sobrepasa el precio de la otra**. 
![[bertrand_game_theory_graph 2.png|center]]

Por lo tanto, se llega a una especie de *juego* donde cada firma decide poner un precio $p_i=p_{-i}-\epsilon$ para llevarse toda la demanda. Al ir iterando entre este juego, se llega a un equilibrio donde $\lim\epsilon\to0$ y $p_1=c\;\land\;p_2=c$. . 

- *¿Qué pasa si $p_i<c$?* La firma se va a pérdida. 

- *¿Qué pasa si $p_{i}>p_{-i}$?* La firma no obtiene beneficios. 

Por lo tanto, **se pone un precio igual al costo marginal, como se hace en la competencia perfecta**. Esto es conocido como la paradoja de Bertrand. 

En la competencia Cournot se necesitaba $n\to\infty$ firmas para llegar a la competencia perfecta, sin embargo aca se necesita solo dos firmas. Esto se podría explicar por algunos supuestos, como por ejemplo, suponer que la demanda es ilimitada. 

### Productos diferenciados

Ahora se puede tener un modelo donde los productos son diferenciados. Un consumidor se puede modelar dentro de una recta donde elige *qué tanto* le gusta un producto en comparación al otro. Un ejemplo sería el siguiente, donde se tienen $6$ consumidores con preferencias $s=(0, 0.1, 0.2, 0.5, 0.8, 1)$: 

![[competenciaLineal.png|center]]


Las estrategias de las firmas $A$ y $B$ es el precio a elegir, vale decir, $p_i\in\mathbb{R}_+$. Cuando las firmas anuncian sus precios, los consumidores pueden optar por moverse a través de la recta. 

Si nos fijamos, un consumidor cualquiera con preferencia $x$ debe caminar una distancia $\vert x\vert$ para llegar a consumir $A$ y una distancia $\vert 1-x\vert$ para consumir $B$.

![[distancialineal.png|center]]

Además, se asumirá un costo por *caminar*, vale decir, para atraer a un consumidor, determinada por la siguiente función: 

$$c(d)=t\cdot d^2\;\;\;t\in\mathbb{R}_+$$

Donde $d$ es la distancia y $t$ un parámetro positivo cualquiera. Por ende, las firmas tienen los siguientes costos para cada consumidor: 

$$C(x)=\begin{cases}
p_A+tx^2&\text{Firma A}\\  \\
p_B+t(1-x)^2&\text{Firma B}
\end{cases}$$


Si se llegase a tener un consumidor indiferente entre $A$ y $B$, se podría establecer que $C_A(x')=C_B(x')$, derivando al siguiente resultado: 

$$x'=\frac{1}{2}+\frac{p_B-p_A}{2t}$$

Esto quiere decir que, ante productos exactamente iguales, se cumple que $x'$ es la proporción de consumidores que van hacia $A$ y $B$. Notemos que si $p_A=p_B=0$ entonces $x'=\frac{1}{2}$, lo que hace sentido. 

En este caso particular, se puede encontrar el equilibrio de Nash al calcular los beneficios de cada firma: 

$$\begin{align}
\Pi_A(p_A,p_B)&=p_A\left[\frac{1}{2}+\frac{p_B-p_A}{2}\right]\\  \\
\Pi_B(p_A,p_B)&=p_B\left[\frac{1}{2}-\frac{p_B-p_A}{2}\right]
\end{align}$$

Como se tiene simetría, el equilibrio de Nash se encuentra en $p_A^*=p_B^*=t$. Por ende, bajo este modelo bastaría encontrar el consumidor indiferente para obtener el equilibrio. 

Encontrar el consumidor indiferente tiene que ver con las estrategias de precios de las firmas, ya que dependiendo de éstas se pueden acercar o alejar más del consumidor:

![[distancialinealP.png|center]]


## Estrategias Mixtas 

Muchas veces hay juegos donde realizar una estrategia aleatoria es lo mejor que se puede hacer. Un futbolista puede ser muy bueno pegando penales hacia la derecha, pero si el portero sabe que él sólo le pegará hacia ese lado, su estrategia fracasará. De aquí nace el concepto de **randomizar acciones**. Ahora el vector perfil de estrategias se le asignará una distribución de Probabilidades tal que se maximize el **pago esperado**. 

>[!note] Estrategias Mixtas 
>
>Para un jugador $i$, una **estrategia mixta** $\sigma_i$ es una distribución de probabilidades sobre las acciones $s_i\in S_i$ y $\sigma_i$ se representa como un vector $\sigma_i\in[0,1]^{\vert S_i\vert}$ tal que: 
>
>$$\sigma_i(s_i)\geq 0\;\;\;\forall s_i\in S_i\;\land\;\sum^{}_{s_i\in S_i}\sigma_i(s_i)=1$$
>
>Una estrategia pura $s_i$ también es una estrategia mixta donde se le asigna probabilidad $1$ a la estrategía $s_i$ y probabilidad zero al resto de las estrategias. 

Por lo tanto, el pago esperado llegaría a ser un promedio de los pagos de las estrategias puras que forman las estrategias mixtas. 

#### Ejemplo: 

Notemos el siguiente juego, donde trivialmente se tienen dos equilibrios de Nash al jugar únicamente estrategias puras. 


|       |  **a**  |  **b**  |
|:-----:|:-------:|:-------:|
| **A** | $(2,1)$ | $(0,0)$ |
| **B** | $(0,0)$ | $(1,2)$ |


Pero si quisieramos calcular los pagos en estrategias mixtas, deberíamos definir un vector $\sigma_i$ que represente la probabilidad de cada decisión de cada jugador. 

Por ejemplo, sea $\sigma_1=(1/5, 4/5)$ y $\sigma_2=(1/2, 1/2)$. El pago esperado para la estrategia $A$ sería el siguiente cálculo: 

$$\begin{align}
EU_1[A,\sigma_2]&=\frac{1}{2}U_1[A,a]+\frac{1}{2}U_1[A,b]=\frac{1}{2}2+\frac{1}{2}0=1
\end{align}$$

Notemos que el pago esperado depende del vector de probabilidades del otro jugador, $\sigma_2$. Se le hace un cálculo de esperanzas en función a la probabilidad que el otro jugador juege tal estrategia. Sin embargo, queda la retórica de como obtener el equilibrio de Nash dado que existe la posibilidad de randomizar ciertas jugadas.

>[!note] Equilibrio de Nash en Estrategias Mixtas
>
>Un perfil de estrategias mixtas $\sigma^*=(\sigma_1^*,\sigma_2^*,\dots,\sigma_n^*)$ es un **equilibrio de Nash en estrategias mixtas** si para cada jugador $i$, $\sigma_i^*$ es una mejor respuesta a $\sigma_{-i}^*$: 
>
>$$EU_i(\sigma_i^*,\sigma_{-i}^*)\geq EU_i(\sigma_i',\sigma_{-i}^*)\;\;\forall\sigma_i'\in\Sigma_i$$
>
>Si miramos la desigualdad de cerca, se cumple que: 
>
>$$\sum^{}_{s_i\in S_i}[\sigma_i^*(s_i)EU_i(s_i,\sigma_{-i}^*)\geq\sum^{}_{s_i\in S_i}[\sigma_i'(s_i)EU_i(s_i,\sigma_{-i}^*)]\;\;\forall\sigma_i'\in\Sigma_i$$


Notemos que de la definición se puede desprender que si una estrategia mixta es una mejor respuesta, entonces cada una de las estrategias puras deben ser mejor respuestas también. En particular, cada una debería dar el mismo pago. 

Si existe una estrategia pura $\bar{s_i}$ con probabilidad positiva que da menos pago que otra estrategia $s_i$, se puede mejorar el pago usando una estrategia mixta, donde $\sigma_i'(\bar{s_i})=0$ y $\sigma_i'(s_i)=\sigma(\bar{s_i})+\sigma(s_i)=0$

Por lo tanto, siguiendo del ejemplo anterior, la idea es definirnos **un vector con parámetros indeterminados** y ver las utilidades esperadas. Por ejemplo, para encontrar las utilidades del Jugador $1$ **dado el vector** $\sigma_2=(q,1-q)$ del otro jugador, se llega que: 

$$\begin{align}
EU_1[A,\sigma_2]&=qU_1[A,a]+(1-q)U_1[A,b]=2q\\  \\
EU_1[B,\sigma_2]&=qU_1[B,a]+(1-q)U_1[B,b]=1-q
\end{align}$$

Entonces, como se quiere llegar a una estrategia mixta cuyo pago sea indiferente, se resuelve el sistema de ecuación para encontrar los valores de $\vec{\sigma_2}$: 

$$\begin{align}
2q=1-q\implies q=\frac{1}{3}\implies\vec{\sigma_2}=\binom{1/3}{2/3} 
\end{align}$$

Ahora, para el Jugador $2$ se hace el mismo procedimiento, se buscan las utilidades esperadas en función de $\vec{\sigma_1}$, que por el momento está indefinido por los parámetros $(p,1-p)$. Haciendo los mismos cálculos anteriores, se llega que: 

$$\vec{\sigma_1}=\binom{2/3}{1/3}$$
#### Ejemplo: Buscar el Equilibrio de Nash en el Ténis  

Se tiene el siguiente juego, donde el Jugador $1$ es aquel que sirve y el Jugador $2$ defiende. Ambos pueden decidir para que lado servir o defender: 



|       |  **l**  |  **r**  |
|:-----:|:-------:|:-------:|
| **L** | $(50,50)$ | $(80,20)$ |
| **R** | $(90,10)$ | $(20,80)$ |



Antes que nada, de lo desprendido anteriormente, debemos recordar que **cada estrategia pura que forma una estrategia mixta debe ser una mejor respuesta**. 

Para calcular la mejor respuesta del Jugador $2$, se deben calcular los pagos esperados del Jugador $1$, entonces nos definimos $\vec{\sigma_2}=(q,1-q)$. Por lo tanto, los pagos esperados del primer jugador sería: 

$$\begin{align}
EU_1[L,(q,1-q)]&=qU_1(L,l)+(1-q)(L,r)=80-30q\\  \\
EU_1[R,(q,1-q)]&=qU_1(R,l)+(1-q)U_1(R,r)=20+70q
\end{align}$$

Notemos que la forma de plantear el ejercicio es, qué utilidad tendrá el Jugador $1$ **dado que jugo $L$**. De ahí se plantea lo mismo pero **dado que juega $R$**. Para que llegen a ser mejor respuesta los pagos deben ser iguales, entonces se resuelve el sistema de ecuación: 

$$80-30q=20+70q\implies q=0.6\implies\vec{\sigma_2}=\binom{0.6}{0.4}$$

Ahora, se repite el proceso pero para el otro jugador, sea $\sigma_1=(p,1-p)$: 

$$\begin{align}
EU_2[(p,1-p),l]&=pU_2(L,l)+(1-p)U_2(R,l)=10+40p\\  \\
EU_2[(p,1-p),r]&=pU_2(L,r)+(1-p)U_2(R,r)=80-60p
\end{align}$$

Volviendo a repetir el proceso anterior se llega que: 

$$10+40p=80-60p\implies p=0.7\implies\vec{\sigma_1}=\binom{0.7}{0.3}$$

Algo importante a notar en el cálculo de los equilibrios de estrategias mixtas es que **el efecto estratégico domina el efecto directo**, vale decir, las acciones a hacer por un Jugador $i$ depende también de la información que tiene el Jugador $-i$ sobre $i$.  Se tiene un estado de "*confusión sostenible*", donde ambos Jugadores podrían llegar a jugar un equilibrio no óptimo. En palabras simples, el equilibrio de Nash de Estrategias Mixtas nos dice que no hay manera de salir de tal situación con desviaciones individuales. 

## Juegos Evolutivos 

Si se llegasen a interpretar los jugadores como poblaciones, se podría estudiar un grupo de juegos como *juegos evolutivos*. En términos biológicos, son estrategias donde los genes más aptos van a aumentar su proporción en la población, mientras que los menos desaparecerán. 

Existen dos definiciones, muy abstractas, de lo que son los juegos evolutivos. En palabras básicas, es una serie de juegos donde se llega a una **estabilidad evolutiva** si cualquier desviación $\epsilon>0$ del equilibrio de Nash no conduce a una dominancia de otra especie. 

>[!question] Estabilidad evolutiva 
>
>Existen dos definiciones formales para el concepto de la estabilidad evolutiva. En un juego simétrico de dos jugadores, una estrategia pura $s$ es **evolutivamente estable** si hay un $\bar{\epsilon}>0$ tal que para toda $\epsilon<\bar{\epsilon}$ se tiene que: 
>
>$$(1-\epsilon)u_i(s,s)+\epsilon u_i(s,s')>(1-\epsilon)u_i(s',s)+\epsilon u_i(s',s'),\;\;\forall s'\neq s$$
>
>Existe una segunda definición en términos del **equilibrio de Nash**: Un juego simétrico de dos jugadores, una estrategia pura $s$ es **evolutivamente estable** si: 
>
>- $(s,s)$ es un equilibrio de Nash **simétrico**, es decir, $u_i(s,s)\geq u_i(s',s),\;\;\forall s'$
>  
>
>- Si existe un $s'\neq s$ tal que $u_i(s,s)=u_i(s',s)$, entonces $u_i(s,s')>u_i(s',s')$. 
>  
>  Ambas condiciones deben satisfacerse simultáneamente para cumplir con ser una estabilidad evolutiva. 
>

 Algunas lecciones a considerar de la definición: 

- El resultado de la evolución no es necesariamente eficiente. 

- Una estrategia estrictamente dominada no puede ser una estabilidad evolutiva, porque la estrategia que lo domina va a ser una mutación exitosa. 

- Si $(s,s)$ es un equilibrio de Nash **estricto**, entonces $s$ es una estrategia evolutivamente estable. 

Por lo tanto, **[[Juego Evolutivos.canvas|el método más práctico para confirmar que una estrategia es evolutivamente estable]]** es hacerse la siguiente pregunta: ¿Es $(s,s)$ un equilibrio de Nash simétrico? 

1. Si la respuesta es "No", entonces no es evolutivamente estable. 
2. Si la respuesta es "Si", nos preguntamos si es un equilibrio de Nash estricto. 


![[Juego Evolutivos.png|center|500]]


Al comienzo, las definiciones suenan intimidantes, pero se clarifican con ejemplos.
#### Ejemplo: Competencia intraespecie 

Vamos a asumir un juego donde una población de animales están genéticamente programadas para jugar. Los genes más exitosos van a aumentar su proporción en la población. 

Supondremos que sale una pequeña minoria de la población que juega una estrategia diferente a $s$, *¿esa pequeña minoría va a prosperar o desaparecer?*. 

Se puede ver en el siguiente ejemplo, de leones decidiendo si cooperar o no al cazar: 


|       |  **C**  |  **N**  |
|:-----:|:-------:|:-------:|
| **C** | $(2,2)$ | $(0,3)$ |
| **N** | $(3,0)$ | $(1,1)$ |


En este juego, se llega que trivialmente el equilibrio de Nash es $(N,N)$. Aunque, podemos ver que jugar $(C,C)$ da mejores pagos para ambos jugadores. Lo más lógico sería que ambos leones decidan cooperar, pero, *¿La estrategia $C$ puede ser evolutivamente estable?*

Supongamos que toda la población se *"diese"* cuenta de tal observación y todos jugaran $C$. Ahora, veamos lo que pasaría si aparece una pequeña mutación que empiece a jugar $N$: 


|       |  **C**  |  **$\textbf{\textcolor{green}{N}}$**  |
|:-----:|:-------:|:-------:|
| **$\textbf{\textcolor{red}{C}}$** | $(2,2)$ | $(\textcolor{red}{0},\textcolor{green}{3})$ |
| **N** | $(3,0)$ | $(1,1)$ |


Notemos que la población original (en rojo) dejaría de ganar $2$ y empezaría a percibir ninguna utilidad. Por el otro lado, la mutación obtiene un pago de $3$, valor mayor a la utilidad de los individuos normales. Esto nos indica que $C$ **no es una Estrategia Evolutivamente Estable**. 

Esto se puede ver en términos de pagos esperados. Asumimos una estrategia mixta, que en realidad más que representar probabilidades nos representará proporciones. Por lo tanto, sea $\vec{\sigma}=(1-\epsilon,\epsilon)$, para un $\epsilon>0$ pero muy pequeño, tal que nos represente la desviación de la población.  Calculando el pago de la estrategia de los mutantes: 

$$\begin{align}
EU_C[1-\epsilon,\epsilon]&=(1-\epsilon)2+\epsilon 0=2-2\epsilon\\  \\
EU_N[1-\epsilon,\epsilon]&=(1-\epsilon)3+\epsilon 1=3-2\epsilon
\end{align}$$

Notamos que ante un $\epsilon$ muy pequeño, se llega que $EU_C < EU_N$, vale decir, no es la mejor Estrategia Mixta al haber una mejor combinación. 

Ahora, *¿cómo sería el análisis para la estrategia $N$?*. Supongamos que todos parten jugando $N$ y hay una proporción $\epsilon$ que llega a jugar $C$. Por lo tanto, los pagos esperados del Jugador 1: 

$$\begin{align}
EU_C[1-\epsilon,\epsilon]&=2\epsilon\\  \\
EU_N[1-\epsilon,\epsilon]&=1+2\epsilon
\end{align}$$

Nuevamente, $EU_C< EU_N$, entonces $N$ tampoco es una Estrategia Evolutivamente Estable. 

#### Ejemplo: 

Se tiene el siguiente Juego: 

|       |  **A**  |  **B**  |  **C**  |
|:-----:|:-------:|:-------:|:-------:|
| **A** | $(2,2)$ | $(0,0)$ | $(0,0)$ |
| **B** | $(0,0)$ | $(0,0)$ |$(1,1)$   |
| **C** | $(0,0)$ | $(1,1)$ | $(0,0)$ |


*¿Es $C$ una Estrategia Evolutivamente Estable?* Primero veamos el juego de una perspectiva *micro*, donde un $\epsilon$ pequeño juega $C$: 

|       |  **B**  |  **C**  |
|:-----:|:-------:|:-------:|
| **B** | $(0,0)$ | $(1,1)$ |
| **C** | $(1,1)$ | $(0,0)$ |

Entonces, definimos el vector $\sigma=(\epsilon,1-\epsilon)$ para el Jugador $2$ y se llega que: 

$$\begin{align}
EU_C&=\epsilon\\  \\
EU_B&=1-\epsilon
\end{align}$$

En este caso, al comparar $EU_C$ con $EU_B$ llegamos que $B$ si sobreviviría, pero luego se llega a una recurrencia cuando se hace en análisis inverso: 

$$\begin{align}
EU_C&=\epsilon\\  \\
EU_B&=1-\epsilon
\end{align}$$

Por lo tanto, una mutación de $B$ invadiría una población de $C$ y así vice versa. Por lo tanto, es posible establecer que ambos no son Estrategias Evolutivamente Estables. 

De hecho, $(C,C)$ y $(B,B)$ no son equilibrios de Nash, por lo tanto, es posible establecer que si para una estrategia $s$, $(s,s)$ no es un equilibrio de Nash, entonces no es una Estrategia Estrictamente Dominada (se obtiene de la definición). 




## Juegos Secuenciales 

En los otros tipos de juegos que se han analizado, los jugadores decidían simultaneamente sin observar las acciones de los otros jugadores. La diferencia con los juegos secuenciales consiste que los jugadores **juegan en turnos** y **observan la historia del juego**. 

Notemos que si los jugadores no pudiesen observar la acción del resto, daría lo mismo si las desiciones fueran simultáneas o secuenciales. Pero ahora, como existen decisiones en secuencias, se tiene, valga la redundancia, juegos secuenciales. 

>[!success] Juegos Secuenciales
>Un juego secuencial es un tipo de juego en Teoría de Juegos donde los jugadores toman decisiones en secuencia, y cada jugador puede observar las acciones de los jugadores que le precedieron antes de tomar su decisión. Estos juegos suelen representarse con un árbol de juego, que muestra las posibles acciones en cada etapa y los pagos asociados.

Como dice la definición, estos juegos se visualizan a través de **árboles de decisiones**. Por esto mismo, la forma de ver los juegos es pensar *hacia adelante*, en la decisión que hará el otro posterior a la tuya. 

En este tipo de juegos, a diferencia de los anteriores, existen equilibrios **no eficientes**. Esto es muy común en el ámbito de las inversiones y se denomina normalmente como *"riesgo moral" (moral hazard)*. 

#### Ejemplo: El juego de la entrada al mercado 

Este ejemplo se utilizará únicamente para dar a entender en qué consisten los árboles de decisiones y cual es su lectura. 

Se tienen dos firmas, donde la empresa $A$ es dueña de un monopolio y la empresa $B$ está evaluando en entrar o no al mercado. 

- Si la empresa $B$ no entra, la empresa $A$ mantiene el monopolio y recibe un pago de 10, mientras que la empresa $B$ no pierde ni gana. 

- Si la empresa $B$ entra se tienen dos opciones de réplica por parte de $A$: competir o acomodarse. 

- Si la empresa $A$ compite, ambos reciben un pago de $1$, mientras que si se acomoda, $A$ recibe $4$ y $B$ recibe $6$. 

![[test-3.png|center|500]]


Por lo tanto, claramente el equilibrio de Nash sería $(4,6)$. Pareciera ser una respuesta *eficiente*, pero esto no ocurre en todos los casos. 

### Competencia de Cournot en Juegos Secuenciales 

La competencia de Cournot ya fue definida anteriormente, donde firmas en un oligopolio compiten por cuanto producir. Por lo tanto, la estrategia es $S_i=\mathbb{R}_+$. Pero, **ahora la Firma $1$ decide primero y luego decide la Firma $2$**. Por lo tanto, los pagos los determinan los costos de producción y el precio del mercado: 

$$\begin{align}
c(q)&=c\cdot q\tag{Costo marginal}\\  \\
p(q_1,q_2)&=a-b(q_1+q_2)\tag{Precio del mercado}
\end{align}$$

Nuevamente, se tienen las mismas utilidades de antes: 

$$\begin{align}
\Pi_1(q_1,q_2)&=(p-c)q_1=[a-b(q_1+q_2)-c]q_1=pq_1-cq_1\\  \\
\Pi_2(q_1,q_2)&=(p-c)q_2=[a-b(q_1+q_2)-c]q_2=pq_2-cq_2
\end{align}$$

Pero como esto es secuencial, se le denominará **competencia Stackelberg**. Entonces, la pregunta a hacer es *¿A qué firma le conviene partir variando su producción?*. Lo mejor es verlo en **retrospectiva**, vale decir, una **inducción hacia atrás**. En el *último dia*, al tener un juego simultáneo, se tiene que las utilidades del Equilibrio de Nash para el Jugador $2$ es: 

$$\begin{align}
BR_2(q_1)&=\frac{a-c}{2b}-\frac{q_1}{2}
\end{align}$$

Por lo tanto, en cierto sentido, la firma $1$ entiende que las utilidades de $2$ depende de su producción ($q_1$). Notemos lo siguiente: 

$$\frac{\partial BR_2(q_1)}{\partial q_1}<0$$

Esto quiere decir, **cuando $q_1$ aumenta, como respuesta, $q_2$ baja**. Y ahora, si nos fijamos en las utilidades de la firma $1$: 

$$BR_1(q_2)=\frac{a-c}{2b}-\frac{q_2}{2}$$

Entonces, **le conviene que $q_2$ sea menor para obtener más utilidades**. Y eso se logra, justamente, al producir más. 

Aunque, algo a notar es que la relación $q_1\to q_2$ no es unitaria, de hecho, nos podemos fijar que: 

$$\frac{\partial BR_2(q_1)}{\partial q_1}=-\frac{1}{2}$$

Esto quiere decir que, al cabo que $q_1$ produce $2$ unidades, $q_2$ reduce una unidad. Esto implica que la proporción $q_1+q_2$ aumenta, teniendo un impacto positivo en los precios a los consumidores $\downarrow p(\uparrow\Delta)=a-b(\uparrow\Delta)$. 

Notemos, por lo tanto, que si se volviera a la función utilidad y se deja utilidad de la Firma $1$ en función de su propia producción: 

$$\frac{\partial\Pi_1[q_1,q_2(q_1)]}{\partial q_1}=0\implies q_1=\frac{a-c}{2b}$$

Esto es una cantidad mayor que el caso donde se llega al equilibrio simultáneo. Por esto mismo, **es mejor decidir primero**. 

Ahora, existe un teorema que nos dice que, en este tipo de juegos, bajo ciertas condiciones, siempre se puede forzar una victoria del primer jugador o el segundo fuerza una victoria o *empate*. 

>[!check] Teorema de Zermelo
>
>En cualquier juego finito de suma cero y de información perfecta para dos jugadores (en el que el azar no interviene), si el juego se juega sin errores, entonces o el primer jugador puede forzar una victoria, o el segundo jugador puede forzar un empate, o el segundo jugador puede forzar una victoria.
>
>En otras palabras, con estrategia óptima de ambos jugadores:
>
>- Si el juego es favorable para el primer jugador, él tiene una estrategia ganadora.
>
>- Si el juego es desfavorable para el primer jugador, entonces el segundo jugador tiene una estrategia ganadora.
>  
>  - Si ninguno de los jugadores tiene una estrategia ganadora, entonces el juego terminará inevitablemente en empate.
>    
>    En otras palabras, con estrategia óptima de ambos jugadores: 
>    
> - Si el juego es favorable para el primer jugador, él tiene una estrategia ganadora. 
> - Si el juego es desfavorable para el primer jugador, entonces el segundo jugador tiene una estrategia ganadora. 
> - Si ninguno de los jugadores tiene una estrategia ganadora, entonces el juegoterminará en un empate
>   
>   
Es importante resaltar que este teorema no proporciona una estrategia explícita para ganar o empatar; simplemente establece que tal estrategia existe.

Notar que esto es un teorema de **existencia**, vale decir, nos dice que la posibilidad, no así del cómo llegar. 

Visto de forma gráfica, sería el siguiente árbol de decisión: 

![[test2.png|center|500]]


La demostración de esto se puede hacer bajo inducción. Claramente el caso base a elegir depende que parte del teorema se quiere demostrar.  

>[!success] Estructura de Información 
>Decimos que un juego secuencial es de información perfecta si en cada nodo de decisión del juego el jugador que toma la decisión sabe en qué nodo está. (Sabe todo lo que ha pasado anteriormente. Toda la historia del juego está observada por todos los jugadores.)

Notemos que en los juegos simultaneos era muy trivial determinar como era la *historia*. Sin embargo, ahora cada jugada, representada por nodos, representa la historia del juego. De hecho, haciendo hincapie en la teoría de la información, la información faltante de un juego es medible a través de la ecuación de Shannon: 

$$I_{\text{Shannon}}=-\sum^{\Omega}_{i=1}\mathbb{P}(x_i)\log_2(\mathbb{P}(x_i))$$

Vale decir, ante un juego con resultados finitos $(\Omega)$ con una probabilidad asignada a cada nodo $(\mathbb{P}(x_i))$ la ecuación de Shannon nos puede decir cuanta información faltante hay en un juego. 

Ahora, como sabemos que las estrategias del jugador pueden definir la historia del juego, se puede definir el concepto de **estrategia pura**: 

>[!success] Estrategia pura 
>Una estrategia pura de un jugador $i$ en un juego secuencial de información perfecta es una esquema completa de acciones que especifica qué acción el jugador va a elegir en cada nodo de decisión del jugador.

#### Ejemplo 

Se tiene el siguiente juego secuencial, primero veremos las posibles estrategias puras de cada jugador. 

![[test3.png|center|400]]


Primero, para cada jugador, podemos establecer sus estrategias puras por los siguientes conjuntos: 

$$\begin{align}
\text{Jugador 1}&=\lbrace Uu,Ud,Dd,Du\rbrace\\  \\
\text{Jugador 2}&=\lbrace r,l\rbrace
\end{align}$$

Notemos que a pesar que el primer jugador no tiene que optar por alguna estrategia a jugar en $D$, se debe especificar de igual manera las decisiones de tal nodo. 

Ahora, para resolver el juego se ocupa **inducción hacia atrás**. Sabemos que el Jugador $1$ ante $u$ o $d$ eligiría $d$. Por el otro lado, dado que el Jugador $1$ jugará $d$, el oponente decidirá jugar $r$. Por último, bajo el mismo argumento, se termina jugando $D$. 

![[test4.png|center|400]]


Por último, notar que dado el conjunto de estrategias $S_1\times S_2$ y los pagos, es posible escribir la matriz de pagos: 


|       |  **l**  |  **r**  |
|:-----:|:-------:|:-------:|
| **Uu** | $(2,4)$ | $(0,2)$ |
| **Ud** | $(3,1)$ | $(0,2)$ |
|   **Du**    |$(1,0)$         |$(1,0)$         |
| **Dd** | $(1,0)$ | $(1,0)$ |


Si lo vemos de esta forma, se tienen dos equilibrios de Nash en $(Du,r)$ y $(Dd,r)$. Aunque la resolución del juego secuencial solo nos dió $(Dd,r)$.  

Ahora, notemos que, en realidad, jugar $u$ en vez de $d$ es una irracionalidad. No debería ser un equilibrio de Nash ya que $3>2$. Pero esto se debe exclusivamente al escribir el juego en forma normal. En este tipo de casos, jugadores toman acciones irracionales en **nodos que no llegan al juego**.

De igual forma, es un mal necesario. No es posible escribir la tabla *"real"* que si representa el juego dada las restricciones, ya que necesariamente se perdería información: 

|       |  **l**  |  **r**  |
|:-----:|:-------:|:-------:|
| **Uu** | $(2,4)$ | $(0,2)$ |
| **Ud** | $(3,1)$ | $(0,2)$ |
|   **Du**    |   $$?$$      |   $$?$$      |
| **Dd** | $$?$$ | $$?$$ |

Por ejemplo, en este caso, *¿dónde se pondría el pago $(1,0)$?*. Si llegasemos a eliminar las jugadas $Du$ y $Dd$ por $D$ el problema aún persiste: 

|        |  **l**  |  **r**  |
|:------:|:-------:|:-------:|
| **Uu** | $(2,4)$ | $(0,2)$ |
| **Ud** | $(3,1)$ | $(0,2)$ |
| **D** |  $$?$$  |  $$?$$  |


