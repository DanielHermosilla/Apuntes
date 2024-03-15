
# Series de Fourier 

Unos de los conceptos más importantes de las matemáticas son las **Series de Fourier**, concepto que introducen la resolución de varios problemas físicos y matemáticos, como lo son ecuaciones en derivadas parciales.

Como motivación, las series de Fourier nacen ante la necesidad de aproximar funciones sin la necesidad de hacer una Serie de Taylor, que como requisito pide que la función sea clase $C^1$. 

Las series de Fourier han permitido poder relacionar casi todo tipo de funciones a través de series trigonométricas, dando la oportunidad de analizar fenómenos no regulares (como señales u ondas). 

Anterior a la definición de la serie de Fourier, es necesario definir algunos conceptos: 

>[!example] Convergencia puntual de una serie de funciones 
>Para cada $k\in\mathbb{N}\cup\lbrace 0\rbrace$, sea $f_k:\mathbb{R}\to\mathbb{R}$ una función. Se dice que la serie de funciones $\sum^{\infty}_{k=0}f_k(x)$ **converge puntualmente** en $I\subset\mathbb{R}$ si para cada $x\in I$ la sucesión de numeros reales la sucesión definida por $S_n(x)=\sum^{n}_{k=0}f_k(x)$ converge. 

>[!example] Continuidad por tramos 
>Una función es continua por tramos en un intervalo $[a,b]$ si: 
>
>- $f$ es continua excepto en un número finitos de puntos 
>  
>  
>- Los límites $f(x_{0}^+)$ y $f(x_{0}^-)$ existen y son números reales. 

>[!example] Paridad de una función 
>Se dice que una función $f$ es: 
>
>- **Par:** Si $f(-x)=f(x)$ para todo punto en su dominio 
>  
>  - **Impar:** Si $f(-x)=-f(x)$ para todo punto en su dominio 

Los ejemplos más comunes de funciones pares e impares llegarían a ser la función $x^2$ y $x^3$ respectivamente: 

![[ParidadFunc 1.png|center|650]]

Una propiedad **muy** importante de estas funciones, es la de la multiplicación de funciones: 

$$\begin{align}
\text{Par}\cdot\text{Par}=\text{Impar}\cdot\text{Impar}&=\textbf{Par}\\\\
\text{Par}\cdot\text{Impar}=\text{Impar}\cdot\text{Par}&=\textbf{Impar}
\end{align}$$



A partir de esto, se define la **serie de Fourier**, dada una función continua por tramos en $[-\pi,\pi]$: 

$$S_F=\frac{a_0}{2}+\sum^{\infty}_{k=1}(a_k\cos(kx)+b_k\sin(kx))$$

Donde: 

$$\begin{align}
a_k&=\frac{2}{\pi}\int^{\pi}_{-\pi}f(x)\cos(kx)\;dx&\forall k\in\mathbb{N}\cup\lbrace 0\rbrace\\  \\
b_k&=\frac{2}{\pi}\int^{\pi}_{-\pi}f(x)\sin(kx)\;dx&\forall k\in\mathbb{N}
\end{align}$$

>[!error] Teorema de convergencia puntual de Fourier 
>Sea una función $f$ donde su primera derivada $f'$ es derivable por tramos en $[-\pi,\pi]$, entonces se cumple que: 
>
>$$\frac{f(x_{0}^+)-f(x_{0}^-)}{2}$$
>
>Para cada punto $x_0$ en el interior del intervalo. Sin embargo, para los límites $\pm\pi$ se cumple que: 
>
>$$\frac{f(-\pi^+)+f(\pi^-)}{2}$$


Un ejemplo claro de esto se puede ver para la función de Heavside, definida como: 

$$f_H(x)=\begin{cases}1&\forall x>0\\  \\
0&\forall x<0\end{cases}$$

Claramente la función es continua por tramos. De hecho, su único punto de discontinuidad es en $x=0$. Si esbozamos la serie de Fourier de la función, es posible visualizar que se cumple el teorema de convergencia puntual de Fourier para $x_0$: 

![[ConvergenciaDiscontinuidad.png|center|800]]

