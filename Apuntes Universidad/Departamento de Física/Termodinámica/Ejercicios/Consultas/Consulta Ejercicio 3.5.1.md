
Se tienen $N$ moléculas ideales que ocupan una caja que se divide imaginariamente en dos partes iguales. 

4. Mostrar que si $m=N/2+\Delta$, donde $\Delta$ es pequeño en relación a $N$, entonces 

$$P(\Delta)=\left(\frac{2}{N\pi}\right)^{1/2}\exp\frac{-2\Delta^2}{N}$$

Ocupando la aproximación de Stirling en la forma: 

$$\ln(n!)=\frac{1}{2}\ln(2\pi)+(n+1/2)\ln(n)-n$$

### Respuesta 

Sea $X\sim\text{Binom}(N,\frac{1}{2})$ la variable aleatoria que determina la cantidad de moléculas que se encuentran en un lado de la caja. Por lo tanto, para $X=N/2+\Delta$ se tiene que: 

$$P(N/2+\Delta)=\binom{N}{N/2+\Delta}\left(\frac{1}{2}\right)^{2(N/2+\Delta)}$$

Por lo tanto, desarrollando el binomio: 

$$\begin{align}
P(N/2+\Delta)&=\frac{N!}{(N/2+\Delta)!(N/2+\Delta)!}\left(\frac{1}{2}\right)^{N+2\Delta}\\\\
\ln\left(P(N/2+\Delta)\right)&=\ln\left(\frac{N!}{(N/2+\Delta)!(N/2+\Delta)!}\left(\frac{1}{2}\right)^{N+2\Delta}\right)\\\\
&=\ln(N!)-\left[\ln\left((\frac{N}{2}+\Delta)!\right)+\ln\left((\frac{N}{2}+\Delta)!\right)+(N+2\Delta)\ln(2)\right]\\\\
&=\ln(N!)-\left[2\ln\left((\frac{N}{2}+\Delta)!\right)+(N+2\Delta)\ln(2)\right]\\\\
&=\frac{1}{2}\ln(2\pi)+(N+1/2)\ln(N)-N-\left[2\ln\left((\frac{N}{2}+\Delta)!\right)+(N+2\Delta)\ln(2)\right]\\\\
\text{Sea}\; H&=\frac{N}{2}+\Delta\\\\
&=\frac{1}{2}\ln(2\pi)+(N+1/2)\ln(N)-N-\left[2(\frac{1}{2}\ln(2\pi)+(H+\frac{1}{2})\ln(H)-H\right]H!\ln(2)\\\\
\end{align}$$






