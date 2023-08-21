
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

La integral $1$ y $2$ se cancelan cuando $\epsilon\to0$. Por lo tanto, las integrales quedan: 

$$\begin{align}
E_{\text{above}}\cdot l-E_\text{below}\cdot l&=0\\  \\
E_{\text{above}}&=E_{\text{below}}
\end{align}$$

Se concluye que el campo $\vec{E}$ paralelo a la superficie **es siempre continuo**. 

## Análisis del potencial 

Para el análisis del [[Trabajo del campo eléctrico|potencial]] se hace algo equivalente: 

$$\begin{align}
V(\vec{r_1})-V(\vec{r_2})&=-\int^{\vec{r_1}}_{\vec{r_2}}\vec{E}\;d\vec{l}
\end{align}$$

Con $\vec{r_1}$ y $\vec{r_2}$ [[vectores]] perpendiculares a la superficie, uno estando en el lado positivo del campo y otro en el negativo. Por último, se impone que $\vec{r_1}\to\vec{r_2}\implies V(\vec{r})\;\text{es continuo}$ 

#### Ejemplo 

El campo eléctrico y potencial en un cable coaxial neutro. 


![[Captura de pantalla 2023-08-21 a la(s) 09.36.10.png|center]]


El cable interno tiene una densidad de carga $\rho$ y el externo $\sigma$. Para que el cable sea neutro, se debe cumplir que: 

$$\begin{align}Q_{int}+Q_{ext}&=0\\\\ 
\rho\cdot Vol+\sigma\cdot Sup&=0\\\\ 
\rho\cdot\pi a^2\cdot l+\sigma 2\pi\cdot b\cdot l &=0\\\\
\sigma&=\frac{-\rho a^2}{2b}\;\;\left[\frac{C}{m^2}\right]\end{align}$$


Entonces, aplicando la Ley de Gauss se pueden generar cilíndros de distintos tamaños:

![[IMG_8956FCD15233-1.jpeg|center|500]]


Entonces, se llega que: 

$$\vec{E}(r)=\begin{cases}\frac{\rho}{2\epsilon_0}r&r<a\\ \\
\frac{\rho}{2\epsilon_0}\frac{a^2}{r}&a<r\leq b\\  \\
0&r>b\end{cases}
$$

Que llegaría a ser una figura como la siguiente (para casos prácticos se considera $5=a$): 

```functionplot
---
title: Campo eléctrico
xLabel: r
yLabel: Campo eléctrico
bounds: [0, 10, 0, 10]
disableZoom: True
grid: True
---
f(x)=2x
g(x)=10/(x-3.5)+3
```

 Ahora, para calcular el potencial entre $r=0$ y $r=b$ habría que hacer una doble integral. Aplicando la fórmula se llega que: 

$$V(b)=\frac{-\rho}{2\epsilon_0}\left(\frac{a^2}{2}+a^2\ln(\frac{b}{a})\right)$$

Analizando esta expresión, se puede notar que es más difícil mover cargas en el campo interno porque existe un campo eléctrico en el cable externo. Por el otro lado, cuando se está en el cable externo, se es muy fácil mover cargas ya que afuera no hay un campo eléctrico. 