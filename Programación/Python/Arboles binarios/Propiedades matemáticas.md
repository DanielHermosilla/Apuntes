
### Relación entre nodos internos y externos

Sea $e_n$ el número de nodos externos de un árbol binario con $n$ nodos internos, entonces $e_n = n + 1$ 

### Relación entre largo de caminos internos y externos 

El largo de los caminos internos, denominado *LCI*  y denotado por $I_n$ se define como: 

$$I_n = \sum^{}_{x\in\text{Nodos internos}}\text{Distancia(Raiz,x)}$$ 
De manera análoga, el largo de los caminos externos, *LCE*, se denota como $E_n$ y se define como: 

$$E_n = \sum^{}_{y\in\text{Nodos externos}}\text{Distancia(Raiz,y)}$$ 
Es decir, la suma de las distancias desde la raiz hasta las hojas, o bien, nodos externos. 

Además, se cumple la siguiente propiedad: 

$$E_n = I_n + 2n$$ 
### Enumeración de árboles binarios con n nodos 

Si se tienen $n$ nodos indistiguibles, se llama $a_n$ al número de árbooles binarios distintos que podemos construir se guía por la siguiente fórmula: 

$$a_n = \sum^{}_{0\leq k\leq n-1}a_ka_{n-k-1}$$ 
Con la condición inicial $a_0 = 1$ 