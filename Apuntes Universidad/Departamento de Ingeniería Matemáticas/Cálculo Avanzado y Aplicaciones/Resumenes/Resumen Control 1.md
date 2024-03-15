
# Campos vectoriales y escalares 


Por lo general, un campo vectorial se puede imaginar como una función que asigna a cada punto en el espacio un vector específico, representado comúnmente con propiedades físicas, como la velocidad, fuerza o flujo eléctrico en un punto. Visualmente se puede imaginar como un *campo* de flechas, donde cada flecha indica la dirección y magnitud de un vector en su punto de origen. 
![[campo3ddi.png|center]]
Por lo tanto, es de imaginar que al definir un campo vectorial, al definirlo sobre un punto en específico, se hable de una función $f:\mathbb{R}^n\to\mathbb{R}^n$. 

>[!tip] Campo vectorial 
>
>Un campo vectorial en $\mathbb{R}^n$ es una función $\vec{F}:D\subseteq\mathbb{R}^n\to\mathbb{R}^n$ que se le asocia a cada punto $\vec{x}$ de su dominio $D$ un vector $\vec{F}(\vec{x})$. El campo vectorial se dibuja gráficamente *"pegando"* una flecha $\vec{F}(\vec{x})$ a cada punto $\vec{x}$ de su dominio. 

Análogamente, podríamos pensar que un campo escalar es una función que asigna a cada punto en el espacio un único valor escalar, a menudo representando propiedades físicas como temperatura, presión o densidad. 
![[campo_escalar_exotico_3d-2.png|center]]
El campo escalar, por lo general, ya es conocido por el *Cálculo en Varias Variables*, sin embargo, su definición formal es la siguiente: 

>[!tip] Campo escalar 
>
>Una función $f:D\subseteq\mathbb{R}^n\to\mathbb{R}$ que asocia un número real a cada punto $\vec{x}$ de su dominio $D$ es llamado un **campo escalar**. Por ejemplo, un campo vectorial $\vec{F}(x_1,x_2,\dots,x_n)$ en $\mathbb{R}^n$ tiene $n$ campo escalares componentes $f_1,f_2,\dots,f_n$ de modo que: 
>
>$$\vec{F}(x_1,x_2,\dots,x_n)=(f_1(x_1,x_2,\dots,x_n),f_2(x_1,x_2,\dots,x_n),f_n(x_1,x_2,\dots,x_n))$$

<div style="page-break-after: always;"></div>

## Operadores sobre campos 

Dado que los campos vectoriales son un concepto nuevo en el curso, se definiran algunas operaciones sobre estas funciones que se ocuparán para numerosas aplicaciones. 

>[!info] Diferencial del campo vectorial 
>
>Sea $\vec{F}=(F_1,F_2,F_3)=F_1\hat{i}+F_2\hat{j}+F_3\hat{k}$  un campo vectorial diferenciable en un punto $\vec{r_0}=(x_0,y_0,z_0)$, sabemos que el diferencial de la función está representada por la matriz Jacobiana. 
>
>$$J_\vec{F}(\vec{r_0})=\begin{pmatrix}
\frac{\partial F_1}{\partial x}(x_0,y_0,z_0) & \frac{\partial F_1}{\partial y}(x_0,y_0,z_0) & \frac{\partial F_1}{\partial z}(x_0,y_0,z_0) \\
\frac{\partial F_2}{\partial x}(x_0,y_0,z_0) & \frac{\partial F_2}{\partial y}(x_0,y_0,z_0) & \frac{\partial F_2}{\partial z}(x_0,y_0,z_{0)} \\
\frac{\partial F_3}{\partial x}(x_0,y_0,z_0) & \frac{\partial F_3}{\partial y}(x_0,y_0,z_0) & \frac{\partial F_3}{\partial z}(x_0,y_0,z_0)
\end{pmatrix}$$

El Jacobiano, al igual que en las funciones escalares, nos mostrará como varía un campo vectorial en cierto punto.  

Por ejemplo, acá se tiene el Jacobiano aplicado en una zona del campo vectorial (un cubo):
![[Jacobiano3D 1.png|center|600]]

