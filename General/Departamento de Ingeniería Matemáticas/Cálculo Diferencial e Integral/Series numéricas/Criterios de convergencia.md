Sea $(a_n)$ sucesión. La [[Series numéricas|serie]] $\sum a_k$ converge sólo si:

1. **Criterio de Cauchy**: 

$$ (\forall\epsilon > 0) \enspace(\exists N \in\mathbb{N})\enspace(\forall n,m\geq N)\enspace m>n, \enspace |\sum^{m}_{n+1}a_k| <\epsilon\implies\text{converge}$$

2. **Criterio de mayoración:** Sea $(a_n)$, $(b_n)$ sucesiones **no negativas**. Si $\exists n_0 \in\mathbb{N}$ y $\alpha_{n_0} > 0$  tal que $\forall n \geq n_0; \enspace a_n \leq \alpha_{n_0} b_n$. 

$$\text{Si}\enspace \sum b_n\enspace\text{converge}\implies \sum a_n\enspace\text{converge}$$ 
 Por contrarrecíproca podemos decir que: 

$$\text{Si}\enspace \sum a_n \enspace\text{diverge}\implies\sum b_n\enspace\text{diverge}$$

3. **Comparación de cuociente:** Sea $(a_n)$ y $(b_n)$ suceciones **no negativas** y sea $c = \lim_{n\rightarrow\infty}\frac{a_n}{b_n}$.

- Si $c$ = 0: 

$$ \sum b_n\enspace\text{converge}\implies\sum a_n\enspace\text{converge} $$ 
- Si $c > 0$:   
$$ \sum b_n\enspace\text{converge}\iff\sum a_n\enspace\text{converge} $$

 *Ejemplo*: 

$$a_n =  \sum^{}_{k=1} \sin(\frac{1}{k}) $$

Recordemos que: 

$$\sum^{}_{k=1}\frac{1}{k}\enspace\text{diverge}$$ 
Entonces, notemos que: 

$$ \lim_{k \rightarrow\infty} \frac{\sin(\frac{1}{k})}{{\frac{1}{k}}} = 1$$

Por contrareccíproca, como $c=0$, $b_n$ no converge, entonces $a_n$ tampoco. 

4. **Criterio del cuociente**: Sea $(a_n)$ una sucesión **no negativa** y $r = \lim_{n\rightarrow\infty}\frac{a_{n+1}}{a_n}$ 

- Si r < 1:
- $$\sum a_k\enspace\text{converge}$$
- Si $r > 1 \lor r = +\infty$:
$$\sum a_k\enspace\text{diverge}$$ Si $r=1$ no se puede saber

5. **Criterio de la raíz n-ésima:** Sea $(a_n)$ una sucesión **no negativa** y sea $r = \lim_{n\rightarrow\infty} \sqrt[n]{a_n}$

- Si r < 1: 
- $$\sum a_k\enspace\text{converge}$$
- Si $r > 1 \lor r = +\infty$:
- 
$$\sum a_k\enspace\text{diverge}$$
-  Si $r=1$ no se puede saber

6. **Criterio de la [[Integrales impropias|integral impropia]]:** Sea $f: [1,\infty]\rightarrow\mathbb{R}^+$ **[[Función continua|continua]] y decreciente**. Entonces: 

$$ \sum^{}_{n\geq 1} f(n) < +\infty\iff\int^{\infty}_{1}f(x)dx < +\infty $$
Notar que decir que una función sea $f(x) < \infty$ es lo mismo a decir que es convergente.

7. **Generalización del criterio de la raíz n-ésima**: Sea $(a_n)$ una sucesión **no negativa**, $r = \lim_{n\rightarrow\infty}(\sup u_n)$ . Con $u_n = \sqrt[n]{a_n}$.

- Si r < 1: 
 $$\sum a_k\enspace\text{converge}$$
- Si $r > 1 \lor r = +\infty$:
- 
$$\sum a_k\enspace\text{diverge}$$

-  Si $r=1$ no se puede saber
- 