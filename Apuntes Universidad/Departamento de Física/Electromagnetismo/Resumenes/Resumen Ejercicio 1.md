
# Electrostática 

La electrostática hace referencia a cualquier evento de la electrodinámica donde las cargas y partículas a analizar se mantienen en reposo. De ahí, el sufijo de *estática*. 

## Ley de Coulomb 

La ley de Coulomb es la ley fundamental de la electrostática, dado que relaciona la fuerza de interacción entre cargas eléctricas. Su forma y expresión tiene cierto símil con la fuerza de atracción gravitacional. 

$$\vec{F}=\frac{1}{4\pi\epsilon_0}\frac{qQ}{\vert\vert r-\vec{r'}\vert\vert^2}\cdot\frac{(\vec{r}-\vec{r'})}{\vert\vert \vec{r}-\vec{r}'\vert\vert}$$

Notar que la expresión del denominador corresponda a la **norma euclidiana**, por lo tanto, se puede simplificar a: 

$$\vec{F}=\frac{1}{4\pi\epsilon_0}\cdot\frac{qQ(\vec{r}-\vec{r'})}{(r^2+r^{'2})^{\frac{3}{2}}}$$ 
Todo esto, en dirección radial entre las cargas. 

## Principio de superposición 

Tanto para el cálculo de campos eléctricos y fuerzas, es fundamental definir el principio de superposición. Este establece que ante una distribución de cargas cualquiera (ya sea lineal, volumétrica, etc) se puede superponer las cargas.

#### Ejemplo: 

Tomemos una partícula ubicada en $P$ y una superficie con densidad de superficie $\sigma$:

![[Captura de pantalla 2023-08-28 a la(s) 15.14.39.png|center]]

Lo que nos representa la densidad $\sigma$ es la siguiente igualdad: 

$$\sigma=\frac{Q}{\text{Área}}$$

Por lo tanto, si se quisiera calcular la carga eléctrica en la superficie, se puede llegar a la siguiente igualdad: 

$$\int_A\sigma\;dA=Q$$

De tal forma, es posible calcular la fuerza de Coulomb ejercida por la superficie. 

## Campo eléctrico 

El campo eléctrico para una carga puntual se define de la siguiente forma: 

$$\vec{E}(r)=\frac{1}{4\pi\epsilon_0}\cdot\frac{q}{r^2}\hat{r}$$

Como su nombre lo indica, es un campo vectorial que representa la presencia de cargas eléctricas. De hecho, el flujo se ve representado por la siguiente ecuación: 

$$\Phi_E=\int^{}_{S}E\cdot da$$

![[Captura de pantalla 2023-08-28 a la(s) 15.22.14.png|center|500]]


Notemos que los flujos se definen en función de una superficie, por eso la integral está en función de $S$, representando la superficie. De hecho, a partir de esta idea es donde nace la **ley de Gauss**. 

## Ley de Gauss 

Para una superficie, se define el campo eléctrico como: 

$$\oint E\cdot da=\frac{Q_{enc}}{\epsilon_0}$$

Vale decir, basta definir una superficie cualquiera para poder determinar su campo eléctrico. Al aplicar teoremas de divergencia se llega a la **ley de Gauss diferencial:**

$$\nabla\cdot E=\frac{1}{\epsilon_0}\rho$$


## Trabajo del campo eléctrico 

Supongamos que se tiene una carga puntual con su respectivo campo eléctrico. *¿Qué pasaría si la partícula se mueve de un punto $a$ hacia un punto $b$?*. Por lo general, para calcular trabajos, se puede realizar su integral de línea: 

$$\int^{b}_{a}E\cdot dl$$

![[Captura de pantalla 2023-08-28 a la(s) 15.29.16.png|center|450]]


Notemos que, trivialmente, si llegase ser el caso donde $r_a=r_b$, entonces se cumplirían las siguientes premisas: 

$$\oint E\cdot dl=0\;\;\land\;\;\nabla\times E=0$$

## Potencial del campo eléctrico 


Dado que la función del campo eléctrico es conservativa, se puede definir el potencial del campo eléctrico: 

$$V(r)=-\int^{r}_{\aleph}E\cdot dl$$

Donde $\aleph$ representa un punto arbitrario. Aun así, se puede resumir en la siguiente equivalencia: 

$$E=-\nabla V$$