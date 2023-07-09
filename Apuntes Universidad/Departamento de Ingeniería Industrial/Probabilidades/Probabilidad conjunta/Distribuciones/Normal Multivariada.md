Si $Z=(Z_1,Z_2,\dots, Z_k)$ es un vector de [[Variable aleatoria continua|variable aleatorias]] [[Departamento de Ingeniería Industrial/Probabilidades/Probabilidad conjunta/Probabilidad conjunta continua/Independencia|independientes]],  todas $\text{Normal}(0,1)$ y $\mu\in\mathbb{R}^m, A\in\mathbb{R}^{m\times k}$, entonces decimos que el vector $X=(X_1,\dots, X_m)=AZ + \mu$ es una normal multivariados de parámetros $\mu, \sum = AA^T$. Esto se denota como $X\sim N(\mu,\sum)$ 

Notemos que la PDF sería la siguiente: 

$$\begin{align}
\text{PDF}_z &= \Pi_{i=1}^{k}\frac{1}{\sqrt{2\pi}}e^{\frac{-1}{2}z_{i}^{2}}\\\\
&=\frac{1}{\sqrt{(2\pi)^2}}e^{\frac{-1}{2}(z_{1}^{2}+\dots + z_{k}^{2})=z^t z}\\\\
&=\frac{1}{\sqrt{(2\pi^k)}}e^{\frac{-1}{2}z^tz}\\\\
\text{TCV}& x=g(z)=AZ+\mu\\\\
&\implies g^{-1}=A^{-1}(x-\mu)\;\land\; \vert J_g\vert = det(J_g) = det(A)\\\\
PDF_z &= TCV = \frac{1}{\sqrt{(2\pi)^k}}\cdot c^{\frac{-1}{2}(x-\mu)^t(A^{-1}(x-\mu))}\cdot\frac{1}{\text{det}(A)}\\\\ 
\frac{1}{\text{det}(A)}&=\frac{1}{\vert J_{g^{-1}}\vert} = \frac{1}{\sqrt{\vert\sum\vert}}\\\\
&\implies \frac{1}{\sqrt{(2\pi)^k\vert\sum\vert}}\cdot e^{-\frac{1}{2}(x-\mu)^t \sum^{-1}(x-\mu)}\end{align}$$ 
Donde $\vert\sum\vert=\text{Det}(\sum)$  y $\sum$ es la matriz de [[Covarianza|covarianza]]. 

Acordándonos que $J_{g^{-1}} = \frac{\partial g^{-1}}{\partial x} = A^{-1}\; \vert J_{g^{-1}}\vert=\vert A\vert$ 

Llegaría a ser de la siguiente forma: 

![[Pasted image 20230602092930.png|center]]


## Propiedades 

Si $X=(X_1,X_2\dots, X_k)\sim\text{Normal}(\mu,\sum)$, entonces: 

- $X_i\sim Normal(\mu_i,\sum_{i,i})$ 
- $\text{Cov}(X_i,X_j)=\sum_{i,j}$ 
- Para toda secuencia de reales $(a_1,\dots, a_k)$ la variable aleatoria $Y=\sum_{i}a_iX_i$ sigue una [[Distribución Normal]] 
- Si $\text{Cov}(X_i,X_j)=\sum_{i,j}=0$ entonces $X_i$ y $X_j$ son [[Departamento de Ingeniería Industrial/Probabilidades/Probabilidad conjunta/Probabilidad conjunta continua/Independencia|independendientes]]