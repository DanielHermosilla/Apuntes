
Son de la forma: 

$$\begin{align}
x'(t)&=F(x,y)\\\\
y'(t)&=G(x,y)
\end{align}$$ 
Donde la solución se presenta a través de un **plano de fase**, vale decir, una trayectoria. 

![[planodefases.jpg|center|500]]


Donde se tiene una función de $y$ en función de $x$. 

#### Ejemplo 

La ecuación del pendulo es un sistema dinámico no lineal: 

$$\text{SNL}=\begin{cases}x'&=y\\\\y'&=-\frac{g}{L}\sin(x)-\frac{b}{m}y\end{cases}$$ 
Notemos que $\sin(x)$ es no lineal. 

Muchas veces para poder resolver este tipo de ejercicios, se hacen *polinomios de Taylor*. Por ejemplo, en ángulos pequeños, se dice que $\sin(x)\approx x$. 

Para estos casos, se definen las siguientes funciones:

$$\text{SNL}=\begin{cases}x'&=F(x,y)&t\in I\\\\y'&=G(x,y)&F,G\in\mathbb{C}^1\;\text{en ambas variables}\end{cases}$$

De aquí se introduce el concepto de sistema lineal autónomo o no autónomo. 


## Autonomía 

Se dice que un sistema no lineal es autónomo cuando se tiene que $F=F(x,y), G=G(x,y)$ y no ocurre que $F=F(x,y,t)$ o $G=G(x,y,t)$ que sería el caso no autónomo. Bajo el ejemplo anterior, un sistema **no autonomo** sería el siguiente: 


$$\text{SNL}=\begin{cases}x'&=y\\\\y'&=-\frac{g}{L}\sin(x)-\frac{b}{m}y + f(t)\end{cases}$$

Por lo tanto, a partir de sistemas autónomos se puede hacer un plano de fases a partir de las condiciones iniciales y se llega a un punto de equilibrio donde $(x'=0,y'=0)$. 

Notemos que en el sistema no lineal, se puede definir lo siguiente: 

$$\begin{align}\mathbb{X}&=\begin{pmatrix}x\\y\end{pmatrix}\end{align}$$ 
Se podría reescribir esto de la siguiente forma: 

$$\mathbb{X}=\begin{cases}\mathbb{X}'=\mathbb{F}(X)&\mathbb{F}=\begin{pmatrix}F\\G\end{pmatrix}\\\\\mathbb{X}(0)=\mathbb{X}_0\end{cases}$$ 
Esto, por [[Teoría de Existencia y Unicidad|TEU]] nos dice que existe la solución, es única y es local. 

## Linealización 

Un método de linealizar, como fue mencionado anteriormente, es hacer una aproximación por el polinomio de Taylor en torno a un punto $x^*$, es decir: 

$$F(x,y)=F(x^*,y^*)+\frac{\partial F}{\partial x}(x^*,y^*)(x-x^*)+\frac{\partial F}{\partial y}(x^*,y^*)(y-y^*)+e_F(r)$$
$$G(x,y)=G(x^*,y^*)+\frac{\partial G}{\partial x}(x^*,y^*)(x-x^*)+\frac{\partial G}{\partial y}(x^*,y^*)(y-y^*)+e_G(r)$$
Donde $e_F(r)$ es el error de la función, asociado a la distancia entre $(x,y)$ y $(x^*, y^*)$.  

Es ahí cuando aparece la [[matriz Jacobiana]] de la EDO: 

$$\begin{pmatrix}\frac{\partial F}{\partial x}&\frac{\partial F}{\partial y}\\\frac{\partial G}{\partial y}&\frac{\partial G}{\partial y}\end{pmatrix}\bigg\vert_{(x,y)=(x^*,y^*)}\;\text{Evaluada en}\;(x^*,y^*)$$ 
Este análisis se va a hacer en los [[Puntos críticos|puntos críticos]], es decir, cuando se anulan ambas funciones, se llegaría a lo siguiente: 

$$F(x,y)=\cancel{F(x^*,y^*)}+\frac{\partial F}{\partial x}(x^*,y^*)(x-x^*)+\frac{\partial F}{\partial y}(x^*,y^*)(y-y^*)+\cancel{e_F(r)}$$
$$G(x,y)=\cancel{G(x^*,y^*)}+\frac{\partial G}{\partial x}(x^*,y^*)(x-x^*)+\frac{\partial G}{\partial y}(x^*,y^*)(y-y^*)+\cancel{e_G(r)}$$

Por lo tanto, se define la **linealización en torno al punto crítico** como: 

$$\begin{align}
\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}'&=J(x^*, y^*)\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}&\bar{x}=x-x^*\land\bar{y}=y-y^*
\end{align}$$

Por lo tanto, tiene como matriz el Jacobiano y serán interesantes sus [[vector propio|vectores propios]] y [[valores y vectores propios|valores propios]]. 