Notemos también que las funciones trigonométricas de la serie de Fourier son periódicas de período $2\pi$. Vale decir, toda función definida dentro de la serie de Fourier tendrá este salto de discontinuidad que se puede ver en la función de Heavside. 

## Series de Senos y Cosenos 

Si nos fijamos en los términos de la serie de Fourier, es posible percatarnos que algunos términos pueden ser cancelados si la función es **par** o **impar**. 

Haciendo el análisis para las funciones pares, sabemos que para toda función par se cumple que: 

$$\int^{L}_{-L}f(x)\;dx=2\int^{L}_{0}f(x)\;dx$$

Por el otro lado, si la función es impar, se cumple que: 

$$\int^{L}_{-L}f(x)\;dx=0$$

Ahora, notemos que la función **coseno** es **par**, y la función **seno** es **impar**. Además, recordando la definición de multiplicación de funciones pares e impares, es posible reducir la serie de Fourier a la siguiente expresión: 

$$S_F(x)=\begin{cases}\frac{a_0}{2}+\sum^{\infty}_{k=1}a_k\cos(kx)&\text{Si}\;f(x)\;\text{es par}\\\\  \\
\sum^{\infty}_{k=1}b_k\sin(kx)&\text{Si}\;f(x)\;\text{es impar}\end{cases}$$

La demostración de aquello es directo al aplicar la definición de cada término de la serie de Fourier y ocupar los argumentos de las integrales. 

<div style="page-break-after: always;"></div>

## Cambio de Intervalo 

A *priori* la serie de Fourier se ve útil pero sólo para funciones definidas entre $[-\pi,\pi]$, que en realidad son muy pocas las que cumplen eso. 

Por ende, antes de ver el caso general donde se tienen límites $a$ y $b$ cualquiera, se define la serie de Fourier en intervalos de la forma $[-p,p]$: 

$$S_F(x)=\frac{a_0}{2}+\sum^{\infty}_{k=1}\left(a_k\cos\left(\frac{k\pi x}{p}\right)+b_k\sin\left(\frac{k\pi x}{p}\right)\right)$$

Donde: 

$$\begin{align}
a_k&=\frac{1}{p}\int^{p}_{-p}f(x)\cos\left(\frac{k\pi x}{p}\right)\;dx&\forall k\in\mathbb{N}\cup\lbrace 0\rbrace\\  \\
b_k&=\frac{1}{p}\int^{p}_{-p}f(x)\sin\left(\frac{k\pi x}{p}\right)\;dx&\forall k\in\mathbb{N}
\end{align}$$

De hecho, basta notar que al reemplazar $p=\pi$ se vuelve a la definición *"original"* de la Serie de Fourier. 

Ahora, si se quisiera adaptar al caso **más general** con los límites $[a,b]$, se llega a lo siguiente: 

$$S_F(x)=\frac{a_0}{2}+\sum^{\infty}_{k=1}\left(a_k\cos\left(\frac{2k\pi x}{b-a}\right)+b_k\sin\left(\frac{2k\pi x}{b-a}\right)\right)$$

Donde: 

$$\begin{align}
a_k&=\frac{2}{b-a}\int^{b}_{a}f(x)\cos\left(\frac{2k\pi x}{b-a}\right)\;dx&\forall k\in\mathbb{N}\cup\lbrace 0\rbrace\\  \\
b_k&=\frac{2}{b-a}\int^{b}_{a}f(x)\sin\left(\frac{2k\pi x}{b-a}\right)\;dx&\forall k\in\mathbb{N}
\end{align}$$

Nuevamente, se llega a la serie *"original"* al reemplazar $a=-\pi$ y $b=\pi$. 

## Integración con Series de Fourier 

Al igual que las Series de Fourier nos permiten aproximar una función, también es posible representar su integral, que cumple lo siguiente: 

$$\int^{b}_{a}f(x)\;dx=\frac{a_0}{2}(b-a)+\sum^{\infty}_{k=1}\frac{a_k(\sin(kb)-\sin(ka))-b_k(\cos(kb)-\cos(ka))}{k}$$

Esto es resultado de integrar *término a término* la Serie de Fourier de $f(x)$. Gráficamente, para la función $\sin(x)$ en $x\in[0,\pi]$ se vería de la siguiente forma:

![[IntegralFourier.png|center|700]]