Un ejemplo bidimensional sería el siguiente, que muestra el Jacobiano en torno a $(1,1)$ dentro de un campo vectorial que representa una rotación en el plano $F(x,y)=(y,-x)$.  
![[Jacobiano2D.png|center]]
<div style="page-break-after: always;"></div> 


>[!note] Divergencia 
>
>Sea $\vec{F}=(F_1,F_2,F_3)=F_1\hat{i}+F_2\hat{j}+F_3\hat{k}$ un campo vectorial de clase $C^1$. Se define el operador divergencia como:
>
>
$$\text{div}\;\vec{F}:=\frac{\partial F_1}{\partial x}+\frac{\partial F_2}{\partial y}+\frac{\partial F_3}{\partial z}$$Normalmente también resulta útil la notación: $$\nabla=\hat{i}\frac{\partial}{\partial x}+\hat{j}\frac{\partial}{\partial y}+\hat{k}\frac{\partial}{\partial z}$$De modo que se llega a la relación con el operador gradiente de tal forma que se establece: 
$$\text{div}\;\vec{F}=\nabla\cdot\vec{F}$$Notemos que también se cumple que dado $\vec{r_0}\in\Omega$, $\text{div}\;\vec{F}(\vec{r_0})=\text{traza}\;(J_f(\vec{r_0}))$


En términos generales, la divergencia en los campos vectoriales describe la tasa neta de flujo del campo que sale o entra en una región infinitesimal alrededor del punto. Notemos que al ser una tasa, el resultado es **escalar**. 

>[!note] Laplaciano 
>
>Sea $f$ un campo escalar de clase $C^2$, se define el laplaciano de $f$ como: 
>
>$$\Delta f:=\text{div}(\nabla f)=\frac{\partial^2 f}{\partial x^2}+\frac{\partial^2 f}{\partial y^2}+\frac{\partial^2 f}{\partial z^2}$$
>
>De forma análoga se define el Laplaciano para un campo vectorial como: 
>
>$$\Delta\vec{F}=\Delta F_1\hat{i}+\Delta F_2\hat{j}+\Delta F_3\hat{k}$$
>
>Notemos que cumple una relación directa con la divergencia, pues pareciera ser una divergencia para la segunda derivada parcial. De hecho, a menudo se puede escribir también como $\nabla^2$

Su interpretación apunta a como una función o componente de un campo vectorial varía en promedio con respecto a los valores en puntos cercanos. 

>[!note] Rotor
>
>Sea $\vec{F}=F_1\hat{i}+F_2\hat{j}+F_3\hat{k}$ un campo vectorial de clase $C^1$, se define el rotor como: 
>
>$$\text{rot}\;\vec{F}=\left(\frac{\partial F_3}{\partial y}-\frac{\partial F_2}{\partial z}\right)\hat{i}+\left(\frac{\partial F_1}{\partial z}-\frac{\partial F_3}{\partial x}\right)\hat{j}+\left(\frac{\partial F_2}{\partial x}-\frac{\partial F_1}{\partial y}\right)\hat{k}$$
>
>Pareciera ser algo azaroso, pero en realidad se puede describir utilizando el **producto cruz** entre la función y su divergencia:
>
>$$\text{rot}\;\vec{F}=\nabla\times\vec{F}=\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
F_1 & F_2 & F_3
\end{vmatrix}$$

Normalmente representa la magnitud con la que un campo vectorial está rotando. Por ejemplo, si se tiene el campo vectorial $F(x,y)=(-y,x)$, su rotor sería $2\hat{k}$, representando una rotación constante.
![[frame_0.0.png|center|450]]
<div style="page-break-after: always;"></div>

# Integrales de línea 

La integral de línea es una extensión del concepto de integración, donde se mide cuánto de un campo vectorial "fluye" a lo largo de una trayectoria o curva específica. Por lo tanto, antes de poder trabajar sobre este tipo de integral, es necesario definir las curvas. 

## Curvas 

Una curva es una función que se asigna un número real a un punto del espacio. En este caso, a diferencia de la definición "*clásica*" de curvas, se debe ver como **un conjunto de puntos que son recorridos en cierto orden**. 

