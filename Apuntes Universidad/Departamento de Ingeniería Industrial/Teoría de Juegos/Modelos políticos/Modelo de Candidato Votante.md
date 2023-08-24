
Los votantes, al igual que en el modelo de [[Productos Diferenciados|productos diferenciados]], se distribuyen homogéneamente en el segmento de línea $0$ y $1$. Cada punto es un votante con un voto. 

![[Pasted image 20230824104332.png|center]]

Los votantes pueden ser candidatos si quieren. El número de candidatos no es fijo y es endógeno. Un candidato puede cambiar su posición política. 

Por lo tanto, los jugadores son los votantes y la estrategia es ser candidato o no. Los votantes votarían por el candidato más cerca a su posición. 

En los pagos, ser candidato tiene un costo $c>0$ y hay un premio para el ganador $B\geq 2c$. Si gana el candidato en posición $y$, un votante en posición $x$ sufre por la diferencia $\vert x-y\vert$. 

Por lo tanto, si $x$ entra y gana, su pago es $B-c$. Si $x$ entra y pierde al candidato en posición $y$, su pago es $-c-\vert x-y\vert$. Si $x$ no entra y gana el candidato en posición $y$, su pago es $\vert x-y\vert$. 

### Equilibrio de Nash 

Observemos que un votante que no puede ganar no va a ser candidato. Entonces surgen las preguntas: 

- *¿Cuántos candidatos podemos tener en el equilibrio?* 
- *¿Quién va a ser candidato?*

Un equilibrio trivial es el único candidato en posición $\frac{1}{2}$. 

![[Pasted image 20230824105458.png|center]]

Ahora, para el caso con dos candidatos, un posible equilibrio serían los dos extremos: 

![[Pasted image 20230824105750.png|center]]

Cada candidato gana con [[Teoría de probabilidades|probabilidad]] $\frac{1}{2}$. De hecho, el equilibrio se da **cuando cada candidato se posiciona en posiciones simétricas para el equilibrio**. 