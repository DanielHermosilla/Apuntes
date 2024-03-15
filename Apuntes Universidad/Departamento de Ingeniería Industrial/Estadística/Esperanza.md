
El valor [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria discreta/Esperanza/Esperanza|esperado]] de una [[Variable Aleatoria|variable aleatoria]] $X$ se denota como $E[X]$ o $\mu_x$. Esto corresponde **al primer [[Función Generadora de Momento|momento]] de la distribución**. 

Para el caso discreto y continuo se calcula de las siguientes maneras respectivamente: 

$$\begin{align}
E[g(X)]&=\sum_xg(x)\cdot f(x)\tag{Variable discreta}\\  \\
E[g(X)]&=\int_xg(x)\cdot f(x)\;dx\tag{Variable continua}
\end{align}$$

Es importante notar que la **esperanza es lineal**, es decir, si $g(X)=a+bX$, entonces: 

$$E[g(X)]=E[a]+bE[X]$$