>[!cite] Curva paramétrica 
>
>Una **curva paramétrica** $\mathbb{C}$ en $\mathbb{R}^n$ es un conjunto dirigido de puntos de la forma: 
>
>$$\vec{x}=\vec{\alpha}(t)=(\alpha_1(t),\alpha_2(t),\dots,\alpha_n(t))\;\;\;\;{a\leq t\leq b}$$
>
>Donde $\alpha_1,\alpha_2,\dots,\alpha_n$ son funciones continuas en $[a,b]$, decimos que el conjunto es dirigido porque $\vec{\alpha}$ dicta un orden (o sentido) en el cual los puntos de $\mathbb{C}$ son recorridos cuando $t$ varía desde $a$ hacia $b$.
>
>Se dice que la función $\vec{\alpha}:[a,b]\to\mathbb{R}^n$ es una **representación paramétrica** de $\mathbb{C}$. 

Existen distintos tipos de curvas; 

- **Curvas cerradas**: Diremos que una curva es cerrada si $r(a)=r(b)$, vale decir, comienza y termina en el mismo punto. Por ejemplo, un cuadrado o una circumferencia. 

- **Curvas continuas y suaves**: La curva es **continua** si la función $r:[a,b]\to\mathbb{R}^n$ es continua. Diremos que $C$ es derivable (**suave**) en $[a,b]$ si $r$ es derivable en $[a,b]$. 

- **Curva simple**: Las curvas **simples** pueden ser curvas cerradas, pero se dice que una curva es simple si no se intersecta a si misma salvo en los extremos. No simple sería lo contrario. 

El siguiente ejemplo sería el de una curva **no simple** y **cerrada**. Se esboza una intersección pero existen más. 
![[curva2.png|center|600]]
Por último, diremos que la curva es **positiva** cuando se recorre en sentido antihorario. 

<div style="page-break-after: always;"></div>

## Integral de línea 

Un ejemplo usual que se ocupa para introducir las integrales de línea es el del trabajo por el campo de fuerzas sobre una partícula cuando describe una trayectoria. Acordémonos que para el caso de una fuerza constante se tenía que: 

$$\vec{F}\cdot\vec{d}\tag{Trabajo}$$

Ahora, si asumimos que la trayectoria $\mathbb{C}$ no es recta y la fuerza no es constante, se podría decir que la curva se podría definir por un número finito de desplazamientos rectos. Supongamos que la trayectoría está definida por $\vec{\alpha}(t):[a,b]\to\mathbb{R}^3$, si $t$ varía en un intervalo pequeño ($\Delta t$) que el desplazamiento vectorial se vería como $\Delta\vec{d}=\vec{\alpha}(t+\Delta t)-\vec{\alpha}(t)$. 

![[ejemploTrabajo.png|center|600]]



Ahora, si dividimos el intervalo $[a,b]$ en $n$ partes iguales, con $a=t_0<t_1<\dots<t_n=b$ y $\Delta t=t_{i+1}-t_i$ se puede llegar a armar una **suma de Riemann**, donde el trabajo realizado por $\vec{F}$ es aproximadamente: 

