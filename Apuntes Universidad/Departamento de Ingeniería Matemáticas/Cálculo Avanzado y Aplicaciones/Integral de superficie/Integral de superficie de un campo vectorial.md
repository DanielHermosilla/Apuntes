
Esto, haciendo referencia al *flujo vectorial* a través de una superficie. 

Sea $\Sigma$ la [[Superficie|superficie]] de ecuación $\vec{X}=\vec{F}(u,v)$ con $(u,v)\in D$ suave y simple y supongamos que $\Sigma\subset H$, donde $H\subset \mathbb{R}^3$ es un [[Conjuntos abiertos y cerrados|conjunto abierto]]. Sea $\vec{f}:H\subset\mathbb{R}^3\to\mathbb{R}^3$ un [[Campos escalares y vectoriales|campo vectorial]] continuo en $H$. Se llama integral de superficie o flujo del campo vectorial $\vec{f}$ a través de $\Sigma$: 

$$\int\int_\Sigma \vec{f}\cdot\hat{n}\;d\sigma=\int\int_D\vec{f}(\vec{F}(u,v))\cdot\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\;dudv $$

Notemos que esta notación es consistente con la definición, pues: 

$$\hat{n}=\frac{\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)}{\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert}\;\land\;d\sigma=\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert\;dudv$$ 
El significado físico de esto se puede ver bajo la siguiente imagen, donde se tiene un flujo vectorial $\vec{f}$ y una [[Superficie|superficie]] $\Sigma$, entonces $\vec{f}\cdot\hat{n}=\vert\vert\vec{f}\vert\vert\cos\alpha$, que llegaría a ser *cuánto campo de $f$ está en la dirección del plano normal a la superficie.* 

![[Captura de pantalla 2023-08-27 a la(s) 20.40.11.png|center|]]

## Caso con flujo tangencial 

Si $\vec{f}$ llegase a ser [[Vector tangencial|tangencial]] a la superficie, entonces el flujo a través de ella es nulo: 

$$\int\int_\Sigma\vec{f}\cdot\hat{n}\;d\sigma=0$$

![[Captura de pantalla 2023-08-27 a la(s) 20.42.28.png|center|550]]


#### Ejemplo 

Hallar el flujo de $\vec{f}(x,y,z)=(y,x^2-y,xy)$ a través del trozo de superficie cilíndrica de ecuación $y=x^2$ en el primer octante con $x+y+z\leq 2$ indicando en un gráfico la orientación elegida para $\hat{n}$. 

Se tendría una curva $C\in\Sigma$ del siguiente estilo: 

![[Captura de pantalla 2023-08-27 a la(s) 20.45.35.png|center|600]]


Antes que nada, considerando la restricción, se proyecta en el plazo $x-z$ en la curva de ecuación: 

$$z=2-x-x^2$$

![[Captura de pantalla 2023-08-27 a la(s) 20.50.13.png|center|550]]



Notar que al ser una superficie, se parametriza en dos variables, por lo tanto, una parametrización de $\Sigma$ es: 

$$\vec{F}(x,z)=(x,x^2,z)$$ 
Con $(x,z)\in D=\lbrace(x,z)\in\mathbb{R}^2:0\leq x\leq 1\;\land\; 0\leq z\leq 2-x-x^2\rbrace$. Ahora bien, encontrando las [[Derivada parcial|derivadas parciales:]]

$$\frac{\partial \vec{F(x,z)}}{\partial x}\times\frac{\partial \vec{F(x,z)}}{\partial z}=\begin{bmatrix}
\hat{i} & \hat{j} & \hat{k} \\
1 & 2x & 0 \\
0 & 0 & 1
\end{bmatrix}=(2x,-1,0)$$ 
Finalmente, bajo el cálculo del [[Producto vectorial|producto vectorial]] se obtiene el [[conjuntos ortogonales y ortonormales|vector normal]] a la superficie $\Sigma$. 

![[Captura de pantalla 2023-08-27 a la(s) 20.57.36.png|center]]


Por ende, 

$$\begin{align}
\int\int_\Sigma \vec{f}\cdot\hat{n}\;d\sigma&=\int\int_{D_{xz}}\vec{f}(\vec{F}(x,z))\cdot\vec{F^{'}_{x}}(x,z)\times\vec{F^{'}_{z}}(x,z)\;dxdz\\  \\
&=\int\int_{D_{xz}}\vec{f}(x,x^2,z)\cdot(2x,-1,0)\;dxdz\\  \\
&=\int\int_{D_{xz}}(x^2,0,x^3)\cdot(2x,-1,0)\;dxdz\\  \\
&=\int^{1}_{0}\int^{2-x-x^2}_{0}2x^3\;dzdx\\  \\
&=\frac{4}{15}
\end{align}$$


$$\begin{align}
\oint_{C}\vec{F}\cdot d\vec{r} &=\iint_S (\vec{\nabla}\times\vec{F})d\vec{S}\tag{Teorema de Stokes}\\ \\ 
\iint_{\Omega}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) &= \iint_S (\vec{\nabla}\times\vec{F})d\vec{S}\tag{Teorema de Green}
\end{align}$$
