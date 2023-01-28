Dada una sucesión $(a_k)$ vamos a considerar la siguiente sucesión: 

$$ S_n = \sum^{n}_{k=1} a_k \enspace\enspace\text{(suma parcial)} $$ 
También se puede denotar de la siguiente forma: $(\sum a_k)$. Diremos que la serie es **convergente** si existe algún límite $\lim_{n\rightarrow\infty} S_n = S$. En ese caso de dice lo siguiente: 
 $$ S_n = \sum^{\infty}_{k=1} a_k \enspace\enspace\text{(suma de la serie)} $$

Por el otro lado, si el límite no existe, la serie se dirá que es **divergente**. 

#### Ejemplo: 

Sea $a_k = (-\frac{1}{2})^k$ , entonces: 

$$S_n = \sum^{n}_{k=0} (-\frac{1}{2})^k$$

Por la **propiedad geométrica** podemos obtener lo siguiente:

$$ S_n = \frac{1 - (-\frac{1}{2})^{n+1}}{1 - (-\frac{1}{2})} = \frac{2}{3}(1-(-\frac{1}{2})^{n+1} $$

Entonces:

$$ \lim_{n\rightarrow\infty} S_n = \frac{2}{3} \land \sum^{\infty}_{k=0} (-\frac{1}{2})^k = \frac{2}{3} $$ 
Otro ejemplo muy interesante, la *serie armónica*: 

$$ a_k = \frac{1}{k} $$ 
Veamos que la seríe numérica sería: 

$$ 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \dots + \frac{1}{9} + \dots + \frac{1}{16} + \frac{1}{17} + \dots + \frac{1}{32} $$ 
Notemos que: 

1. $\frac{1}{3} + \frac{1}{4} \geq \frac{1}{2}$ 
2. $\frac{1}{5} + \dots + \frac{1}{8} \geq \frac{1}{2}$ 
3. $\frac{1}{17} + \dots + \frac{1}{32} \geq \frac{1}{2}$ 

Por lo tanto: 
$$ S_{2^k} \geq 1 + \frac{k}{2} $$
Tenemos que $S_{2^k}$ es *no acotada* y es una subsucesión de $S_n$, por conclusión, $S_n$ es **no acotada**. 

En el estudio de series, el siguiente teorema es importante: 

### Teorema 

Si $(\sum a_k)\enspace \text{converge}\implies \lim_{k\rightarrow\infty} a_k = 0$  

Esto se demuestra a partir del *criterio de Cauchy*:

$$ (\sum a_k) \enspace\enspace\text{converge si y sólo si:}$$ $$ \forall \epsilon > 0, \exists N \in \mathbb{N} \enspace\text{tal que si tomo}\enspace n>m \geq N \implies |S_n - S_m| < \epsilon $$ Notar que $|S_n - S_m| = |\sum^{m}_{k=n + 1} a_k  | < \epsilon$ 

Para poder demostrar esto, primero hay que postular el [[Teorema de Cauchy]], teorema que es muy similar al *criterio de Cauchy*. 

Ahora veamos su **recíproca**: 

$$ \lim_{k\rightarrow\infty} a_k = 0 \implies (\sum a_k)\enspace \text{diverge} $$

Un clásico ejemplo de esto es la *serie armónica* que acabamos de resolver, donde $\sum \frac{1}{n}$ diverge pero la sucesión converge a 0. 

También veamos la **contrarecíproca**: 

$$ \lim_{k\rightarrow\infty} a_k \neq 0 \implies (\sum a_k)\enspace\text{no converge}$$ 
## Resumen

Por lo tanto, si tenemos una serie donde $a_k$ toma términos generales podemos, hasta ahora, tomar dos criterios: 

1. Criterio de Cauchy
2. Criterio de convergencia absoluta: convergencia de los módulos de los términos. 