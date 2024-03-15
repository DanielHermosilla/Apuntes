
Podemos suponer un circuito donde se tiene una fuente de poder. Sabemos que en la fuente de poder tenemos una [[Diferencia de potencial|diferencia de potencial]], donde un extremo tiene potencial $V_E=0$ y el otro $V_D=V$. Sabemos que esta diferencia de potencial genera un [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] que no permite "pasar" las cargas libres por la bateria. 

Sin embargo, existe un [[Departamento de Física/Mecánica/Energía/Trabajo|trabajo]] denominado como **fuerza electromotriz** que hace que las cargas puedan pasar: 
$$\vec{f_s}+\vec{E}=0$$

Si descomponemos el [[Potencia eléctrica|potencial]]: 

$$\begin{align}
V&=\int^{a}_{b}\vec{E}\cdot d\vec{l}\\  \\
&=\int^{b}_{a}\vec{f_s}\;\cdot d\vec{l}
\end{align}$$

Como la fuerza electromotriz es nula fuera de la bateria, se llega que: 

$$\begin{align}
V&=\int^{b}_{a}\vec{f_s}\cdot d\vec{l}\\  \\
	&=\oint\vec{f_s}\cdot d\vec{l}=\epsilon\tag{Definición de fuerza electromotriz} 
\end{align}$$

```tikz

\usepackage{tikz}
\usepackage{amsmath}

\begin{document}

\begin{tikzpicture}[scale=1.5]

% Batería
\draw[thick] (0,0) -- (0,2);
\draw[thick] (1,0) -- (1,2);
\draw (0.5,2) node[above] {$V_D = V$};
\draw (0.5,0) node[below] {$V_E = 0$};
\draw[->, red, thick] (0.7,1.5) -- (0.7,0.5) node[midway,right] {$\vec{E}$};
\draw[->, blue, thick] (0.3,0.5) -- (0.3,1.5) node[midway,left] {$\vec{f_s}$};

% Leyendas
\node[text width=6cm, right] at (3,1) {
\textbf{Descomposición del potencial:}
\[ V = \int^{a}_{b} \vec{E} \cdot d\vec{l} \]
\[ V = \int^{b}_{a} \vec{f_s} \cdot d\vec{l} \]
\textbf{Definición de fuerza electromotriz:}
\[ V = \int^{b}_{a} \vec{f_s} \cdot d\vec{l} \]
\[ V = \oint \vec{f_s} \cdot d\vec{l} = \epsilon \]
};

\end{tikzpicture}

\end{document}
```
## Batería en un circuito y leyes de Kirchoff 

Una batería ideal es una bateria donde no se considera la [[Segunda ley de la termodinámica|segunda ley de la termodinámica]], vale decir, no se considera que hay disipaciones de [[Energía|energía]]. Sin embargo, en la vida real, se considera una [[Departamento de Física/Electromagnetismo/Corrientes estacionarias/Ley de Ohm|resistencia]] interna, donde existe disipación. 

En un circuito real, se acumula carga y cambiaría el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] y el [[Potencia eléctrica|potencial eléctrico]]. Pero esto no iría acorde a la [[Trabajo y Energía en Electrostática|electrostática]], por lo tanto, se postula la **ley de Kirchoff de corriente**:  

$$\sum I_\text{in}=\sum I_\text{out}\tag{Primera ley de Kirchoff}$$

Además, recordando que hay cargas moviendose en un camino cerrado, segun la [[Ley de Gauss|ley de Gauss]] se tiene lo siguiente: 

$$-\oint\vec{E}\cdot d\vec{l}=0$$

Por lo tanto, se postula la segunda **ley de Kirchoff de voltajes**: 

$$\sum V_i=0\tag{Segunda ley de Kirchoff}$$


Por lo tanto, la corriente en el circuito se define como: 

$$I=\frac{\epsilon}{R_i+R}$$

Donde, al ocupar la [[Departamento de Física/Electromagnetismo/Corrientes estacionarias/Ley de Ohm|Ley de Ohm]], se llega que: 

$$\begin{align}
V_R&=IR\\  \\
&=\frac{R}{R_i+R}\epsilon<\epsilon\;\;\;\;\;\;\;R_i>0
\end{align}$$

Notemos que $V_R=\epsilon$ solo en $R_i=0$, pero eso no existe por la definición anterior. 