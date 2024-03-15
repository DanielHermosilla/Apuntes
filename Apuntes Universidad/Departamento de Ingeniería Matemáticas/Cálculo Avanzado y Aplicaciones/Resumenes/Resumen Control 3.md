# Contenidos: 

1. Funciones homolorfas: Condiciones de Cauchy-Riemann 

2. Series de potencias: Radio de convergencia y series conocidas 

3. Integrales complejas: Teorema de Cauchy-Goursat 

No entra fórmula integral de Cauchy. 
# Cálculo Complejo 

Los números complejos nacen de la necesidad de poder introducir un elemento que puedan transformar a los números reales en un anillo matemático. 

De tal forma, se introduce el plano complejo que representan los puntos de los números reales e imaginarios. 

>[!example] Función en $\mathbb{C}$
>
>Se define una función $f:\mathbb{C}\to\mathbb{C}$ a aquella que se pueda descomponer en una parte **real e imaginaria**. De tal forma, por lo general, se representaran a las funciones de la siguiente forma: 
>
>$$\begin{align}
 f:\mathbb{C}&\to\mathbb{C}\\  \\
f(x,y)&\to u(x,y)+iv(x,y)\end{align}$$
Así, las funciones representan un **conjunto de puntos** en el plano complejo que representarían una **curva en el plano complejo**. 

La definición e implicancias de la continuidad las hereda del cálculo real. Lo que cambia es la definición de diferenciabilidad, lo que en este caso se les denominará como **funciones homolorfas**. 

## Diferenciabilidad 

Por definición de derivada, se dirá que una función compleja dentro de un conjunto abierto $D$ es derivable en $z_0$ si existe el siguiente límite: 

$$\lim_{z\to z_0}\frac{f(z)-f(z_0)}{z-z_0}=f'(z_0)$$

Esto cumple con todas las propiedades aritméticas de la derivada: derivada de la suma, regla de la cadena, etc. 

>[!example] Teorema de Cauchy-Riemann 
>
>Si una función compleja es derivable en un punto $z_0$ entonces se deben cumplir las siguientes igualdades: 
>
>$$\begin{align}
\frac{\partial u}{\partial x}(x_0,y_0)&=\frac{\partial v}{\partial y}(x_0,y_0)\\  \\
\frac{\partial u}{\partial y}(x_0,y_0)&=-\frac{\partial v}{\partial x}(x_0,y_0)\end{align}$$
En tal caso, la derivada se puede escribir como: $$f'(z)=\frac{\partial u}{\partial x}+i\frac{\partial v}{\partial x}$$

Sin embargo, la condición de Cauchy-Riemann **no es suficiente** para verificar que una función  es diferenciable. De hecho, es una implicancia: 

$$\text{Diferenciable}\implies\text{Ecuación de Cauchy-Riemann}$$

**La forma precisa para verificar que la diferencial existe en un punto es al evaluar el límite por definición**. Esto se debe que las derivadas parciales podrían tener una disrregularidad en torno a la vecindad de $z_0$. 

La forma de convertir la implicancia en una equivalencia es que **las derivadas parciales existen y son continuas en el dominio**. Así, de tal forma: 

$$\text{Diferenciable}\iff\text{Ecuación de Cauchy-Riemann continua}$$

## Integrales Complejas 

Dado que la función compleja representa una curva dentro del plano complejo, la integral representa, justamente, una **integral de línea**. Así, se define como: 

$$\int_Cf(z)\;dz=\int^{b}_{a}f(z(t))\cdot z'(t)\;dt$$

Si establecemos nuestra forma típica de función donde $f(z)=u(x,y)+iv(x,y)$ es posible reescribir la integral como: 

$$\int_Cf(z)\;dz=\int_C(u\;dx-v\;dy)+i\int_C(u\;dy+v\;dx)$$

Aun así, podemos notar que al aplicar el **Teorema de Green** a ambas interales de línea se tiene que: 

$$\int_Cf(z)\;dz=\iint_R(-v_x-u_y)\;dxdy+i\iint(u_x-v_y)\;dxdy$$

