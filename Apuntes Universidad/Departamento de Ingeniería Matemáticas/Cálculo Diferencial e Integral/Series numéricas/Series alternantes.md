Si $(a_k)$ es una sucesión de términos positivos, decreciente y con $\lim_{n\rightarrow\infty} = 0$. Por lo tanto, se puede construir la siguiente [[Series numéricas|serie]], que se llamará serie alternante:

$$ \sum (-1)^k a_k $$
 
 ### Teorema: Criterio de Leibniz

Todas las series alternantes **son convergentes** si $a_k$ es decreciente. 

#### Demostración

Tenemos lo siguiente: 

$$ s_{2n-1} \leq s_{2n+1} \leq s_{2n+2} \leq s_{2n} $$

Es decir, los impares crecen, pero están acotadas por $s_{2n}$ y las pares decrecen y están acotadas por $s_{2n-1}$. 

Además, nos podemos fijar que: 

$$s_{2n+1} - s_{2n} = -a_{2n-1}$$

Por hipótesis sabemos que $\lim_{n\rightarrow\infty} -a_{2n-1}$ debe ser 0, por lo tanto, ambas [[Series numéricas|series numéricas]] convergen. 

Notemos lo siguiente: 

$$ \sum\frac{(-1)^k}{k}\enspace\text{converge}\enspace\land\enspace\sum\frac{(-1)^k}{2^k}\enspace\text{converge}$$

Todo esto por el criterio de Leibniz, aun así, si tomamos los **módulos** llegamos a lo siguiente:

$$ \sum\frac{1}{k}\enspace\text{diverge}\enspace\land\enspace\sum\frac{1}{2^k}\enspace\text{converge}$$

Por lo tanto, llegamos a definir lo que sería las sucesiones **[[Convergencia condicional|condicionalmente convergentes]]**, que convergen únicamente bajo una seria alternada y las **[[Convergencia absoluta|absolutamente convergentes]]** que convergen tanto para series alternadas como no alternadas. 

#definición 