
>[!error] Corriente estacionaria 
>
>Sabemos que la [[Corriente eléctrica|corriente]] equivale a las cargas en movimiento. Por el otro lado, una **corriente estacionaria** se puede describir con un [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo]] de velocidad $\vec{V}(\vec{r})$ que **no depende del tiempo**. 

Todo esto, generan **lineas de corriente**, parecidas al concepto de lineas de campo o de fluido. 
![[campoCorriente.png|center|500]]
Por lo tanto, se puede definir la corriente como **la cantidad de carga que transcurre en el tiempo**, vale decir, matemáticamente se puede relacionar como: 

$$I=\frac{dQ}{dt}=\frac{\text{Carga}}{\text{Tiempo}}\tag{Ampere}$$


## Variación de corriente a través de una superficie 

Ahora, podríamos definirnos una superficie que está sometida a un flujo de corriente y definirnos un diferenciar de superficie infinitesimal $dS$. 

Ahora, la pregunta a hacer es cual es la variación de corriente que atraviesa esta superficie en un tiempo $dt$. 

![[surface_portion.png|center|400]]
Por ejemplo, si tengo la siguiente superficie y asumimos que la planilla son pedazos infinitesimales $dS$, queremos obtener el flujo de corriente representado en morado en un intervalo de tiempo.  

```tikz 
\begin{document}
\begin{tikzpicture}[scale=1.5]
    % Dibujar la superficie
    \draw[fill=gray!20] (0,0) to[bend left] (4,2) to[bend right] (8,0) -- (4,-2) to[bend left] cycle;
    \node at (4,0) {$S$};
    % Dibujar el flujo de corriente
    \foreach \x in {0,1,...,8} {
        \draw[->,blue] (\x,-3) -- (\x,3);
    }
    \node[blue] at (9,2) {$\vec{v}$};
    % Dibujar el diferencial de superficie
    \draw[fill=red!20] (3.5,0.5) to[bend left] (4.5,1.5) to[bend right] (5.5,0.5) -- (4.5,-0.5) to[bend left] cycle;
    \node[red] at (4.5,1.8) {$dS$};
    % Dibujar el ángulo theta
    \draw[dashed] (4.5,-0.5) -- (4.5,2);
    \draw[<->] (4.6,1) arc (90:135:1);
    \node at (4.2,1.3) {$\theta$};
    % Dibujar la altura h
    \draw[<->] (6,-2) -- node[right] {$h$} (6,0);
    % Dibujar la profundidad p
    \draw[<->] (8,-3) -- node[below] {$p$} (9,-3);
\end{tikzpicture}
\end{document}
```

Notemos que el diferencial de carga se puede expresar como: 

$$\begin{align}
dQ&=\left(\text{Volumen}\right)\cdot\rho\\  \\
&=(v\cdot dt)\cdot dp\cdot dh\cos\theta\cdot\rho\\  \\
\frac{dQ}{dt}&=\rho dp\;dh\cdot v\cos\theta\\  \\
&=ds\cdot v\cos\theta\\  \\
&=\rho\vec{v}\cdot d\vec{s}
\end{align}$$

Algunas observaciones del cálculo: 

- $dQ$ es un elemento diferencial de carga que pasa por un área infinitesimalmente pequeña en un tiempo $dt$.

- $v \cdot dt$ es una distancia infinitesimal que el fluido recorre en un tiempo $dt$. Esta es la distancia que el fluido fluye en esa pequeña cantidad de tiempo.

-  $dh$ es la variación de la altura si miramos la superficie desde el lado

- $\cos\theta$ ajusta el área para tener en cuenta la dirección del flujo con respecto a la superficie.

- $dp$ es la dimensión perpendicular al flujo de la corriente (por ejemplo, podría ser un "ancho" infinitesimalmente pequeño).

- $\rho$ es la densidad de carga del fluido, es decir, cuánta carga hay por unidad de volumen.

 Por ende, se llega a la siguiente igualdad: 

$$dI=\frac{dQ}{dt}=\rho\vec{V}\cdot d\vec{s}$$ 
Notemos que $\rho\vec{V}$ lo podemos definir como **densidad de corriente vectorial**, y por consiguiente, lo podemos definir como un vector: 

$$\vec{J}=\rho\vec{V}$$

En conclusión, la **corriente que cruza una superficie cualquiera en un tiempo dado**, se tiene la siguiente igualdad: 

$$dI=\vec{J}\cdot d\vec{s}$$ 
Y para poder llegar a la corriente, simplemente se integra: 

$$I=\int_S\vec{J}\cdot d\vec{s}$$ 
Notemos que la densidad de corriente, por lo general se define en función de variables de posición y tiempo ($\vec{r},\vec{t}$), pero en el caso estacionario solo depende de la [[Posición|posición]].  