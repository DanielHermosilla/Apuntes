
Se quiere producir algo para generar demanda y hay que guardar la producción en un inventario. Existe un costo por guardar las cosas en inventario, por producir cosas, etc. 

La idea es minimizar los **costos de producción** para satisfacer la **demanda**.

Los periodos de demanda se dividen por $T$ intervalos: $d_1,d_2,\dots, d_T$. 

Producir una caja en el periodo $t$ cuesta $p_t$. El costo de producir en el período $t$ es $c_t$. El costo de inventario del periodo $t$ al $t+1$ por caja es $h_t$. Se comienza con un inventario $I_0$. 

### Solución 

Nos definimos $x_t$ como la cantidad para producir en $t$. $x_t$ es **no negativo** y podría ser tanto continuo o discreto dependiendo del producto. 

Si se produjiera todos los dias la demanda, entonces el costo sería: 

$$\sum^{T}_{t=1}(c_t+p_tD_t)$$

Por el otro lado, si se produjiera todo en $t=1$: 

$$c_1+p_1\left(\sum^{T}_{t=1}D_t\right)+\sum^{T-1}_{t=1}h_t\left(\sum^{T}_{s=t+1}D_s\right)$$

Por lo tanto, nos definimos las siguientes variables: 

$$\begin{align}
y_t\in\lbrace 0,1\rbrace&\;\;\;\;\text{Se produce en el período}\;t\\  \\
x_t\geq 0&\;\;\;\;\text{Cantidad producida en}\;t\\  \\
I_t\geq 0&\;\;\;\;\text{Inventario de}\;t\;\text{a}\;t+1
\end{align}$$

Además, el inventario se puede definir como: 

$$I_t=I_{t+1}+x_t-D_t\;\;\;t\in\lbrace 1,\dots, T\rbrace$$

Además, 

$$x_t\leq M\cdot y_T$$

Con $M$ una constante  

Así, la función objetivo llegaría a ser la siguiente: 

$$\min\sum^{T}_{t=1}(c+y_t+p_tx_t)+\sum^{T-1}_{t=1}h_tI_t$$

El 