
Se puede representar bajo dos fórmulas equivalentes, dependiendo de la [[fase]]. 

$$ E_{1} = E_{0} *\sin(wt) $$
$$ E_{2} = E_{0} *\sin(wt + \phi) $$

Al **superponer** las dos ondas y ocupar la suma de ángulos, llegamos a la onda en función del tiempo:
$$ E(t) = 2E_{0}*\cos(\frac{\phi}{2}) *\sin (wt + \frac{\phi}{2}) $$
A partir de esto, podemos calcular la [[intensidad de onda]]:
$$ I = \langle\space (E_{0})^{2} \space \rangle$$$$ I = \langle \space (2E_{0}*\cos(\frac{\phi}{2}) *\sin (wt + \frac{\phi}{2}))^{2} \space \rangle $$
Como el promedio de una constante siempre es una constante, entonces: 
$$ I = (2E_{0}\cos(\frac{\phi}{2})\space \langle \space \sin^{2}(wt + \frac{\phi}{2})\space \rangle$$
Nos podemos fijar que: 
$$ \langle \space \sin(x) \space \rangle = 0 $$
Pero, como está al cuadrado, la función se desplaza **verticalmente**, quedando:
$$ \langle \space \sin^{2}(wt + \frac{\phi}{2}) \space \rangle = \frac{1}{2} $$![[senocuadrado.png|center]]

Por lo tanto, la **ecuación final** sería: 
$$ I = 2(E_{0})^{2}\cos^{2}(\frac{\phi}{2}) $$
Y la **intensidad máxima** sería: 
$$ I_{0} = 2(E_0)^{2} $$
Y en conclusión la [[intensidad de onda]] de la forma más *simplificada* posible sería: 
$$I(\theta) = I_{0}\cos^{2}(\frac{\phi}{2})$$ Donde $\theta$ representa el ángulo del rayo con la normal, similar a las [[rendijas]]: 

![[graficoelectromagnetica.jpeg|center]]

Y podemos llegar a la siguiente igualdad: $$ \frac{\phi}{2\pi} = \frac{\Delta L}{\lambda} = \frac{d\sin(\theta)}{\lambda}$$$$ \phi = \frac{2\pi d \sin(\theta)}{\lambda}$$ Donde $\Delta L$ equivale a la distancia entre las antenas o rayos electromagnéticos (es lo mismo que $d\sin(\theta)$).

Aplicando lo mismo, podemos llegar a lo siguiente, conociendo la [[fase]]:
$$ I(\theta) = I_{0}\cos^{2}(\frac{\pi d \sin(\theta)}{\lambda}) $$

#concepto