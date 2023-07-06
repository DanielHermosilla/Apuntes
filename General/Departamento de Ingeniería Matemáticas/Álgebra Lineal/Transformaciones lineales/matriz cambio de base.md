Cuando definimos la [[matriz representante]] nos pudimos percatar que dependía de las [[Base|bases]] de los [[subespacios vectoriales]] de las [[transformaciones lineales]]. Además, su cantidad de combinaciones, compuesta por el conjunto $\ell$, era, justamente, la multiplicación de las dimensiones de ambas bases. Por lo tanto, **no se tiene unicidad**. 

Entonces, sea $V$ un [[Espacios vectoriales]] sobre el cuerpo $K$, con $dim \space V = n$. Además, sea $\beta$ y $\beta^{'}$ dos bases de $V$. 

Claramente, los [[vectores]] de $\beta^{'}$ tiene una representación única en $\beta$ con sus respectivas [[coordenadas]]. 

$$ v_1^{'} = \alpha_{11} v_1 + \alpha_{21} v_2 + \dots + \alpha_{n1} v_n $$
$$ \vdots \space \space \space \space \space \space \space \space \space \space \space \space \space \space  \space \space \space \space \space \space \space \space \space \space \space \space \space \space \vdots \space \space \space \space \space \space \space \space \space \space \space \space \space \space  \vdots  $$
$$ v_2^{'} = \alpha_1j v_1 + \alpha_2j v_2 + \dots + \alpha_nj v_n $$
$$ \vdots \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \space \vdots \space \space \space \space \space \space \space \space \space \space \space \space \space \space  \vdots  $$
$$ v_n^{'} = \alpha_1n v_1 + \alpha_2n v_2 + \dots + \alpha_nn v_n $$

Por lo tanto, denominaremos a la matriz **cambio de base** a aquella [[matriz representante]] que nos muestra las [[coordenadas]] de $\beta$ sobre $\beta^{'}$, es decir, 

$$ M_{\beta^{'} \beta} (id_v) = \begin{bmatrix}
			\alpha_{11} & \dots & \alpha_{1j} & \dots & \alpha_{1n} \\ 
			 
			\vdots &  & \vdots & & \vdots \\ 
			\alpha_{n1} & \dots & \alpha_{nj}& \dots & \alpha_{nn}
		\end{bmatrix} \in M_{nn}( \kappa )$$

la matriz representante de la identidad de V, colocando como base de partida a $\beta^{'}$ y de llegada a $\beta$.  

### Composición de matrices

A partir de lo anterior podemos estudiar la relación entre distintas bases. Ahora, sea $U, U^{'}$ base de U, el conjunto de partida, y $V, V^{'}$ base de V, el conjunto de llegada. 

Por lo tanto, para estudiar la relación entre $M_{UV}$ y $M_{U^{'}V^{'}}$, cabe señalar lo siguiente: 
$$ id_{v} \space o \space T \space o \space id_u = T$$
Entonces, podemos llegar a la siguiente conclusión: 

$$M_{U^{'}V^{'}}(T) = M_{U^{'}V^{'}}(id_{v} \space o \space T \space o \space id_{u)}= M_{V V^{'}}(id_{v}) \space M_{UV}(T) \space M_{U^{'}{U}}(id_{v})$$

![[diagramacambiobase.jpeg|center|350]]


#concepto 