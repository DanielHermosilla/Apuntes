
Supongamos un polinomio definido por: 

$$

P(x) = \sum_{0\leq k\leq n}{a_k x^k}

$$

Entonces, una forma **no óptima** de calcular el polinomio sería la siguiente: 

```Python 

def evalp(a,x):

	"""Evalúa en el punto x el polinomio cuyos coeficientes son a[0], a[1],...
	
	Retorna el valor calculado
	
	"""
	
	P=0
	
	for k in range(0,len(a)):
	
	# Invariante: P=a[0]+a[1]*x+...+a[k-1]*x**(k-1)
	
		P += a[k]*x**k
	
	return P
```

Esto no tendría orden lineal, ya que hay una exponencial involucrada lo que implica un orden logarítmico. 

Pero, en cada iteración se tiene el valor $kesimo - 1$ , entonce, se podría guardar el valor anterior y no ir ocupando exponenciales: 

```Python 

	def evalp(a,x):
	
	"""Evalúa en el punto x el polinomio cuyos coeficientes son a[0], a[1],...
	
	Retorna el valor calculado
	
	"""
	
	P=0
	
	y=1
	
	for k in range(0,len(a)):
	
	# Invariante: P=a[0]+a[1]*x+...+a[k-1]*x**(k-1) and y=x**k
	
		P += a[k]*y
	
		y *= x
	
	return P
	```

En este caso, se guarda el valor en la variable *y*. 