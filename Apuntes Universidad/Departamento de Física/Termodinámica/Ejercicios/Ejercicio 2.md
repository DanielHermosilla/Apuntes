

1. Se tiene que la entropía es $1\;J/K$ 

Para llegar a esto, se impuso que: 

$$S=k_b\ln(\Omega)$$
$$1=k_b\ln(\Omega)$$
$$\frac{1}{k_b}=\ln(\Omega)$$
$$e^{\frac{1}{k_b}}=\Omega$$


Por lo tanto, la información faltante de Shannon se describe como: 

$$I=-\sum x_i\log_2(x_i)$$

Se tiene que $\Omega=e^{\frac{1}{k_b}}$, entonces la información faltante es: 

$$I=-\sum^{e^{\frac{1}{k_b}}}x_i\log_2(x_i)$$
Donde cada $x_i$ es equiprobable. Aplicando la definición de $I_{max}$: 
$$I=\log_2(e^{\frac{1}{k_b}})$$

2. Para las mediciones binarias se ocupa la información faltante de Shannon donde se impone $K=\frac{1}{\ln_2}$. Por lo tanto, como las mediciones de Shannon se miden en *bits*, vale decir, en $0$ y $1$. 

Como se tiene que $\Omega=e^{\frac{1}{k_b}}$, entonces se tiene esa cantidad posible de combinaciones. Por lo tanto, $e^{\frac{1}{k_b}}/2$ mediciones se realizarían. 

3.  Sabemos que se necesitan hacer $e^{\frac{1}{k_b}}/2$ mediciones, entonces hacemos la siguiente relación: 

$$1000\text{mediciones}\to 1\text{segundo}$$
$$e^{\frac{1}{k_b}}/2\to x\;\text{segundos}$$

Por lo tanto, se demoraría $\frac{e^{\frac{1}{k_b}}}{2000}$ segundos. 



Notar que $e^{\frac{1}{k_b}}\approx e^{\frac{1}{1,38\times10^{-23}}}$

