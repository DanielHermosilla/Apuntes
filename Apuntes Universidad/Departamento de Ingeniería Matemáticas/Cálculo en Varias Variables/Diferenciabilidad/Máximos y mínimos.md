
Un punto $a\in A$ es **mínimo global** para $f$ en $A$ si para todo $x\in A$ se tiene $f(x)\geq f(a)$. Lo mismo pero contrario es para el **máximo global**.  

Por otro lado, se dice que un punto $\bar{x}\in A$ es llamado **mínimo local** (de manera análoga para **máximo local**) si existe un radio $R$ tal que la desigualdad ocurra dentro de tal [[Bolas|bola]], es decir; 

$$\forall x\in B(\bar{x},r)\cap A\;,\;f(x)\geq f(\bar{x})$$ ![[IMG_53B8AE2F3C1F-1.jpeg|center]]

## Proposición 

Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ con A [[Conjuntos abiertos y cerrados|abierto]]. Supongamos que $a\in A$ es mínimo local de $f$ y $f$ [[Diferenciabilidad|diferenciable.]] Entonces: 

$$\nabla f(a) = \vec{0}$$ 
El mismo caso sería para un máximo local. Parecido a la *[[Regla de Fermat|regla de Fermat]]* pero para varias variables. 

### Demostración 

Supongamos que $f$ posee un mínimo local en un punto $a\in A$. Esto quiere decir que va a existir un radio $r>0$ tal que: 

$$f(x)\geq f(a)\;\forall x\in B(a,r)\cap A$$ 
Definamos una [[Funciones escalares|función escalar]]: 

$$\phi(t) = f(a + te_i)$$ 
Con $e_i$ el [[vectores|vector canónico]] de $\mathbb{R}^n$ y $t\in (-r,r)$. Note que la función va a cumplir lo siguiente: 

$$\phi(t)\geq\phi(0)\;\forall t\in (0,r)$$

Luego,

$$\phi'(0) = \lim_{t\rightarrow 0^+}\frac{\phi(t) - \phi(0)}{t} \geq 0$$ 
Análogamente, 

$$\frac{\phi(t)-\phi(0)}{t}\leq 0\;\forall t\in(-r,0)$$ $$\implies\phi'(0)\leq 0$$ 
Por tanto, $\phi'(0)=0$. Esto es equivalente a, por [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Diferenciabilidad/Regla de la cadena|regla de la cadena]]: 

$$\nabla f(a)\;·\;e_i = 0\iff\frac{\partial f}{\partial x_i}(a)=0$$ 
Como $e_i$ es arbitrairo, entonces se obtiene que $\nabla f(a)=\vec{0}$. 


## Teorema: (Test de la segunda derivada)

Análogo al curso de *Cálculo Diferencial e Integral*, habría que ver el signo de los [[valores y vectores propios|valores propios]] para ver si la función es creciente o decreciente. 

Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$ de [[Derivadas de orden superior|clase]] $C^2(A)$ con $A$ [[Conjuntos abiertos y cerrados|abierto]] y $a\in A$ un [[Puntos críticos|punto crítico]] de $f$ en $A$. Si $f''(a)$ es definida positiva entonces corresponde a un mínimo local. Análogo para los máximos locales. 

### Demostración 

Acordándonos del polinomio de Taylor, tenemos lo siguiente: 

$$f(a + h) = f(a) +\nabla f(a)\;·\;h+\frac{1}{2}h^Tf''(a + sh)h$$

Como $a$ es un [[Puntos críticos|punto crítico]] el polinomio termina de la siguiente forma: 

$$ f(a + h) = f(a) +\frac{1}{2}h^Tf''(a + sh)h $$ $$\iff  f(a + h) -f(a) =  \frac{1}{2}h^Tf''(a + sh)h $$ 
Si $f''$ es positivo, el polinomio es positivo, y si $f''$ es negativo el polinomio va a ser negativo. 