**Por cumplir el teorema de Cauchy-Riemann** se llegaría al siguiente resultado: 

$$\int_cf(z)\;dz=0+i\cdot0=0$$

De tal forma, se puede concluir que **toda función homolorfa tiene una integral nula**. 


>[!example] Fórmula Integral de Cauchy 
>
>Ahora es posible **determinar el valor de una función a través de una integral**. En específico, para todo punto $z_0$ dentro de un conjunto abierto conexo se cumple que: 
>$$f(z_0)=\frac{1}{2\pi i}\int_C\frac{f(z)}{z-z_0}\;dz$$


>[!example] Fórmula Derivada de Cauchy 
>
>Al igual que el teorema anterior, es posible determinar **la derivada de una función en un punto** al plantear la siguiente igualdad: 
>
>$$\frac{f^{(n)}(z_0)}{n!}=\frac{1}{2\pi i}\int_C\frac{f(z)}{(z-z_0)^{n+1}}$$

## Series de potencias complejas

Si nos acordamos del polinomio de Taylor, es posible representar una función en forma de sumatorias infinitas. En específico, se cumplía para una función $C^n$ que: 

$$f(z)=\sum^{\infty}_{n=k}\frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$$

Si convertimos el término en función de las $n$ en una constante $a_n$ se plantea la **serie de potencias complejas**: 

$$\sum^{\infty}_{n=0}a_n(z-z_0)^n$$


Así, para saber si la función converge bajo cierto radio se plantean los dos criterios de convergencia: 

- **Límite del sucesor**: La serie converge si se cumple que existe el siguiente límite. En tal caso, el límite nos dice el **comportamiento de la convergencia**. 

$$\lim_{n\to\infty}\bigg\vert\frac{a_n}{a_{n+1}}\bigg\vert=R$$

- **Criterio de raiz n-ésima**: La serie se comporta en función de $R$. Se cumplen los mismos criterios anteriores. 

$$\lim_{n\to\infty}\sqrt[n]{a_n}=R$$

Así, para saber los comportamientos de la convergencia se hace el siguiente análisis: 

$$R=\begin{cases}>1&\text{Diverge}\\  \\
=1&\text{No se sabe}\\  \\
<1&\text{Converge}\end{cases}$$

Existen otros criterios también que se pueden ver bajo los [[Departamento de Ingeniería Matemáticas/Cálculo Diferencial e Integral/Series numéricas/Criterios de convergencia|criterios de convergencia]]. 

Así mismo, es importante saberse las **series importantes**: 

$$\begin{align}
e^z&=\sum^{\infty}_{n=0}\frac{z^n}{n!}\;\;\;\forall z\in\mathbb{C}\\  \\
\cos{z}&=\sum^{\infty}_{n=0}\frac{(-1)^nz^{2n}}{(2n)!}\;\;\;\forall z\in\mathbb{C}\\  \\
\sin{z}&=\sum^{\infty}_{n=0}(-1)^n\frac{z^{2n+1}}{(2n+1)!}\;\;\;\forall z\in\mathbb{C}\\  \\
\frac{1}{1-z}&=\sum^{\infty}_{k=0}z^k\;\;\;\vert z\vert <1\\ \\
\sum^{N}_{k=0}a^k&=\frac{1-a^{N+1}}{1-a}\;\;\;\text{Progresión geométrica}\\  \\
\sum^{m}_{k=n}a^k&=\frac{a^n-a^{m+1}}{1-a}\;\;\;\text{Progresión geométrica}
\end{align}$$

## Series de Taylor 

Puesto que se conoce las expansiones en series, se postula la aproximación en series de Taylor: 

$$f(z)=\sum^{\infty}_{k=0}c_k(z-p)^k\;\;\;\forall k\in D(p,r)$$

Donde la constante $c_k$ es equivalente a: 

$$c_k=\frac{1}{k!}f^{(k)}(p)$$

