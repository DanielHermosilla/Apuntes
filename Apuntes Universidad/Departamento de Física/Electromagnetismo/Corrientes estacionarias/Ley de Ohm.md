
Por la definición de [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] sabemos que al multiplicar el campo por una carga existe una fuerza, vale decir: 

$$\vec{F}=q\vec{E}$$

Ahora, si aplicamos el concepto de [[Corriente estacionaria|densidad de corriente vectorial]] a esta definición, se cumple que: 

$$\vec{J}=g\vec{E}$$ 
Donde $g$ es la conductividad del material y $\eta=\frac{1}{g}$ es la resistividad del material. Esta es una forma de expresar la Ley de Ohm de forma microscópica. 

La intuición de esto nace de la definición de fuerza, precisamente de las leyes de Newton: 

$$\begin{align}
\vec{F}&=q\vec{E}\\  \\
m\vec{a}&=q\vec{E}\\  \\
\vec{a}&=\frac{q}{m}\vec{E}
\end{align}$$

Esto nos dice que las cargas **tienen una [[Aceleración|aceleración]]**. Si las cargas fueran libre, la velocidad sería proporcional a $\vert\vec{V}\vert\approx\frac{1}{2}at^2$. Pero en realidad, las cargas no completamente libres por los choques que hacen entre ellas. 

```tikz 

\usepackage{tikz}
\usepackage{pgf}

\begin{document}

\begin{tikzpicture}[scale=1]
    % Dibujar el campo eléctrico
    \foreach \x in {-4,-2,...,4} {
        \foreach \y in {-4,-2,...,4} {
            \draw[->,red] (\x,\y) -- (\x+1,\y);
        }
    }
    \node[red] at (6,4) {$\vec{E}$};

    % Dibujar las cargas
    \foreach \i in {1,...,10} {
        % Generar una posición aleatoria
        \pgfmathsetmacro{\x}{rand*4}
        \pgfmathsetmacro{\y}{rand*4}
        
        % Dibujar la carga
        \draw[fill=blue] (\x,\y) circle (0.2);
        
        % Dibujar la velocidad
        \draw[->,blue] (\x,\y) -- ++(rand*0.5,rand*0.5);
        
        % Dibujar la aceleración
        \draw[->,green] (\x,\y) -- ++(1,0);
    }
    \node[blue] at (-6,4) {Cargas};
    \node[green] at (-6,-4) {Aceleración};

    % Dibujar los choques
    \foreach \j in {1,...,5} {
        % Generar dos posiciones aleatorias
        \pgfmathsetmacro{\xa}{rand*4}
        \pgfmathsetmacro{\ya}{rand*4}
        \pgfmathsetmacro{\xb}{rand*4}
        \pgfmathsetmacro{\yb}{rand*4}
        
        % Dibujar las cargas que chocan
        \draw[fill=yellow] (\xa,\ya) circle (0.2);
        \draw[fill=yellow] (\xb,\yb) circle (0.2);
        
        % Dibujar la línea que une las cargas que chocan
        \draw[dashed,yellow] (\xa,\ya) -- (\xb,\yb);
    }
    \node[yellow] at (6,-4) {Choques};
\end{tikzpicture}

\end{document}
```


Por lo tanto, vamos a considerar el tiempo medio de choque $t_\text{med}$. De tal forma, se tiene lo siguiente para la [[Velocidad|velocidad]]: 

$$\begin{align} 
\vec{V}&\sim\vec{a}\cdot t_\text{med}\\ \\ 
\vec{V}&\sim\frac{q}{m}t_\text{med}\cdot\vec{E}\\ \\ 
\vec{J}&=\rho\vec{v}\sim\left(\frac{\rho\cdot q\cdot t_\text{med}}{m}\right)\cdot\vec{E}
\end{align}$$ 
A partir de este cálculo se obtiene la ley de Ohm de forma cualitativa. 

## Versión macroscópica de la Ley de Ohm

Podemos asumir un [[Conductores eléctricos|conductor]] con una [[Potencia eléctrica|diferencia de potencial]] $V$, conductividad $g$ y una carga $Q$, se tiene un [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] uniforme a través de la superficie.


```tikz 
\usepackage{tikz}

\begin{document}

\begin{tikzpicture}[scale=1.5]
    % Dibujar el cilindro
    \draw (0,0) -- (4,0) -- (4,4) -- (0,4) -- cycle;
    \draw[fill=gray!20] (0,0) arc (180:360:2 and 0.5);
    \draw[fill=gray!20] (0,4) arc (-180:0:2 and 0.5);
    
    \node at (2,2) {$Q$};

    % Dibujar la diferencia de potencial
    \draw[<->] (-1,0) -- node[left] {$V$} (-1,4);

    % Dibujar la conductividad
    \node at (-0.5,2) {$g$};

    % Dibujar el campo eléctrico
    \foreach \x in {0.5,1.5,...,3.5} {
        \draw[->,red] (\x,1) -- ++(0,1);
    }
    \node[red] at (4.5,2) {$\vec{E}$};

    % Dibujar el largo del conductor
    \draw[<->] (5,0) -- node[right] {$l$} (5,4);
\end{tikzpicture}

\end{document}

```

 Si nos definimos el largo del conductor como $l$, podemos definir el campo uniforme como: 
 
$$\vec{E}=\frac{V}{l}\hat{k}$$

A partir de la definición inicial, se llega a la siguiente equivalencia: 

$$\vec{J}=g\frac{V}{l}\hat{k}$$

Por lo tanto, haciendo cálculos: 

$$\begin{align}
I&=\int\vec{J}\cdot d\vec{s}\\  \\
&=\vec{J}\cdot A\hat{k}\\   \\
&=\frac{g\;v}{l}\hat{k}\cdot A\hat{k}\\  \\
&=g\frac{A}{l}\cdot V\\  \\
V&=\left(\frac{l}{A}\frac{1}{g}\right)\cdot I
\end{align}$$

Por lo tanto, se define la resistencia del conductor como: 

$$V=RI$$

Y, por los cálculos anteriores, **la resistencia llegaría a ser**: 

$$R=\frac{1}{g}\cdot\frac{l}{A}$$