Recordemos que la aproximación de la Serie de Fourier es la **aproximación numérica del valor de la integral**, vale decir, es una especie de suma acumulada de la función integral. 

<div style="page-break-after: always;"></div>

# Transformada de Fourier 

La transformada de Fourier es una herramienta esencial que permite descomponer una función (usualmente temporal) en sus componentes frecuenciales. Mientras que la serie de Fourier descompone funciones periódicas en una suma de senos y cosenos (es decir, oscilaciones de distintas frecuencias), la transformada de Fourier se extiende a funciones no periódicas, representándolas en términos de una integral de ondas sinusoidales que abarca todo el espectro de frecuencias. Esta transformación es crucial en áreas como el procesamiento de señales, la física y la ingeniería, ya que ofrece una perspectiva diferente y a menudo más simplificada al analizar el comportamiento frecuencial de las señales y sistemas. Para el caso de este curso, se verá su aplicación para la **resolución de ecuaciones en Derivadas Parciales**. 

La transformada de Fourier de una función integrable se define de la siguiente forma: 

$$\begin{align}
\widehat{f}:\mathbb{R}&\to\mathbb{C}\\  \\
s&\to\widehat{f}(s)=\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}f(y)e^{-iys}dy
\end{align}$$

Es posible notar que la definición es muy parecida a la transformada de Laplace. De hecho, existe también la **antitransformada de Fourier:** 

$$\begin{align}
\check{g}:\mathbb{R}&\to\mathbb{C}\\  \\
x&\to\check{g}(x)=\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}g(s)e^{ixs}ds
\end{align}$$

El *cómo se llega* a la definición no puede ser abordable con los conocimientos del curso, pero existen algunos ejemplos de motivación que esbozan las ideas por detrás. 

>[!error] Teorema de inversión 
>Sea $f:\mathbb{R}\to\mathbb{C}$ una función integrable. Entonces se tiene que, para una función continua se cumple que: 
>
>$$f(x)=T^{-1}(Tf)(x)=\check{\widehat{f}}(x)$$

Nuevamente, una definición muy análoga a la transformada de Laplace. Se postula principalmente que la antitransformada de una transformada es la función original. 

## Transformada de una derivada 

Con una demostración que se agarra fuertemente que la funciones de las transformadas son integrables, se postula que la transformada de la derivada es: 

