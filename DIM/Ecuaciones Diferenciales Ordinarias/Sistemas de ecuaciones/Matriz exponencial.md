
Se define como $A\in M_{n\times n}(\mathbb{R})(A\in\mathbb{R}^{n\times n})$, luego: 

$$e^{a}=\sum^{\infty}_{k=0}\frac{A^k}{k!}$$ $$\iff I + \sum^{\infty}_{k=1}\frac{A^k}{k!}$$ 
Entonces, se tiene una [[Series numéricas|serie numérica]], que podría o converger o diverger. 

## Norma de frobenius 

Sea $A\in M_{n\times n}(\mathbb{R})(A\in\mathbb{R}^{n\times n})$, luego la función: 

$$||A||_F=\sqrt{\sum^{n}_{i=1}\sum^{n}_{j=1}A_{ij}^{2}}\;\;\;\text{es norma}$$ 
Entonces, por proposición, se establece que: 

$$||e^A||_F\leq e^{||A||_F}$$ 
#### Demostración 
$$||I + \sum^{n}_{k=1}\frac{A^k}{k!}||\leq ||I|| + \sum^{n}_{k=1}\frac{||A^k||}{k!}$$ $$\iff\leq ||I|| + \sum^{\infty}_{k=1}\frac{||A||^k}{k!}$$$$\iff 1 + \sum^{\infty}_{k=1}\frac{||A||^k}{k!} = e^{||A||}$$ $$\implies ||I+\sum^{n}_{k=1}\frac{A^k}{k!}||\leq e^{||A||}$$ 

# Propiedades 


Sean $A,B\in M_{n\times n}(\mathbb{R})$, luego: 

1. $e^{A·0} = I$ 

2. $\frac{d}{dt}e^{At} = Ae^{At}$ 

3. $e^{A(t+s)} = e^{At}e^{As}$, en particular: 

$$e^{At}\;\;\text{es invertible con}\;\;(e^{At})^-1 = e^{-At}$$ 
4. $Be^{At} = e^{At}B$ si $AB = BA$ .

5. $e^{(A+B)t} = e^{At}e^{Bt}$ si $AB = BA$ 

