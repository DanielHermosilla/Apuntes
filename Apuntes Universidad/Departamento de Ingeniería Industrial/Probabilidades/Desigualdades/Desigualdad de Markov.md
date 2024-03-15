
Sea $X$ una [[Variable aleatoria continua|variable aleatoria]] que toma valores no negativos, para todo real $a>0$ se cumple que: 

$$\mathbb{P}(X\geq a)\leq\frac{E[X]}{a}$$ 
### Demostración 

Sea la variable aleatoria cualquiera $Y$, que toma los siguientes valores: 

$$Y=\begin{cases}\alpha &\text{si}\; X\geq\alpha\\\\
0&\text{si no}\end{cases}$$ 
Entonces, sabemos que la [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Esperanza|esperanza]] cumple lo siguiente: $E[Y]\leq E[X]$. Por lo tanto, 

$$\alpha\mathbb{P}(X\geq\alpha)+0\implies\alpha\mathbb{P}(x\geq\alpha)\leq E[X]$$ 
### Ejemplo 

Sea $X$ el tiempo de llegada de un bus. Si $E[X]=1$ ¿Qué tan grande puede ser $\mathbb{P}(X\geq 10)$? 

Ocupando la desigualdad de Markov: 

$$\mathbb{P}(X\geq 10)\leq\frac{1}{10}$$ 
Ahora nos informan que $Var(X)=1$, ¿Qué podriamos decir ahora de $\mathbb{P}(X\geq 10)$? 

Como tenemos la [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Varianza|varianza]], sabemos que ésta se define como: 

$$\begin{align}
Var(x)&=E[(x-E[X])^2]\\\\
Y&=(x-E[X])^2\\\\
\mathbb{P}(y\geq b)&=\mathbb{P}\left((x-E[X])^2\geq b^2\right)\;\;\; b^2>0\\\\
&\leq\frac{Var(x)}{b^2}\\\\
\mathbb{P}(\vert x-E[x]\vert\geq b)&\leq\frac{Var(x)}{b^2}\\\\ 
\mathbb{P}(x\leq 10)&=\mathbb{P}(x-1\geq 9)\leq\mathbb{P}(x-1\geq 9)+\mathbb{P}(x-1\leq -9)\\\\
&=\mathbb{P}(\vert x-1\vert\geq 9)\leq\frac{1}{81}\end{align}$$ 
Esto se conoce como [[Desigualdad de Chebyshev|desigualdad de Chebyshev]]