
## Sistema lineales de EDO's 

Ocurre cuando se tiene más de una ecuación diferencial a resolver. Se pueden representar de forma matriciales de la siguiente forma: 

$$\begin{align}
\dot{x_1} &= x_1 + x_2 \\ 
\dot{x_2} &= 4x_1 + x_2
\end{align}$$ 
La solución se saca obteniendo los vectores propios y valores propios, es decir: 

$$x(t)=Ve^{\lambda t}$$ 
Donde $V$ corresponde al vector asociado al valor propio $\lambda$. La **solución general** corresponde a la suma de las soluciones, es decir: 

$$x(t) = AVe^{\lambda t} + BVe^{\lambda t}$$

Donde $x_1$ corresponde a la primera fila y $x_2$ a la segunda, es decir: 

$$\begin{align}
\text{Sea}\; x(t) &= A\begin{pmatrix}\textcolor{red}{a}\\\textcolor{blue}{b}\end{pmatrix}e^{\lambda_1 t} + B\begin{pmatrix}\textcolor{red}{c}\\\textcolor{blue}{d}\end{pmatrix}e^{\lambda_2 t}\\\\
x_1 &= A\textcolor{red}{a}e^{\lambda_1 t} + B\textcolor{red}{c}e^{\lambda_2 t}\\\\
x_2 &= A\textcolor{blue}{b}e^{\lambda_1 t} + B\textcolor{blue}{d}e^{\lambda_2 t}\end{align}$$ 




# Transformada de Laplace 

Se define como transformada de Laplace a la siguiente función: 

$$\mathbb{L}[f](s)=\int^{+\infty}_{0}e^{st}f(t)dt$$ 
Si la transformada existe, entonces la mínima asíntota se llamará **cota**. 

### Definiciones: 

1. **Orden exponencial**: Una función es de orden exponencial si existe $\alpha\in\mathbb{R}$ y $M>0$ tal que: 

$$\vert f(t)\vert\leq Me^{\alpha t}\;\;\forall t\geq 0$$ 
El menor $\alpha$ que cumpla la condición es su *orden exponencial*

2. **Espacio $\mathbb{C}_\alpha$**: conjunto de funciones que son continuas por pedazos y de orden exponencial $\alpha$ Es un sub espacio vectorial de todas funciones de $[0,+\infty)$ en $\mathbb{R}$ 


### Propiedades 

1. **Linealidad**: La transformada es un operador lineal. 

2. Si $f\in\mathbb{C}_\alpha$ entonces para todo $s>\alpha$ existe $\mathbb{L}[f](s)$ y converge absolutamente. Además, se cumple lo siguiente: 

$$\begin{align}
\bigg\vert\mathbb{L}[f](s)\bigg\vert &\leq\frac{M}{s-\alpha}\\\\ 
\lim_{s\rightarrow\infty}\mathbb{L}[f(t)](s)&=0
\end{align}$$ 

3. **Transformada de una derivada**: Si se tiene una función $f\in\mathbb{C}_\alpha$ derivable, la transformada de Laplace de su derivada para $s>\alpha$ es la siguiente: 

$$\mathbb{L}[f'](s)=s\mathbb{L}[f](s)-f(0^+)$$ 
Para la segunda derivada se tiene lo siguiente: 

$$\mathbb{L}[f''](s)=s^2\mathbb{L}[f](s)-sf(0^+)-f'(0^+)$$ 
4. **Transformada de una primitiva**: Sea $f\in\mathbb{C}_\alpha$ localmente integrable, donde: 
$$F(t)=\int^{t}_{a}f(u)du$$ 
Entonces, para $s>\alpha$ se tiene que: 

$$\mathbb{L}[F'](s)=s\mathbb{L}(s)-F(0^+)$$ 
Y si se ocupa la transformada para $F$ se tiene: 

$$\mathbb{L}[F](s)=\frac{1}{s}\mathbb{L}[f](s)-\frac{1}{s}\int^{a}_{0}f(u)du$$ 
### Traslaciones 

Una traslación en el dominio temporal $t$ corresponda a un factor exponencial en el dominio de Laplace s. Si se quisiera trasladar una función $\mathbb{1}_{(t-a)}f(t-a)$, entonces: 

$$\mathbb{L}[\mathbb{1}_{(t-a)}f(t-a)](s)=e^{-sa}\mathbb{L}[f(t)](s)$$ 
De la misma forma, una traslación corresponde a un factor exponencial en el dominio temporal: 

$$\mathbb{L}[f(t)](s-a) = \mathbb{L}[e^{at}f(t)](s)$$ 