$$W=\sum^{n-1}_{i=0}\vec{F}\left(\vec{\alpha}(t_i)\right)\cdot\vec{\alpha'}(t_i)\;\;\Delta t$$

Ahora, lo interesante es cuando $n\to\infty$, donde se llega que el trabajo es precisamente la siguiente integral: 

$$W=\int^{b}_{a}\vec{F}(\vec{\alpha}(t))\cdot\vec{\alpha'}(t)\;dt$$


Por lo tanto, a partir de este concepto, se puede definir la **integral de línea**: 

>[!example] Integral de línea 
>
>Supongamos que $\mathbb{C}$ es una curva **suave** en $\mathbb{R}^n$ y que $\vec{F}$ es un campo vectorial definido y continuo sobre la traza de $\mathbb{C}$. Entonces la integral de línea de $\vec{F}$ a lo largo de $\mathbb{C}$ está definida por: 
>
>$$\int^{}_{C}\vec{F}\cdot d\vec{x}=\int^{b}_{a}\vec{F}(\vec{\alpha}(t))\cdot\vec{\alpha'}(t)\;dt$$
>
>Donde $\vec{\alpha}$ es una representación **suave** de $\mathbb{C}$ y "$\cdot$" representa el producto punto entre vectores. 


De aquí, directamente por la definición de la positividad de la curva, se puede deducir el primer teorema: Si $\mathbb{C}$ es una curva **seccionalmente suave** y $\vec{F}$ es un campo vectorial definido y continuo sobre la traza de $\mathbb{C}$, entonces: 

$$\int_{-\mathbb{C}}\vec{F}\cdot d\vec{x}=-\int^{}_{\mathbb{C}}\vec{F}\cdot d\vec{x} $$

Por último, notar que también **se cumple la linealidad**. Si $\mathbb{C}$ es una curva **seccionalmente suave**, $\vec{F}$ y $\vec{G}$ son campos vectoriales continuos sobre la traza de $\mathbb{C}$ y $a,b\in\mathbb{R}$, entonces: 

$$\int^{}_{\mathbb{C}}(a\vec{F}+b\vec{G})\cdot d\vec{x}=a\int^{}_{\mathbb{C}}\vec{F}\cdot d\vec{x}+b\int^{}_{\mathbb{C}}\vec{G}\cdot d\vec{x}$$
<div style="page-break-after: always;"></div>

## Campos conservativos 

Notemos la siguiente intuición; sea $f(x,y)$ una **función en varias variables**, vale decir, una función que depende implícitamente de otra variable $t$: 

$$\begin{align}
t&\to f\left(x(t),y(t)\right)
\end{align}$$

Si nos acordamos de la definición de regla de la cadena, podemos notar que al derivar $t$, se debe llegar a lo siguiente: 

$$\frac{d}{dt}\left[f\left(x(t),y(t)\right)\right]=\frac{\partial f}{\partial x}\cdot x'(t)+\frac{\partial f}{\partial y}\cdot y'(t)$$

Esto puede ser reescrito de otra forma como un **producto punto** entre las derivadas parciales llegando a: 

$$\frac{d}{dt}\left[f\left(x(t),y(t)\right)\right]=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)\cdot\left(x'(t),y'(t)\right)$$

Notemos que esto es algo **muy parecido** a la **integral de línea**, donde se multiplica la derivada de la parametrización por una función. Ahora, notemos que el vector de la izquierda, en realidad es el **vector gradiente**. Podríamos de hecho, intentar hacer la integral de línea de ésta. Sea $F(x,y)=\nabla f(x,y)$, entonces: 

$$\begin{align}
\int^{}_{C}F\cdot dr&=\int^{b}_{a}F(x(t),y(t))\cdot (x'(t),y'(t))\;dt\\  \\
&=\int^{b}_{a}\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\right)\cdot\left(x'(t),y'(t)\right)\; dt\\  \\
&=\int^{b}_{a}\frac{d}{dt}\left[f\left(x(t),y(t)\right)\right]\;dt\\  \\
&=f(x(b)),y(b))-f(x(a),y(a))\tag{TFC}
\end{align}$$

Notemos que esto **no depende de la parametrización de la curva**, vale decir, hay una **independencia del camino**. 

>[!example] Campos conservativos 
>
>Sea $F:\Omega\subseteq\mathbb{R}^n\to\mathbb{R}^n$, un campo vectorial regular, $\Omega\subseteq\mathbb{R}^n$ un conjunto abierto y $C\subseteq\Omega$ una curva **regular a trozos**. 
>
>Supongamos que $\rho_0$ es el punto inicial de $C$ y $\rho_1$ es el punto final de $C$. Si existe $f:\Omega\subset\mathbb{R}^n\to\mathbb{R}$ tal que $F=\nabla f$, entonces: 
>
>$$\int^{}_{C}F\cdot dr=f(\rho_1)-f(\rho_0)$$
>
>A la función $f$ se le llamará **potencial**. 

A partir de esta demostración y definición, se pueden llegar a **las tres equivalencias** principales: 

-  Las integrales de línea de $\vec{F}$ son independientes del camino. 

-  $\int_{\mathbb{C}}\vec{F}\cdot d\vec{x}=0$ para toda curva cerrada $\mathbb{C}$ y seccionalmente suave. 

