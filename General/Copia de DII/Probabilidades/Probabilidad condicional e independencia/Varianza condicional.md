
Sean $X$ e $Y$ [[Variable aleatoria continua|variables aleatorias]], se puede pensar que: 
- $Var(X\vert Y=y)$ es análogo a pensar $E[X\vert Y=y]$ 
- $Var(X\vert Y)$ es análogo a $E[X\vert Y]$ 

Notemos que

$$\begin{align}
Var(X\vert Y=y)&=E[(X-E[X\vert Y=2])^2\vert Y=y]\\\\
Z(x)&=(X-E[X\vert Y=2])^2\\\\
&= E[Z\vert Y=y]\end{align}$$ 
Entonces, su definicion formal es: 

$$Var(X\vert Y=y)=E[(X-E[X\vert Y=2])^2\vert Y=y]$$ 
Notemos que para el caso discreto se puede desarrollar de la siguiente forma: 

$$\begin{align}Var(X\vert Y=y)&=\sum_{x\in R_x}(x-E[X\vert Y=y])^2P_{X\vert Y}(x\vert y)\\\\
&=\sum_{x\in R_x}x^2P_{X\vert Y}(x\vert y)-2E[X\vert Y=y]\sum_{x\in R_x}xP_{X\vert Y}(x\vert y) + E[X\vert Y=y]^2\sum_{x\in R_x}
P_{X\vert Y}(x\vert y)\\\\
&=E[X^2\vert Y=y]-2E[X\vert Y=y]^2 + E[X\vert Y=y]^2\\\\
&=\textcolor{red}{E[X^2\vert Y=y]-E[X\vert Y=y]^2}\end{align}$$ 
Por lo tanto, lo rojo sería la forma equivalente de la varianza condicional simplificado a lo máximo. 