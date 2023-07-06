Imaginemonos una [[Función continua]] que va $\mathbb{R}: [a,b] \rightarrow \mathbb{R}_{+}$ donde su imagen representa el radio de una circumferencia inscrita en un sólido:

![[Volumen.png|center]]

Como nos podemos fijar en la función, $f(x)$ estaría representando el radio de nuestra circumferencia, perteneciente a una [[Partición|partición]] del sólido. 

Fijemonos que en el intervalo $[a,b]$ podemos tomar una [[Partición|partición]] donde $\Delta X_i$ equivaldría al ancho de un **cilíndro sólido**. 

![[cilindro.jpeg|center]]

Entonces, si analizamos el cilíndro, su área sería el **área de la base** por el **ancho**: 

$$ \text{Área: } \pi R^2 (X_i) \Delta X_i $$

Y por ende, el vólumen del sólido sería la sumatoria de todas las áreas de las particiones:

$$ \sum^{n}_{i = 1} \pi R^2 (X_i) \Delta X_i $$

Esto lo podemos identificar como una [[Suma de Riemann|suma de Riemann]], y podemos tender la [[Partición|partición]] a 0.

$$|P| \rightarrow 0 \implies Volumen = \int^{b}_{a} \pi R^2(x) \space dx $$

Ahora, de forma general, podemos obtener el área de cualquier [[Partición|partición]] independiente de que si es una circumferencia o no, al ocupar la ecuación de [[Área bajo la curva|área bajo la curva]].  Entonces, el volumen de cualquier función se vería representada bajo la siguiente [[Suma de Riemann|suma de Riemann]]:

$$ \sum^{n}_{i = 1} A(X_i) \Delta X_i $$
$$\equiv \int^{b}_{a} A(x) \space dx $$
$$ \equiv \int^{b}_{a} \int^{b}_{a} f(x) \space dx $$

Con esto podemos concluir que el volumen de una [[Función continua]], de la forma más generalizada posible, equivale a una **doble [[Integral de Riemann]]**.

#Aplicación 