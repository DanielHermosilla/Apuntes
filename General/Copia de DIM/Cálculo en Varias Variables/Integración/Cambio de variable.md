### Motivación 

Consideremos la [[transformaciones lineales|aplicación lineal]]: 

$$T(x,y)=(2x-y,\frac{1}{2}x + \frac{3}{2}y)$$ 
Definida sobre $R=[0,1]\times [0,2]$. 

Es decir, la siguiente transformación lineal: 

![[IMG_D8BF3B609B89-1.jpeg|center|700]]

Notemos que la representación [[matriz|matricial]] de $T$ en la [[Base|base canónica]] es: 

$$T=\begin{bmatrix}
2 & -1\\
\frac{1}{2} & \frac{3}{2}\\
\end{bmatrix}$$

$$\implies\text{det(T)}=\frac{7}{2}$$ 
Así, tenemos que: 

$$7=\text{Área}(T(R))=\text{Área}(R)det(T)$$
$$ \dots = 2\;\frac{7}{2}$$$$\dots = 7$$ 
Esta igualdad se puede extender para cualquier [[Integral sobre rectángulos|rectángulo]] $R\subset \mathbb{R}^n$ y obtener para una [[transformaciones lineales|transformación lineal]] $T:R\rightarrow T(R)$ la identidad respecto a los [[Volumen|volumenes]], es decir: 

$$Vol(T(R)) = Vol(R)det([T])$$ 
## Teorema del cambio de variable 

Sea $A\subset\mathbb{R}^n$ un conjunto [[Conjuntos abiertos y cerrados|abierto]] y [[Conjuntos compactos|acotado]]. Vamos a considerar una función $g:A\rightarrow\mathbb{R}^n$ una función de clase $C^1$ en $A$ e **inyectiva** sobre $A$. 

Si $f:g(A)\rightarrow\mathbb{R}$ es [[Integral en varias variables|integrable]] sobre $g(A)$; entonces: 

$$\int^{}_{g(A)}f(y)\;dy=\int^{}_{A}(f\; o\;g)(x)\;|det\;g'(x)|\;dx$$ 
Donde $g'(x)$ es la [[matriz Jacobiana]]. 

### Aplicaciones: coordenadas polares

Podemos ocupar [[Coordenadas polares|coordenadas polares]]. Es decir; 

![[IMG_8C3D6744493E-1.jpeg|center]]

Tenemos que la [[matriz Jacobiana]] de este cambio de variable es: 

$$g'(r,\theta) = \begin{bmatrix}

\cos\theta & -r\sin\theta \\ 
\sin\theta & r\cos\theta \\ 

\end{bmatrix}$$ 
Por lo tanto, el [[determinante]] sería: 

$$\implies det(g'(r,\theta)) = r$$ 
### Ejemplo 

Calcular el área de la elipse $\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2}\leq1$

Entonces, defino mis cambios de variables trasladando el origen con las [[Coordenadas polares|coordenadas polares]]: 

$$x= h + r\cos\theta\;\land\; y=k + r\sin\theta$$ 
![[IMG_17120E8FFB26-1.jpeg|center]] 

Si lo reemplazamos en la función original, nos queda $\frac{r^2\cos^2\theta}{a^2} + \frac{r^2\sin^2\theta}{b^2} = 1$ .Queremos saber ahora como se comporta el valor $r$. Entonces, ocupo el siguiente cambio de variable, multiplicando por $a$ y $b$: 

$$x = h + \boldsymbol{a}r\cos\theta\;\land\;y = k +\boldsymbol{b}r\sin\theta$$ 
Entonces la [[matriz Jacobiana]] quedaría como: 

$$g'(r,\theta) =\begin{bmatrix}
a\cos\theta & -ar\sin\theta \\ 
b\sin\theta & br\cos\theta
\end{bmatrix}$$

$$\implies det(g'(r,\theta)) = abr$$ 
 ![[IMG_D03F832FCE8A-1.jpeg|center]]

Así, 

$$\int^{}_{R}1=\int^{1}_{0}\int^{2\pi}_{0}1\;abr\;d\theta\;dr = ab2\pi\int^{1}_{0}r\; dr = 2ab\pi\frac{r^2}{2}\bigg\lvert_{0}^{1}=ab\pi$$

### Ejemplo  

Calcular el volumen de la región límitada por: 

$$0\leq z\leq 9-x^2-y^2$$ 
Y sobre la región exterior a $x^2 + y^2 = 1$ e interior a $x^2 + y^2 = 9$. 

![[Captura de Pantalla 2023-01-10 a la(s) 13.46.50.png|center]]

Sería equivalente a calcular el [[Volumen|volumen]] de esto sin un cilíndro en el medio. 

Usamos el cambio de variable cilíndrico:

$$ 
\text{Cilíndricas}=\begin{cases} 
       x =r\cos\theta \\
	   y=r\sin\theta\\
	   z=z
   \end{cases}
$$

Entonces la [[matriz Jacobiana]] sería: 

$$J(r,\theta,z) = \begin{bmatrix} \cos\theta & -r\sin\theta & 0 \\ 
\sin\theta & r\cos\theta & 0 \\ 
\theta & 0 & 1 \end{bmatrix} = r$$ 
Con este cambio de variable la región está descrita por: 

$$1\leq r\leq 3$$
$$0\leq\theta\leq 2\pi$$ $$0\leq z\leq 9-r^2$$ 
Por lo tanto, el volumen buscado es: 

$$Vol(R)=\int^{3}_{1}\int^{2\pi}_{0}\int^{9-r^2}_{0}r\; dz\; d\theta\; dr$$ Ya que $r$ es el valor del [[determinante]] de la [[matriz Jacobiana]]. 