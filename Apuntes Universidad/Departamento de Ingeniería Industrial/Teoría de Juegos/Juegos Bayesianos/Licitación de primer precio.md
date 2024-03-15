
Asumimos valores privados, ofertas sobre-cerrado donde hay sólo $2$ oferentes. El valor para un oferente $i$ es $v_i\geq 0$ que viene de una [[Distribución Uniforme|distribución uniforme]] entre $[0,1]$. $v_i$ es el máximo precio que el oferente está dispuesto a pagar. 

La estrategia de un oferente $i$ es una función $s_i:[0,1]\to[0,1]$ de los posibles valores a las ofertas. Es decir, un oferente con valor $v_i$ ofrecerá $s_i(v_i)=b_i$. 

Si un oferente $i$ gana el objeto, su pago será $v_i-b_i$. 

Supongremos que ambos oferentes usarán la misma estrategia $s(v_i)$ y que la estrategia es creciente y diferenciable. Por lo tanto: 

$$u_i(b_i,b_j)=\begin{cases}v_i-b_i&\text{si}\;b_i>b_j\\  \\
\frac{v_i-b_i}{2}&\text{si}\;b_i=b_j\\  \\
0&\text{si}\;b_i<b_j\end{cases}$$

Entonces, los [[Pagos|pagos esperados]] cuando amvos usan la estrategia $s$ llegaría a ser: 

$$\begin{align}
EU_i(b_i,v_i,s)&=(v_i-b_i)\mathbb{P}(\text{Gana}\;i)+ 0\cdot\mathbb{P}(\text{Gana}\;j)+\frac{v_i-b_i}{2}\mathbb{P}(\text{Empate})
\end{align}$$

Dado que la probabilidad de la distribución uniforme es $0$ para valores únicos y las estrategias son estrictamente creciente, entonces: 

$$EU_i(b_i,v_i,s)=(v_i-b_i)\mathbb{P}(\text{Gana}\;i)$$

Notemos que no se puede empatar por la [[Función de Densidad de Probabilidad (PDF|función de densidad de probabilidad (PDF)]], vale decir: 

$$\mathbb{P}(v_i=v_j)=\int^{v_i}_{v_j}f(v_y)dy=0$$

Notemos que gane $i$ es equivalente a decir $v_j<s^{-1}(b_i)$. Como $v_j$ es una distribución uniforme sobre $[0,1]$, se llega que: 

$$EU_i(b_i,v_i,s)=(v_i-b_i)s^{-1}(b_i)$$

Si ahora imponemos condición de primer orden al tomar la [[Derivada parcial|derivada parcial]] (notar que tenemos una función inversa): 

$$\begin{align}
\frac{\partial EU_i}{\partial b_i}&=(-1)s^{-1}(b_i)+v_i\frac{ds^{-1}(b_i)}{db_i}-b_i\frac{ds^{-1}(b_i)}{db_i}
\end{align}$$

Si se usa regla de la derivada de la función inversa, se llega que: 

$$\begin{align}
\frac{\partial EU_i}{\partial b_i}&=(-1)s^{-1}(b_i)+(v_i-b_i)\frac{1}{s'(s^{-1}(b_i)}=0
\end{align}$$

Por lo tanto, se tiene una [[EDO lineal de orden n|ecuación diferencial lineal]], donde se tiene que: 

$$-v_i + (v_i-s(v_i))\frac{1}{s'(v_i)}=0$$

Y, además: 

$$v_is'(v_i)+s(v_i)=v_i$$

Si se toma la [[Integral de Riemann|integral]] a ambos lados, se tiene que: 

$$s(v_i)=\frac{v_i}{2}$$ 
Vale decir, **los oferentes ofrecen la mitad de su valor verdadero**. 