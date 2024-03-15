
Para el gas ideal se asumira un *modelo de jugete*, considerando un sistema de $N$ partículas encerradas en un volumen $V$, se imponen las siguientes hipótesis: 

1. Las interaccinoes entre partículas son tan débiles para ser despreciadas. 
2. El volumen de las moléculas es despreciable, se consideran puntuales. 
3. Las partículas son iguales e indistinguibles. 

### Separación del número de configuraciones accesibles $\Omega$ 

Para determinar el número de configuraciones accesibles, es notorio notar que el estado [[Sistema macroscópico|macroscópico]] lo define el número de [[Partícula|partículas]] ($N$), el volumen ($V$) y la energía ($E$). Por lo tanto, existen las configuraciones a través de $3N$ coordenadas y $3N$ momentos.  

Notemos que el hecho que las partículas no interactuen significa que la energía no se ve alterada, entonces las asignaciones de momentos es independiente: 

$$\Omega=\Omega_E\Omega_V$$
### Energía del gas 

Ahora notemos que la energía de cada molécula es puramente cinética, entonces la energía total llegaría a ser: 

$$E=\sum^{N}_{i=1}\frac{1}{2m}\vec{p_{i}^{2}}$$

Donde $\vec{p}$ es el momento de cada partícula, suma que contiene $3N$ términos si consideramos las dimensiones $x,,y,z$ del gas ideal. De igual forma, siempre es posible realizar los cambios de variable: 

$$\omega_1=\frac{p_{1,x}}{(2m)^{1/2}}$$

Y asi, sucesivamente, variando los subíndices de $p$. Por ende, la energía se puede reducir a la ecuación como: 

$$E=\sum^{3N}_{i=1}\omega_{i}^{2}$$ 
Notemos que el espacio $\omega_i$ en realidad es el espacio de la ecuación de una hiperesfera en $3N$ dimensiones de radio $r=E^{1/2}$. La superficie de esta esféra se determina por: 

$$\frac{2\pi^{3N/2}r^{3N-1}}{\tau(3N/2)}$$

Donde $\tau$ es la [[Función Gamma|función Gamma]]. Aun así, lo importante es saber que la **superficie es proporcional a $r^{3N-1}$**. Dado que se estudia el estado [[Sistema macroscópico|macroscópico]], entonces la superficie es de la forma $\text{cte}\times r^{3N}=\text{cte}\times E^{3N/2}$. 

Por conclusión, la magnitud de $\Omega_E$ es el modo de asignar los distintos momentos (vale decir, los $3N\;\omega_i$) donde el vector de la energía cinética se mueve por la hipersuperficie de la hiperesfera. Entonces, $\Omega_E$ es proporcional a dicha superficie: 

$$\Omega_E=KE^{3N/2}$$

Con $K$ una constante conocida. 

### Entropía 

Dado que se tiene el valor de los tres parámetros macroscópicos, es posible calcular la [[Entropía|entropía]] aplicando la definición: 

$$S=\frac{3Nk_B}{2}\ln(E)+Nk_B\ln(V)-k_B\ln(N!)+C'$$ 
Donde $C'=k_B\ln(C)$ es una constante. Lo apropiado para que el logaritmo tenga unidades adimensionales es asumir que los argumentos tienen valores fijos. Al estado de valores fijos se le llamará $S_O$, cuya resta con la entropía $S$ representará el cambio de entropía entre estados: 

$$S-S_O=\frac{3Nk_B}{2}\ln\left(\frac{E}{E_0}\right)+Nk_b\ln\left(\frac{V}{V_0}\right)$$


Ahora, si se quisiera generalizar aun más, podríamos notar lo siguiente: 

$$S-S_O=\frac{3\mathbf{R}k_B}{2}\ln\left(\frac{E}{E_0}\right)+Nk_b\ln\left(\frac{V}{V_0}\right)$$

Donde $\mathbf{R}$ son los grados de libertad. 

### Temperatura del gas ideal 

Si se aplica la definición de [[Temperatura absoluta|temperatura absoluta]] se llega que: 

$$\frac{1}{T}=\left(\frac{\partial S}{\partial E}\right)_V=\frac{3Nk_B}{2E}$$ 
De donde se deduce que la [[Energía|energía]] del gas ideal monoatómico es: 

$$E_\text{mono}=\frac{3Nk_BT}{2}$$

Para el diatómico se cambia el $3$ por un $5$. Notemos que es **independiente del volumen** y sólo depende de la temperatura. Esto **solo ocurre con los gases reales**. 

### Ecuación de estado del gas ideal 

Recordemos que la presión es **fuerza por unidad de área** en esencia. Por lo tanto, es posible reemplazarla por el valor de energía en la ecuación anterior. Si consideramos la definición de presión como tal para el caso de gases ideales, se llega a la relación: 

$$P=\frac{2E}{3V}$$

Y ahora sí, al reemplazarla con la **energía monoatómica**, se llega que: 

$$PV=Nk_BT$$ 

Notar que el resultado es independiente si el gas es mono o diatómico. 

Los gases no ideales llegarían a ser aquellos que cumplen que: 

$$\frac{PV}{RT}=z(P,T)\neq 1$$

Donde $z$ es **el factor de compresibilidad**.

Este factor de compresibilidad se interpreta de la siguiente forma:

$$P_1V_1=RT_1$$
A presión ambiente, por lo general, se cumple que: 

- $P_2=1bar$
- $T_2=300K$

### Ecuación de Van der Waals 

La presión efectiva toma en cuenta que al chocar con la pared hay moléculas de un lado pero no del otro. La del otro lado las estarían frenando. Las moléculas que chocan con la pared dependen de $N/V$ y el efecto de frenado depende de las moléculas cercanas. Luego, la corrección es de la forma $1/v^2$. 

Por ende, las variables efectivas llearian a ser: 

$$P_\text{efectiva}=P+\frac{a}{v^2}$$

$$v_\text{efectivo}=v-b$$

$$P_\text{efectiva}v_\text{efectivo}=RT$$

Los parámetros de $a$ y $b$ se determinan para cada gas. 

La constante $a$ mide la interacción entre las moléculas, por el otro lado, el $b$ tiene que ver con el volumen del líquido condensado. 
### Capacidad térmica y calor específico

Para un gas ideal, el [[Capacidad calórica|calor específico]] molar para un volumen constante se define como: 

$$c_V=\frac{r}{2}R$$

En este caso, no depende de la temperatura, pero en los modelos reales **si hay dependencia de la temperatura**. 