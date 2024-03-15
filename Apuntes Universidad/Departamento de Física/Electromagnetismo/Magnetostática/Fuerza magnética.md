
Por lo general en los [[Conductores eléctricos|conductores eléctricos]] no existe un [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] al haber una [[Corriente estacionaria|corriente estacionaria]] pero sí hay una **fuerza de atracción** entre ambos flujos de corriente. Esta fuerza de atracción no se puede explicar mediante la electrostática. 

Por ejemplo, corrientes en distintas dirreciones se **repelen**:

```tikz 
\usepackage{tikz}

\begin{document}
\begin{tikzpicture}[scale=2]
    % Wires
    \draw[very thick, gray] (0,0) -- (0,4);
    \draw[very thick, gray] (2,0) -- (2,4);

    % Current directions (using arrows)
    \foreach \y in {1, 2, 3} {
        \draw[->, red, thick] (0, \y) -- (0, \y+0.5) node[midway, left] {$I$};
        \draw[->, red, thick] (2, \y) -- (2, \y-0.5) node[midway, right] {$I$};
    }

    % Repulsion indication (using outward arcs)
    \draw[blue, thick, <->] (0.1,2) -- (1.9,2) node[midway, above] {Repulsión};

\end{tikzpicture}
\end{document}
```



Un ejemplo introductorio de esta fuerza eléctrica se puede ver por el siguiente ejemplo: nos podriamos ver el problema de una carga de prueba sometida a una fuerza hecha por un cable infinito y coaxial. 


```tikz 
\begin{document}
\begin{tikzpicture}[scale=2]
    % Infinite charge distribution line
    \draw[very thick] (-3,0) -- (3,0);
    \foreach \x in {-2.5,-2,...,2.5} {
        \draw[red,fill=red] (\x, 0) circle (0.1);
    }

    % Test particle
    \draw[blue,fill=blue] (0,1) circle (0.2);

    % Velocity vector
    \draw[blue,thick,->] (0,1) -- (1,1) node[anchor=south] {$\vec{V}$};

    % Annotations
    \node at (0,-0.5) {Distribución infinita de carga};
    \node at (0,1.5) {Partícula de prueba};
\end{tikzpicture}
\end{document}
```


La partícula **sin velocidad** está sometida, trivialmente, por la fórmula $\vec{F}=Q\vec{E}$. El campo eléctrico depende de la distribución de carga, según la [[Ley de Gauss|ley de Gauss]]. Sin embargo, al haber una **velocidad involucrada**, vale decir, una partícula **en movimiento**, se tendría que considerar la [[Transformaciones de Lorentz|transformación de Lorentz]] al tener un [[Momento lineal relativista|momento lineal relativista]]. 

Por ende, se postula la **fuerza magnética**: 

$$\vec{F}_\text{mag}=Q\vec{V}\times\vec{B}$$

Donde $Q$ es la carga de prueba, $\vec{V}$ es la velocidad de la carga de prueba y $\vec{B}$ es el campo magnético dado. 

Ahora, el caso general corresponde a la **fuerza de Lorentz**: 

$$\vec{F}=Q\vec{E}+Q\vec{V}\times\vec{B}$$

Por lo tanto, analizando algunos casos; 

- Cuando $\vec{V}=0$, la fuerza magnética es nula. Hace sentido con la definición de [[Magnetostática|magnetostática]]. 

- Cuando $\vec{V}\neq 0$ y $\vec{B}=\text{cte}$, se puede hacer en análisis del [[Producto vectorial|producto vectorial]] de la velocidad con el campo magnético.  Haciendo tal análisis, es posible encontrar que **la particula va a tener un movimiento circular**: 

```tikz 

\usepackage{tikz}
\usepackage{tikz-3dplot}

\begin{document}
\tdplotsetmaincoords{70}{110} % sets the perspective
\begin{tikzpicture}[tdplot_main_coords, scale=1.5]

    % Draw helix representing the spiraling motion
    \def\loops{5}
    \def\height{4}
    \draw[thick,blue,domain=0:2*\loops*pi,samples=300,smooth] plot ({sin(deg(\x))},{cos(deg(\x))},{\height*\x/(2*\loops*pi)});

    % Draw particle at some point on helix
    \def\particleAngle{7*pi/4}
    \fill[red] ({sin(deg(\particleAngle))},{cos(deg(\particleAngle))},{\height*\particleAngle/(2*\loops*pi)}) circle (0.1);

    % Draw magnetic field direction
    \draw[->, ultra thick, purple] (0,0,0.5*\height) -- (0,0,1.5*\height) node[anchor=south] {$\vec{B}$};

    % Annotations
    \node at (2.5,-2.5,0) {Trayectoria de la partícula};
    \node[red] at ({sin(deg(\particleAngle))+1},{cos(deg(\particleAngle))}, {\height*\particleAngle/(2*\loops*pi)}) {Partícula};

\end{tikzpicture}
\end{document}
```

Por ende, se llegaría que: 

