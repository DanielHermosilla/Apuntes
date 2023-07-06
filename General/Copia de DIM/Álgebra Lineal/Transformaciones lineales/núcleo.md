Sea  $T:U \rightarrow V$ una [[transformaciones lineales]], denotaremos el núcleo de $T$ como el conjunto: 
$$ Ker \space T = \lbrace x \in U \space | \space T(x) = 0 \rbrace $$ Claramente $Ker \space T \ne \emptyset$  ya que por definición de las [[transformaciones lineales]], $\exists T(0) = 0$ 

### Teorema 

Sea  $T:U \rightarrow V$ una [[transformaciones lineales]], entonces 
$$T \space es \space inyectiva \iff Ker \space T = \lbrace 0 \rbrace$$ 
###### Demostración 

$$ \implies ) \space \text{Dado} \space \in Ker \space T, \space T(u), T(u) = 0 = T(0). \text{Como T es inyectiva, se tiene u = 0} $$$$ \longleftarrow )\space \text{Sea }T(u_1) = T(u_2), \text{ por linealidad } T(u_1 - u_2) = 0. \text{ Luego }u_1 - u_2 \in Ker \space T = \lbrace 0 \rbrace, \text{ de donde } u_1 = u_2. $$ 
### Teorema 

Sea  $T:U \rightarrow V$ una [[transformaciones lineales]] **inyectiva**, entonces la [[combinación lineal]] de los elementos de $U$ es de [[dependencia]] independiente en $V$. 

Esto hace sentido, ya que cada elemento de la imagen es único, es decir, se le asigna una única combinación. 

#definición 