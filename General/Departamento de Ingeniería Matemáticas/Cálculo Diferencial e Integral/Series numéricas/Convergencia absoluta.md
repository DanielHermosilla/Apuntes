Una [[Series numéricas|serie]] se dice ==absolutamente== convergente si: 

$$\sum|a_k|\enspace\text{converge}$$ 
### teorema: 

Si $\sum a_n$ es absolutamente convergente $\implies\sum a_n$ es convergente

#### Demostración 

Por el [[Departamento de Ingeniería Matemáticas/Cálculo Diferencial e Integral/Series numéricas/Criterios de convergencia|criterio de Cauchy]] se tiene que: 

$$ (\forall\epsilon > 0) \enspace(\exists N \in\mathbb{N})\enspace(\forall n,m\geq N)\enspace m>n, \enspace |\sum^{m}_{n+1}a_n| <\epsilon\implies\text{converge}$$
Pero, sabemos que $|\sum^{m}_{n}a_n|\leq\sum^{n}_{k=n}|a_k|<\epsilon$ 

Entonces, la serie es convergente. 