$$\widehat{f'}(s)=is\widehat{f}(s)$$

Ahora, para una función $k$ veces derivable, se cumple que: 

$$\widehat{f^{k}(x)}(s)=(is)^k\widehat{f}(s)$$

Ya con esto, y el teorema de inversión, es posible resolver ecuaciones diferenciales. 

#### Ejemplo: Ecuación Diferencial Ordinaria 

Considerando la siguiente EDO, con $y$ diferenciable: 

$$3y''+2y'+y=f(x)$$

Es posible aplicar la transformada de Fourier a ambos lados, al igual que se hacía con Laplace: 

$$\begin{align}
(-3s^2+2is+1)\widehat{y}(s)&=\widehat{f}(s)\\\\
\frac{\widehat{f}(s)}{-3s^2+2is+1}&=\widehat{y}(s)
\end{align}$$

Luego, por el teorema de inversión se puede aplicar la antitransformada, llegando que la solución corresponde a: 

$$y(x)=\frac{1}{\sqrt{2\pi}}\int^{\infty}_{-\infty}e^{ixs}\frac{\widehat{f}(s)}{-3s^2+2is+1}ds$$


<div style="page-break-after: always;"></div>


## Convolución 

Dada dos funciones integrables, se define la convolución como: 

$$(f*g)(x)=\int^{\infty}_{-\infty}f(x-y)g(y)dy=\int^{\infty}_{-\infty}g(x-y)f(y)dy$$

Saliendo un poco de la abstracción, la convolución es extremadamente útil en muchas áreas de las matemáticas. Es una forma *poco usual* de combinar dos funciones entre sí, pero que en la práctica hace mucho sentido. Esto no sólo se ocupa en análisis eléctricos, si no también en la Estadística para el análisis de distribuciones de datos. 

Gráficamente, en términos simples, la convolución "desliza" una función sobre la otra y calcula el área solapada en cada punto, resultando en una función suavizada. 

Un ejemplo simple es la función $\sin(x)*\sin(2x)$: 

![[convolucion.png|center|600]]

Por lo tanto, se postula la definición de la convolución con su transformada y antitransformada: 

$$\begin{align}
\widehat{f*g}(s)&=\widehat{f}(s)\widehat{g}(s)\sqrt{2\pi}\tag{Transformada}\\  \\
T^{-1}(\widehat{f}(s)\widehat{g}(s))(x)&=\frac{1}{\sqrt{2\pi}}(f*g)(x)\tag{Antitransformada}
\end{align}$$



## Resumen de propiedades 

Para resumir todas las propiedades se propone la siguiente tabla: 

|       **Propiedad**       |                                          **Transformada**                                         |
|:-------------------------:|:-------------------------------------------------------------------------------------------------:|
|         Linealidad        |                 $\widehat{\alpha f + \beta g}=\alpha\widehat{ƒ}+\beta\widehat{g}$                 |
|  Traslación en el espacio |                           $\widehat{f(x-x_0)}(s)=e^{isx_0}\widehat{f}(s)$                         |
|  Traslación en frecuencia |                           $\widehat{e^{is_0x}f(x)}(s)=\widehat{f}(s-s_0)$                         |
|   Modulación del coseno   |  $\widehat{f(x)\cos(\omega_0 x)}(s)=\frac{1}{2}[\widehat{f}(s-\omega_0)+\widehat{f}(s+\omega_0)]$ |
|     Modulación del seno   | $\widehat{f(x)\sin(\omega_0 x)}(s)=\frac{1}{2i}[\widehat{f}(s+\omega_0)-\widehat{f}(s-\omega_0)]$ |
|      Cambio de escala     |           $\widehat{f(ax)}(s)=\frac{1}{\vert a\vert}\widehat{f}\left(\frac{s}{a}\right)$          |
|    Inversión del espacio  |                                $\widehat{f(-x)}(s)=\widehat{f}(-s)$                               |
|         Convolución       |                     $\widehat{f*g}(s)=\sqrt{2\pi}\widehat{f}(s)\widehat{g}(s)$                    |
|         Derivación        |                            $\widehat{f^{(k)}(x)}(s)=(is)^k\widehat{f}(s)$                         |


<div style="page-break-after: always;"></div>


# Ecuaciones en Derivadas Parciales 


Una ecuación en derivadas parciales (EDP) es una ecuación cuya función incógnita tiene dos o más variables independientes. El orden de la ecuación lo establecerá la derivada de más alto orden. 

Algunas de las similitudes que mantienen con las Ecuaciones Diferenciales Ordinarias es que estas también se descomponen en una solución **homogénea** y **particular**. De hecho, también se cumple que sus soluciones corresponden a combinaciones lineales, que se pueden representar por el operador Laplaciano: 

$$L=\nabla=A\frac{\partial^2}{\partial x^2}+B\frac{\partial^2}{\partial y^2}+C\frac{\partial^2}{\partial z^2}$$
#### Ejemplo: Campo eléctrico 

Existen varias ecuaciones en derivadas parciales que son icónica de la física, como la ecuación de la onda o expansión del calor. Como un ejemplo introductorio, se presentará la ecuación de derivadas parciales del **potencial eléctrico**  

Se definirán dos vectores $\vec{x}=(x_1,x_2,x_3)$ y $\vec{y}=(y_1,y_2,y_3)$ para definir un punto en el espacio. Por lo tanto, es posible ver que el campo eléctrico generado por una cantidad finita de cargas $q_j$ se puede escribir de forma discreta como: 

$$\vec{E}(\vec{x})=\sum^{N}_{j=1}\frac{q_j}{4\pi\epsilon_0}\cdot\frac{\vec{x}-\vec{y_j}}{\vert\vert\vec{x}-\vec{y_j}\vert\vert^3}$$

Además, por propiedad de los campos eléctricos, éste es conservativo. Es decir: 

$$\begin{align}
\vec{\nabla}\times\vec{E}&=0\\  \\
\implies\vec{E}&=-\nabla\varphi
\end{align}$$

Si analizamos el caso para una distribución de cargas continuas, es posible reescribir el campo eléctrico como una integral con densidad de carga $\rho(\vec{y})$: 

$$\vec{E}(\vec{x})=\frac{1}{4\pi\epsilon_0}\iiint_\mathbb{R^3}\rho(\vec{y})\frac{\vec{x}-\vec{y}}{\vert\vert\vec{x}-\vec{y}\vert\vert^3}d\vec{y}$$

Por el otro lado, notemos que el campo eléctrico también proviene de un potencial, que en este caso es el **potencial eléctrico**: 

$$\vec{E}=-\nabla\phi$$

Por lo tanto, 

$$\phi(\vec{x})=\frac{1}{4\pi\epsilon_0}\iiint_\mathbb{R^3}\rho(\vec{y})\frac{1}{\vert\vert\vec{x}-\vec{y}\vert\vert}$$

Si asumimos un conjunto abierto $w$ con frontera $\partial w$, para poder calcular el flujo del campo eléctrico a través de la frontera se postula que: 

$$\begin{align}
\iint_{\partial w}\vec{E}\cdot d\vec{S}(\vec{x})&=\frac{1}{4\pi\epsilon_0}\iint_{\partial w}\left(\iiint_\mathbb{R^3}\rho(\vec{y})\frac{\vec{x}-\vec{y}}{\vert\vert\vec{x}-\vec{y}\vert\vert^3}d\vec{y}\right)d\vec{S}(\vec{x})\\  \\
&=\frac{1}{4\pi\epsilon_0}\iiint_{\mathbb{R}^3}\rho(\vec{y})\left(\iint_{\partial w}\frac{\vec{x}-\vec{y}}{\vert\vert\vec{x}-\vec{y}\vert\vert^3}d\vec{S}\right)d\vec{y}
\end{align}$$

Utilizando el teorema de Gauss, se puede decir que: 

$$\iint_{\partial w}\frac{\vec{x}-\vec{y}}{\vert\vert\vec{x}-\vec{y}\vert\vert^3}d\vec{S}=\begin{cases}4\pi&\text{si}\;\vec{y}\in w\\  \\
0&\text{si}\;\vec{y}\notin w\end{cases}$$

Por lo tanto, 

$$\iint_{\partial w}\vec{E}\cdot d\vec{S}(\vec{x})=\frac{1}{\epsilon_0}\iiint_w\rho(\vec{y})d\vec{y}$$

Si se aplica el teorema de divergencia para el campo eléctrico, se obtiene que: 

$$\begin{align}
\int\int\int_w\vec{\nabla}\cdot\vec{E}\;dV-\frac{1}{\epsilon_0}\iiint_w\rho\;dV&=0\\  \\
\iiint_w\left(\nabla\phi+\frac{1}{\epsilon_0}\rho\right)dV&=0
\end{align}$$

Como lo anterior debe ser valido para todo $w$, se concluye que el integrando debe ser nulo. De tal manera se llega a una **ecuación de Laplace**: 

$$-\nabla\phi=\frac{1}{\epsilon_0}\rho$$

Como se puede ver, se resolvió el problema para una función en dos variables mediante los teoremas de integrales de superficie. Más adelante se comprobará que es posible resolver este tipo de sistemas a partir de la **Transformada de Fourier**. 


<div style="page-break-after: always;"></div>


## Condiciones iniciales y de borde 

Las ecuaciones en derivadas parciales para poder ser resueltas se complementan de **condiciones de bordes** y **condiciones iniciales**. 

- **Condición de borde de tipo Dirichlet**: Por lo general estas condiciones de borde se plantean en la **frontera de un conjunto**. Si tenemos un conjunto $\Omega\subseteq\mathbb{R}$ con frontera $\partial\Omega$ y se tiene una función $u$ que no depende de la variable independiente, entonces las condiciones de borde se dan por la siguiente igualdad, con una función $g$ conocida:

$$u(x,y,z)=g(x,y,z)\;\;\;\forall x,y,z\in\partial\Omega$$


Un ejemplo sería para una esfera unitaria, $x^2+y^2+z^2=1$ donde se tienen los valores de $u(x,y,z)$ representado por el gradiente de colores sobre la superficie: 

![[conBordes.png|center]]

- **Condición de borde de tipo Neumann:** Se caracterizan por ser representadas de la forma: 

$$\nabla u\cdot\hat{n}=\frac{\partial u}{\partial\hat{n}}(t,\cdot)=h(\cdot)\;\;\;\text{sobre}\;\partial\Omega\;\;\;\forall t\in [t_0,T]$$ 
Donde $h$ es una función conocida que va por la frontera de $\Omega$. 

Para las condiciones iniciales, al igual que en las ecuaciones diferenciales ordinarias, se deben imponer la misma cantidad de condiciones iniciales que el orden de la derivada parcial. 

## Separación de variables 

El método de separación de variables, también ocupado en Ecuaciones Diferenciales Ordinarias, permite resolver Ecuaciones en Derivadas Parciales **introduciendo las series de Fourier**. 

Este tipo de resolución se da por lo general en ecuaciones que son lineales. Para este caso, se asumirá la siguiente ecuación: 

$$u_t(t,0)=\alpha u_{xx}\;\;\;0<x<L,\;\;t>0\tag{1}$$

Con $\alpha>0$ y condiciones de borde de tipo Dirichlet, donde: 

$$u(t,0)=u(t,L)=0\;\;\;\forall t>0$$

Por último, como es una EDP que evoluciona en el tiempo, se imponen las condiciones iniciales: 

$$u(0,x)=f(x)$$

La función a buscar es una función en dos variables $u(t,x)$ que puede ser comprendida como la ecuación del calor. Por tal motivo, se sigue una serie de pasos para la resolución de estas ecuaciones: 

### Separar variables 

Se intenta buscar dos funciones no triviales que puedan satisfacer: 

$$U(t,x)=T(t)X(x)$$

Por lo tanto, se introducen dos nuevas incógnitas, haciendo que se necesiten dos ecuaciones para encontrarlas. Notemos que la separación de variables son dos funciones que dependen **de una única variable**. Si se sustituyen en la ecuación original $(1)$ se tiene que: 

$$T'(t)X(x)=\alpha T(t)X''(x)$$

Asumiendo soluciones no triviales donde $X(x)\neq 0$, es posible decir que: 

$$T'(t)=\alpha\lambda_1 T(t)$$

Donde 

$$\lambda_1=\frac{X''(x)}{X(x)}$$

Haciendo el proceso inverso, se puede decir que: 

$$X''(x)=\lambda_2X(x)$$

Por lo tanto, si tomamos cualquier valor $(t,x)$ donde $T(t)\neq0$ y $X(x)\neq 0$

$$\alpha\lambda_1=\mathbf{\frac{T'(t)}{T(t)}=\alpha\frac{X''(x)}{X(x)}}=\lambda_2$$

Ahora, si nos fijamos en la parte enegrecida, se tiene la siguiente igualdad, donde un lado depende de una variable y el otro de la otra: 

$$\frac{T'(t)}{T(t)}=\alpha\frac{X''(x)}{X(x)}$$

Si queremos que ambas soluciones cumplan la igualdad para todo valor, esta igualdad debe ser igual a una constante. De tal modo, se deduce que: 

$$\begin{align}
T'(t)+\alpha\lambda T(t)&=0\tag{2}\\  \\
X''(x)+\lambda X(x)&=0\tag{3}
\end{align}$$

Con $\lambda$ una constante. 

Para la ecuación $(2)$ se deduce que la solución es: 

$$T(t)=Ce^{-\alpha\lambda t}$$

Para la ecuación $(3)$ se tienen distintos tipos de soluciones que dependen del signo de $\lambda$, ya que el polinomio característico llegaría a ser: 

$$p(m)=m^2+\lambda$$

- Si $\lambda<0$ se tiene que: 

$$X(x)=C_1e^{\sqrt{-\lambda x}}+C_2e^{\sqrt{-\lambda x}}$$

Con la definición de raiz cuadrada para los complejos. 

- Si $\lambda=0$, entonces: 

$$X(x)=C_1+C_2x$$

- Si $\lambda>0$: 

$$X(x)=C_1\cos(\sqrt{\lambda}x)+C_2\sin(\sqrt{\lambda}x)$$


### Imposición de las condiciones de borde 

Al imponer las condiciones de borde va a ser posible acotar los valores posibles de $\lambda$ a un conjunto numerable. 

Se puede verificar fácilmente que $\lambda=0$ corresponde a la solución trivial. Por lo tanto, se buscará para $\lambda\neq 0$. 

Para las condiciones de borde se debe satisfacer que: 

$$U_\lambda(t,0)=U_\lambda(t,L)=0\;\;\;\forall t>0$$

De $U_\lambda(t,0)=0$ se puede decir que: 

$$e^{-\alpha\lambda t}(C_1+C_2)=0\;\;\;\forall t>0$$

Como el exponencial no puede ser $0$, entonces: 

$$C_2=-C_1$$

De la segunda condición de borde se llega que: 

$$e^{\sqrt{-\lambda}L}-e^{-\sqrt{-\lambda}L}=0$$

Luego, como $L$ es dato del problema, se tiene que $\lambda=(k\pi/L)^2$ con $k\in\mathbb{Z}$. Luego, como interesa $\lambda\neq0$ y las soluciones de $k$ son iguales para $-k$, se estudia el caso donde $k\in\mathbb{N}$. 

Por lo tanto, volviendo al primer paso, se llega que las soluciones en variables separadas son de la forma: 

$$\begin{align}
U_\lambda(t,x)&=C_ke^{-\alpha(k\pi/L)^2t}\left[e^{ik\pi x/L}-e^{-ik\pi x/ L}\right]\\\\
&=C_ke^{-\alpha(k\pi/L)^2t}\;2i\sin(k\pi x/L)\\\\
&=A_k\Phi_k(t,x)
\end{align}$$

Como $A_k=2iC_k$, se tiene que: 

$$\Phi(t,x)=e^{-\alpha(k\pi/L)^2t}\sin(k\pi x/L)$$

Así, se ha obtenido una familia de soluciones para la ecuación diferencial: 

![[EcuacionCalor.png|center]]

Si se observan los primeros $5$ valores, se puede observar que estos corresponden a una especie de modos normales. 

### Imposición de la condición inicial 

Acordándonos que la condición inicial se había definido como $u(0,x)=f(x)$, entonces no estaría del todo incorrecto proponer una ecuación sinusoidal cuando $t=0$. Se puede ver por el gráfico que el comportamiento cumple tal requerimiento. Entonces: 

$$f(x)=A\sin(k_0\pi x/L)$$

Dado que la $k$-esima solución de $\Phi_k(0,x)=\sin(k\pi x/L)$, entonces es posible corroborar lo siguiente: 

$$\begin{align}
u(t,x)&=A\Phi_{k_0}(t,x)\\  \\
&=Ae^{\alpha(k_0\pi/L)^2t}\sin(k_0\pi x/L)
\end{align}$$

Esto se puede expresar de forma más general para constantes arbitrarias $A_m\in\mathbb{R}$ con la siguiente función de condiciones iniciales: 

$$f(x)=\sum^{m}_{i=1}A_i\sin(k_i\pi x/L)$$

Ahora, dado que cualquier combinación lineal de soluciones también son soluciones, basta verificar que se cumple lo siguiente con las condiciones de borde: 

$$\begin{align}
u(t,0)&=\sum^{m}_{i=1}A_ie^{\alpha(k_i\pi/L)^2t}\sin(0)=0\\  \\
u(t,L)&=\sum^{m}_{i=1}A_ie^{-\alpha(k_i\pi/L)^2t}\sin(k_i\pi)=0
\end{align}$$

Es directo verificar que $u(0,x)=f(x)$. 

Ahora, ¿qué hubiera ocurrido si $f(x)$ no hubiera sido una función sinusoidal, si no una función cualquiera? Bastaría con escribir $f(x)$ como una **serie de Fourier de senos**: 

$$f(x)=\sum^{\infty}_{k=1}A_k\sin(k\pi x/L)$$

Por lo tanto, de la forma más resumida posible, **el método de Separación de Variables busca resolver EDPs de la forma**: 

$$u(t,x)=\sum A_kU_k(t,x)$$

Donde los coeficientes de $A_k$ se ajustan para cumplir condiciones de borde e iniciales. 
 
