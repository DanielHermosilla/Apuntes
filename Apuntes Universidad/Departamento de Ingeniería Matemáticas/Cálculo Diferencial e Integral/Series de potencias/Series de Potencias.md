
Dada una sucesión $(a_k)_{k\in\mathbb{N}}$ sucesión de números reales y $\alpha\in\mathbb{R}$, a la siguiente [[Series numéricas|serie]] la denominaremos **serie de Potencias**.  

$$ S = \sum^{}_{k\in\mathbb{N}}a_k (x-\alpha)^k $$

Si nosotros llegasemos a reemplazar a $x$ por un $x_0$ cualquiera y llegase a converger, es lo mismo que decir que: 

$$ T = \sum a_kx^k\enspace\text{converge para}\enspace x = x_0 - \alpha$$ 
Es decir, para estudiar las series de potencias, basta estudiar el caso de $\alpha = 0$. 

#### ejemplo

$$\sum^{}_{k\in\mathbb{N}}x^k = \frac{1}{1-x}\enspace\forall x \in (-1,1) $$ 
Diverge si $|x|\geq 1$. 

Ahora, podríamos definir la siguiente función: 

$$f(-1,1)\rightarrow\mathbb{R}$$
$$f(x)\rightarrow\frac{1}{1-x}$$ 
Notemos que algo **equivalente** a esta función sería lo siguiente: 

$$g(-1,1)\rightarrow\mathbb{R}$$
$$g(x)\rightarrow\sum x^k$$

## Proposición

Si la [[Series numéricas|serie]] $\sum a_k x_{0}^k$  converge con $x_0 \neq 0$, entonces $\forall a \in (0,|x|)$ y $\forall x \in [-a,a]\implies\sum a_k x^k$ [[Convergencia absoluta|converge absolutamente.]] Es decir, el lugar donde convergen las series de potencias son intervalos.  

## Corolario 

Si $\sum a_k x_{0}^k$ diverge, entonces  $\sum a_k x^k$ también diverge si $|x| > |x_0|$ 

Por lo tanto, notemos que las series de potencias tienen **intervalos donde convergen e intervalos donde divergen**.  Entonces, el supremo del conjunto de convergencia lo llamaremos el [[Radio de convergencia|radio de convergencia]]. 

Por conclusión si el radio de convergencia es un número "$R$", entonces: 

$$\text{en}\enspace(-R,R)\enspace\text{converge}\enspace\land\enspace\text{en}\enspace(-R,R)^\complement\enspace\text{diverge}$$ 
Para saber si el intervalo es abierto o cerrado hay que estudiar los casos partículares. 