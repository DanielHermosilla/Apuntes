
# Pregunta 1 

Sea $z = f(u,v)\in C^2(\mathbb{R}^2)$; considere $u(x,y) = x^3-y^3\; ;\; v(x,y)=\frac{2y}{x}$. Además:  

$$\frac{\partial z}{\partial u}(0,2)=1\; ;\;\frac{\partial z}{\partial v}(0,2)=-1\; ;\;\frac{\partial^2 z}{\partial u^2}(0,2)=1$$ y $$\frac{\partial^2 z}{\partial v^2}(0,2)=2\; ;\;\frac{\partial^2 z}{\partial u\partial v}(0,2)=-2$$ 
Calcular $\frac{\partial^2 z}{\partial y\partial x}(1,1)$

# Pregunta 2 

Justifique por qué $f(x,y)=x^2 + y^2 + \frac{2\sqrt{2}}{3}xy$  alcanza sus valores máximos  y mínimos sobre $S=\lbrace (x,y)\in\mathbb{R}^2\; |\; x^2 + y^2\leq 1\rbrace$. Luego, calculelos. 

# Pregunta 3 

Considere la siguiente función: 
$$ 
g(x,y)=\begin{cases} 
       x^2y^2\ln(x^2 + y^2) & (x,y)\neq (0,0) \\
      0 & (x,y) = (0,0) 
   \end{cases}
$$ 
Determine los puntos donde las derivadas direccionales existen. 

# Pregunta 4 

Sea $f:\mathbb{R}\rightarrow\mathbb{R};\;f\in C^1(\mathbb{R})$ y $g:\mathbb{R}^n\rightarrow\mathbb{R};\; g\in C^1(\mathbb{R}^n)$. Considere: 

$$ 
h(x)=\begin{cases} 
       f(||x||)\; g(\frac{x}{||x||}) & (x)\neq\vec{0} \\
      0 & (x) =\vec{0} 
   \end{cases}
$$

1) Demostrar que si $|f(a)|^2\leq a^2\; ;\forall a\in\mathbb{R}$ entonces $h$ es diferenciable en todo $\mathbb{R}^n$. 
2) Demuestre que $||x||\;f'(||x||)g(\frac{x}{||x||}) =\nabla h(x)· x$ 