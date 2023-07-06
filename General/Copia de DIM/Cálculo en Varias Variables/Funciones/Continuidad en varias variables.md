Una función $F:A \subset \mathbb{R}^n \rightarrow \mathbb{R}^m$ es [[Función continua|continua]] en $\bar{x} \in A$ si para toda sucesión $(X_k) \subset A$ tal que $x_k \rightarrow \bar{x}$ se tiene que $F(x_k) \rightarrow F(\bar{x})$. Esta definición es muy similar a la definición de [[Función continua|continuidad]] en una variable pero de forma extendida. 

Diremos que $F$ es continua en el conjunto $A$ si lo es en todo punto de $A$. 

## Proposición: linealidad

Aca también se cumple el álgebra de funciones continuas. Sea $A \subset \mathbb{R}^n$ y $x\in A$. Supongamos que las aplicaciones $h,g: A \rightarrow \mathbb{R}^m$ son continuas en $x \in A$ y sean $\alpha, \beta \in \mathbb{R}$ [[escalares]] cualesquiera. Entonces: 

$$\alpha h + \beta g: A \rightarrow \mathbb{R}^m \;\;\text{tambien es continua}$$ 
Para el caso $m=1$ se cumple que: 
1) $hg: A \rightarrow \mathbb{R}$ es continua en $x$. 
2) $\frac{h}{g}: A\rightarrow\mathbb{R}$ es continua en $x$ siempre cuando $g(x) \neq 0$. 

La demostración se hace por **álgebra de límites**. 

## Ejemplo (discontinuidad): 

Determinar los puntos de $R^2$ donde la función $f(x)$ es continua:

-Si $(x,y) \neq (0,0): f(x,y) = \frac{x^2 - y^2}{x^2 + y^2}$ 
-Si $(x,y) = (0,0): f(x,y) = 0$ 

Claramente es continua en el conjunto $\mathbb{R}^2 / {(0,0)}$ por álgebra de continuas. Por lo tanto, basta analizar el punto $(\bar{x}, \bar{y}) = (0,0)$. 

Consideremos las [[Sucesiones en varias variables|sucesiones]]: 

$$(x_k , y_k) = (0, \frac{1}{k})\;\;\land\;\;(\bar{x_k},\bar{y_k})=(\frac{1}{k},0) $$ 
En este caso tenemos que: 

$$ (x_k, y_k) \rightarrow (0,0)$$ $$(\bar{x_k}, \bar{y_k}) \rightarrow (0,0)$$ 
Pero notemos lo siguiente: 

$$f(x_k, y_k) = \frac{-(1/k)^2}{(1/k)^2} = -1$$ $$ f(\bar{x_k}, \bar{y_k}) = \frac{(1/k)^2}{(1/k)^2} = 1$$ 
Lo anterior nos dice que el límite $\lim_{(x,y)\rightarrow\infty} f(x,y)$ no existe. Por lo tanto, la función no es continua en el punto $(0,0)$. 

## Ejemplo: continuidad 

Consideremos la función $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ definida por: 

-Si $(x,y) \neq (0,0): f(x,y) = \frac{|x|^3}{x^2 + y^2}$ 
-Si $(x,y) = (0,0): f(x,y) = 0$ 

Lo resolvemos acotando y por **teorema del Sandwich**: 

Notar que: 

$$ 0 \leq |x| |x|^2 \leq |x| (x^2 + y^2) $$ $$\implies 0 \leq f(x,y) = \frac{|x|^3}{x^2 + y^2} \leq |x|$$ 
Sea $(x_k, y_k) \rightarrow (0,0)$. Esto es equivalente a que $x_k\rightarrow 0\;\; \land y_k \rightarrow 0$. Luego de la desigualdad anterior, por **teorema del Sandwich** llegamos que: 

$$ 0 \leq f(x_k, y_k) \leq |x_k| $$

Por lo tanto: 

$$ f(x_k, y_k) \rightarrow 0 = f(0,0) $$ 