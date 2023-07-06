
Un punto $a\in A$ para el cual $f$ es [[Diferenciabilidad|diferenciable]] y además se calcula el [[vector gradiente]] y da el [[vectores|vector]] nulo, entonces se denomina punto crítico de $f$. 

### Ejemplo 

Considere $A = \mathbb{R}^2\;|\;\lbrace xy = 0\rbrace$ y $f:A\rightarrow\mathbb{R}$ definida por $f(x,y) = x^2 + y^2 + \frac{1}{x^2y^2}$. Hallar los puntos críticos de $f$. 

Notemos que: 

$$\frac{\partial f}{\partial x} = 2x - 2x^{-3}y{^-2}$$ $$\frac{\partial f}{\partial y} = 2y - 2y^{-3}x^{-2}$$ 
Por lo tanto, resolver el [[sistema de ecuación]] para que ambas [[Derivadas parciales|derivadas parciales]] sean iguales a 0. 

$$\implies x - \frac{1}{x^3y^2} = 0\;\;|\times x$$
$$\implies y - \frac{1}{y^3x^2} = 0\;\;|\times y$$

$$\implies x^2 - \frac{1}{x^2y^2} = 0$$ $$\implies y^2 - \frac{1}{x^2y^2} = 0$$ Por lo tanto, $x^2 = y^2$, luego $x\pm y$, y reemplazando, $x=\pm 1\land y=\pm 1$.  