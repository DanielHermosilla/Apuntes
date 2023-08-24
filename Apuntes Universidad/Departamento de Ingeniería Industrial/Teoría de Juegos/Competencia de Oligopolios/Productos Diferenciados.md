
Asumamos un modelo lineal, del $0$ a $1$, donde cada punto es un consumidor y cada consumidor va a comprar una unidad del producto. 

![[Pasted image 20230824102126.png|center]]

Por lo tanto, la distancia entre el consumidor y la firma representa el gusto del consumidor y la característica de la firma. 

La estrategia es un precio no-negativo, $p_i\in\mathbb{R}_+$ y cada consumidor tiene que caminar una distancia $x$ para comprar $A$ o una distancia $(1-x)$ para comprar $B$. Suponemos que caminar es costoso, donde el costo es $t\cdot d^2$ donde $d$ es la distancia y $t$ es un parámetro positivo. 

Entonces, para el consumidor $x$, comprar $A$ cuesta $p_A+tx^2$ y comprar $B$ cuesta $p_B+t(1-x)^2$. Si el consumidor es indiferente entre $A$ y $B$, entonces: 

$$\begin{align}
p_A+tx^2&=p_B+t(1-x)^2\\  \\
p_A+tx^2&=p_B+t-2tx+tx^2\\  \\
p_A&=p_B + t - 2tx\\  \\
x&=\frac{1}{2}+\frac{p_B-p_A}{2t}
\end{align}$$

Entonces $\frac{1}{2}+\frac{p_b-p_A}{2t}$ de los consumidores comprarían $A$, por el otro lado $\frac{1}{2}-\frac{p_B-p_A}{2t}$ comprarían de $B$. De la misma forma, los beneficios llegarían a ser: 

$$\Pi(p_A,p_B)=\begin{cases}p_A\left[\frac{1}{2}+\frac{p_B-p_A}{2t}\right]&\text{Beneficio de A}\\  \\
p_B\left[\frac{1}{2}+\frac{p_B-p_A}{2t}\right]&\text{Beneficio de B}\end{cases}$$

Como las firmas son simétricas, en el [[Departamento de Ingeniería Industrial/Teoría de Juegos/Formalidades Técnicas/Equilibrio de Nash|Equilibrio de Nash]] la [[La mejor respuesta|mejor respuesta]] es $t$.  Sin embargo, en este modelo *idealizado*, se podría tener una firma en cualquier punto de la línea: 

![[Pasted image 20230824103048.png|center]]

