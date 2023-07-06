Sea $y = f(x)$ la ecuación de una curva. Nos interesaría obtener una expresión para el **largo de la curva**. Es decir, la medición total de una curva si la tomaramos y la estiramos por completo. 

Para calcular esto, consideraremos una [[Partición|partición]] $Q = \lbrace x_0, \dots, xn \rbrace$ donde consideraremos la [[Distancia entre dos puntos]] bajo la siguiente fórmula: 
$$ d(x_i, x_{i+1}) = \sqrt{ (x_i - x_{i+1})^2 + (f(x_i) - f(x_{i+1}))^2 } $$ ````
```ad-info
color: 200, 200, 200

Nota que la fórmula de la distancia se obtiene a través del [[teorema de Pitágoras]] 

````

Gracias a una aplicación del [[Teorema del Valor Medio]] podemos decir que $\exists \xi$ tal que:
$$ f(x_i) - f(x_{i+1}) = f'(\xi)(x_i - x_{i-1}) \space \space \xi \in (x_i, x_{i+1}) $$
De esta manera, podemos reemplazar lo siguiente en la fórmula de la distancia, así obteniendo lo siguiente: $$ d = (x_i - x_{i-1}) \sqrt{1 + (f'(\xi))^2} $$ Entonces, expresandolo como una [[Suma de Riemann|suma de Riemann]] podemos decir que la **longitud del Arco de la Curva** equivale a: $$ L = \int^{b}_{a}\sqrt{1 + (f'(x))^2} \space dx $$ A partir de esto podemos obtener el [[Manto de revolución]]. A todo esto es trivial saber que

#Aplicación 

 