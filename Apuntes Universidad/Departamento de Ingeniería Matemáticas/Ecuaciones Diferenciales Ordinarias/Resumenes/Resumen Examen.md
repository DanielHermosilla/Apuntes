
## Resolución de sistema lineales

Para solucionar un sistema de EDO's , se busca su **matriz fundamental**, que es, básicamente, la matriz que contiene la multiplicación de los vectores propios, con los valores propios en la diagonal y la inversa al final. 

#### Ejemplo 

La siguiente EDO tiene como matriz lo siguiente: 

$$\begin{align}
y'' - 9y &= 0\\\\
\binom{x_1}{x_2}'&=\begin{pmatrix}
0 & 1 \\
9 & 0
\end{pmatrix}\binom{x_1}{x_2}\\\\
e^{At}&=\begin{pmatrix}
1 & 1 \\
-3 & 3
\end{pmatrix}\begin{pmatrix}
e^{-3t} & 0 \\
0 & e^{3t}
\end{pmatrix}\frac{1}{6}\begin{pmatrix}
3 & -1 \\
3 & 1
\end{pmatrix}
\end{align}$$

Tiene las siguientes propiedades: 

1. $e^{A\cdot 0}=0=I$
2. $\frac{d}{dt}e^{At}=Ae^{At}$ 
3. $e^{A}(t+s)=e^{At}e^{As}$. En particular, quiere decir que $e^{At}$ es invertible y su inversa es: $(e^{At})^{-1}=e^{-At}$.
4. $AB=BA\iff Be^{At}=e^{At}B$
5. $AB=BA\iff e^{At}e^{Bt}$

Básicamente, las propiedades hace que se comporte igual que una exponencial común. 

La **solución a un sistema homogéneo** se puede escribir entonces como: 

$$X_h(t)=Pe^{Dt}C$$

Con $C$ un vector constante que depende de las condiciones iniciales. Ahora, cuando se tiene que la exponencial es invertible, se dice que es la *matriz exponencial canónica* $\Phi$ 

P