### Ejemplo: 

Hallar los puntos de la gráfica de la función $g(x,y) = (xy)^{-1}$ que están más cercanos al origen. 


![[IMG_CE1919F6124B-1.jpeg|center]]

Luego, la [[Distancia|distancia]] entre los puntos de la gráfica de $g$ y el origen está dado por la [[norma]] euclidiana: 

$$d(x,y) = \sqrt{(x-0)^2 + (y-0)^2 + ((xy)^{-1}-0)^2}$$ $$\iff d(x,y) = \sqrt{x^2 + y^2 + (xy)^{-2}}$$ 
Nos basta con minimizar la expresión: 

$$x^2 + y^2 + (xy)^{-2} = f(x,y)$$ 
Claramente el dominio de $f$ es $\mathbb{R}^2 | \lbrace{(xy \neq 0)}\rbrace$. Del ejemplo anterior sabemos que los [[Puntos críticos|puntos críticos]] son $x\pm 1$ y $y\pm 1$. Además, tenemos que: 

$$\frac{\partial f}{\partial x} = 2x - \frac{2xy^2}{(x^2y^2)^2} = 2x - \frac{2}{x^3y^2}$$ $$\implies\frac{\partial^2 f}{\partial x^2} = 2 + \frac{6x^2y^2}{x^6y^4} = 2 + \frac{6}{x^4y^2}$$ Por último, 

$$\frac{\partial f}{\partial y} = 2 + \frac{6}{y^4x^2}$$ $$\frac{\partial^2 f}{\partial y^2} = 2 + \frac{6}{y^4x^2}$$ $$\frac{\partial^2 f}{\partial x\partial y} = \frac{4xy^3}{y^6x^4} = \frac{4}{y^3x^3}$$ 
En conclusión, la [[Matriz Hessiana|matriz Hessiana]] es: 

$$ f''(x,y)=\begin{equation}
		\begin{bmatrix}
			2 + \frac{6}{x^4y^2} & \frac{4}{y^3x^3}\\ 
			\frac{4}{y^3x^3} & 2 + \frac{6}{x^4y^2}
		\end{bmatrix}
\end{equation}
		$$

Si calculamos los [[valores y vectores propios|valores propios]] bajo el [[polinomio característico]] con los puntos $(1,1)$ que eran los [[Puntos críticos|puntos críticos]] llegamos a que los [[valores y vectores propios|valores propios]] son todos positivos. Por lo tanto, $f(1,1)$ es un mínimo local y está a distancia mínima del origen. La distancia habría que evaluarla en la [[Distancia|distancia]] anterior, donde se llega que la [[Distancia|distancia]] es $\sqrt{3}$. 


##  Teorema valores propios de $C^2$ 

Sea $\alpha_1,\alpha_2,\dots,\alpha_n\in\mathbb{R}$ los valores propios de $f''(a)$. Con $f$ siendo de [[Derivadas de orden superior|derivada de orden superior]] en $A$ con $A$ [[Conjuntos abiertos y cerrados|abierto]] y tal que $\nabla f(a)=\vec{0}$. Entonces: 

- Si cada [[valores y vectores propios|valor propio]] de la [[Matriz Hessiana]] es positivo entonces $a$ es [[Máximos y mínimos|mínimo local]]. 
- 
- Si cada [[valores y vectores propios|valor propio]] de la [[Matriz Hessiana]] es negativo entonces $a$ es [[Máximos y mínimos|máximo local]]. 
- 
- Si dos [[valores y vectores propios|valores propios]] poseen distinto signo, digamos $\alpha_1 >0\land\alpha_2<0$, entonces $a$ es un *punto silla* en el sentido que existen dos direcciones $v_1,v_2\in S(0,1)$ para los cuales se cumple que: 
- $$f(a+tv_1)\leq f(a)$$ $$f(a+tv_2)\geq f(a)$$
- Para un $t$ suficientemente pequeño. 