
Dado un estado [[Sistema macroscópico|macroscópico]] y en [[Departamento de Física/Termodinámica/Equilibrio|equilibrio]], entonces se puede determinar $\Omega$ en función de $E,V,M,T,N,P$. 

Luego, se puede determinar la **entropía** del sistema bajo la constante de Boltzmann: 

$$S=k_b\ln\Omega$$

La entropía se puede definir como la [[Pérdida de información|pérdida de información]] en función de las variables macroscópicas. Esto está definida para un sistema en equilibrio. 

Otra forma de definirla es de la siguiente manera, dado una [[Variable aleatoria discreta|variable aleatoria]] $X$, su entropía es: 

$$S(X)=-\sum^{n}_{i=1}K\cdot\mathbb{P}(x_i)\cdot\ln(\mathbb{P}(x_i))$$

#### Ejemplo 

Si se hace el ejercicio de pensar una molécula en una caja, entonces se podría decir que su configuración es $\Omega\approx\text{Cte}\cdot V$. Ahora, si se llegase a ampliar el volumen de la caja y se agregase otra molécula, al ser independientes, se tendría que $\Omega_2=\Omega_1\cdot\Omega_1=\text{Cte}^2V^2$. Ahora, para el caso de $N$ moléculas, se puede llamar la constante como $C$ y se llega que $\Omega_n=CV^N$. Si a esto lo llevamos al término de entropía: 

$$\begin{align}
S&=k\ln\Omega_n\\  \\
&=k\ln(CV^n)\\  \\
&=\cancelto{S_0}{k\ln C}+Nk\ln V\\  \\
S&=S_0+Nk\ln V
\end{align}$$

Por lo tanto, la entropía en cierto sentido depende de la cantidad de moléculas y el volumen. 

Si vemos el siguiente problema, donde ocurre una expansión de volumen al doble, se podría calcular la **expansión de entropía**. 

![[Captura de pantalla 2023-08-18 a la(s) 11.25.29.png|center|350]]

Llegamos que: 

$$\begin{align}
\Delta S&=S_{\text{final}}-S_{\text{inicial}}\\  \\
&=\left[\cancel{S_0}+Nk\ln 2 + \cancel{Nk\ln V}\right]-\left[\cancel{S_0}+\cancel{Nk\ln V}\right]\\  \\
\Delta S&=Nk\ln 2
\end{align}$$

A través de esto, se puede ver que la constante no importa en realidad. Ahora, si el cambio fuera de un mol de partículas, donde definimos $N_a\cdot k=R$, entonces: 

$$\Delta S=R\ln 2$$

Esto sería equivalente a, aproximadamente, $6\cdot 10$ bits.