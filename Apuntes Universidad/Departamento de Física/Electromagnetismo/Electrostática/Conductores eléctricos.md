
Existen tres tipos de conductores eléctricos: 

- **Aisladores**: No hay carga circulando. 

- **Conductores**: Si hay carga libre. 

- **Semiconductores**: También existe carga libre bajo ciertas condiciones. 

# Propiedades de los conductores en electrostática

Sea un cuerpo $C$ que tiene una carga eléctrica. Diremos que $C$ es un *conductor ideal* cuando tiene infinitas cargas libres. Además, sabemos que si se tiene un [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] las cargas se van a mover, vale decir, existe un [[Flujo del campo eléctrico|flujo de carga]]. 

Si tengo $\vec{E}$, las cargas se mueven y el campo cambia, por lo tanto, **no hay electrostática**. Esto es una contradicción, por lo tanto, **no existe [[Departamento de Física/Métodos Experimentales/Circuitos eléctricos/Campo eléctrico|campo eléctrico]] dentro de la carga: 

$$\vec{E}=0,\;\;\text{En un volumen en electrostática}$$


Ahora, si suponemos dos placas metálicas neutras donde existe un [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] circulando por el medio, se va a cumplir también que: 


$$\vec{E_{ext}}+\vec{E_{int}}=\vec{E_{t}}=0$$

![[Captura de pantalla 2023-08-28 a la(s) 09.01.01.png|center]]


Ahora, si nos fijamos en la [[Divergencia y rotación del campo eléctrico|ecuación de la divergencia]] se cumple lo siguiente: 

$$\vec{\nabla}\cdot\vec{E}=\frac{\rho}{\epsilon_0}$$

Como se sabe que $\vec{E}=0$, entonces: 

$$\begin{align}
\vec{E}&=0\\  \\
\implies\vec{\nabla}\cdot\vec{E}&=0\\  \\
\implies\rho&=0
\end{align}$$

Es decir, **la densidad de carga también es nula**. 

Por consiguiente, también se cumple que en un conductor la carga inducida se acumula en la [[Superficie|superficie]]. Es el único lugar en el que puede estar. 

Además, si suponemos que tenemos una carga dentro del conductor que ejerce un [[Trabajo y Energía en Electrostática|trabajo]] de un punto $\vec{a}$ hacia un punto $\vec{b}$, entonces se tendría lo siguiente: 

$$V(\vec{b})-V(\vec{a})=-\int^{\vec{b}}_{\vec{a}}\vec{E}\cdot dl$$

Nuevamente, como el [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] es nulo, entonces se cumple que $V(\vec{b})=V(\vec{a})$, por lo tanto, se concluye que **el trabajo es constante por la superficie**. 

Ahora, si se aplican las [[Condiciones de borde|condiciones de borde]], al saber que las cargas circulan por la [[Superficie|superficie]] se tiene que $E^{''}_{+}=E^{''}_{-}$, por lo tanto, **el campo eléctrico es perpendicular a la superficie del conductor**. 