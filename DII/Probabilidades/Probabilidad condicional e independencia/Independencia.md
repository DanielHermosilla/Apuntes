
Los [[Evento|eventos]] son independientes si y solo si: 

$$P(A\cap B)=P(A)\; ·\;P(B)$$ 
### Ejemplo 

Lanzo un dado dos veces, sea $x_1$ el resultado del primer lanzamiento, y $x_2$ el resultado del segundo. Sea: 
- $A_1$ la probabilidad de sacar un 5 o un 6 en el primer lanzamiento  
- $A_2$ la probabilidad sacar un 5 o un 6 en el segundo lanzamiento 
- 
¿Qué puedo decir de $P(B|A)$? 

Por definición de [[Probabilidad Condicional|probabilidad condicional]]: 

$$P(B|A) = \frac{P(B\cap A)}{P(A)} = \frac{P(A)\; ·\;P(B)}{P(A)} = P(B)$$ 
## Independencia para *n* eventos 

Podemos verificar que si hay independencia, se cumple que: 

$$P(A_1\cap A_2\cap \dots A_n) = P(A)\; · \; P(A_1)\; · \;\dots P(A_n)$$ 
Además, se debe cumplir la independencia para cada par por separado, es decir:

$$P(A_1\cap A_2) = P(A_1)\; ·\; P(A_2)$$
$$P(A_1\cap A_3) = P(A_1)\; ·\; P(A_3)$$
$$\vdots$$$$P(A_1\cap A_n) = P(A_1)\; ·\; P(A_n)$$

Y así con todos los pares

## Caso con distintos [[Espacio muestral|espacios muestrales]]

Se puede tener un problema con un dado y una moneda, donde $\Omega_1=\lbrace c,s\rbrace$ y $\Omega_2 = \lbrace 1,2,3,\dots,6\rbrace$. 

Por lo tanto, "$A\cap B$ " en realidad representaría $(A\times \Omega_2)\cap (\Omega_1\times B)$ 

## Propiedades 

Si $A,B$ son independientes $\implies A,B^C \land A^C,B\land B^C,A^C$ son independientes. 