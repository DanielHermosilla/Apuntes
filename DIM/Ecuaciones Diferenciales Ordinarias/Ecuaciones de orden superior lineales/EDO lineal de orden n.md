
Se tienen los siguientes Problemas de Cauchy donde: 

$$y^{(n)} + \bar{a_{n-1}}y^{n-1} + \dots = \bar{Q(x)}$$ 
Donde 
$$y(x_0),\  y'(x_0),\dots,\ y^{n-1}(x_0)$$ Son las variables iniciales. 

## Coeficientes constantes 

Primero se cálcula la solución homogenea, es decir, $\bar{Q(x)}=0$, donde 

$$P(D)= D^n + \bar{a_{n-1}}D^{n-1} + \dots \ \ \ \text{Operador diferencial}$$ 
Y también se podría encontrar el polinomio carácteristico: 


$$P(\lambda)= \lambda^n + \bar{a_{n-1}}\lambda^{n-1} + \dots \ \ \ \text{Polinomio característico}$$

Por lo tanto, se tienen $n$ raíces complejas $\lambda_l$, de multiplicidad $m_l$, y $\sum m_l = n$ valores característicos.  Por lo tanto, se llegan a polinomios de la forma: 

$$p(\lambda) = (\lambda^2 + 1)^2(\lambda - 1)(\lambda + 2) = 0$$ 
Donde se llegan a cosas del estilo: $$\text{Raices}=\begin{cases}
\lambda_1=-2 & m_1 = 1 \\ 
\lambda_2 = 1 & m_2 = 5 \\ 
\lambda_3 = i & m_3 = 2 \\
\lambda_4 = -i & m_4 = 2 \\ 
\end{cases}$$ 
En este ejemplo, la construcción de la función sería la siguiente: 

$$y_h = \alpha_1e^{-2x} + \alpha_2e^{x} + \alpha_3xe^{x} + \alpha_4x^2e^x + \alpha_5x^3e^x + \alpha_6x^4e^x + \alpha_7\cos(x) + \alpha_8\sin(x) + \alpha_9x\cos(x) + \alpha_{10}x\sin(x)$$ 
Entonces, hay que considerar cuando hay raices complejas y/o reales. Entonces, reescribiendo la solución: 

$$(D-\lambda_1)^{m_1}(D-\lambda_2)^{m_2}\dots((D-\sigma_c)^2 + \omega_{c}^{2})^{m_c} + \dots + (D-\lambda_l)^{m_l}y = 0$$ 
Además se sabe que $$\text{Factores}=\begin{cases}
(D-\lambda_1)^{m_1}y = 0 & m_1 \ \text{soluciones} \\ 
(D-\lambda_2)^{m_2}y = 0 & m_2 \ \text{soluciones} \\ 
\vdots \\
((D-\sigma_c)^2 + \omega_{c}^{c})^{m_c}y = 0 & m_c \ \land \ m_l\  \text{soluciones} \\ \end{cases}$$ 
Dado que los operadores diferenciales son comutativos, se podría mover el operador hasta llegar a: 

$$(D-\lambda)y = y' - \lambda y=0\implies y = \alpha e^{\lambda x}$$

En este caso, en $y=\alpha e^{\lambda x}$ se dice que es una raiz, y por lo tanto $e^{\lambda x}$ se le denomina **anulador.** 

Haciendo un segundo análisis: 

$$(D-\lambda)(f(x)e^{\lambda x}) = D(fe^{\lambda x}) - \lambda fe^{\lambda x} = 0$$ $$\implies = f'e^{\lambda x}$$ 
Entonces, se tiene que por propiedad: 

### Propiedad: 

$$(D-\lambda)^m\left[f(x)e^{\lambda x}\right] = f^{(m)}(x)e^{\lambda x}$$ 
Por lo tanto, las $n$ soluciones del problema son: 

- 2. $(D-\lambda)^xe^{\lambda x} = 0$ 
- 3. $(D-\lambda)^3(x^2e^{\lambda x})$ 

## Teorema 

La solución de: 

$$(D-\lambda_1)^{m_1}(D-\lambda_2)^{m_2}\dots((D-\sigma_c)^2 + \omega_{c}^{2})^{m_c} + \dots + (D-\lambda_l)^{m_l}y = 0$$

Está dada por una [[combinación lineal]] de las soluciones: 

$$\lbrace e^{\lambda_1x}, xe^{\lambda_1x},\dots,x^{m_1-1}e^{\lambda_1 x}, e^{\lambda_2x},xe^{\lambda_2x},\dots,x^{m2-1}e^{\lambda_2 x}, e^{\sigma x}\cos(\omega x), xe^{\sigma x}\cos(\omega x), \dots, x^{m-1}e^{\lambda x}\sin(\omega x), e^{\lambda_lx}, xe^{\lambda_lx},\dots, x^{m-1}e^{\lambda x}\rbrace$$ 
Dado $y_h\in H$, entonces $$y_h = \alpha_1 y_1 + \dots + \alpha_n y_n$$
$$y'_{h} = \alpha_1 y_1' + \dots + \alpha_n y_n'$$
$$y_{h}^{n-1} = \dots$$ 
Entonces, se tiene la siguiente [[matriz]]: 

$$\begin{bmatrix}
y_1 & \dots & y_n \\
y_1' & \dots & y_n' \\ 
\vdots & \vdots & \vdots\\ 
y_{1}^{(n-1)} & \vdots & y_n^{n-1} \\ 
\end{bmatrix} \begin{bmatrix}
\alpha_1 \\
\alpha_2 \\ 
\vdots \\ 
\alpha_n \\ 
\end{bmatrix} = \begin{bmatrix}
y_h \\
y_h' \\ 
\vdots \\ 
y_{h}^{n-1} \\ 
\end{bmatrix}$$ 
Como es [[dependencia|independiente]] entonces la matriz es invertible y también por [[Teoría de Existencia y Unicidad|TEU]] se puede demostrar que tiene solución única para generar $y_h$. 