Notemos que es **exactamente la misma expresión que la expansión en series de Taylor en $\mathbb{R}$**. No obstante, con la **fórmula derivada de Cauchy** es posible expander aun más la definición de la constante: 

$$\begin{align}
c_k&=\frac{1}{k!}f^{(k)}(p)\\  \\
&=\frac{1}{2\pi i}\oint_{\partial D(p,r)}\frac{f(w)}{(w-p)^{k+1}}\;dw\tag{Fórmula de Cauchy}
\end{align}$$

Así, si quisieramos llegar a la expresión más explícita para una serie de Taylor, se tendría lo siguiente: 

$$f(z)=\sum^{\infty}_{k=0}\left(\frac{1}{2\pi i}\oint_{\partial D(p,r)}\frac{f(w)}{(w-p)^{k+1}}\;dw\right)(z-p)^k\;\;\;\forall k\in D(p,r)$$


## Desigualdad de Cauchy 

Se postula lo siguiente para un conjunto abierto $\Omega$ y una función homolorfa. Sea $M_r$ el supremo de la función, entonces: 

$$\forall k\geq 0\;\;\;\vert f^{(k)}(p)\vert\leq\frac{k!M_r}{r^k}$$

#### Demostración 

La demostración es directa del teorema de la derivada de Cauchy. En específico, se tiene que: 

$$\begin{align}
\frac{1}{k!}f^{(k)}(p)&=\frac{1}{2\pi i}\oint_{\partial D(p,r)}\frac{f(w)}{(w-p)^{k+1}}\;dw
\end{align}$$

De modo que, manipulando un poco la igualdad: 

$$\begin{align}
\vert f^{(k)}(p)\vert&\leq\frac{k!}{2\pi}\oint_{\partial D(p,r)}\frac{\vert f(w)\vert}{r^{k+1}}\;\vert dw\vert
\end{align}$$

Donde se impone el cambio de variable $w-p=r\implies r+p=w$. Ahora, intengrando dentro de la frontera: 

$$\begin{align}
\frac{k!}{2\pi}\oint_{\partial D(p,r)}\frac{\vert f(w)\vert}{r^{k+1}}\;\vert dw\vert&=\frac{k!}{2\pi}\int^{2\pi}_{0}\frac{\vert f(p+re{i\theta})\vert}{r^{k+1}}\vert rie^{i\theta}\vert\;d\theta\\  \\
&\leq\frac{k!}{2\pi}\frac{1}{r^k}\int^{2\pi}_{0}\vert f(p+re^{i\theta})\vert\;d\theta\\  \\
&\leq\frac{k!}{2\pi}\frac{1}{r^k}M_r2\pi\\  \\
&=\frac{k!M_r}{r^k}\end{align}$$


Y así, por lo tanto, se plantea el **teorema de Louville** que establece que si una función es acotada y es homolorfa, entonces $f$ es constante en $\mathbb{C}$. 

# Teorema de los residuos 

Se dice que $p\in\mathbb{C}$ es un **punto singular** de una función de variable compleja si $f$ no es homolorfa en $p$ y en todo entorno de $p$ existen puntos donde la función es homolorfa. 

Por el otro lado, $p\in\mathbb{C}$ es un **punto singular aislado** de $f(z)$ si $f$ no es homolorfa en $p$ y existe un radio $R>0$ tal que $f\in H(D(p,R)\backslash\lbrace p\rbrace)$

#### Ejemplo 

Un ejemplo clásico es la siguiente función: 

$$f(z)=\frac{\sin(z)}{z}$$ 
Claramente $f$ es homolorfa $\forall z\in\mathbb{C}\backslash\lbrace 0\rbrace$. Así, $p=0$ es un **punto singular aislado**. 










Además, se agrega la definición de **punto singular evitable**, donde al tener un punto singular aislado se tiene un límite: 

$$L_0(p)=\lim_{z\to p}f(z)$$

Al igual que en cálculo en $\mathbb{R}$, la definición de una función podría ser *"reparada"* en todo el espacio al añadir el valor del límite en la singularidad. 

