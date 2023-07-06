
Ante tener una frontera factible y distintas [[Función Utilidad|funciones utilidad]] se podría optimizar una decisión: 

![[Optimizar decisiones.png|center]]

En este caso, lo óptimo está en la frontera del conjunto factible con la curva de indiferencia. En este caso, lo mejor sería la curva de indiferencia $C_3$, pues es la que está mas arriba y a la derecha, otorgando la mayor utilidad. En lo más **óptimo**, esta curva es **tangente** a la frontera factible. 

![[Optimizar decisiones 2.png|center]]

Por ende, la [[Tasa marginal de sustitución|tasa marginal de sustitución]] debe ser igual al [[Costo de oportunidad|costo de oportunidad]] de una hora de tiempo libre, o en otras palabras, el negativo del producto marginal: 

$$TMS = -PMg$$ 
### Optimización matemática

Por lo tanto, esto llega a ser un problema de optimización donde se busca maximizar la [[Función Utilidad|función utilidad]] sujeto a la restricción del conjunto de la frontera factible, es decir; 

$$max_{t,y} U(t,y)$$
Sujeto a: 

$$y\leq f(24-t)\ \ \ \text{(función que determina el tiempo libre)}$$ 
 Por lo tanto, la **función objetivo** sería la función utilidad, las **variables de decisión** seria *t* e *y* y las **restricciones** la [[Función producción|función producción]] que determina la frontera del conjunto factible. 

Como en el ejemplo anterior, $U(t,y)$ es creciente en y, entonces el óptimo se obtiene cuando la restricción es activa, es decir, $y = f(24-t)$. Luego, se obtiene *y* en función de *t*, que se podría reemplazar en la **función objetivo**: 

$$y(t)=f(24-t)$$ $$\implies max_{t,y}\ U(t,y(t))$$ 
Se optimiza en una variable, por lo tanto, se busca que la [[Derivada parcial|derivada parcial]] de la función objetivo en función de *t* sea 0. Es decir: 

$$\implies\frac{dU}{dt} = \frac{\partial U}{\partial t} + \frac{\partial U}{\partial y}\; ·\;\frac{\partial y}{\partial t}\ \ \ \text{(Regla de la cadena)}$$ 
Notemos lo siguiente: 

$$\frac{\partial y}{\partial t} = -f'(24 - t)$$ $$\implies f'(24-t) = \frac{\partial U}{\partial t}\big / \frac{\partial U}{\partial y}$$ Que justamente es equivalente a: 

$$\iff\ \text{-PMg}=\text{TMS}$$ 