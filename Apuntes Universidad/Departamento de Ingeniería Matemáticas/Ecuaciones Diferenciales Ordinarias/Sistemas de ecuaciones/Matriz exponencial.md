
Se define como $A\in M_{n\times n}(\mathbb{R})(A\in\mathbb{R}^{n\times n})$, luego: 

$$e^{a}=\sum^{\infty}_{k=0}\frac{A^k}{k!}$$ $$\iff I + \sum^{\infty}_{k=1}\frac{A^k}{k!}$$ 
Entonces, se tiene una [[Series numéricas|serie numérica]], que podría o converger o diverger. 

Otra forma de verlo es dado un [[Sistema de ecuaciones|sistema de ecuaciones]] donde se tiene un [[Problema lineal no homogéneo|problema linea no homogéneo]], es decir, se tiene algo de la siguiente forma: 

$$D=\begin{cases}X'(t) = A(t)X(t) + B(t)\\\\X(t_0)=X_0\rightarrow\text{Condiciones iniciales}\end{cases}$$

Entonces, **ante un $A(t)$ constante**, se llega que: 

$$e^{At} = Pe^{Dt}P^{-1}$$ 
Donde $P$ son los [[vector propio|vectores propios]] (columna) y $D$ son los [[valor propio|valores propios]] (diagonal). Por ende, 

$$det(A-\lambda I)=0$$ 
Y con el [[polinomio característico]] se llega que: 

$$(A-\lambda I)v = 0$$

## Norma de frobenius 

Sea $A\in M_{n\times n}(\mathbb{R})(A\in\mathbb{R}^{n\times n})$, luego la función: 

$$||A||_F=\sqrt{\sum^{n}_{i=1}\sum^{n}_{j=1}A_{ij}^{2}}\;\;\;\text{es norma}$$ 
Entonces, por proposición, se establece que: 

$$||e^A||_F\leq e^{||A||_F}$$ 
#### Demostración 
$$||I + \sum^{n}_{k=1}\frac{A^k}{k!}||\leq ||I|| + \sum^{n}_{k=1}\frac{||A^k||}{k!}$$ $$\iff\leq ||I|| + \sum^{\infty}_{k=1}\frac{||A||^k}{k!}$$$$\iff 1 + \sum^{\infty}_{k=1}\frac{||A||^k}{k!} = e^{||A||}$$ $$\implies ||I+\sum^{n}_{k=1}\frac{A^k}{k!}||\leq e^{||A||}$$ 



# Propiedades 


Sean $A,B\in M_{n\times n}(\mathbb{R})$, luego: 

1. $e^{A·0} = I$ 

2. $\frac{d}{dt}e^{At} = Ae^{At}$ 

3. $e^{A(t+s)} = e^{At}e^{As}$, en particular: 

$$e^{At}\;\;\text{es invertible con}\;\;(e^{At})^{-1} = e^{-At}$$ 
4. $Be^{At} = e^{At}B$ si $AB = BA$ .

5. $e^{(A+B)t} = e^{At}e^{Bt}$ si $AB = BA$ 


### Ejemplo 

Se tiene una esfera que representa las emisiones en el planeta, dividido en el hemisferio Norte y hemisferio Sur.

![[IMG_E48893366E9B-1 1.jpeg|center|450]]


Parecido al caso de la [[Ley de enfriamiento]], se tiene que $x_1(t)$ y $x_2(t)$ representa la concentración de $CO_2$. Por lo tanto, se modela de la siguiente forma: 

$$x_1' = -\alpha x_1 + \beta(x_2-x_1)+ f_1,\;\;\; x_1(0)=x_1\degree$$ $$x_2' = -\alpha x_2 + \beta(x_1-x_2)+ f_2,\;\;\; x_2(0)=x_2\degree$$ 
Donde $\alpha > 0$ es la tasa de deposición o desaparación y $\beta > 0$ es la tasa de intercambio hemisférico. $f_1$ y $f_2$ son las fuentes de $CO_2$. 

Primero, se escribe el sistema en forma [[matriz|matricial]]: 

$$X=\begin{bmatrix}x_1(t)\\x_2(t)\end{bmatrix}\;\;\;\;\text{(Vector de estado)}$$ 
$$X' = \begin{bmatrix}-(\alpha + \beta)&\beta\\\beta&-(\alpha + \beta)\end{bmatrix}X + \begin{bmatrix}f_1\\f_2\end{bmatrix}$$ 
Notemos que la matriz que acompaña a $X$, denominada la matriz $A$ es constante. Sin embargo, el lado derecho podría ser variable. Por último, sabemos las condiciones iniciales: 