- Existe un campo escalar $f:D\subseteq\mathbb{R}^n\to\mathbb{R}$ tal que $\vec{F}=\nabla f$. 

Notemos, que la principal condición para que se cumpla, es que $F=\nabla f$, vale decir, **la función debe ser el gradiente de otra**. Por lo tanto, se plantea el siguiente teorema para saber si $\vec{F}$ es un campo vectorial conservativo: 

>[!example] Condición para campos conservativos 
>
>Si $\vec{F}=(F_1,\dots,F_n)$ es un campo vectorial conservativo de clase $C^1$ en un conjunto abierto $D$ de $\mathbb{R}^n$, entonces: 
>
>$$\frac{\partial F_i}{\partial x_j}(x)=\frac{\partial F_j}{\partial x_i}(x)\;\;\;\;\;\;\;\;\;\forall x\in D\;\;\land\;\;\forall i,j\in\lbrace 1,\dots,n\rbrace$$
>
>Todo esto si $D$ es conexo, vale decir, para todo par de puntos dentro de $D$ se puede formar una curva que esté completamente contenida dentro de $D$. 

Es decir, las derivadas parciales mixtas del campo vectorial deben coincidir para cada componente.

Aún así, existe también otra forma de verificar que un campo vectorial sea conservativo, y es por el **Teorema de Stokes**, que luego se retomará para relacionar la integral de línea con la de superficie. 

>[!example] Teorema de Stokes 
>
>Para un campo vectorial $\vec{F}$ en el espacio tridimensional, si cumple las siguientes condiciones: 
>
>- $\vec{F}$ es continuamente diferenciable en un conjunto abierto que contiene a la región de interés. 
>  
>  - El **rotor** de $\vec{F}$, denotado como $\nabla\times\vec{F}$, es el vector cero en toda la región, es decir, $\nabla\times\vec{F}=\vec{0}$. 
>    
>    Entonces, el campo $\vec{F}$ es conservativo. En otras palabras, existe una función escalar $f$ tal que $\vec{F}=\nabla f$, donde $f$ es el potencial. 

<div style="page-break-after: always;"></div>

## Regiones Simplementes Conexas 

A partir de las definiciones anteriores, se mencionó sobre la necesidad que se cumpla que $D$ sea un conjunto conexo. Intuitivamente, como fue descrito anteriormente, significa que toda curva cerrada $C$ contenida en $D$ pueda ser deformada, sin quebrarse y sin salirse de $D$ hasta reducirse a un punto. 

>[!cite] Conjuntos simplementes conexos 
>
>Sea $D$ un subconjunto abierto y conexo de $\mathbb{R}^2$. Se dice que $D$ es **simplemente conexo** si, para toda curva cerrada $\mathbb{C}$ contenida en $D$, la región interior a $\mathbb{C}$ es también un subconjunto de $D$.

El ejemplo clásico de un conjunto que no cumple esto es el anillo o el toro de revolución: 
![[toro.png|center]]
Notemos que el hecho de tener un hueco o un hoyo hace que no se cumpla la premisa de ser simplemente conexo. 

## Teorema de Green 

>[!example] Teorema de Green 
>
>Sea $\Omega\subseteq\mathbb{R}^2$, un conjunto simplemente conexo y conexo, cuya **frontera** está dada por una curva $C$, regular y simple. Supongamos además que $C$ está recorrida en recorrido antihorario. 
>
>Además, sea $F:A\subseteq\mathbb{R}^2\to\mathbb{R}^2$ una función de clase $C^1$ en $A$, y $\bar{\Omega}\subseteq A$. Además, $F=(P,Q)\iff P\hat{i}+Q\hat{j}$. Entonces:  $$\oint_CF\cdot dr=\oint_CPdx+Qdy=\int\int_\Omega\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dxdy$$

Además, se puede desprender que si se tiene una curva **cerrada** donde $R$ es el área que encierra la región interior a $C$ (**región acotada por $C$)**, se cumplen las siguientes igualdades: 

$$\text{Area de R}=\oint_Cxdy=-\oint_Cydx=\frac{1}{2}\oint_C-ydx+xdx$$

