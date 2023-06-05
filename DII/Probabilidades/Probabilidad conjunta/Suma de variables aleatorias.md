
Si $X_1$ y $X_2$ son dos [[Variable aleatoria discreta|variables aleatorias discretas]] e [[Probabilidades/Probabilidad conjunta/Probabilidad conjunta continua/Independencia|independientes]], la [[PMF conjunto|PMF]] de $Y=X_1 + X_2$ está dada por: 


$$p_y(y)=\sum_{x_2\in R_{x_2}}p_{x_1}(y-x_2)\cdot p_{x_2}(x_2)$$

$$p_x(x)=\sum_{x_1\in R_{x_x}}p_{x_2}(y-x_1)\cdot p_{x_1}(x_1)$$

Esto se llama **convolución**. 

## Caso de Poisson 

Si se tiene $X_1,\dots,X_k$ son variables aleatorias con [[Distribución de Poisson]], de parámetros $\lambda_1,\dots,\lambda_k$, entonces: 

$$\sum_{i=1}^{k}X_i\sim\text{Poisson}\left(\sum_{i=1}^{k}\lambda_i\right)$$ 
### Ejercicio propuesto 

Sea $X\sim\text{Binomial}(n,p)$ y $Y\sim\text{Binomial}(m,p)$ variables aleatorias [[Probabilidades/Probabilidad conjunta/Probabilidad conjunta continua/Independencia|independientes]], probar que $X+Y$ tambien es una binomial usando **convolución**: 

**Hint**: Identidad de Valdelmort: 

$$\begin{pmatrix}n+m\\z\end{pmatrix}=\sum_{y=0}^{n}\begin{pmatrix}n\\z-y\end{pmatrix}\begin{pmatrix}m\\y\end{pmatrix}$$ 
## Caso de Distribución Uniforme 

Sean dos variables aleatorias con [[Distribución Uniforme]], entonces, se tiene lo siguiente: 

$$\begin{align}
W &= U + V
\end{align}$$ 
Esta tiene la siguiente PMF: 

$$f_w(w)=\begin{cases}w&\text{si}\;w\in[0,1]\\\\2-w&\text{si}\;w\in(1,2]\\\\0&\text{si no}\end{cases}$$ 
Tendría el siguiente gráfico: 

![[Pasted image 20230605092327.png|center]]

