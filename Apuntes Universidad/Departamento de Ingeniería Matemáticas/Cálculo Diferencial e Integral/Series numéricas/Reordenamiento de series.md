
Antes de introducir el tema, veamos el siguiente ejemplo de un reordenamiento de una [[Series numéricas|serie numérica]]: 

Sabemos que la siguiente serie converge a $\ln(2)$, entonces, veamos lo siguiente: 

$$\ln(2) = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} + \dots $$ 
Por consecuencia, *¿estaría correcto escribir lo siguiente?*

$$\implies (1 - \frac{1}{2}) - \frac{1}{4} + (\frac{1}{3}-\frac{1}{6})-\frac{1}{8}+\dots $$
$$\implies \frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \frac{1}{10}$$
$$ \implies\frac{1}{2}(1-\frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} + \dots) $$

Llegariamos a la siguiente inconsistencia: 

$$ \frac{1}{2}\ln(2) \implies \ln(2) = 0\enspace\text{(Falso)} $$

El error está en el primer paso, es decir, **pensar que una serie es la suma de sus términos**. Una serie es el **límite de la sucesión de las sumas parciales, no así de la suma de los términos**. Entonces al reordenar los valores, estaría alterando la sucesión. 

### Teorema 

Si tengo una serie [[Convergencia condicional|condicionalmente convergente]] y tomo cualquier número real o ínfinito $(\alpha)$, entonces **existe un reordenamiento** de $\sum a_n$ que converge a $\alpha$. 