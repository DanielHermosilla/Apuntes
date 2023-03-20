
Si se quisiera calcular la función exponencial sin ocupar los métodos nativos, se podría ocupar una descomposición binaria de los números para optimizar el código. 

Antes que nada, notar que un número siempre se puede representar en función de potencias de $2$. Por ejemplo:

$$77 = 2^6 + 2^3 + 2^2 + 2^0$$ 
Entonces el número en binario se escribiría de la siguiente forma: $1001101$ donde los $0$ representa si no exisste la potencia de $2$ y el $1$ la existencia. 

Entonces, si se quiere calcular $x^{77}$ lo descomponemos a binario: $x^{77} = x^{64 + 8 + 4+ 1}$. Entonces el algoritmo parte multiplicando $x$ por si mismo y sucesivamente en múltiplos de $2$. Es decir: 

$$x\times x=x^2$$ $$x^2\times x^2 = x^4$$ $$x^4\times x^4 = x^{16}$$ $$\vdots$$ $$x^{32}\times x^{32} = x^{64}$$
Y paramos cuando llegamos al máximo exponencial en binario.  De ahi basta con multiplicar los valores necesarios para llegar a 77, es decir, $x^{77} = x^{64 + 8 + 4+ 1}$.

Entonces, tomando como [[Invariantes|invariante]] a $z^k=(z^2)^{k/2}$, se puede lograr lo siguiente: 

```Python 

def potencia(x, n):

	y=1
	k=n
	z=x
	
	while k>0:
	
		if k%2==0: # caso k par
		
			z=z*z
			k//=2
	
		else: # caso k impar
	
			y*=z
			k-=1
	
	return y

```
