
Sea $X\in VA$  y $a,b\in\mathbb{R}$.

¿Cual sería la [[Esperanza|esperanza]] de $E[aX + b]$? 

Notemos que la [[Esperanza de una función de variable aleatoria|esperanza de una función de variable aleatoria]] nos permite definir $aX + b$ como una función auxiliar. Es decir, $g(x) = aX + b$. Entonces, se calcula $E[g(x)]$. 

Por lo tanto, 

$$E[g(x)] = \sum_{x\in R_x}(aX + b)P_x(x)$$ 
$$=a\sum_{x\in R_x} xP_x(x) + b\sum_{x\in R_x}P_x(x)$$ $$=aE[X] + b$$ 
Esto nos demuestra la **linealidad de la esperanza**. 