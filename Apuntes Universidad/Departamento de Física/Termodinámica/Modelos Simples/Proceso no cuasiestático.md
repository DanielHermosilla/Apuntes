
Acordándonos que la frontera de un [[Sistemas|sistema]] es la interacción que tiene con el medio, entonces, analizamos el caso cuando la frontera está en **equilibrio [[Temperatura absoluta|térmico]]**. Por el otro lado, hay procesos fuera del equilibrio al interior del sistema y se crea entropía dentro de ella. 

Como sabemos que la variación de [[Entropía|entropía]] se define como: 

$$dS=\frac{q}{T}\tag{Transferencia}$$

Por lo tanto, se llega que: 

$$dS=\frac{q}{T}+\delta S_\text{Irreversible}$$

Donde $\delta S_\text{Irreversible}$ es la entropía creada debido a proceso irreversibles dentro del sistema. 

Analizando la entropía irreversible, notamos que: 

$$\begin{align}
dS&>\frac{q}{T}\\  \\
q&<TdS
\end{align}$$

Entonces, aplicando la definición de variación de [[Energía|energía]]: 

$$dE=q+w$$

Se llega que: 

$$\begin{align}
dE&=\left(\cancelto{T}{\frac{\partial E}{\partial S}}\right)dS+\left(\cancelto{-P}{\frac{\partial E}{\partial V}}\right)dV\\  \\
dE&= TdS-PdV\\  \\
dE&= q + w
\end{align}$$

Pero, como $q\neq TdS$ y $w\neq -PdV$, implica que $q<TdS$ y $w>-PdV$. 

Notemos la diferencia con el proceso [[Proceso cuasiestático|cuasiestático]], donde se hubiera tenido los siguientes valores: 

$$\begin{align}
w&=-PdV\\  \\
q&=TdS
\end{align}$$

Por lo tanto, en **margenes generales**, es posible formalizar con desigualdades: 

$$\begin{align}
w&\geq -PdV\\  \\
q&\leq TdS
\end{align}$$