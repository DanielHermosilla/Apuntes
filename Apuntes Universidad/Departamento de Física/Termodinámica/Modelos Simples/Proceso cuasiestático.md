
Este es un concepto supérfumo. 

>[!tip] Proceso cuasiestático 
>
>Aquel proceso en que el estado inicial, el estado final y todos los estados intermedios son de equilibrio. 

Este concepto solo sirve en el mundo de la [[Termodinámica|termodinámica]]. No existe *en el mundo real*. 

## Aproximación al proceso cuasiestático 

Notemos que es posible tratar de aproximarse al proceso cuasiestático al *"ralentizar"* el proceso. Pero notar que esto sería un **proceso diferente**. 

![[Pasted image 20230926145843.png|center]]

## Curva en el plano P-V 

Todo estado de equilibrio es un punto en el plano $P-V$. Por lo tanto, todo proceso es cuasiestático y que lleva el sistema de un estado $1$ al $2$ **es una curva continua** en el plano $P-V$. 

#### Ejemplo 

Se tiene una válvula que se abre ligeramente de modo que el [[Sistemas|sistema]] se expande $\Delta V$ y se cierra de nuevo. Calcular $W_\text{cuasistático}$ realizado por el medio sobre el sistema. 

![[Pasted image 20230926150537.png|center]]

Tomamos como medio el émbolo ideal y el sistema todo el gas en ambos cilindros y en el capilar. 

Notemos que el trabajo es la energía intercambiada entre el medio y el sistema a través de la frontera entre ambos. En este caso, el émbolo sería la frontera del sistema. Notemos que una buena aproximación sería asumir que el émbolo está en equilibrio. Entonces: 

$$\begin{align}
W&=\int^{f}_{i}-P\;dV\\  \\
&=\int^{f}_{i}-P_0\;dV\\  \\
&=-P_0\int^{f}_{i}dV\\  \\
W&=-P_0(V_f-V_i)
\end{align}$$

Pero notemos que no es cuasiestático, ya que todos los procesos intermedio son de equilibrio y la presión va variando. **Pero**, esta variación no cuasiestática es **externa a la interacción del medio con el sistema**, entonces, es válido el cálculo. 

