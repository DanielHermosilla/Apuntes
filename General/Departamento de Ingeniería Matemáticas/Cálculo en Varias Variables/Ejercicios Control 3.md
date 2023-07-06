
### Problema 1 

Calcular la [[Integral en varias variables|integral]]: 

$$\int\int\int_Vdiv(F)dv$$ 
Donde $F(x,y,z) = (xz, xy, yz)\;;\; divF =\nabla · F$  y $V$ está dado por la región limitada por $z = x^2 + y^2$ y el plano $z = x + y +\frac{3}{2}$ 

##### Solución 

Primero calculamos la **intersección** del paraboloide con el plano: 

$$x^2 + y^2 = x + y + \frac{3}{2}$$ $$x^2-x+y^2-y=\frac{3}{2}$$ Se hace *completación de cuadrados*: 

$$(x-\frac{1}{2})^2 + (y-\frac{1}{2})^2 = 2$$ 
Por lo tanto, esa **circumferencia** nos daría la intersección del paraboloide limitado por el plano. 

Por lo tanto, como tenemos una circunferencia, nos pasamos a [[Departamento de Física/Mecánica/Cinemática/Coordenadas polares|coordenadas polares]]: 

$$x = r\cos\theta +\frac{1}{2}\;\land\; y = r\sin\theta +\frac{1}{2}$$ 
Donde tenemos que: 

$$0\leq r\leq\sqrt{2}\;\land\; 0\leq\theta\leq 2\pi$$ 
Además, la coordenada $z$ siempre *choca* con el plano y el paraboloide, es decir: 

$$x^2 + y^2\leq z\leq x + y + \frac{3}{2}$$ $$\implies r^2 + \frac{1}{2} + \cos\theta + \sin\theta\leq z\leq r\cos\theta + r\sin\theta + \frac{5}{2}$$ 
Entonces: 

$$\int\int\int^{}_{V}divF = \int^{\sqrt{2}}_{0}\int^{2\pi}_{0}\int^{r\cos\theta + r\sin\theta + \frac{5}{2}}_{r^2 + \frac{1}{2} + \cos\theta + \sin\theta}(z + r\cos\theta + r\sin\theta)r\;dzd\theta dr$$

### Problema 2

Considere la región $D$ limitada superiormente por $z = 2-x^2-(y-1)^2$ e inferiormente por el cono invertido $z=\sqrt{x^2 + (y-1)^2}$. Calcule el volumen de $D$ (Examen 2022.2)

##### Solución 

Considerar el cambio de variable [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Cambio de variable|cilíndrica]], entonces: 

$$z=z\;\land\; x=r\cos\theta\;\land\; y=r\sin\theta + 1$$ 
Luego, desde la restricción superior tenemos que: 

$$2 =  x^2 - (y-1)^2$$ 
Asi, 

$$z = \sqrt{x^2+(y-1^2)} = \sqrt{r^2}=r$$ $$z = z-x^2 + (y-1)^2 = 2-r^2$$ 
Entonces la intersección sería: 

$$r = 2 - r^2$$ $$\iff r^2 + r - 2 = 0$$ 
Consideramos $r=1$ ya que nos representa [[Distancia|distancia]] y ésta siempre es positiva. Por lo tanto, la intersección representa una circumferencia centrada en $(0,1)$ de radio $r=1$. Con la intersección podemos ver como varía $z$. 

Además se tiene que el ángulo va a ser $0\leq\theta\leq 2\pi$ y: 

$$r\leq z\leq 2-r^2$$ 
Se logra al reemplazar con el cambio de variable las cotas superiores e inferiores. 

En conclusión, el [[Volumen|volumen]] está dado por: 

$$\int\int\int 1 = \int^{1}_{0}\int^{2\pi}_{0}\int^{2-r^2}_{r}r\;dzd\theta dr$$ 

### Problema 3

Considere la región $D$ limitada superiormente por $1 = x^2 + (y-1)^2 + z^2$ e inferiormente por el cono invertido $z=\sqrt{x^2 + (y-1)^2}$. Calcule el volumen de $D$. Ocupar cambio de variable [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Coordenadas esféricas|esférico]]. 

### Problema 4

Considere el sólido $v$ limitado por: 

$$x^2 + z^2 = 9\;;\; y + z = 3\;;\; y = -3$$ 
Calcule el volúmen de $v$. 

### Problema 5

Hallar el volumen de la región definida por: 
$$y=\sqrt{x^2 + z^2}$$ Y los planos: 

$$x + z = 0\;;\;y = a\;;\;a>0\;;\;z\geq -x$$ 
### Problema 6

Calcular el volumen de la región limitada por

$$y\geq\sin(z)\;;\;y=z\;;\;y=\pm\pi\;;\;x=\pm 1$$

### Problema 7

Calcular el volumen exterior a la esfera $x^2 + y^2 + (z-2)^2 = 20$ e interior al cono $z=8-\sqrt{x^2+y^2}$  y $z\geq 0$. 

### Problema 8

Calcular el volumen de la región limitada por $x\geq\sin(z)$ y $x\leq 2+\cos(z+\frac{\pi}{2})$

### Problema 9 

Calcular el volumen exterior a la esfera $x^2 + y^2 + (z-2)^2 = 4$ e interior al cono $z = 8 -\sqrt{x^2 + y^2}$ 

### Problema 10 

Calcular el volumen de la región limitada por $y=xz$ y $x^2 + z^2 = 9$ 

### Problema 11 

Calcular $$\int\int^{}_{D}x-y + 1\;dA$$ con $D$ definida por las gráficas de: 

$$y = (x-1)^3 + 1$$ $$y = \sqrt[3]{x-1} + 1$$ 
#### Solucion 

1 (no ocupar polares)


### Problema 12 

Hallar el [[Volumen|volumen]] de la región limitada por $z=\sqrt{3}\;;\;z=0$ y por el hiperboloide $x^2 + y^2 - z^2 = 1$. 

### Problema 13 

Calcular el volumen del sólido definido por $z=x^2 + y^2\;\land\; z = 1$ usando [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Coordenadas esféricas|coordenadas esféricas]]. 

### Problema 14 

Evaluar la integral 

$$\int\int\int^{}_{S}\sqrt{x^2 + y^2 + z^2}\;dv$$ 
donde $S$ es la integral región determinada por $z=\sqrt{x^2 + y^2}\;\land\; x^2 + y^2 + z^2 = 2az$ 