Ahora, es posible extender el teorema de Green para el caso donde el conjunto no es conexo, como lo sería para un anillo. Vale decir, cuando el conjunto contiene *hoyos* o *vacios* en su interior. Formalmente se podrían describir como la región $R$ que presenta las siguientes características: 

Sean $C_1, C_2, \dots, C_k$ $k$ curvas de **cerradas** y **seccionalmente suaves**, contenida en $\mathbb{R}^2$, que tienen las siguientes propiedades: 

-  Dos cualesquiera de esas curvas no se intersectan 

- Todas las curvas $C_2,\dots C_k$ están situadas en la región interior de $C_1$ 

- Para cada $i\neq j$, $i>1$, $j>1$, la curva $C_i$ está situada en la región exterior de la curva $C_j$ 
![[2D_green_example_with_true_holes-3.png|center|450]]

>[!example] Extensión del Teorema de Green 
>
>Sea $\Omega\subset\mathbb{R}^2$, un **conjunto abierto** no vacio, donde su **frontera** corresponde a **curvas cerradas simples seccionalmente suaves**, todas recorridas en sentido antihorario disjuntas entre ellas, y $C_1,\dots,C_n\subset C_0$. 
>
>Además, sea $F:A\subseteq\mathbb{R}^2\to\mathbb{R}^2$ una función suave tal que: 
>$$F=P\hat{i}+Q\hat{j}\;\;\land\;\;\bar{\Omega}\subseteq A$$
>
>Entonces: 
>$$\begin{align}
>\int\int_{\Omega}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)dA&=\oint_{C_o}P\;dx + Q\;dy - \sum^{n}_{i=1}\oint_{C_i}P\;dx+Q\;dy
>\end{align}$$

De forma simple, llegaría a ser lo equivalente al primer planteamiento del Teorema de Green a excepción que se **restan las curvas cuyas regiones causan algun *hoyo* dentro del conjunto $\Omega$**. 

<div style="page-break-after: always;"></div>

# Integral de superficie 

Las integrales de superficie son una especie de extención de la integral de línea al medir cómo un campo vectorial *"fluye"* a través de una superficie y no sólo a lo largo de una curva. Nos podríamos imaginar una hoja delgada y flexible suspendida en el espacio, y un flujo de airea (que puede variar en dirección y magnitud) soplando a través de ella. La integral de superficie nos da una medida cuantitativa de cuanto aire pasaría por la hoja en lugar de simplemente rozarla. Al igual que con las integrales de línea, antes de sumergir a la integral como tal, es necesario definir lo que son las superficies en el contexto del cálculo vectorial.
![[surface_integral_modified.png|center|550]]
## Representación Paramétrica de una Superficie 

Existen tres formas de representar las superficies, pero para efectos de este curso, se ocupará la **representación paramétrica**. 

Acordándonos que la representación paramétrica de las curvas nos dejaban ver el espacio geométrico del recorrido en función de **una variable**, para el caso de las superficies se van a ocupar **dos variables** (notemos también que las superficies ocupan una dimensión más que las curvas). 

>[!cite] Superficie paramétrica 
>
>Sean $T$ un subconjunto conexo del plano $\mathbb{R}^2$ y $X,Y,Z:T\subseteq\mathbb{R}^2\to\mathbb{R}$ funciones continuas. El subconjunto de $\mathbb{R}^3$: 
>
>$$S=\lbrace (X(u,v),Y(u,v),Z(u,v))\;\; :\;\; (u,v)\in T\rbrace$$
>
>Se llama una **superficie paramétrica**. 

Y, por lo tanto, al combinar los tres componentes de la superficie paramétrica se tendrá las **ecuaciones paramétricas** de la superficie $S$. 

$$\text{Ecuaciones paramétricas}=\begin{cases}x&=X(u,v)\\  \\
y&= Y(u,v)\;\;\;\;\;\; (u,v)\in T\\  \\
z&= Z(u,v)\end{cases}$$


Por último, si introducimos un vector $\vec{r}$ que une el origen a un punto $(x,y,z)$ de la superficie, se podría combinar las tres ecuaciones paramétricas para llegar a la **ecuación vectorial** de $S$. 

