
Recordar que el gradiente de una función $f:\mathbb{R}^n\rightarrow\mathbb{R}$ es su [[matriz Jacobiana]] dada por: 

$$\nabla f =(\frac{\partial f}{\partial x_1}(x_0),\frac{\partial f}{x_2}(x_0)\dots,\frac{\partial f}{\partial x_n}(x_0)) $$

Por lo tanto, definimos la **superficie $(S)$** mediante una [[Funciones escalares|función escalar]] [[Diferenciabilidad|diferenciable]] al conjunto: 

$$S(f) =\lbrace x\in\mathbb{R}^n\;|\;f(x)=0\;;\;\nabla f(x)\neq 0\rbrace$$ 
# Ecuación 

Por lo tanto, la ecuación del plano tangente llegaría a ser: 

$$T_f(x,y) = f(x_0,y_0) + Df(x_0,y_0)\begin{bmatrix}
x-x_0\\y-y_0
\end{bmatrix}$$ 
### Ejemplo 

$f(x,y) = \frac{x^2}{a^2} + \frac{y^2}{b^2}$ define la superficie $z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$. Lo cual se puede reescribir como: 

$$ g(x,y,z) = 0$$ 
Con $$g(x,y,z) = \frac{x^2}{a^2} +\frac{y^2}{b^2}-z$$ 
Note que si $z=0$; entonces tenemos: 

$$\frac{x^2}{a^2}+\frac{y^2}{b^2}=0\implies (x,y)=(0,0)$$ 
Cuando $z=1$; tenemos una elipse: 

$$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$$ A nivel geométrico tenemos lo siguiente: 

![[IMG_629D78A871E9-1.jpeg|center|450]]

Ahora, si $x = 0$, entonces $z =\frac{y^2}{b^2}$, y si $y=0$ entonces $z=\frac{x^2}{a^2}$. Note que: 

$$\nabla g(x,y,z) = (\frac{2x}{a^2}, \frac{2y}{b^2}, -1)\neq\vec{0}\;\forall (x,y,z)\in\mathbb{R}^3$$ 
## Proposición 

Consideremos una [[Funciones escalares|función escalar]] y supongamos que $f$ es de clase $C^1$. Para una constante $c\in\mathbb{R}$ definimos el conjunto de nivel : 

$$S(f)=\lbrace x\in\mathbb{R}^n\;|\;f(x)=c\rbrace$$ 
Entonces, para cualquier punto que yo tome en $S(f)$ el [[vector gradiente]] de $\nabla f(x_0)$ evaluado en tal punto va a ser perpendicular a $S$ en $x_0$. 

### Demostración 

Debemos verificar que si tengo un punto "$a$" tangente a $S$ en "$x_0$", entonces $a$ es perpendicular a $\nabla f(x_0)$.

![[IMG_B09BA468D4B8-1.jpeg|center|550]]

Por lo tanto, queremos que el [[producto escalar]] entre $a$ y el [[vector gradiente]] sea igual a 0 para garantizar que sea perpendicular. 

Si $a$ es tangente a $S$, podemos construir una curva $x(t)\subset S$ tal que: 

$$x(t_0) = t_0$$ y $$x'(t_0) = a$$ 
Sabemos que este sistema tiene solución, ya que $x(t)\subset S$, sigue que: 

$$f(x(t)) = c\;\;\forall x\in Dom(x(t))$$ 
Al derivar tenemos, por [[Regla de la cadena|regla de la cadena]]: 

$$\nabla f(x(t))\;·\;x'(t) = 0$$ 
En particular, si tomamos $t=t_0$ tenemos que: 

$$\nabla f(x(t_0))\;·\;x'(t_0)=0$$ $$\iff\nabla f(x_0)\;·\;a = 0$$ 
Esto nos dice que el [[vector gradiente]] es perpendicular con $a$ 

--- 

Recordemos que dado un punto $x_0\in\mathbb{R}^n$ y un [[vectores|vector]] normal $N\in\mathbb{R}^n$, podemos crear la ecuación del plano mediante la fórmula: 

$$\Uppi =\lbrace x\in\mathbb{R}^n/N\;·\;(x-x_0)=0\rbrace$$ 
![[IMG_DD4C08DF9F7D-1.jpeg|center|]]

Si queremos que $x\in\mathbb{R}^n$ sea parte del plano tenemos que pedir que $N\;·\;(x-x_0)=0$. 

### Ejemplo 

Hallar la ecuación del plano tangente al elipsoide: 

$$\frac{3}{4}x^3 + 3y^2 + z^2 = 12$$ 
$$\iff\frac{x^2}{16} +\frac{y^2}{4}+\frac{z^2}{12}=1$$ 
En el punto $P_0 =(2,1,\sqrt{6})$. 

Sabemos que el [[vector gradiente]] nos dará el [[vectores|vector normal]]. Por lo tanto: 

$$N=\nabla f(x_0)\;\;x_0 = (2,1,\sqrt{6})$$ 
Tenemos que el vector sería: 

$$\nabla f(x) = (\frac{3}{2}x, 6y, 2z)$$ 
Reemplazando en $x_0$: 

$$\nabla f(x_0) = (3,6,2\sqrt{6})$$ 
El plano buscado es 

$$\Uppi =\lbrace (x,y,z)\in\mathbb{R}^3\;|\;(3,6,2\sqrt{2})\;·\;(x-z,y-1,z-\sqrt{16})\rbrace$$$$\iff (x,y,z)\in\mathbb{R}^3\;|\;3x+6y+2\sqrt{6}z - 24 = 0$$ 