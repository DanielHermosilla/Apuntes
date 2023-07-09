
Recordemos que una funcion $f:\mathbb{R}\rightarrow\mathbb{R}$ es [[Departamento de Ingeniería Industrial/Probabilidades/Repasos/Funciones/Derivada|diferenciable]] en $x_0\in Domf$ si el siguiente límite existe: 

$$f'(x_0) = \lim_{h\rightarrow 0} \frac{f(x_0 + h) - f(x_0)}{h}$$ 
Por lo tanto, para poder definir la difenciabilidad en varias variables extendemos la definición de tal límite: 

$$ \lim_{h\rightarrow 0} \frac{|f(x_0 + h) - f(x_0) - f'(x_0)h|}{h} = 0 $$ 
Por lo tanto, la **definición** es la siguiente: Sea $A$ un [[Conjuntos abiertos y cerrados|conjunto abierto]] no vacio y $x_0\in A$. Consideremos $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^m$. Tenemos que $f$ es diferenciable en el punto $x_0\in A$ (en este caso un [[vectores|vector]]) si existe una aplicación lineal de $\mathbb{R}^n\rightarrow\mathbb{R}^m$ llamada **diferencial** y denotada por $Df(x_0)$ que satisface el límite anteriormente planteado. Debe satisfacer entonces: 

$$\lim_{||h||\rightarrow 0} \frac{||f(x_0 + h) - f(x_0) - Df'(x_0)h||_{\mathbb{R}^m}}{||h||_{\mathbb{R}^n}} = 0 $$ 
Eventualmente se va a postular que la diferenciabilidad en torno a una variable va a poder representarse a través de una [[matriz Jacobiana]]. 

### Proposición: Diferenciabilidad implica [[Continuidad en varias variables|continuidad]]

Si $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^m$ es diferenciable en $x_0$ entonces $f$ es continua en $x_0$. *¿Cómo ocupar este resultado?* 

Se ocupa con su **contrareccíproca**: 

$$ f\;\;\text{no es continua}\implies f\;\;\text{no es diferenciable}$$ 

#### Demostración 

Notemos que $x_0 + h\rightarrow x_0$ cuando $h \rightarrow\vec{0}$ , por lo tanto, nos gustaría probar que $f(x_0 + h)\rightarrow f(x_0).$ 

Podemos estudiar

$$||f(x_0 + h) - f(x_0)|| = || f(x_0) - f(x_0) - Df(x_0)h + Df(x_0)h|| $$ $$\implies\leq ||f(x_0 + h) - f(x_0) - Df(x_0)h|| + ||Df(x_0)h||$$ 
Como $||Df(x_0)h|| \leq ||Df(x_0)|| \times||h||$ obtenemos: 

$$||f(x_0) - f(x_0)|| \leq ||f(x_0 + h) - f(x_0) -Df(x_0)h|| + ||Df(x_0)||\times||h|| $$ $$\iff [\frac{||f(x_0 + h) - f(x_0 - Df(x_0)h)}{||h||}] ||h||$$ 
Por lo tanto, por definición de [[Diferenciabilidad|diferenciabilidad]], tenemos que se nos irá a 0. Por lo tanto, es [[Continuidad en varias variables|continua]]. 

### Proposición: Unicidad

Si la diferencial existe de una función existe en un punto, entonces es **única**. 

#### Demostración 

Supongamos por contradicción que existen dos $Df(x_0)$ y $\bar{D}f(x_0)$ tal que si tomo un [[vectores|vector]] no [[nulidad|nulo]] $(\vec{v})$ entonces $Df(x_0)v \neq\bar{D}f(x_0)$. Consideremos un $\vec{h} = tv$  con $t\in\mathbb{R}$ y notemos que $\vec{h}$ se va al vector nulo cuando $t\rightarrow 0$. 

Luego, la diferencia entre: 

$$\frac{||f(x_0 + h) - f(x_0) - Df(x_0)h|| + ||f(x_0 + h) - f(x_0) - \bar{D}f(x_0)h||}{||h||}$$ 
Por desigualdad triangular inversa: 

$$\implies \geq\frac{||Df(x_0)h - \bar{D}f(x_0)h||}{||h||}$$ 
$$\iff\frac{||Df(x_0)(tv) - \bar{D}f(x_0)(tv)||}{||tv||}$$ 
Como $t$ está definido como un [[escalares|escalar]] y la [[Norma en varias variables|norma]] es lineal, entonces: 

$$\iff \frac{|t|}{|t|}\frac{||Df(x_0)(v) - \bar{D}f(x_0)(v)||}{||v||}$$ $$\iff \frac{||Df(x_0)(v) - \bar{D}f(x_0)(v)||}{||v||} \neq 0$$ 
Es una contradicción, pues llegamos a lo siguiente: 

$$\iff \frac{|t|}{|t|}\frac{||Df(x_0)(v) - \bar{D}f(x_0)(v)||}{||v||}$$ $$\frac{||Df(x_0)(v) - \bar{D}f(x_0)(v)||}{||v||} \neq 0 \leq\frac{||f(x_0 + h) - f(x_0) - Df(x_0)h|| + ||f(x_0 + h) - f(x_0) - \bar{D}f(x_0)h||}{||h||} $$ 
El lado derecho debería ser 0, ya que es la definición de diferenciabilidad. 

### Proposición 

1) Si $f$ es constante, entonces $Df(x_0)$ es la aplicación nula. 
2) Si $f$ es lineal, entonces $Df(x_0) = f$. 
3) Para $F = (f_1,f_2,\dots,f_n)$ tenemos que: 
$$ F\;\;\text{diferenciable}\iff f_{i\forall i\in\lbrace i,\dots,n\rbrace}\;\;\text{diferenciable}$$ 
#### Ejemplo 

$$F(x_{ij}) = (x^2 + y^2, xy): \mathbb{R}^2\rightarrow\mathbb{R}^2$$ 
Es diferenciable, ya que cada componente del [[vectores|vector]] es diferenciable. 