$$\vec{r}(u,v)=(X(u,v),Y(u,v),Z(u,v))\;\; :\;\; (u,v)\in T$$

El resultado de las transformaciones sería el siguiente: 

![[parametric_surface_representation-1.png|center|700]]

<div style="page-break-after: always;"></div>

## Producto Vectorial Fundamental 

Tras haber definido la parametrización de superficies, es posible considerar los siguientes vectores, dada una parametrización $\vec{r}(u,v)$: 

$$\frac{\partial\vec{r}}{\partial u}=\left(\frac{\partial X}{\partial u},\frac{\partial Y}{\partial u},\frac{\partial Z}{\partial u}\right)\;\;\;\land\;\;\;\frac{\partial\vec{r}}{\partial v}=\left(\frac{\partial X}{\partial v},\frac{\partial Y}{\partial v},\frac{\partial Z}{\partial v}\right)$$

>[!example] Producto Vectorial Fundamental 
>
>El producto vectorial $\frac{\partial\vec{r}}{\partial u}\times\frac{\partial\vec{r}}{\partial v}$ se denomina **producto vectorial fundamental** de la representación $\vec{r}$. Sus componentes pueden expresarse como determinantes jacobianos: 
>
>$$\frac{\partial\vec{r}}{\partial u}\times\frac{\partial\vec{r}}{\partial v}=\begin{bmatrix}
\hat{x} & \hat{y} & \hat{z} \\
\frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & \frac{\partial Z}{\partial u} \\
\frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & \frac{\partial Z}{\partial v}
\end{bmatrix}=\left(\frac{\partial (Y,Z)}{\partial (u,v)},\frac{\partial (Z,X)}{\partial (u,v)},\frac{\partial (X,Y)}{\partial (u,v)}\right)$$

Si $(u,v)$ es un punto en $T$ en el cual $\frac{\partial\vec{r}}{\partial u}$ y $\frac{\partial\vec{r}}{\partial v}$ son continuas y el producto vetorial fundamental es no-nulo, entonces el punto imagen $\vec{r}(u,v)$ se llama **punto regular de $\vec{r}$**. 

Notemos que el plano determinado por $\frac{\partial\vec{r}}{\partial u}$ y $\frac{\partial\vec{r}}{\partial v}$ se llaman **planos tangentes a la superficie** y justamente, como se tiene un plano tangente, el **producto vectorial fundamental representa el vector normal a la superficie**. 
![[sphere_tangent_v3.png|center]]
Por lo tanto, la intuición a desarrollar al definir la integral de línea tiene que ver justamente con el vector normal a la superficie, ya que esto nos da el sentido al flujo que transcurre por la superficie. 


## Área de una superficie 

A partir de la definición anterior, es posible calcular el área de la superficie al ocupar el vector tangencial y su norma: 

>[!example] Área de una superficie 
>
>Dada la superficie $\Sigma$ de ecuación $\vec{r}=\vec{F}(u,v)$ con $(u,v)\in D$, si $\Sigma$ es suave y simple, el área de la misma se puede calcular mediante: 
>
>
$$A(\Sigma)=\int\int_D\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv$$Con $D\subset\mathbb{R}^2$ acotado y de frontera de área nula, vale decir, un conjunto abierto. Además, notar que $\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}$ es otra forma de definir el producto vectorial fundamental. 

Acordándonos que el plano tangente se devine como $\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)$, entonces lo que se está haciendo es recorrer la superficie mediante el plano tangente a través todo el dominio. 

Ahora, notemos que al hacer el cálculo $\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv$ lo que se está haciendo, en realidad, es obtener la **norma** del vector normal a la superficie. Y justamente esta norma representa el área del pequeño paralelógramo que se forma en el producto cruz. 

Un ejemplo trivial es el **producto cruz** de los vectores $\vec{v_1}=(1,0,0)$ y $\vec{v_2}=(0,0,1)$. Esto claramente forman un cuadrado de área $1$ entre ellos, y al hacer el producto $\vec{v_1}\times\vec{v_2}$ se obtiene el vector $\vec{v_3}=(0,1,0)$, que casualmente es perpendicular a $\vec{v_1}$ y $\vec{v_2}$ y además $\vert\vert\vec{v_3}\vert\vert=1=\text{Área}$. 

