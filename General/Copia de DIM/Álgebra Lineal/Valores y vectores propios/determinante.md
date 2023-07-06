A partir del calculo de los [[valor propio|valores propios]] se introduce el concepto de determinante para poder obtener un polinomio que nos pueda dar los coeficientes de cada [[valor propio]]. 

El determinante es un valor real que se le asignará a una [[matriz]] que además nos dirá si es invertible o no. 

Por lo tanto, definiremos determinante como: 

1.  Si $A$ es de $1 \times 1 \enspace |A| = a$ donde $A = a$  
2. Si $A$ es de $n \times n \enspace |A| = \sum_{i=1}^{n} (-1)^{i+1} a_{i1} |A^{i1}|$

La fórmula pareciera ser muy confusa, pero se puede extrapolar del caso $2 \times 2$ al más general. 

### Caso $2 \times 2$ 

Sea la siguiente [[matriz]]: 
$$ \begin{bmatrix} a & b \\ c & d \end{bmatrix} $$
Entonces, su determinante es la multiplicación cruzada de sus diagonales y la resta. Es decir: 

$$ ad - bc =\text{determinante} $$ 
### Caso general 

Sea una [[matriz]] $3 \times 3$, entonces tenemos lo siguiente: 

$$ \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & j\end{bmatrix} $$

Por lo tanto, desde aquí tenemos que tomar **pivotes** e ir calculando sus determinantes. Es decir, nos *paramos* en una fila o columna y empezamos a calcular las determinantes de las matrices restantes. Tomemos como ejemplo la primera fila; partiríamos con $a$ como pivote: 

1) Primer pivote: 

$$ \begin{bmatrix} \cancel{\mathbf{a}} & \cancel{b} & \cancel{c} \\ \cancel{d} & e & f \\ \cancel{g} & h & j\end{bmatrix} \implies \det \begin{bmatrix} e & f \\ h & j \end{bmatrix} \implies a(ej - fh) $$

2) Segundo pivote: Análogo al proceso anterior, ~~tachamos~~ las filas y columnas correspondientes al siguiente pivote. Eso si, los signos se van **intercalando**. Es decir, si en el primer cálculo hicimos el cálculo del determinante tal y como es, al segundo se le invierten los signos y así sucesivamente. Entonces: 

$$ \begin{bmatrix} \cancel{a} & \cancel{\mathbf{b}} & \cancel{c} \\ d & \cancel{e} & f \\ g & \cancel{h} & j\end{bmatrix} \implies -\det \begin{bmatrix} d & f \\ g & j \end{bmatrix} \implies b(gf - dj) $$
3) Tercer pivote: 
$$ \begin{bmatrix} \cancel{a} & \cancel{b} & \cancel{\mathbf{c}} \\ d & e & \cancel{f} \\ g & h & \cancel{j}\end{bmatrix} \implies -\det \begin{bmatrix} d & e \\ g & h \end{bmatrix} \implies c(dh - ge) $$

4) Suma de los cálculos: Como último paso, se suman todos los cálculos obtenidos. Si la matriz hubiera sido de dimensiones mayores que $3 \times 3$ probablemente se necesitaría seguir pivoteando. Por lo tanto: 


$$ \det\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & j\end{bmatrix} = a(ej - fh) + b(gf - dj) + c(dh - ge) $$

Como se puede apreciar, existen **varías formas** de calcular la determinante. Es más, se puede elegir pivotear tanto por filas como columnas. El truco está en elegir la fila o columna a conveniencia, es decir, la que nos simplifique más los cálculos. Siempre buscar aquellos valores donde existen *ceros* para poder anular algunos cálculos de determinantes. 

Existen varias **proposiciones importantes** de las determinantes, pero la más importante es la siguiente: 

$$ A \enspace\text{es invertible si y sólo si}\enspace \det A \neq 0 $$ 
A partir de esto, podemos obtener el [[polinomio característico]] que nos facilitará el cálculo de los [[valor propio|valores propios]]. 

## Propiedades 

1. Sea la siguiente matriz: 

$$ A = \begin{bmatrix} a_{11} & \dots & a_{1n} \\ \vdots & \vdots & \vdots \\ a_{k1} + b_{k1} & \dots & a_{kn} + b_{kn} \\ \vdots & \vdots & \vdots \\ a_{n1} & \dots & a_{nn} \end{bmatrix} $$

Entonces: 

$$ \det A = \det \begin{bmatrix} a_{11} & \dots & a_{1n} \\ \vdots & \vdots & \vdots \\ a_{k1}  & \dots & a_{kn} \\ \vdots & \vdots & \vdots \\ a_{n1} & \dots & a_{nn} \end{bmatrix} + \det \begin{bmatrix} a_{11} & \dots & a_{1n} \\ \vdots & \vdots & \vdots \\  b_{k1} & \dots & b_{kn} \\ \vdots & \vdots & \vdots \\ a_{n1} & \dots & a_{nn} \end{bmatrix} $$ 
Esta propiedad se ocupa muy poco, pero podría llegar a ser util para el cálculo de determinantes grandes. Esto se prueba mediante inducción. 

2. Si $B$ se obtiene de $A$ permutando dos filas, entonces $\det B = -\det A$. A esto se le denomina una **[[función]]  alternada**. 

3. Si $A$ tiene dos filas iguales, entonces $\det A = 0$. 

4. **Determinante de la identidad**: Siempre es 1, independiente de su dimensión. Esto nos comprueba otra vez más que la identidad si es invertible. 

5. Si amplificamos alguna fila por algun factor, la determinante no cambia. 