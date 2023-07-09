
Recordando la noción de preimagen de *Introducción al Álgebra* podemos definir una función $f:A\rightarrow B$ y su preimagen denotada por el conjunto: 

$$ f^{-1}(C):=\lbrace x\in A\;:\; f(x)\in C\rbrace $$ 
Por definición sabemos que $f^{-1}(C)$ es subconjunto de $A$. 

## Teorema 

Si una función $f:A\subset\mathbb{R}^n\rightarrow\mathbb{R}^p$ es [[Continuidad en varias variables|continua]] en $A$, entonces la preimagen de todo [[Conjuntos abiertos y cerrados|conjunto cerrado]] en $\mathbb{R}^p$  es un conjunto cerrado incluido en A. 

### Demostración 

Supongamos que $f$ es [[Continuidad en varias variables|continua]] en $A$. Sea $C\subset\mathbb{R}^p$ un conjunto cerrado en $\mathbb{R}^p$ y problemos que $f^{-1}(C)$ es también cerrado en A. Para ello, tomamos una [[Sucesiones en varias variables|sucesión]] $(x_n)$ definida en $f^{-1}(C)$ y que converge a un cierto $x\in\mathbb{R}^d$. La idea es probar que $x\in f^{-1} (C)$. 

Como $f$ es [[Continuidad en varias variables|continua]] tenemos que $f(x_n)\rightarrow f(x)$ está bien definida. Y, por la definición de preimagen, $f(x_n)\in C$ es cerrado, por lo tanto, $x\in f^{-1} (C)$ 