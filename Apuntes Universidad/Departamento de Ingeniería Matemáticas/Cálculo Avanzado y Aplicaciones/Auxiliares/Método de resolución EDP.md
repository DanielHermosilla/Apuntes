
Sea la siguiente ecuación: 

$$u_t-u_{xx}=2x\;\;\;x\in(0,1)$$
Con: 

$$\begin{align}
u(t,0)&=u'(t,1)=0\\  \\
u(0,x)&=2
\end{align}$$

No se puede usar separación de variable porque no es homogénea. 

Como no es homogéneo, necesito encontrar una solución particular. Buscamos $\phi=\phi(x)$ tal que sea solución: 

$$\begin{align}
\cancelto{0}{\phi_t}-\phi_{xx}&=2x\tag{1}\\  \\
\phi(0)=\phi_x(1)&=0
\end{align}$$

Como $\phi$ no depende del tiempo, es posible "*matar*" el término que dependen del tiempo. Por lo tanto, viendo la condición $(1)$: 

$$\begin{align}
\phi_{xx}&=-2x\\  \\
\phi_x&=-x^2 + a\\  \\
\phi&=\frac{-x^3}{3}+ax+b
\end{align}$$

Como se tienen dos condiciones de borde, las ocupamos para despejar las constantes: 

$$\begin{align}
\phi(0)=0&\implies b=0\\  \\
\phi'(1)=0&\implies a=1
\end{align}$$

Por lo tanto, la función $\phi(x)$, que llegaría a ser la función particular, es: 

$$\phi(x)=-\frac{x^3}{3}+x$$

Como sabemos que la solución es de la forma: $u=u_\text{homogéneo}+u_\text{particular}$, faltaría encontrar la solución homogénea. Es decir: 

$$\begin{align}
u&=u_h+u_p\\  \\
u_h&=u-\phi
\end{align}$$

Entonces, *¿qué ecuación resuelve $u_h$?*: 

$$\begin{align}
\frac{\partial u_h}{\partial t}-\frac{\partial^2u_h}{\partial x^2}&=\left(\frac{\partial u}{\partial t}-\frac{\partial^2u}{\partial x^2}\right)-\left(\frac{\partial\phi}{\partial t}-\frac{\partial^2\phi}{\partial x^2}\right)\\  \\
&=2x-(2x)=0
\end{align}$$

Por lo tanto, viendo las condiciones iniciales: 

$$\begin{align}
u_h(t,0)&=u(t,0)-\phi(0)\\  \\
&=0-\phi(0)
\end{align}$$

Por el otro lado; 

$$\begin{align}
\frac{\partial u_h}{\partial x}&=u_x(t,1)-\phi'(1)=0
\end{align}$$

Por último: 

$$\begin{align}
u_h(0,x)&=u(0,x)-\phi(x)\\  \\
&=2+\frac{x^2}{3}-x
\end{align}$$

Luego, $u_h$ es solución: 

$$\begin{align}
\frac{\partial u_h}{\partial t}-\frac{\partial^2 u_h}{\partial x^2}&=0\\  \\
u_h(t,0)=\frac{\partial u_h}{\partial x}(t,1)&=0\\  \\
u_h(0,x)&=\frac{x^3}{3}-x+2
\end{align}$$

Supongamos que, por separación de variables: 

$$u_h(x)=T(t)X(X)$$

Entonces: 

