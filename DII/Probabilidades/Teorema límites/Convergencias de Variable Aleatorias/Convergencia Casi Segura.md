
La secuencia de [[Variable aleatoria continua|variable aleatorias]] $X_1, X_2, X_3, \dots$ definida sobre el mismo [[Espacio muestral|espacio muestral]] $\Omega$ y función de probabilidad $P$, **converge casi seguramente** a la [[Variable aleatoria continua|variable aleatoria]] $X$ (definida sobre el mismo [[Espacio muestral|espacio muestral]] $\Omega$ y función de probabilidad $P$), es decir, $X_n\to^{C.S}X$ si: 

$$P\left(\lbrace\omega\in\Omega:\lim_{n\to+\infty}X_n(\omega)=X(\omega)\rbrace\right)=1$$ 
A veces se denota como: 

$$P(\lim_{n\to+\infty}X_n=X)=1$$ 
Ahora, si se tieme una convergencia casi segura, entonces se cumple lo siguiente: 

Si $X_n\to^{C.S}X$ entonces $X_n\to^{p}X$, es decir, [[Convergencia en Probabilidad|converge en probabilidad]] 

### Ejemplo 

Sea un lanzamiento de una moneda balanceada $\Omega=\lbrace C,S\rbrace$ y definimos la secuencia de [[Variable aleatoria continua|variable aleatorias]]: 

$$X_n(\omega)=\begin{cases}\frac{n}{n+1}&\text{si}\;\omega=C\\\\
(-1)^n&\text{si}\;\omega = S\end{cases}$$ 
a) Determinar para los diferentes elementos de $\Omega$ si la secuencia resultante converge o no. 

Notemos que en caso de cara: 

$$X_n: \frac{n}{n+1}\to1$$ 
Y en el caso de sello: 

$$X_n: (-1)^n\to-1,1$$

No converge. 

b) Encontrar: 

$$P\left(\lbrace\omega\in\Omega:\lim_{n\to+\infty}X_n(\omega)=X(\omega)\rbrace\right)=1$$

Se cumple para $\omega = C$.

c) ¿Existe una variable aleatoria $X$ tal que $X_n\to^{C.S}X$? 

No, ya que existe una convergencia que va a -1. 

### Ejemplo 

Sea $U\sim\text{Uniforme}[0,1]$. Definimos la secuencia de variable aleatorias como: 

$$X_n(U)=\begin{cases}1&\text{si}\;0\leq U<\frac{1}{2}+\frac{1}{n}\\\\0&\text{si no}\end{cases}$$ 
Además, definimos: 

$$X(U)=\begin{cases}1&\text{si}\;0\leq U<\frac{1}{2}\\\\ 
0&\text{si no}\end{cases}$$ 
Mostrar que $X_n\to^{C.S} X$ .

Sabemos que por definición: 

$$P\left(\lbrace\omega\in\Omega:\lim_{n\to+\infty}X_n(\omega)=X(\omega)\rbrace\right)=1$$

Se busca que $P(A)=1$ cuando $n\to\infty$. Poniendonos en casos: 

- Para $\omega <\frac{1}{2}$, $X_n(\omega)=X(\omega)=1$. Por lo tanto, $\omega\in[0,\frac{1}{2})\subset A$. 
- Para $\omega>\frac{1}{2}$, $X(\omega)=0$, por lo tanto, $\exists\; m\in\mathbb{N}:\;\forall n>m\; X_n(\omega)=0$. Luego, $(\frac{1}{2},1]\subset A$ 
- Cuando $\omega = \frac{1}{2}$, $X(\omega)=0$, $X_n(\omega)=\frac{1}{2}$ . En este caso, $\frac{1}{2}\notin A$ 

Por lo tanto, $A$ esta definido en $[0,1]\backslash\lbrace\frac{1}{2}\rbrace$, vale decir, $\Omega\backslash\lbrace\frac{1}{2}\rbrace$ 