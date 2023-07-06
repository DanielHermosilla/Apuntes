
Sea una [[combinaciones lineales]] que tenemos sobre unos [[espacios vectoriales]], diremos que tenemos una combinación **linealmente dependiente** si:
$$ \exists \space \text{escalares} \space (\alpha_{1}, \dots, \alpha_{n}) \text{ \textbf{no nulos} tal que } \sum_{i=1}^{n}\alpha v_{i} = 
0 $$  Y, por el otro lado, diremos que es **linealmente independiente** al obtener la negación de lo anterior: 

$$ \nexists \space \text{escalares} \space (\alpha_{1}, \dots, \alpha_{n}) \text{ \textbf{no nulos} tal que } \sum_{i=1}^{n}\alpha v_{i} = 
0 $$
En otras palabras, significa que la **única forma** para obtener la combinación lineal igual a cero es que **todos** los [[escalares]] sean **necesariamente** 0. 

### Algoritmo 

La forma para verificar la dependencia lineal es armando un [[sistema de ecuación]], bajo el siguiente el ejemplo:

$$ \alpha_{1} v_{1} + \alpha_{2} v_{2} + \dots + \alpha_{n} v_{n} $$
Es lo equivalente a tener lo siguiente: 

$$ \begin{equation}
		\begin{bmatrix}
			v_{1} & v_2 & \dots & v_n
			
		\end{bmatrix} *
		\begin{bmatrix}
			\alpha_1 \\
			\alpha_2 \\
			\dots \\ 
			\alpha_n
		\end{bmatrix} = \begin{bmatrix}
			0 \\
			0 \\
			\dots \\ 
			0
		\end{bmatrix}
\end{equation}
		$$
Si es que llegasemos a tener variables libres, entonces significa que existen infinitas combinaciones de $\alpha$ para que la [[combinación lineal]] sea 0. O de otra forma, existen infinitas formas en que un escalar anule a un vector para que la [[combinación lineal]] sea 0. 

Si ocurre lo anterior, tendríamos una combinación **linealmente dependiente**. 

#concepto 