$$\begin{align}
T'X-TX''&=0\\  \\
T'X&=TX''\\  \\
\frac{T'}{T}&=\frac{X''}{X}
\end{align}$$

El lado izquierdo depende de $t$ y el derecho sólo de $x$. La única forma que sean iguales es que sean equivalentes a una constante: 

$$\frac{T'}{T}=\frac{X''}{X}=\lambda$$

Es decir: 

$$\begin{align}
T'-\lambda T&=0\\  \\
X''-\lambda X&=0
\end{align}$$

Viendo las nuevas condiciones de borde: 

$$\begin{align}
u_h(t,0)=0&\implies T(t)X(0)=0
\end{align}$$

Luego, $x(0)=0$. Ahora, con la otra condición: 

$$\frac{\partial u_h}{\partial x}(t,1)\implies T(t)X'(1)=0$$

Luego, $X'(1)=0$

Así entonces, $X$ es solución: 

$$\begin{align}
X''-\lambda X&=0\;\;\;x\in (0,1)\\  \\
X(0)=X'(1)&=0
\end{align}$$

Viendo los casos posibles de $\lambda$, dado que este cambia el tipo de solución: 

- Si $\lambda = 0$, entonces: 

$$X''(x)=0\implies X(x)=ax+b$$

Viendo las condiciones de borde: 

$$X(0)=0\implies b=0$$
$$X'(1)=0\implies a=0$$

Entonces, para $\lambda=0$ la solución es nula. Pero no se busca la solución nula. 

- Si $\lambda>0$, entonces se puede escribir como un número al cuadrado. Sea $\lambda=k^2$. Entonces: 

$$\begin{align}
X''-k^2X&=0\\  \\
X(x)&=ae^{kx}+be^{-kx}
\end{align}$$

Viendo las condiciones de borde: 

$$\begin{align}
X(0)=0\implies a+b=0\\  \\
X'(1)=0\implies ake^k-bke^{-k}=0\tag{2}
\end{align}$$

Si nos fijamos en $(2)$, como $k$ está definido como positivo, no puede ser $0$. Además, $b=-a$. Entonces: 

$$\begin{align}
k(ae^k+ae^{-k})&=0\\  \\
ak(e^k+e^{-k})&=0
\end{align}$$

Luego, $a=0\implies a=b=0$ y nos daría la solución nula. 

- Si $\lambda <0$, entonces se puede escribir como $\lambda =-k^2$. La ecuación diferencial será de la forma: 

$$X''+k^2X=0$$

Con solución trigonométrica: 

$$X(x)=a\cos(kx)+b\sin(kx)$$

Evaluando en las condiciones de borde: 

$$\begin{align}
X(0)=a&=0\\  \\
X'(1)&=bk\cos(k)=0
\end{align}$$

Luego, $\cos(k)=0$, por lo tanto $k=(2n-1)\cdot\pi/2$ con $n\geq 1$ .

Entonces, $\lambda_n$ tiene varias soluciones de la forma: 

$$\lambda_n=-\left((\frac{2n-1}{2})\pi\right)^2$$

Entonces, la solución llegaría a ser: 

$$X_n(x)=b_n\sin\left(\frac{(2n-1)\pi}{2}\right)$$

Ahora, volviendo a la ecuación de antes que dependía de $T$, se tiene que: 

$$T'-\lambda T=0$$

Entonces, trivialmente se tiene 

$$T(t)=ae^{\lambda t}$$

Asi, $\forall n\in\mathbb{N}, n\geq 1$ se tiene que: 

$$\begin{align}
\lambda_n&=-\left(\frac{(2n-1)}{2}\pi\right)^2\\  \\
X_n(x)&=b_n\sin\left(\frac{(2n-1)\pi}{2}\right)\\  \\
T_n(t)&=a_ne^{-\left(\frac{(2n-1)}{2}\pi\right)^2t}
\end{align}$$

Finalmente, 

$$\begin{align}
u_n(t,x)&=T_n(t)X_n(x)\\\\ 
&=\cancelto{c_n}{a_nb_n}e^{-\left(\frac{(2n-1)}{2}\pi\right)^2t}\sin\left(\frac{(2n-1)\pi}{2}x\right)
\end{align}$$ 

Ahora, viendo las condiciones iniciales: 

$$\begin{align}
u_h(0,x)&=2+\frac{x^3}{3}-x
\end{align}$$
Luego, 

$$u_h(0,x)=2+\frac{x^3}{3}-x=\sum^{\infty}_{n=1}c_n\sin(\frac{2n-1}{2}\pi x)$$

Esta función solo tiene senos, entonces la función es impar. Como la función está definida de $x>0$, la definimos con extensión impar
