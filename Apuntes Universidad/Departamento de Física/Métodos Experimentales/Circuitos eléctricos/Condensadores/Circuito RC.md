El uso de un [[Condensador|condensador]] consiste principalmente en evitar las cargas repentinas a circuitos eléctricos. 

Por lo tanto, un [[Condensador|condensador]] se puede cargar y descargar. Entonces, debido al tiempo que se demora en cargarse y descargarse se pueden considerar estados diferentes en circuitos *RC*.

![[Captura de Pantalla 2022-12-26 a la(s) 18.41.03.png|center|450]]

El estado estacionario corresponde al comportamiento del circuito una vez que ya ha pasado suficiente tiempo despues de la conexión o desconexión. 

Por lo tanto, si tenemos un [[Condensador|condensador]] en un circuito cerrado, su carga sería $Q_0 = CV$. Cuando el interruptor se abre el [[Condensador|condensador]] empieza a descargarse y se cumple lo siguiente: 

$$ I(t) = \frac{dQ(t)}{dt}\;\;\text{(Intensidad en el tiempo)} $$

$$ I(t) = \frac{V(t)}{R}\;\;\text{(Ley de Ohm)} $$ 
$$ C = \frac{Q}{\Delta V}\;\;\text{(definición condensador)} $$ 
Por lo tanto, se llega a lo siguiente: 

$$ \frac{dQ}{dt} = -\frac{Q}{RC} $$ 
Esta constante "$RC$" ($\tau$) es una forma de medida del tiempo.  Se dice que a los $5RC$ se tiene una descarga o carga total. Se puede apreciar que la caida es como la inversa de una función exponencial: 

![[Captura de Pantalla 2022-12-26 a la(s) 18.53.37.png|center|500]]