$$\begin{align}
ma_c&=QV_\perp B\\  \\
m\frac{V_{\perp}^{2}}{R}&=QV_\perp B
\end{align}$$

Entonces, es posible definir la **frecuencia de ciclotrón** al tener un movimiento: 

$$w=\frac{V_\perp}{R}=\frac{Q}{m}B$$


## Fuerza sobre un cable con corriente 

De la [[Corriente estacionaria|corriente estacionaria]] se saben las siguientes ecuaciones: 

$$\begin{align}
\vec{J}&=\rho\vec{V}\\  \\
I&=\int^{}_{S}\vec{J}\cdot d\vec{S}
\end{align}$$

Si aplicamos la definición básica de [[Corriente eléctrica|corriente eléctrica]], es posible llegar a las siguientes conclusiones al asumir un cable con corriente y densidad $\eta$: 

$$\begin{align}
I&=\frac{dQ}{dt}\\  \\
&=\frac{\eta dl}{dt}\\  \\
&=\frac{\eta v\cancel{dt}}{\cancel{dt}}\\  \\
\vec{I}&=\eta\vec{V}\tag{Corriente en el cable}
\end{align}$$

Dado que se tiene la corriente sobre un cable, es posible calcular la fuerza magnética: 

$$\begin{align}
\vec{F}_\text{mag}&=\int_\text{Cable}dQ\vec{V}\times\vec{B}\\  \\
&=\int_\text{Cable}\eta\;dl\;\vec{V}\times\vec{B}\\  \\
&=\int_\text{Cable}\eta\;\vec{V}\times\vec{B}\;dl\\  \\
&=\int\vec{I}\times\vec{B}\;dl\iff\int_\text{Cable}I\;\times\vec{B}\;d\vec{l}\tag{Fuerza en cable}
\end{align}$$


#### Ejemplo 

Levantar una masa con $I$ y $\vec{B}$.  El campo magnético apunta hacia adentro del plano con lineas. Se tiene una región con un campo magnético uniforme hacia adentro.

![[Captura de pantalla 2023-10-06 a la(s) 09.10.53.png|center]]


Por lo tanto, se debe encontrar $I$ para levantar la masa. Sabemos que: 

$$\vec{F}_\text{mag}=I\int d\vec{l}\times\vec{B}$$

Como $d\vec{l}$ es el camino, entonces: 

$$\begin{align}
d\vec{l}&=dy\hat{j}\\  \\
\vec{B}&=\hat{k}\\  \\
d\vec{F_1}&=Id\vec{l}\times\vec{B}\\  \\
&=I(dy\hat{j})\times (-B\hat{k})\\  \\
&=IdyB\hat{i}
\end{align}$$

La otra fuerza es exactamente igual, entonces por simetría; $d\vec{F_1}=-d\vec{F_3}$ se cancelan. 

Para encontrar las fuerzas horizontales; 

$$\begin{align}
d\vec{F_3}&=I(dx\hat{i})\times(-B\hat{k})\\  \\
&=-IdxB\hat{i}\times\hat{k}\\  \\
&=IBdx\hat{j}
\end{align}$$

Entonces, 

$$\begin{align}
\vec{F_3}&=\int d\vec{F_3}\\  \\
&=\hat{j}\int^{L}_{0}IB\;dx\\  \\
\vec{F_3}&=\hat{j} IBL
\end{align}$$

En equilibrio se cumple que: 

$$\begin{align}
\vec{F_3}-m\vec{g}&=0\\  \\
IBL&=m\vec{g}\\  \\
I&=\frac{mg}{BL}
\end{align}$$




## Fuerza sobre una corrienta volumétrica 

Anteriormente se había llegado que $\vec{J}=\rho\vec{v}$. Por lo tanto, es posible expresar lo siguiente: 

$$\begin{align}
\vec{F}&=\int dq\vec{v}\times\vec{B}\\  \\
&=\int\rho\;d\vec{c}\;\vec{v}\times\vec{B}\\  \\
&=\int\rho\vec{v}\times\vec{B}\;d\vec{c}\\  \\
&=\int\vec{J}\times\vec{B}\;d\tau'
\end{align}$$


#### Ejemplo 

Se tiene una lamina con densidad de carga superficial $\sigma$ y velocidad $\vec{v}$.

![[Captura de pantalla 2023-10-06 a la(s) 09.28.29.png|center]]

Por lo tanto, notemos que el largo llegaría a ser $ds=v\;dt\;dl_\perp$. Entonces: 

$$\begin{align}
dq&=ds\sigma\\  \\
&=v\;dt\;dl_\perp\sigma\\  \\
&=v\sigma\;dl_\perp\;dt\\  \\
\frac{dQ}{dt}&=v\sigma\;dl_\perp 
\end{align}$$

Podemos definir una densidad de corriente superficial: 

$$\vec{K}=\sigma\vec{V}$$

Entonces, es posible escribir la ecuación de la fuerza en términos de $\vec{K}$. 

$$\begin{align}
\vec{F}&=\int\vec{K}\times\vec{B}\;ds
\end{align}$$

