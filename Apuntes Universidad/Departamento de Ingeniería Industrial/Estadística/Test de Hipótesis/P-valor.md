
Se definirá el p-valor como una medida intermedia para evaluar $H_0$ y $H_1$. Dada una muestra de datos $x=x_1,\dots, x_n$ definimos el test esta´distico de interés como: 

$$t^*=T(X)=\frac{\bar{X_n}-\mu_0}{\sigma/\sqrt{n}}$$

Y, se definirá el p-valor, como: 

$$\textit{p-valor}=P_r(\vert\; t\;\vert >\;\vert t^*\vert\;\;\vert H_0\;\text{es verdadero})$$

La probabilidad que ocurra un valor $t$ mayor a $t^*$ condicional en que $H_0$ es verdadera. 

Es decir, *el mínimo nivel de significancia que, dada nuestra muestra, nos llevaría a rechazar la hipótesis nula*. 

Hay $4$ pasos para usar el p-value en un test de hipótesis: 

1. Definimos $H_0$ y $H_1$

2. Asumiendo que la nula es verdadera, calculamos el valor del test estadístico: 

$$t=T(X)=\frac{\bar{X_n}-\mu_0}{\sigma /\sqrt{n}}$$

3. Conocemos el valor de $t$ por tabla. Luego, calculamos el *p-value*. 

4. Definimos un nivel de significancia en algunos valores tradicionales 

## Dualidad con intervalos de confianza

Supongamos que tenemos las siguientes hipótesis: 

$$\begin{align}
H_0\;:\;\mu&=\mu_0\\  \\
H_1\;:\;\mu&\neq\mu_0
\end{align}$$

El siguiente test debe tener un nivel de significancia $\alpha$. 

Por lo tanto; 

1. Obtenemos el intervalo de confianza de $1-\alpha\%$ para $\mu$: 

$$\bar{X}\pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$$

2. Rechazamos la nula si el intervalo de confianza no contiene a $\mu_0$. 

## Test de $t$-medias 

Considerando dos poblaciones distribuidas normalmente con $X\sim N(\mu_x, \sigma^{2}_{x})$ y $Y\sim N(\mu_y, \sigma^{2}_{y})$, queremos saber si las dos poblaciones después de $n$ observaciones tienen la misma media. 

Por lo tanto, se tiene el siguiente test de hipótesis: 

$$º\begin{align} 
H_0\;:\;\mu_x=\mu_y&\iff\mu_x-\mu_y=0\\  \\
H_1\;:\;\mu_x\neq\mu_y&\iff\mu_x-\mu_y\neq 0
\end{align}$$

### Test de dos y una cola  

Se rechaza la hipótesis cuando $\mu_x\neq\mu_y$ cuando la diferencia entre ambos es mucha hacia ambos "lados". Si se considera únicamente un lado, llegaría a ser test de una cola. 