#### Ejemplo 

Extendiendo el ejemplo anterior, se tiene que $p=0$ es un punto singular evitable de la siguiente función: 

$$f(z)=\frac{\sin(z)}{z}$$ 
Notemos que: 

$$\lim_{z\to 0}\frac{\sin z}{z}=1$$

De este modo, la función $\bar{f}$ puede ser *"reparada"* por lo siguiente para ser homolorfa en todo $\mathbb{C}$: 

$$\bar{f(z)}=\begin{cases}
\frac{\sin(z)}{z}&\text{si}\;z\neq 0\\  \\
1&\text{si}\;z=0\end{cases}$$



>[!example] Polo 
>
>Dadas todas las definiciones anteriores, se define polos si se tiene un punto $p$ que es un punto **singular aislado** de $f(z)$ y además existe un entero $m\geq 1$ tal que el siguiente límite existe y es **no nulo**: 
>
>$$L_m(p)=\lim_{z\to p}(z-p)^mf(z)$$
>
>El menor entero $m\geq 1$ se dirá que es el **orden del polo**. Se dirá que se tiene un *polo simple* cuando el orden es $1$. 

#### Ejemplo 

Nuevamente, con la misma función, veamos que el valor $p=0$ es el polo de la siguiente función: 

$$f(z)=\frac{\cos(z)}{z}$$ 
Dado que: 

$$\begin{align}
L_m(p=0)&=\lim_{z\to 0}(z-0)\frac{\cos(z)}{z}\\  \\
&=\lim_{z\to 0}\cos(z)\\  \\
&=\cos(0)\\  \\
&=1
\end{align}$$



Notar que si $p$ es un polo de una función, entonces **no puede ser un punto singular evitable**. 

## La idea detrás de los residuos 

Por el otro lado, podríamos tener el caso donde se tiene la siguiente función: 

$$g(z)=(z-p)^mf(z)$$

En tal caso, si $p$ es un polo de $f(z)$, entonces el valor $z=p$ llegaría a ser un **punto singular evitable**. Vale decir, $g(z)$ podría llegar a ser reparada de la siguiente forma: 

$$\hat{g(z)}=\begin{cases} 
(z-p)^mf(z)&\text{si}\;z\in\Omega\backslash\lbrace p\rbrace\\  \\
\lim_{z\to p}(z-p)^mf(z)&\text{si}\;z=p\end{cases}$$ 
Ahora, veamos lo que ocurre si hacemos una **expansión en Series de Taylor** de $\hat{g(z)}$. 


$$\begin{align}
g(z)&=\sum^{\infty}_{k=0}c_k(z-p)^k\;\;\;\forall k\in D(p,r)\tag{Definición Taylor}\\  \\
(z-p)^mf(z)&=\sum^{\infty}_{k=0}c_k(z-p)^k\tag{1}
\end{align}$$

Acordándonos de la definición del coeficiente $c_k$, es posible desglosarlo al máximo: 

$$\begin{align}
c_k&=\frac{g^{(k)}(p)}{k!}\\  \\
&=\frac{1}{2\pi i}\oint_{\partial D(p,r)}\frac{g(w)}{(w-p)^{k+1}}\;dw\tag{Teorema derivada}\\  \\

\end{align}$$

Ahora, desglozamos $g(w)=(w-p)^mf(z)$: 

$$\begin{align}
c_k&=\frac{1}{2\pi i}\oint_{\partial D(p,r)}\frac{f(w)}{(w-p)^{k-m+1}}\;dw
\end{align}$$

Así, volviendo nuevamente al desarrollo de Taylor, se puede retomar $(1)$ y escribir $f(z)$ como una serie de potencias: 

$$f(z)=\frac{c_0}{(z-p)^m}+\frac{c_1}{(z-p)^{m-1}}+\dots+\frac{c_{m-1}}{(z-p)}+R(z)\tag{2}$$

Cuando la potencia $m$ se *"agota"*, se tiene $R(z)$ que se llamaría el resto. Éste estaría definido por

