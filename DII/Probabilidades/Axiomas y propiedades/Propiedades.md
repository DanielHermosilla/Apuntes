
### Probabilidad del complemento 

Corresponde al siguiente enunciado
$$\mathbb{P}(A^c)=1-\mathbb{P}(A)$$ 
Esto se demuestra por los [[Axiomas|axiomas]]: 

$$1=\mathbb{P}(\Omega)=\mathbb{P}(A\bigcup A^c)$$
$$ = \mathbb{P}(A) + \mathbb{P}(A^c)$$ 
### Probabilidad del vacio 

Corresponde al siguiente enunciado
- $$\mathbb{P}(\emptyset)=0$$
Esto se desmuestra por la propiedad anterior:

$$\mathbb{P}(\emptyset)=\mathbb{P}(\Omega^c)$$
$$= 1 - \mathbb{P}((\Omega^c)^c)$$$$= 1 - \mathbb{P}(\Omega)$$$$ 0 = 1 - 1$$ 
### Monotonía 

El [[Conjuntos|subconjunto]] de un [[Evento|evento]] tiene menos probabilidad que el evento en sí: 

$$A\subset B\implies\mathbb{P}(A)\leq\mathbb{P}(B)$$ 
Demostrándose por la propiedades de [[Conjuntos|conjuntos]]: 

$$\mathbb{P} = \mathbb{P}((B\cap A)\cup(B \ A))$$
$$ = \mathbb{P}(A)+\mathbb{P}(B\backslash a)\leq\mathbb{P}(A)$$

### Resta: 

La resta de dos probabilidades es la resta de la primera con la intersección: 

$$\mathbb{P}(A\backslash B)=\mathbb{P}(A)-\mathbb{P}(A\cap B)$$ 
### Principio inclusión-exclusión 

La probabilidad de la unión de dos eventos corresponde a lo siguiente, dado a la posibilidad de ser disjuntos: 

$$\mathbb{P}(A\cup B) = \mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$$ 
Demostración: 

$$\mathbb{P} = \mathbb{P}(A\cup(B\backslash A))$$
$$=\mathbb{P}(A)+\mathbb{P}(B\backslash A)$$$$=\mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A\cap B)$$ 
También se puede escribir de la **forma general**: 

$$\mathbb{P}(\bigcup_{i=1}^{n}A_i)=\sum_{i=1}^{n}\mathbb{P}(A_i)-\sum_{i<j}\mathbb{P}(A_i\cap A_j) + \sum_{i<j<k}\mathbb{P}(A_i \cap A_j\cap A_k)\mp\dots (-1)^{n+1}\ \mathbb{P}(\bigcap_{i=1}^{n}A_i)$$ 