
El [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]] es continuo excepto cuando hay distribuciones de carga superficial. Notemos si tenemos una superficie cualquiera, se puede trazar sus campos eléctricos por arriba (*above*) y por abajo (*below*):

![[Captura de pantalla 2023-08-21 a la(s) 09.12.45.png|center]]


Podemos crear una superficie [[Ley de Gauss|Gaussiana]] que pase por ambos campos, y hacer tender su altura $\epsilon\to0$. Por lo tanto, se tiene lo siguiente: 

$$\oint_{\text{partícula}}\vec{E}\;d\vec{s}=\frac{Q}{\epsilon_0}=\frac{A\sigma}{\epsilon_0}$$

Entonces, para poder integral ocupando la [[Ley de Gauss]], se postula lo siguiente: 

$$\int_{\text{lados}}\vec{E}\;d\vec{s}+\int_{\text{tapa superior}}\vec{E}\;d\vec{s}+\int_{\text{tapa inferior}}\vec{E}\;d\vec{s}=\frac{A\sigma}{\epsilon_0}$$

Pero, cuando $\epsilon\to0$, entonces el área de los lados también tiende a cero. Entonces, se llega a lo siguiente:

![[IMG_F415E7F6FAF1-1.jpeg|center|500]]

Si trazamos el campo eléctrico perpendicular a la pastilla, entonces las integrales de la tapa superior e inferior llegan a ser: 

$$\begin{align}E_+A-E_-A&=\frac{A\sigma}{\epsilon_0}\\ \\ 
E_+-E_-&=\frac{\sigma}{\epsilon_0}\end{align}
$$

Vale decir, el **campo eléctrico es perpendicular a la superficie discontinua**. Ahora, si miramos la componente paralela, vale decir, $E_{\text{above}}$ y $E_{\text{below}}$. Usando la [[Ley de Gauss]] diferencial, vale decir, $\vec{\nabla}\times\vec{E}=0$, se puede plantear lo siguiente (*notar que se enumeraran los lados verticales de la pastilla como $1$ y $2$ y el de arriba y abajo como $3$ y $4$*): 

$$\cancelto{0}{\int^{}_{1}\vec{E}\;d\vec{l}}+\cancelto{0}{\int^{}_{2}\vec{E}\;d\vec{l}}+\int^{}_{3}\vec{E}\;d\vec{l}+\int^{}_{4}\vec{E}\;d\vec{l}=0$$

La integral $1$ y $2$ se cancelan cuando $\epsilon\to0$. Por lo tanto, la s integrale