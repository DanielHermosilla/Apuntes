
Una asignación es un emparejamiento. Un emparejamiento es una función $\mu:I\to H$ que es inyectiva y suryectiva. Así, cada agente recibe una casa y cada una es asignada a un sólo agente. 

Así, las asignaciones llegan a ser [[Distribución Pareto-Eficiente|Pareto-Eficiente]]. 

Nos definimos el mercado de casas como $\langle I,H,\succeq,\mu\rangle$.

Un emparejamiento está en el **núcleo de la economía** si no existe un [[Conjuntos|subconjunto]] $T\subset I$ y un emparejamiento $v$ tal que: 

- $v(i)\in\lbrace j_i\rbrace$ para cada $i\in T$. 
- $v(i)\succeq_i\mu(i)$ para cada $i\in T$
- $v(i)\succeq_i \mu(i)$ para algún $i\in T$

### Algoritmo de Ciclo Máximo de Intercambio 

Cada agente apunta al dueño de su casa preferida. Como existe un número finito de casas, existe al menos un ciclo. Los agentes en cada ciclo reciben su casa preferida y dejan el mercado. 

Si aun quedan agentes en el mercado, se hace otra iteración. Es como si fuera una recursión hasta que todos dejan el mercado. 

Esto funciona **para cualquier número de agentes y casas**. 

>[!example] Teorema 
>El resultado del algoritmo CMI es el único emparejamiento que está en el núcleo del mercado de casas. 

Además, **el núcleo de un mercado de casas es a prueba de estrategias que mienten**. 

## Mecanismos de asignación sin una asignación inicial 

Suponemos que nadie tiene una asignación sobre alguna casa. 

### Dictatorialidad en serie simple 

 El agente que tiene el primer turno elige su casa preferida. El del segundo turno elige, y así sucesivamente. Los agentes toman sus turnos según el orden de $f$. Esto es **siempre Pareto Eficiente**. 

Ahora, se podría hacer otra premisa para el dueño de la casa, este puede:

1. Quedarse en su casa 
2. O dejar la casa y entrar en la lotería

En la lotería se garantiza que lo peor que puede pasar es quedarse con su propia casa. 

Por lo tanto, el modelo se puede mejorar al ordenar los agentes con una loteria y aplicando la dictatorialidad en serie hasta que alguien quiere la casa inicialmente asignada. Cuando eu dueño ya tenga la casa inicialmente asignada, sigue sin cambiar el proceso. 