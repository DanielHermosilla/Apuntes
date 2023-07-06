Diremos que una función es continua en un punto cuando 

$$\forall(x_n)\subset A, x_n\rightarrow\bar{x}\implies f(x_n)\rightarrow f(\bar{x})$$ 
En simples términos, es cuando para toda sucesión que tiende  a un punto en el dominio tiene la misma imagen. Esto se puede corroborar facilmente con el cálculo de límites: Si el límite de la función tendiendo a tal punto hacia ambos lados coincide con la imagen entonces es **continua**. 

![[Captura de Pantalla 2022-12-06 a la(s) 20.59.28.png]]

En ese caso, la función es no continua 

## Caracterización epsilon-delta

Una forma para ver si una función es continua es bajo la caracterización epsilon-delta: 

$$\forall \epsilon > 0, \exists\delta>0, \forall x \in A \: [|x - \bar{x}] \leq \delta \implies |f(x) - (f\bar{x}) \leq \epsilon ] $$ 

