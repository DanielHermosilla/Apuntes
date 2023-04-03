
Método de diseño de algoritmos que se basa en subdividir el problema en sub-problemas y resolverlos recursivamente para luego combinar el las soluciones. 

### Ejemplo: multiplicación de polinomios

Sean dos polinomios a multiplicar: 

$$

A(x) = a_0+a_1 x+a_2 x^2 + \ldots + a_{n-1}x^{n-1}

$$
$$

B(x) = b_0+b_1 x+b_2 x^2 + \ldots + b_{n-1}x^{n-1}

$$

Normalmente para resolverlo es multiplicar cada término de $A(x)$ por los de $B(x)$. Pero eso es muy ineficiente. 

Se podría simplificar al dividir, por ejemplo: 

$$
A(x)=2+3x-6x^2+x^3
$$
$$ A(x)=(2+3x) + (-6+3x)x^2 $$ 
Entonces, en general se puede reescribir como 

$$

A(x) = A'(x)+A''(x)x^{n/2}

$$
$$

B(x) = B'(x)+B''(x)x^{n/2}

$$
$$

C = A'B'+(A'B''+A''B')x^{n/2}+A''B''x^n

$$

Si se llama $T(n)$ el número de operaciones, se podría ocupar el [[El teorema Maestro|teorema Maestro]] para calcular la eficiencia del algoritmo: 

$$

T(n) = 4T \left(\frac{n}{2}\right)+Kn

$$

Y se llega que $$

T(n)=\Theta(n^2)

$$
Lo que no es mejor que el algoritmo anterior, pero si se define lo siguiente:

$$

\begin{align}

D &= (A'+A'')(B'+B'')\\

E &= A'B'\\

F &= A''B''

\end{align}

$$

Y entonces, llegar que: 
$$

C = E+(D-E-F)x^{n/2}+Fx^n

$$

Utilizando solo 3 multiplicaciones recursivas, implicando que la ecuación sería: 

$$

T(n) = 3T \left(\frac{n}{2}\right)+Kn

$$

Y por el [[El teorema Maestro|Teorema Maestro]] se llega que 
$$
T(n)=\Theta(n^{\log_2{3}}) \approx \Theta(n^{1.59})
$$

Un algoritmo un poco más eficiente. Esto se llama *Algoritmo de Karatsuba*. 