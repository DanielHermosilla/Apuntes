
>[!example] Teorema de Stokes 
>
>Sea $\Sigma$ una superficie orientable regular y con borde una curva $C$, curva cerrada simple. $\Sigma$ posee una normal $\hat{n}$ y es tal que la dirección de recorrido de la curva $C$ sea orientada positivamente con respecto a la normal $\hat{n}$, es decir, respeta la *regla de la mano derecha*. Sea $F:\Omega\subset\mathbb{R}^3\to\mathbb{R}^3$ , entonces: 
>
>$$\oint_C F\cdot dr=\int\int_\Sigma(\nabla\times\vec{F})d\Sigma$$


Notar que este teorema no relaciona una superficie que encierra algo, como el [[Teorema de Gauss]], si no más bien una superficie cualquiera que tiene bordes. 

```tikz 
\usepackage{tikz}
\usepackage{tikz-3dplot}

\begin{document}

\tdplotsetmaincoords{60}{130}
\begin{tikzpicture}[tdplot_main_coords, scale=1.5, transform shape]

% Dibujo la superficie
\filldraw[fill=blue!30,opacity=0.7] (0,0,0) -- (3,0,0) -- (3,3,2) -- (0,3,2) -- cycle;
\draw (0,0,0) -- (3,0,0) -- (3,3,2) -- (0,3,2) -- cycle;

% Dibujo la normal en el centro de la superficie
\draw[-stealth, thick, red] (1.5,1.5,1) -- (1.5,1.5,3) node[above] {$\hat{n}$};

% Dibujo la curva C alrededor del borde de la superficie
\draw[thick,->] (0,0,0) -- (2.5,0,0);
\draw[thick,->] (3,1,0.7) -- (3,2,1.32);
\draw[thick,->] (2.5,3,2) -- (1.5,3,2);
\draw[thick,->] (0,2,1.3) -- (0,1,0.7);
\draw[thick] (0,0,0) -- (0.2,0,0);

% Etiqueta adicional
\node at (1.5,1.5,-0.5) {Superficie $\Sigma$};
\node at (3.5,1.5,2) {C};

\end{tikzpicture}

\end{document}

```

#### Ejemplo 

Sea la superficie del plano $x+y+z=1$, limitado por los planos $x=0, y=0, z=0$, en el primer octante con normal apuntando hacia arriba. 

Sea $F:\mathbb{R}^3\to\mathbb{R}^3$, $F(x,y,z)=(2xy+yz,x^2-z^2,x+y+z)$. Calcular usando Stokes: 

$$\oint_CF\cdot dr$$ 

Notar que esto es la siguiente figura: 

```tikz 
\usepackage{tikz}
\usepackage{tikz-3dplot}

\begin{document}

\tdplotsetmaincoords{60}{120}
\begin{tikzpicture}[tdplot_main_coords, scale=2, transform shape]  % Aumento la escala aquí

% Dibujo la superficie: el triángulo en el primer octante del plano x+y+z=1
\filldraw[fill=blue!30, opacity=0.7] (0,0,1) -- (0,1,0) -- (1,0,0) -- cycle;
\draw (0,0,1) -- (0,1,0) -- (1,0,0) -- cycle;

% Dibujo la normal en el centro de la superficie apuntando hacia fuera del primer octante
\draw[-stealth, thick, red] (0.333,0.333,0.333) -- (0.666,0.666,0.666) node[anchor=south] {$\hat{n}$};

% Dibujo los ejes cartesianos más largos
\draw[-stealth, thick] (0,0,0) -- (2.5,0,0) node[anchor=west] {$x$};
\draw[-stealth, thick] (0,0,0) -- (0,2.5,0) node[anchor=north] {$y$};
\draw[-stealth, thick] (0,0,0) -- (0,0,2.5) node[anchor=east] {$z$};

% Etiquetas adicionales
\node at (0.5,0.5,-2) {Superficie $x+y+z=1$};

\end{tikzpicture}

\end{document}

```

Notemos que si miramos esto en el eje $x-y$ se tiene un rectángulo que corte en $(1,0), (0,0), (0,1)$, vale decir, limitado por la recta $x+y=1$. Por lo tanto, podemos decir que los límites de integración sería $0\leq x\leq 1$ y $0\leq y\leq 1-x$. 

Entonces, $S=\lbrace\Phi=(x,y,1-x-y)\in\mathbb{R}^2\;\vert\; 0\leq x\leq 1\;\land\; 0\leq y\leq 1-x\rbrace$. Por lo tanto, ocupando el teorema de Stokes, calculamos el rotor de $F$: 

$$\text{rot}\;\vec{F}=\nabla\times\vec{F}=\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
2xy+yz & x^2-z^2 & x+y+z
\end{vmatrix}=(1+2z,y-1,0)$$

Ahora, para obtener $d\Sigma$ hay que hacer el [[Producto vectorial|producto vectorial]] fundamental: 

$$\frac{\partial\Phi}{\partial x}\times\frac{\partial\Phi}{\partial y}=\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
1 & 0 & -1 \\
0 & 1 & -1
\end{vmatrix}=(1,1,1)$$

Como es positivo, entonces es el vector normal correcto. De lo contrario, se multiplica todo el vector por $-1$. Luego, 

$$\begin{align}
\oint_CF\cdot dr&=\int\int_\Sigma(\nabla\times F)\cdot n\;d\Sigma\\  \\
&=\int^{1}_{0}\int^{1-x}_{0}(1+2(1-x-y),y-1,x+y-1)\cdot (1,1,1)dydx\\  \\
&=\int^{1}_{0}\int^{1-x}_{0}(1-x)dydx\\  \\
&=\int^{1}_{0}(1-x)y\bigg\vert^{1-x}_{0}dx\\  \\
&=\int^{1}_{0}(1-x)^2dx\tag{u=1-x}\\  \\
&=\int^{1}_{0}u^2du\\  \\
&=\frac{1}{3}
\end{align}$$