### Ejemplo 

En el caso del pendulo no lineal, los puntos críticos se definiran como

$$\mathbb{C}^*=\lbrace(x,y)\;\vert\;x=k\pi,\;k\in\mathbb{Z},\;y=0\rbrace$$ 
Es decir, el péndulo en reposo, sus posiciones verticales. Entonces analizando la matriz Jacobiana en esos puntos: 

$$J(x,y)=\begin{pmatrix}0&1\\\frac{-g}{L}\cos(x)&\frac{-b}{m}\end{pmatrix}$$ 
Notemos que en la parte no lineal quedan valores no constantes. Es decir, el Jacobiano, dependiendo del punto, será diferente. Si se evalúa en los puntos críticos, es decir, $\cos(k\pi)$, se va a tener los valores $(-1)^k$. Es decir, van a haber dos tipos de matrices Jacobianas dependiendo de la paridad de $k$. Por lo tanto, se tendrán las siguientes matrices: 

$$\begin{align}
J(x_{\text{par}},y)&=\begin{pmatrix}0&1\\\frac{-g}{L}&\frac{-b}{m}\end{pmatrix}\\\\J(x_{\text{impar}},y)&=\begin{pmatrix}0&1\\\frac{-g}{L}&\frac{b}{m}\end{pmatrix}
\end{align}$$ 
Analizando el [[polinomio característico]] para los jacobianos, se llega a lo siguiente: 

$$\begin{align}
J_{\text{par}}&=\lambda(\lambda+\frac{b}{m})+\frac{g}{L}=0\\\\J_{\text{impar}}&=\lambda(\lambda+\frac{b}{m})-\frac{g}{L}=0
\end{align}$$ 
Al estar en los [[Puntos críticos|puntos críticos]] de la función, la función no varía en el tiempo y es constante. Es decir, $(x(t),y(t))=(x^*,y^*)\;\;\;\;\forall t$ .  

Desarrollando ambos polinomios, se tiene: 

$$\begin{align}
\lambda^2 + \frac{b}{m}\lambda + \frac{g}{L}=0\;\;\;&\lambda=\frac{-b}{2m}\pm\sqrt{(\frac{b}{2m})^2 - \frac{g}{L}}&\text{Par}\\\\
\lambda^2 + \frac{b}{m}\lambda - \frac{g}{L}=0&\;\;\;\lambda=\frac{-b}{2m}\pm\sqrt{(\frac{b}{2m})^2 + \frac{g}{L}}&\text{Impar}
\end{align}$$ 
Entonces, a partir de este análisis, podemos ver que cuando $\lambda>0$ se tiene inestabilidad y al revez para el caso contrario. La condición de subamortiguamiento sería la siguiente: 

$$\left(\frac{b}{2m}\right)^2<\frac{g}{L}$$ 
Si es que llegase a haber una solución imaginaria, entonces se tendría algo de la forma $\lambda = \sigma + i\omega$, es decir, algo de la forma sinusoidal. No obstante, la parte real $\sigma$ estaría *"amortiguando"* el sistema. 

Esto, graficamente, se verá como espirales cuando hay complejos conjugados y "*guatas*" en los puntos sillas. Por último, cuando $\lambda_1,\lambda_2<0$ se tiene un nodo. 

Los [[vector propio|vectores propios]] también dan información, pues da la información de la dirección del sistema. 

Ahora, con un [[matriz cambio de base|cambio de base]] se puede hacer lo siguiente: 

$$\begin{align}
\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}'&=J\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}\\\\P^{-1}\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}'&= DP^{-1}\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}\\\\
\begin{pmatrix}\check{x}\\\check{y}\end{pmatrix}&=\begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}\begin{pmatrix}\check{x}\\\check{y}\end{pmatrix}\\\\\implies&\begin{cases}\check{x}(t)=c_1e^{\lambda_1 t}\\\\\check{y}(t)=c_2e^{\lambda_2 t}\end{cases}
\end{align}$$ 

## Nulclinas

Son aquellos puntos del plano de fase, donde solo una función es cero, es decir: 

$$\begin{align}
N_x &=\lbrace (x,y)\;\vert\; F(x,y)=0\rbrace\\\\
N_y &=\lbrace (x,y)\;\vert\; G(x,y)=0\rbrace
\end{align}$$ 

## Sistema Dinámico Linealizado 

Cuando se tiene el sistema lineal linealizado, se obtiene la [[matriz Jacobiana]], si volvemos al ejemplo anterior: 

$$J=\begin{pmatrix}
0&1\\-\frac{g}{L}&-\frac{b}{m}
\end{pmatrix}$$ 
Entonces, el plano de fase dependerá de los valores propios del Jacobiano. Si los valores propios de la parte real es negativa, entonces es estable. Por el otro lado, los valores propios de los completos conjugados dan los puntos de espiral. 

