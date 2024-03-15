
Sea $X_1, X_2, \dots, X_n$ [[Variable aleatoria continua|variables aleatorias]] con [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Esperanza|esperanza]] y [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Varianza|varianza]] finita, es decir, $\vert E[X_i]\vert = \vert\mu\vert <\infty$ y $Var[X_i]=\sigma^2<\infty$, entonces: 

$$Z_n = \frac{X_n-\mu}{\sigma/\sqrt{n}}=\frac{X_1+\dots+X_n-n\cdot\mu}{\sqrt{n}\cdot\sigma}$$ 
Converge en distribución a una [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria continua/Distribuciones/Distribución Normal|distribución estándar Normal]] cuando $n\to +\infty$, es decir: 

$$\lim_{n\to+\infty}P(Z_n\leq z)=\Phi(z)$$ 
Para todo $z\in\mathbb{R}$ 