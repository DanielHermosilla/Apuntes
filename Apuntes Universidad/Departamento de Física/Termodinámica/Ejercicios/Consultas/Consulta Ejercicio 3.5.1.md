
Se tienen $N$ moléculas ideales que ocupan una caja que se divide imaginariamente en dos partes iguales. 

4. Mostrar que si $m=N/2+\Delta$, donde $\Delta$ es pequeño en relación a $N$, entonces 

$$P(\Delta)=\left(\frac{2}{N\pi}\right)^{1/2}\exp\frac{-2\Delta^2}{N}$$

Ocupando la aproximación de Stirling en la forma: 

$$\ln(n!)=\frac{1}{2}\ln(2\pi)+(n+1/2)\ln(n)-n$$

### Respuesta 

Sea $X\sim\text{Binom}(N,\frac{1}{2})$ la variable aleatoria que determina la cantidad de moléculas que se encuentran en un lado de la caja. Por lo tanto, para $X=N/2+\Delta$ se tiene que: 

$$P(N/2+\Delta)=\binom{N}{N/2+\Delta}\left(\frac{1}{2}\right)^{2(N/2+\Delta}$$


Como es un sistema de moléculas ideal, la probabilidad es independiente, por lo tanto:

$$P(N/2)\cdot P(\Delta)=\binom{N}{N/2+\Delta}\left(\frac{1}{2}\right)^{2(N/2+\Delta)}$$


Ahora, notar que con la misma variable aleatoria se tiene que $P(N/2)$ equivale a: 

$$\begin{align}
P(N/2)&=\binom{N}{N/2}\left(\frac{1}{2}\right)^{N}\\  \\
&=\frac{N!}{\frac{N}{2}!\frac{N}{2}!}\left(\frac{1}{2}\right)^{N}
\end{align}$$

Por lo tanto, 