$$R(z)=\sum^{\infty}_{k=m}c_k(z-p)^{k-m}$$ 
El resto llegaría a ser homolorfa al tratarse una expansión en series de potencias dentro de un disco $D(p,r)$. 

Ahora, es posible juntar todo el desarrollo de $(2)$ y juntarlo como una única sumatoria: 

$$f(z)=\sum^{\infty}_{k=-m}c_k(z-p)^k$$

Donde para todo $k\geq -m$ se cumple que: 

$$\begin{align}
c_k&=c_{k+m}\\  \\
&=\frac{1}{2\pi i}\oint_{\partial D(p,r)}\frac{f(w)}{(w-p)^{k+1}}\;dw
\end{align}$$

Este desarrollo en particular es lo que introduce las *series de Laurent*. 

>[!example] Residuos 
>Lo que llegaría a ser los coeficientes $c_{m-1}$, vale decir, los $k$ negativos en la sumatoria, se le llamarán **residuos de $f$ en $p$:** 
>
>$$Res(f,p)=\frac{g^{(m-1)}(p)}{(m-1)!}=\frac{1}{2\pi i}\oint_{\partial D(p,r)}f(w)\;dw$$
>
> Otra forma útil de expresar el residuo es la siguiente: 
>
>$$Res(f,p)=\lim_{z\to p}\frac{1}{(m-1)!}\frac{d^{m-1}}{dz^{m-1}}[(z-p)^mf(z)]$$ 


## El teorema de los residuos 

Supongamos que se tiene una función homolorfa en un espacio $\Omega\backslash\lbrace p\rbrace$ donde $p$ es un **punto singular evitable**, de modo que existe la extensión $\bar{f}$. Si $\Omega$ es simplemente conexo y existe un camino cerrado simple, por *Cauchy-Goursat* se tiene que: 

$$\oint_\tau f(z)\;dz=0$$

Ahora, supongamos que $p$ es un polo de $f$ de orden $m$. De esta forma, **no sería posible tener una extensión de $f$** (recordar que los polos, por definición, no pueden ser puntos evitables). De hecho, si ocupamos la Expansión de Taylor para la función, se llega que: 

$$\oint f(z)=2\pi iRes(f,p)$$

>[!example] Meromorfa 
>
>Una función $f$ se dirá que es meromorfa en un conjunto $\Omega$ si existe un conjunto $P\subseteq\Omega$ finito tal que: 
>
>- $f\in H(\Omega\backslash P)$
>  
>- $f$ tiene un polo en cada punto $p\in P$ 
>  
>- $P$ no posee puntos de acumulación 

>[!example] Teorema de los residuos de Cauchy 
>
>Sea $f$ una función meromorfa en un conjunto abierto y sea $P$ el conjunto de todos sus polos. Sea $\tau$ un camino simple y cerrado, recorrido en sentido antihorario, que encierra una región $D\subseteq\Omega$ tal que $T\cap P=\emptyset$. Entonces $\tau$ encierra un número finitos de polos de $f$, y más aun: 
>
>$$\oint_\tau f(z)\;dz=2\pi i\sum^{n}_{j=1}Res(f,p_j)$$


Por último, para simplificar el cálculo de los residuos es posible postular L'hopital en $\mathbb{C}$. Sean $f,g$ homolorfas en $\Omega$ tales que: 

$$g(p)=\dots=g^{(n-1)}(p)=0\neq g^{(n)}(p)$$

Entonces: 

$$\lim_{z\to p}\frac{f(z)}{g(z)}=\begin{cases} 
\text{no existe}&\text{si}\;f^{(k)}(p)\neq 0\;\text{para algún}\;k\in\lbrace 0,1,\dots,n-1\rbrace\\  \\
\frac{f^{(n)}(p)}{g^{(n)}(p)}&\text{si}\;f^{(k)}(p)=0\;\text{para todo}\;k\in\lbrace 0,1,\dots,n-1\rbrace\end{cases}$$

