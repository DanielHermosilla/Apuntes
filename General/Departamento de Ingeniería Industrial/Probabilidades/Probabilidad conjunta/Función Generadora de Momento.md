
La función generadora de momento de una variable aleatoria $S$ se define como la función: 

$$M_x(s)=E[e^{sX}]$$ 

Esta siempre existe si existe un $a>0$ tal que $M_x(s)$ es finita para todo $s\in(-a,a)$.

Notemos que si expandimos la exponencial por Taylor, se podría escribir la función generadora de momento como: 

$$\begin{align} 
\mathbb{E}(e^{sX})&=\mathbb{E}[\sum_{i=0}^{\infty}\frac{(sX)^i}{i!}]\frac{1}{3}\\\\&=\sum_{i=0}^{\infty}\mathbb{E}[\frac{(sX)^i}{i!}]\\\\ &=\sum_{i=0}^{\infty}\frac{s^i}{i!}\mathbb{E}[X^i]
\end{align} $$

Ahora, notemos que si [[Departamento de Ingeniería Industrial/Probabilidades/Repasos/Funciones/Derivada|derivamos]] aquella expansión y evaluamos en $s=0$: 

$$\begin{align}\frac{dM_x}{ds}(s)\bigg\vert_{s=0}&=\sum_{i=1}^{\infty}\frac{s^{i-1}}{(i-1)!}\mathbb{E}[X^i]\bigg\vert_{s=0}\\\\ &=\mathbb{E}[X^1] \end{align}$$ 
Por lo tanto, si se llega a algo general, se puede decir que: 

$$\begin{align}
\frac{d^nM_X(s)}{ds^n}\bigg\vert_{s=0}&=\mathbb{E}[X^n]\end{align}$$ 
## Teorema 

Sean $X$ e $Y$ dos [[Variable aleatoria continua|variables aleatorias]] tal que existe un real $c>0$ tal que las función generadora de momentos de ambas variables aleatorias coinciden para todo $s\in[-c,c]$, entonces: 

$$F_x(t)=F_y(t)$$ 
Para todo $t\in\mathbb{R}$. 


### Ejemplo

Sea una [[Variable aleatoria continua|variable aleatoria]] $X$ que tiene la siguiente distribución:

$$X=\begin{cases}p_x(1) &= \frac{1}{3}\\\\
p_x(2) &= \frac{2}{3}\end{cases}$$ 
Entonces su función generadora de momento es: 

$$\begin{align}
M_x(s) &=\mathbb{E}[e^{sX}]\\\\ 
&=\frac{1}{3}e^s + \frac{2}{3}e^{2s}
\end{align}$$ 
### Ejemplo 

Se tiene una [[Distribución Uniforme]] $[0,1]$, entonces: 

$$\begin{align}
M_y(s)&=\mathbb{E}(e^{sY})\frac{1}{3}\\\\ 
&=\int_{0}^{1}e^{sy}dy\\\\
&=\frac{e^{sy}}{s}\bigg\vert_{y=0}^{1}\end{align}$$ 
## Caso de distribución exponencial 

Sea $X\sim\text{Exp}(\lambda)$. Por lo tanto: 

$$\begin{align}M_X(s)&=\mathbb{E}[e^{sX}]\\\\ 
&=\int_{-\infty}^{\infty}e^{sX}\lambda e^{-x}\mathbb{1}_{\lbrace x>0\rbrace}\\\\
&=\frac{-\lambda}{\lambda-s}e^{-(\lambda-s)x}\bigg\vert_{0}^{+\infty}\\\\
M_X(s)&\begin{cases}\frac{\lambda}{\lambda-s}&\text{si}\; s<\lambda\\\\
+\infty&\text{si}\;s\geq\lambda\end{cases}\end{align}$$ 

## Caso Bernoulli 

Sea $X\sim\text{Bernoulli}(p)$, entonces la función genereradora de momento es: 

$$\begin{align} 
M_{X_i}(s)&=\mathbb{E}[e^{sX_i}]
&=1-p + pe^s\end{align}$$ 
## Caso Binomial 

Dado que sabemos que la [[Distribución binomial]] es la suma de [[Distribución de Bernoulli]], entonces: 

$$M_y(s)=(1-p+pe^s)^n$$ 
Ahora, si tenemos la suma de dos funciones de momento: 

$$\begin{align} 
M_{X+Y}(s)&=M_y(s)\cdot M_y(s)\frac{1}{3}\\\\ 
&=(1-p+pe^s)^{n+m}\end{align}$$ 
Todo esto implica que $X+Y\sim\text{Bin}(n+m,p)$. 


## Suma de Funciones de Momentos 

Sea $X_1,\dots,X_n$ [[Variable aleatoria continua|variables aleatorias]] [[Departamento de Ingeniería Industrial/Probabilidades/Probabilidad conjunta/Probabilidad conjunta continua/Independencia|independientes]], si $Y=X_1 + X_2 +\dots + X_n$ entonces la FGM de $Y$ sería: 

$$\begin{align} 
M_Y(s)&=M_{X_1+\dots+X_n}(s)\\\\ 
&=\mathbb{E}(e^{s(x_1+\dots+x_n})\\\\ 
&=M_{X_1}+M_{X_2}+\dots+M_{X_N}\end{align}$$

