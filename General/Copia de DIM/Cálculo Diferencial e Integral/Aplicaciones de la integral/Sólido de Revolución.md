Son figuras tridimensionales construidas al girar una función en torno al eje Y o en torno al eje X.  El volumen de estos solidos se llamarán **sólidos de revolución**. 

Sea $f[a,b] \rightarrow \mathbb{R}_+$ una [[función continua]]. Esta función la vamos a **girar en torno al eje x**: 

![[solidorevolucion.jpeg|center]]

Este sólido es muy similar a obtener el [[Volumen de una función|volumen de una función]]. La analogía es casi idéntica, podemos tomar una [[Partición|partición]], donde la altura me la define la imagen, y por ende, el volumen quedaría expresado como una [[Suma de Riemann|suma de Riemann]]. 

$$ Volumen = \sum^{n}_{i=1} \pi (f(X_i))^2 \Delta Xi $$

Podemos hacer que la partición tienda a 0 y obtendríamos lo siguiente: 

$$ Volumen = \pi \int^{b}_{a} (f(x))^2 \space dx $$

Esta fórmula es **muy similar** al del [[Volumen de una función|volumen de una función]], la  única diferencia es que la ecuación del sólido de revolución se puede simplificar ya que la imagen **siempre será el radio de la partición**, por ende, en vez de escribir una integral doble, podemos simplemente expresar el área en función de la imagen. Aún así, también sería válido ocupar la formula del [[Volumen de una función|volumen de una función]].  

### Sólido en torno al eje Y 

![[solidoejey.png|center]]

Si nos fijamos en la imagen, f(x) ya no nos representaría el radio de la función. Si tomamos un valor cualquiera, el radio va a estar representado por mi valor "x". Si nos fijamos, lo que queremos hacer es calcular el área de los cilíndros horizontales de la función, por lo tanto, queremos calcular el **perímetro por la altura**: 

$$ \text{Área de los cilíndros horizontales} = 2 \pi x (f(b)-f(x)) $$

De nuevo, la altura sería $(f(b) - f(x))$ y el perímetro sería $2 \pi x$. Queremos hacer girar el cilíndro en torno a su perímetro y multiplicarlo por todos los valores de la altura (de ahí se explica, más adelante, el por qué de la [[Integral de Riemann|integral]]). 

Nuevamente, el volumen sería una [[Suma de Riemann|suma de Riemann]] que sería equivalente a tener: 
$$ Volumen = 2 \pi \sum^{n}_{i} x (f(b) - f(X_i)) \Delta X_i $$
Y, cuando hacemos tender la [[Partición|partición]] a 0 tenemos lo siguiente: 

$$ Volumen = 2 \pi \int^{b}_{a} x(f(b)-f(x)) \space dx $$

Siempre hay que notar que $(f(b) - f(x))$ sea nuestra altura. Podría ser que la altura sea $f(x)-f(a)$ o simplemente $f(x)$. Muchas veces vamos a llegar a que nuestro cilíndro a calcular tenga altura $f(x)$, entonces, la fórmula **general** del volumen de revolución en torno al eje Y sería: 

$$ Volumen = 2 \pi \int^{b}_{a} xf(x) \space dx $$
#### Ejemplo 

Calcular el volumen que se obtiene al girar la región determinada por $y = (x-2)^2$ entre $x \in [2,5]$ en torno al eje Y.

```functionplot
---
title: Función a calcular
xLabel: Radio del cilíndro
yLabel: Altura del cilíndro
bounds: [0,7,0,10]
disableZoom: true
grid: true
---
y = (x-2)^2

```

Notemos que la altura es equivalente a f(x), ya que $f(2) - f(x) = f(x)$. Entonces, ocupando la fórmula anterior podemos llegar que:  

$$ \int^{5}_{2} 2 \pi x f(x) = 2 \pi \int^{5}_{2} x(x-2)^2 \space dx $$

Análogamente podríamos tratar de resolver el mismo ejercicio con el método del sólido de revolución en torno al eje X, pero, dando vuelta nuestros ejes, es decir, integramos en función de Y. Nuestra función quedaría: 
$$ \sqrt{y} + 2 = x $$

Este se llama el *método de los discos*, donde tendríamos que restar el área que pasa por arriba con la de abajo. Nuestro rádio sería $\sqrt{y} + 2 = x$ y también tendríamos que cambiar los límites de integración a las imagenes respectivas cuando $x = 2$ y $x = 5$, es decir, integrar entre 0 y 9. Por lo tanto, el volumen, **equivalente a la forma anterior** sería: 

$$ Volumen = \int^{9}_{0} \pi (5^2 - (\sqrt{y} + 2)^2) \space dy $$

Notar que el área a restar sería, justamente $\pi (\sqrt{y} + 2)^2$, ya que estamos buscando calcular el sólido de revolución entre $x=2$ y $x=5$. 

Tanto el *método de los discos* como el de los *cilíndros* son caminos válidos para cálcular el volumen de revolución, lo que hay que tener claro es **entender bien lo que se está haciendo**; poder **identificar la altura del cílindro** en el *método de los cilíndros* o **identifiar el área a restar** en el *método de los discos*. La conveniencia de cada método depende del ejercicio, pero siempre priorizar el método donde se visualiza mejor el desarrollo. La importancia está en **modelar y conceptualizar**. 

#Aplicación 