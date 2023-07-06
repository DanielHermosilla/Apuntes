Es otra forma de cambiar las coordenadas que se basa en la proyección de los vectores. 

![[IMG_082BCBA99837-1.jpeg|center]]

En este caso llegaríamos a: 

$$\rho=\sqrt{x^2+y^2+z^2}$$ $$z =\rho\cos\phi\;\land\;y=\rho\sin\theta\sin\phi\;\land\;x=\rho\cos\theta\sin\phi$$
Y su [[matriz Jacobiana]] llegaría a ser: 

$$J(\rho,\theta,\phi)=\begin{bmatrix}
\cos\theta\sin\phi & -\rho\sin\theta\sin\phi & \rho\cos\theta\cos\phi \\ 
\sin\theta\sin\phi & \phi\cos\theta\sin\phi & \rho\sin\theta\cos\phi \\ 
\cos\phi & 0 & -\rho\sin\phi
\end{bmatrix} $$ 
Cuyo [[determinante]] llegaría a ser $-\rho^2\sin\phi$. 

### Ejemplo 

Calcular el volumen de la esfera $x^2 + y^2 + z^2 = R^2\;\;R>0$  

Por lo tanto, la proyección en el eje $x$ e $y$ sería un círculo $x^2 + y^2 = R^2$. Por lo tanto: 

![[IMG_9E30E80DC6B4-1.jpeg|center]] 

$$-R\leq x\leq R$$
$$-\sqrt{R^2-x^2}\leq y\leq\sqrt{R^2-x^2}$$ 
Además; 

$$-\sqrt{R^2-x^2-y^2}\leq z\leq\sqrt{R^2-x^2-y^2}$$ 
Por lo tanto, el volumen determinado por la esfera está dada por: 

$$\int^{}_{}\int\int_{S^2(0,z)}1=\int^{R}_{-R}\int^{\sqrt{R^2-x^2}}_{-\sqrt{R^2-x^2}}\int^{\sqrt{R^2-x^2-y^2}}_{-\sqrt{R^2-x^2-y^2}}dzdydx$$ $$\iff\int^{R}_{-R}\int^{\sqrt{R^2-x^2}}_{-\sqrt{R^2-x^2}}2\sqrt{R^2-x^2-y^2}dydx$$ 
Ya que la [[Integral en varias variables|integral]] se hace muy dificil se considera el cambio de [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Coordenadas esféricas|coordenadas esféricas]]. 

Note que $x^2 + y^2 + z^2 = \rho^2 = R^2$. Entonces se dice que $0\leq\rho\leq R$. 

Además, note que $0\leq\theta\leq 2\pi$, que se debe por la proyección: 

![[IMG_22B78201A92A-1.jpeg|center|600]]


Por último, tenemos que $0\leq\phi\leq\pi$. 

Así, usando el [[determinante]] de su [[matriz Jacobiana]] llegaría a ser $-\rho^2\sin\phi$.

Por lo tanto, obtenemos que el [[Volumen|volumen]] de la esfera $x^2 + y^2 + z^2 = R^2$ usando las coordenadas esféricas está dado por: 

$$\int\int\int^{}_{S^2(\vec{0},R)}1=\int^{R}_{0}\int^{2\pi}_{0}\int^{\pi}_{0}\rho^2\sin\phi\; d\phi d\theta d\rho$$ 
Acordándonos de que hay que integrar el módulo de la [[determinante]] de la [[matriz Jacobiana]]. Por lo tanto, resolviendo la [[Integral en varias variables|integral]] se llega a: 

$$V=\frac{4\pi R^3}{3}$$ 
### Ejemplo 

Calcular el [[Volumen|volumen]] dada por la región limitada por $x^2 + y^2 + z^2 = 1$ y $\frac{1}{2}\leq z\leq 1$. 

![[IMG_F4A014B7982D-1.jpeg|center|600]]


Consideremos el cambio de variable: 

$$x = \rho\cos\theta\sin\phi\;\land\; y = \rho\sin\theta\sin\phi\;\land\; z = \rho\cos\phi$$ 
Además, notas que $\rho\neq 1$ ya que estaríamos diciendo que $(0,0,0)=(0,0,0)$. Por lo tanto, calculamos el rango de $\rho$: 

![[IMG_B250C7A1E0CD-1.jpeg|center|590]]

Entonces llegamos que $\frac{1}{2\cos\phi}\leq\rho\leq 1$. 

Ahora para buscar el ángulo $\phi$ de la altura: 

![[IMG_0A05541953C5-1.jpeg|center|590]]

Por identidad trigonométrica llegamos que el máximo valor es $\frac{\pi}{3}$. Entonces: 

$$0\leq\phi\leq\frac{\pi}{3}$$ 
Por último tenemos sobre la proyección la siguiente desigualdad: 

$$0\leq\theta\leq 2\pi$$ 
De esta forma, el [[Volumen|volumen]] llegaría a ser: 

$$\int\int\int_V 1=\int^{2\pi}_{0}\int^{\frac{\pi}{3}}_{0}\int^{1}_{\frac{1}{2\cos\phi}}\rho^2\sin\phi\;d\rho d\phi d\theta$$ $$\iff 2\pi\int^{\frac{\pi}{3}}_{0}\frac{\sin\phi}{3}-\frac{1}{3\;2^3\;\cos^3\phi}\sin\phi\;d\phi=2\pi[-\frac{1}{6}+\frac{1}{3}-\frac{3}{48}]=\frac{10}{48}\pi$$ 

Notar que no se podría haber hecho con el cambio de variable [[Departamento de Ingeniería Matemáticas/Cálculo en Varias Variables/Integración/Cambio de variable|cilíndrica]], ya que llegariamos a lo siguiente: 

$$\frac{1}{2}\leq z\leq\sqrt{1-x^2-y^2}$$

Y la interseción de la base, es decir, $z=\frac{1}{2}$ con la condición, llegamos a: 

$$x^2+y^2+\frac{1}{4}=1\;\implies\; x^2+y^2=\frac{3}{4}$$ 
Así, tenemos que $r=\sqrt{\frac{3}{4}}$. Por lo tanto, el volumen de la región es: 

$$\int\int\int_V 1=\int^{2\pi}_{0}\int^{\frac{\sqrt{3}}{2}}_{0}\int^{\sqrt{1-r^2}}_{\frac{1}{2}}r\;dzdrd\theta$$ 