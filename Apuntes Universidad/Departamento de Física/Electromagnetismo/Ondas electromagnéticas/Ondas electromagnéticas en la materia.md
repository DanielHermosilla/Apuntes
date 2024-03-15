
Haciendo el caso análogo para las [[Ondas electromagnéticas|ondas electromagnéticas]] en el vacio, se trataba con las constante $\epsilon$ y $\mu$. Ahora, como se trabaja en la materia, las variables pasan a ser las siguientes: 

$$\begin{align}
\epsilon_0&\to\epsilon\\  \\
\mu_0&\to\mu  
\end{align}$$

Así, la velocidad pasa a ser la siguiente: 

$$\begin{align}
v&=\frac{1}{\sqrt{\epsilon\mu}}\\  \\
&=\frac{1}{\sqrt{\epsilon_0\mu_0}}\sqrt{\frac{\epsilon_0\mu_0}{\epsilon\mu}}\\  \\
&=c\frac{1}{n}<c\\ \\
n&=\frac{\epsilon\mu}{\epsilon_0\mu_0}
\end{align}$$

Así, el valor $n$ que es siempre menor que la velocidad de la luz, se llama **índice de refracción**. A partir de esto, se cumple todo lo relacionado con ley de Snell y refracción. Esto ayuda a ver las **condiciones de borde de las ondas electromagnéticas**. De igual forma, haciendo un recuerdo de las leyes de la refracción: 

1. Se cumple la siguiente relación con los números de onda: 

$$k_l\sin\theta_l=k_r\sin\theta_R$$

Donde $\theta_l$ es en ángulo de refracción y $\theta_R$ el ángulo reflejado. 

2. El ángulo de incidencia es igual al ángulo de reflexión: 

$$\theta_l=\theta_R$$

3. La ley de Snell: 

$$\frac{\sin\theta_T}{\sin\theta_l}=\frac{n_1}{n_2}$$


Todo esto subyace de analizar el caso arbitrario de incidencia: 

![[Pasted image 20231127090143.png|center|550]]

Donde las ondas incidentes llegarían a ser: 

$$\begin{align}
E_l(z,t)&=E_0e^{i(k_lz-\omega t)}\\  \\
B_l(z,t)&=\frac{1}{v_1}E_{0}e^{i(k_lz-\omega t)}
\end{align}$$

Ahora, para la onda transmitida se tiene que: 

$$\begin{align}
E_T(z,t)&=E_Te^{i(k_zz-\omega t)}\hat{x}\\  \\
B_T(z,t)&=\frac{1}{v_2}E_Te^{i(kz-\omega t)}\hat{y}
\end{align}$$

Donde $v_2$ es la velocidad en el medio $2$. Notemos que $\omega$ y polarización es la misma para cumplir la condición de borde en todo tiempo. 

Por último, para la onda reflejada se tiene que: 

$$\begin{align}
E_r(z,t)&=E_Re^{i(-k_1z-\omega t)}\hat{x}\\  \\
B_r(z,t)&=-\frac{1}{v_1}E_Re^{i(-k_1z-\omega t)}\hat{y}
\end{align}$$

## Condiciones de borde 

Dado que se propone la ley de Snell, se llegan a las siguientes ecuaciones de continuidad: 

$$\begin{align}
\epsilon_1E_{1}^{\perp}&=\epsilon_2E_{2}^{\perp}\\  \\
E_{1}^{\parallel}&=E_{2}^{\parallel}\\  \\
B_{1}^{\perp}&=B_{2}^{\perp}\\  \\
\frac{1}{\mu_1}B_{1}^{\parallel}&=\frac{1}{\mu_2}B_{2}^{\parallel}
\end{align}$$

Juntando las condiciones de borde y la ecuación de la onda: 

$$\begin{align}
E_I+E_R&=E_T\\  \\
E_Ie^{-i\omega t}+E_Re^{-i\omega t}&=E_Te^{-i\omega t}
\end{align}$$

Esto implica directamente que **$\omega$ debe ser igual para todo tiempo**. En otras palabras, **la frecuencia angular se conserva**. Si se sigue haciendo el análisis para cada condición de borde se llega a lo siguiente: 

$$\begin{align}
E_R&=\left(\frac{1-\beta}{1+\beta}\right)E_I\\  \\
E_T&=\left(\frac{2}{1+\beta}\right)E_I
\end{align}$$

Donde $\beta=\mu_1v_1/\mu_2v_2=\mu_1n_2/\mu_2n_1$. Aunque por lo general se hacen las siguientes aproximaciones: 

$$\begin{align}
\mu_1&\approx\mu_2\approx\mu_0\\  \\
\beta&=\frac{\mu_1n_2}{\mu_2n_1}\approx\frac{n_2}{n_1}
\end{align}$$

Así, se llega a la siguiente equivalencia: 

$$\begin{align}
E_R&=\left(\frac{n_1-n_2}{n_1+n_2}\right)E_I\\  \\
E_T&=\left(\frac{2n_1}{n_1+n_2}\right)E_I
\end{align}$$

Así, por último, se define la onda reflejada y transmitida como: 

$$\begin{align}
R&=\left(\frac{n_1-n_2}{n_1+n_2}\right)^2\\  \\
T&=\frac{4n_1n_2}{(n_1+n_2)^2}
\end{align}$$

## Condiciones de borde para medios oblicuos 

Haciendo el análisis análogo para el caso oblicuo, donde se tiene una frecuencia angular constante y velocidad. 