Por ende, definimos el término **diferencial de área** como $\vert\vert\vec{F_{u}^{'}}(u,v)\times\vec{F_{v}^{'}}(u,v)\vert\vert\;dudv=d\sigma$. 


<div style="page-break-after: always;"></div>

## Integral de superficie para un campo escalar 

Dado que en las superficies es importante saber la orientación de cada vector en función a la superficie, entonces se definen dos operaciones distintas para cada tipo de campo. 

>[!example] Integral de superficie para un campo escalar
>
>Sea $\Sigma$ la **superficie** de ecuación $\vec{r}=\vec{F}(u,v)$ con $(u,v)\in D$ suave y simple, supongamos que $\Sigma\subset H$, donde $H\subset \mathbb{R}^3$ es un **conjunto abierto**. 
>
>Sea $f:H\subset\mathbb{R}^3\to\mathbb{R}$ una **función continua** en $H$. Se llama integral de superficie de $f$ sobre $\Sigma$, denotado: 
>
>$$\int\int_\Sigma fd\sigma=\int\int_D f(\vec{F}(u,v))\;\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert\;dudv$$

 Esto sería similar al *costo del área de superficie*. 

  ![[surface_portion.png|center|500]]A partir de la definición se pueden deducir ciertas cosas:

- Observemos que si $f(\vec{X})=1$, entonces, $\forall\vec{X}\in\Sigma$ se tendría que $\int\int_\Sigma d\sigma=\text{Área}(\Sigma)$. 

- Si $\delta>0$ representa la densidad superficial de masa, entonces: 

$$\int\int_\Sigma \delta d\sigma=\int\int_D \delta(\vec{F}(u,v))\;\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert\;dudv=\text{Masa}(\Sigma)$$

- El valor medio de $f$ sobre $\Sigma$ se define como: 

$$f_{med}=\frac{1}{\text{Área}(\Sigma)}\int\int_\Sigma fd\sigma$$ 

## Integral de superficie para un campo vectorial 

La intuición bajo la integral de superficie para el campo vectorial llegaría a ser *cuánto campo de $f$ está en la dirección del plano normal a la superficie.* 

>[!example] Integral de superficie para un campo vectorial 
>
>Sea $\Sigma$ la superficie de ecuación $\vec{X}=\vec{F}(u,v)$ con $(u,v)\in D$ suave y simple y supongamos que $\Sigma\subset H$, donde $H\subset \mathbb{R}^3$ es un **conjunto abierto**. 
>
>Sea $\vec{f}:H\subset\mathbb{R}^3\to\mathbb{R}^3$ un campo vectorial continuo en $H$. Se llama integral de superficie o flujo del campo vectorial $\vec{f}$ a través de $\Sigma$: 
>
>$$\int\int_\Sigma \vec{f}\cdot\hat{n}\;d\sigma=\int\int_D\vec{f}(\vec{F}(u,v))\cdot\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\;dudv $$

Notemos que esta notación es consistente con la definición, pues: 

$$\hat{n}=\frac{\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)}{\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert}\;\land\;d\sigma=\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert\;dudv$$ 

<div style="page-break-after: always;"></div>

## Teorema de Gauss 

El teorema de Gauss relaciona el operador divergencia ($\vec{\nabla}\cdot\vec{F}$) con la integral de superficie para campos vectoriales. 

>[!example] Teorema de Gauss 
>
>Sea $D$ una región sólida acotada en $\mathbb{R}^3$, limitada por una superficie seccionalmente suave y **cerrada** $\Sigma$, y supongamos que $\vec{f}$ es un campo vectorial de clase $C^1$ en $D$ y $\hat{n}$ es la orientación de $\Sigma$ que apunta hacia el exterior. Entonces: 
>
>$$\int\int_{\Sigma}\vec{f}\cdot\hat{n}\;d\sigma=\int\int\int_{D}\text{div}\vec{f}(x,y,z)\;dx\;dy\;dz$$

Vale decir, con tal de tener la región que parametriza el campo vectorial, es posible obtener la integral de superficie. 





