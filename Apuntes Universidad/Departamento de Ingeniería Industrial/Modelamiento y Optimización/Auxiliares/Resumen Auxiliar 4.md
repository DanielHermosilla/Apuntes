
Hiperplano corresponde al conjunto $H_{a.b}=\lbrace x\in\mathbb{R}^n:a^Tx=b\rbrace$

![[Pasted image 20240410162201.png|center]]

Un semi-espacio es el conjunto del tipo $S_{a,b}=\lbrace x\in\mathbb{R}^n:a^Tx\leq b\rbrace$. 

![[Pasted image 20240410162237.png|center]]

## Poliedro 

Contiene dos definiciones: 

1. La intersección finita de semiespaciós: 
$$P=\lbrace x\in\mathbb{R^n}:Ax\leq b\rbrace=\bigcap^{k}_{i=1}\lbrace x\;\vert\;a^{T}_{i}x\geq b_i\rbrace$$

2. Un conjunto $P\subseteq\mathbb{R^n}$ es un poliedro si existe $A\in\mathbb{R}^{m\times n}$ ara algún $m$, y $b\in\mathbb{R}^m$ tal que $P=\lbrace x\in\mathbb{R}^n:Ax\leq b\rbrace$. 

Un conjunto es acotado si existe una constante $K$ tal que el valor absoluto de cada componente es menor o igual a $K$ (básicamente, existe una norma menor o igual).

## Polítopo 

Es un poliedro acotado. Básicamente, un semiespacio logrado por la intersección de hiperplanos. 

>[!cite] Teorema 
>Todo polítopo es la envoltura convexa de sus puntos extremos 

Se dirá que $S$ es un conjunto convexo si para todo $x,y\in S$ y para todo $\lambda\in [0,1]$, se tiene que $x+(1-\lambda)y\in S$. 

Dado un conjunto $S$ cualquiera, su envoltura convexa es: 

$$\text{Conv}(S)=\left\lbrace\sum^{k}_{i=1}\lambda_i x_i:x_1,\dots, x_k\in S,\sum^{k}_{i=1}\lambda_i=1,\;\lambda_i\geq 0\;\forall i=1,\dots, k\right\rbrace$$

## Punto extremo 

Sea $P$ un poliedro. Un punto $x\in P$ es un **punto extremo** de $P$ si no puede ser expresado como una combinación convexa de otros dos puntos del poliedro. 

$$\nexists y,z\in P\backslash\lbrace x\rbrace, \lambda\in [0,1]:\;\;x=\lambda y+(1-\lambda)z$$


## Vértice 

Sea $P\subseteq\mathbb{R}^n$ un poliedro. Un punto $x\in P$ se dice vértice si existe $c\in\mathbb{R}^n$ tal que $c^Tx<c^Ty$ y para todo $y\in P\backslash\lbrace x\rbrace$. 

## Soluciones básicas

Sea un poliedro $P$ definido por restricciones lineales de igualdad y desigualdad. Un punto $x^*\in\mathbb{R}^n$ es: 

1. **Solución Básica** si: 

- Todas las restricciones de igualdad son activas 
- De las restricciones que son activas en $x^*$, hay $n$ de ellas que son linealmente independientes. 

2. **Solución Básica Factible** si además $x^*\in P$. 

>[!cite] Teorema de Equivalencia 
>Sea $P$ un poliedro no vacío, y sea $x^*\in P$. Entonces, las siguientes son equivalentes: 
>
>1. $$

