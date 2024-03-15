
Al pasar corriente por un elemento de circuito, se disipa energía y se produce calor. Esto va acorde a la [[Segunda ley de la termodinámica|segunda ley de la termodinámica]]. 

Asumiendo que existe una intensidad de corriente en un circuito, se puede llegar a la siguiente definición: 

$$I=\frac{\Delta q}{\Delta t}\implies\Delta q=I\cdot\Delta t$$

Donde $\Delta q$ es la carga que se mueve entre dos puntos arbitrarios en un tiempo $\Delta t$. Inicialmente la carga está en un punto $A$ y tiene una [[energía potencial]] eléctrica: 

$$\begin{align}
U_A&=\Delta q\cdot V_A\\  \\
U_B&=\Delta q\cdot V_B 
\end{align}$$

Si la resistencia disipa energía $E$, podemos escribir la conservación en función de la potencia disipada $P$: 

$$E=P\cdot\Delta t\tag{Energía disipada}$$

Además, sabemos que: 

$$\begin{align}
U_A&=U_B+E\\  \\
\Delta q\cdot V_A&=\Delta q\cdot V_B+P\Delta t\\  \\
\Delta q(V_A-V_B)&=P\Delta t\\  \\
V&=V_A-V_B\tag{Caída de potencial en R}
\end{align}$$

Por lo tanto, nos va a quedar que: 

$$\begin{align}
P&=\frac{\Delta q}{\Delta t}\cdot V\\  \\
VI&=P
\end{align}$$

Usando la [[Departamento de Física/Electromagnetismo/Corrientes estacionarias/Ley de Ohm|Ley de Ohm]], donde $V=RI$, llegamos, finalmente: 

$$P=RI^2=\frac{V^2}{R}\tag{Potencia disipada}$$

Normalmente conocido como **ley de Joule**. 