$$X(0)=\begin{bmatrix}x_1\degree\\x_2\degree\end{bmatrix}$$ 
Por lo tanto, para calcular la matriz exponencial se tendrá que hacer la descomposición de $A$ en [[valores y vectores propios]]. Notemos que $A$ es simétrica, entonces es una [[matriz diagonalizable]]. 

$$A=PDP^{-1}$$ 
Primero se calcula el determinante de $A-\lambda I$: 

$$\begin{bmatrix}-(\alpha + \beta)-\lambda&\beta\\\beta&-(\alpha + \beta)-\lambda\end{bmatrix} = (-(\alpha+\beta)-\lambda)(-(\alpha + \beta)-\lambda)-\beta^2=0$$ 
$$\iff (\lambda + (\alpha + \beta))^2 = \beta^2$$$$\implies\lambda=\begin{cases}\lambda_1 = -\alpha\\\\\lambda_2 = -(\alpha + 2\beta)\end{cases}$$ 
Y para los vectores propios: 

$$(A-\lambda_1I)v_1 = 0\implies\begin{bmatrix}-(\alpha + \beta)+\alpha&\beta\\\beta&-(\alpha + \beta)+\alpha\end{bmatrix}v_1 = \begin{bmatrix}0\\0\end{bmatrix}$$  
$$(A-\lambda_2I)v_2 = 0\implies\begin{bmatrix}-(\alpha + \beta)+\alpha + 2\beta&\beta\\\beta&-(\alpha + \beta)+\alpha +2\beta\end{bmatrix}v_2 = \begin{bmatrix}0\\0\end{bmatrix}$$


Por lo tanto, si uno busca las soluciones [[dependencia|linealmente independientes]], se llega que: 

$$v_1\in\langle\begin{pmatrix}1\\1\end{pmatrix}\rangle\;\;\land\;\;v_2\in\langle\begin{pmatrix}-1\\1\end{pmatrix}\rangle$$ 
Por lo tanto, la [[matriz]] $P$ y $D$ llegaría a ser: 

$$P=\begin{bmatrix}1&-1\\1&1\end{bmatrix}\;\;\;\land\;\;\; D=\begin{bmatrix}-\alpha\\-(\alpha+2\beta)\end{bmatrix}$$ 
Entonces, se pasa a forma exponencial, es decir, $e^{At} = Pe^{Dt}P^{-1}$, es decir: 

$$e^{At} = \begin{bmatrix}1&-1\\1&1\end{bmatrix}\begin{bmatrix}e^{-\alpha t}\\ e^{-(\alpha+2\beta)t}\end{bmatrix}P^{-1}$$ 
Realizando la multiplicación: 

$$e^{At} = \frac{1}{2}\begin{bmatrix}e^{-\alpha t}&-e^{-\alpha+2\beta)t}\\e^{-\lambda t}&e^{-(\lambda+2\beta)t}\end{bmatrix}\begin{bmatrix}1&-1\\1&1\end{bmatrix}$$ $$e^{At} = \frac{1}{2}\begin{bmatrix}e^{-\alpha t}+e^{-(\lambda + 2\beta)t}&e^{\lambda t}-e^{-(\lambda + 2\beta)t}\\e^{-\lambda t}-e^{-(\lambda + 2\beta)t}&e^{-\lambda t} + e^{-(\lambda + 2\beta)t}\end{bmatrix}$$ 
Por lo tanto, la **solución homogénea** llegaría a ser: 

$$X_h = \begin{bmatrix}x_{1h}\\x_{2h}\end{bmatrix}=e^{At}\begin{bmatrix}x_1\degree\\x_2\degree\end{bmatrix}=\frac{1}{2}\begin{bmatrix}e^{-\alpha t}+e^{-(\lambda + 2\beta)t}&e^{\lambda t}-e^{-(\lambda + 2\beta)t}\\e^{-\lambda t}-e^{-(\lambda + 2\beta)t}&e^{-\lambda t} + e^{-(\lambda + 2\beta)t}\end{bmatrix}\begin{bmatrix}x_1\degree\\x_2\degree\end{bmatrix}$$ 
Por ende, 

$$X_h = x_1\degree(e^{-\alpha t}-e^{-(\alpha + 2\beta)t}) + x_2\degree(e^{-\alpha t}+e^{-(\alpha+2\beta)t})$$ 
Además, se sabe que la **fórmula de la solución particular** es la siguiente: 

$$\int_{t_0}^{t}e^{A(t-s)}B(s)ds$$
$$\iff\int_{t0}^{t}e^{A(t-s)}\begin{bmatrix}f_1\\f_2\end{bmatrix}ds$$ 
Queda propuesto calcular la solución particular, donde se integra cada componente por sí sola y las filas representan las emisiones por cada hemisferio. 