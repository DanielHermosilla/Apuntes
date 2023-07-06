
Un problema se dice lineal no homogéneo si existe $I$ intervalo 

$$I_0\in I, X_0\in\mathbb{R}^n, A:I\rightarrow M_{n\times n}(\mathbb{R}),\;\;\;B:I\rightarrow\mathbb{R}$$ 
Luego, el problema es: 

$$D=\begin{cases}X'(t) = A(t)X(t) + B(t)\\\\X(t_0)=X_0\rightarrow\text{Condiciones iniciales}\end{cases}$$ 
El problema tiene **solución y es única**. Esto se saca por [[Teoría de Existencia y Unicidad|TEU]]. 

Notemos que si $\Phi: I\rightarrow\mathbb{R}^n$ es tal que: 
$$\Phi'(t)=A(t)X(t)$$$$\Phi(t_0) = 0$$ 
Entonces $\Phi$ es 0. Notemos que $\Phi\leq 0$ es solución del problema, por unicidad, es la única. 


# Variación de parámetro 

Si $A(t)=A$ constante, entonces el problema se dice a [[EDO de coeficiente variables|coeficientes constantes]]. Si $B=0$, entonces el problema se dice homogénea. 

El problema $D$ tiene como única solución: 

$$X(t)=e^{A(t-t_0)}X_0 + \int^{t}_{t_0}e^{A(t-s)}B(s)ds$$

## Demostración 

Veamos primero el problema homogéneo: 

$$X'(t) = A(t)X(t)$$$$X(t_0) = X(0)$$ 

Veamos que $X_n(t) = e^{A(t-to)}X_0$ es solución del problema homogéneo y es único por TEU. 

Para la particular, proponemos $X_p(t) = e^{At}C(t)$, con $C(t)$ una función a encontrar. Para esto: 

$$X_p'(t) = Ae^{At}C(t) + e^{At}C'(t)$$ $$\implies e^{At}C'(t) = B(t)$$ 
Como $e^{At}$ es invertible, entonces $C'(t) = e^{-At}B(t)$. Por [[Teorema Fundamental del Cálculo|TFC]]: 

$$C(t)-C(t_0) = \int^{t}_{t_0}e^{-As}B(s)ds$$ $$\implies X_p(t) = e^{At}(C(t_0)+\int^{t}_{t_0}e^{-As}B(s)ds)$$ 
Luego: $X = X_h + X_p$, y evaluando en $t_0$: 

$$X(t_0) = X_h(t_0) + X_p(t_0)$$ $$=X_0 + C(t_0)$$ $$\implies C(t_0) = 0$$ $$X(t) = e^{A(t-t_0)}X_0 + \int^{t}_{t_0}e^{A(t-s)}B(s)ds$$ 