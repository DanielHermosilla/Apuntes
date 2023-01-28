
Sea $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}$, con A [[Conjuntos abiertos y cerrados|abierto]], y $v\in\mathbb{R}^n$. Se llama derivada direccional de $f$ en el punto $x_0\in A$ y la dirección $v$ a: 

$$D_v f(x_0) = \lim_{h\rightarrow 0}\frac{f(x_0 + hv) - f(x_0)}{h}$$ 
## Observación 

La derivada direccional es la [[Diferenciabilidad|derivada]] usual de una función $g(t) = f(x_0 + tv)$ en $t=0$. 

En efecto, tenemos que: 

$$g'(0) = \lim_{t\rightarrow 0}\frac{g(t)-g(0)}{t}$$ 
Evaluando en $t$: 

$$ g'(0) = \lim_{t\rightarrow 0} \frac{f(x_0 + tv) - f(x_0)}{t} = D_v f(x_0)$$ 
Entonces, a través de esta observación podemos aplicar la [[Regla de la cadena|regla de la cadena]] al definir $g(t)$ como una composición. Por lo tanto: 

$$ g'(0) = Df(x_0) \;o\; v $$ 
De ahi nos damos cuenta que la derivada direccional es la [[Diferenciabilidad|derivada]] aplicada sobre el vector $v$. 

Ademas, $Df(x_0)$ se puede reescribir como la [[matriz Jacobiana]], además que $f$ es una [[Funciones escalares|función escalar]]. Por lo tanto: 

$$ f'(x_0) = (\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\dots) $$ 
Y a esto lo llamaremos [[vector gradiente]], representado por $\nabla f(x_0)$. 

Combinando todo esto, vemos que en el caso que $f:\mathbb{R}^n\rightarrow\mathbb{R}$ [[Diferenciabilidad|diferenciable]] en $x_0$, vale que: 

$$ D_v f(x_0) = \nabla f(x_0)\;o\;v$$ 
Que llegaría a ser simplemente un [[producto punto]] entre el [[vector gradiente]] y [[vectores|vector]] direccional. 

## Observación 

Por lo general se consideran los [[vectores]] de [[Norma en varias variables|norma]] uno. Es decir, $v\in\gamma^n (0,1) = \lbrace v\in\mathbb{R}^n\;\;|\;\;||v|| = 1\rbrace$

Se toma a tal conjunto para que $v$ solo indique dirección. Si no se tiene la [[Norma en varias variables|norma]] uno se normaliza. 

### Ejemplo 

Calcular $D_vf(x_0)$ con $v = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$, $x_0 = (0,0)$ y $f(x,y) = x^2 + y + 1$

Tenemos que la derivada direccional sería: 

$$ \lim_{h\rightarrow 0}\frac{f(x_0 + hv) - f(x_0)}{h} $$ $$\iff\lim_{h\rightarrow 0} \frac{f(h(1/\sqrt{2}, 1/\sqrt{2}) - f(0,0))}{h} = \frac{1}{\sqrt{2}} $$ 
Como $f$ es [[Diferenciabilidad|diferenciable]] en $(0,0)$ tenemos que: 

$$ D_vf(x_0) = \nabla f(x_0)\;o\;v $$ 
Note que: 

$$\nabla f(x,y) = (\frac{\partial f}{\partial x}(x,y)\;,\;\frac{\partial f}{\partial y}(x,y)) $$ $$\iff \nabla f(x,y) = (2x,1) \implies \nabla f(0,0) = (0,1) $$

Por lo tanto, 

$$ D_v f(0,0) = \nabla f(0,0) · (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}) = \frac{1}{\sqrt{2}}  $$ 
## Teorema 

Sea $A\subset\mathbb{R}^n$ con A [[Conjuntos abiertos y cerrados|abierto]] y $x_0\in A$. Si todas las [[Derivadas parciales|derivadas parciales]] en $x_0$ son [[Continuidad en varias variables|continuas]] entonces $F:A\rightarrow\mathbb{R}^m$ es [[Diferenciabilidad|diferenciable]] en $x_0$.

## Aplicación 

Nos sirve para saber en que dirección un plano va a elevarse o decrecer. 

Recordemos que si una función [[escalares|escalar]] $f:\mathbb{R}^n\rightarrow\mathbb{R}$ es [[Diferenciabilidad|diferenciable]] en $x_0\in\mathbb{R}^n$, entonces $D_vf(x_0) = \nabla f(x_0)\;o\;v$, con $||v|| = 1$. Como la esfera $S^{n-1}(\vec{0}, 1)$  es compacta, existen $v_1, v_2 \in S^{n-1}(\vec{0}, 1)$ tal que si calculamos $D_{v1}f(x_0) = \max_{v\in S^{n-1}(\vec{0}, 1)} D_vf(x_0)$ y $D_{v2}f(x_0) = \min_{v\in S^{n-1}(\vec{0}, 1)} D_vf(x_0)$ .  *¿Cómo encontraremos la máxima o mínima dirección hacia un gradiente?*

### Proposición: 

El valor máximo de la derivada direccional de $f$ en $x_0$ es $||\nabla f(x_0)||$  y el mínimo llegaría a ser $-||\nabla f(x_0)||$. Además, el valor máximo se alcanza en la dirección del gradiente $\nabla f(x_0)$ y el mínimo sería su inverso aditivo. 

#### Demostración 

En el caso de $f$ [[Diferenciabilidad|diferenciable]] en $x_0$ tenemos: 

$$D_vf(x_0) = \nabla f(x_0)\;·\;v$$

Luego, $\nabla f(x_0)\;·\;v$ equivale a $||\nabla f(x_0)||\;||v||\;·\;\cos(\theta)$ donde $\theta$ es el ángulo que forman $\nabla f(x_0)$ y $v$. Como $||v|| = 1$, obtenemos que: 

$$D_vf(x_0) = ||\nabla f(x_0)||\;\times\cos(\theta)$$ 
Entonces, ya que $\theta = 0$ cuando ambos vectores son paralelos, entonces de ahí se llega que el máximo es la norma y el mínimo el inverso aditivo. Y, por ende, habría que ir en dirección del gradiente. 