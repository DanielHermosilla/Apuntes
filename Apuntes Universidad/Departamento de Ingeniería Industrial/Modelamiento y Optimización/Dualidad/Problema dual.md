
Dado un problema de optimización de la forma estándar: 

$$\begin{align}
p^*&=\min c^Tx\\  \\
Ax&\geq b\\  \\
x&\geq 0
\end{align}$$

Existe un problema relacionado **con los mismos parámetros**: 

$$\begin{align}
d^*&=\max b^Ty\\  \\
A^Ty&\leq c\\  \\
y&\geq 0
\end{align}$$

El primer problema se llama **primal**, el segundo, **dual**. Notar que las restricciones $b$ del primal es el mismo $b$ de la función objetivo del primal. 

Se siguen ciertas reglas, por ejemplo, si la variable $x_i$ es libre, entonces la restricción $y_i$ irá con una **igualdad**. Si $x_j\geq 0$ entonces $y_j$ ira con un $\leq$ y viceversa. 

### Intuición 

Se puede tener el siguiente ejemplo: 

$$
\begin{aligned}
\min z\left(x_1, x_2\right)=- & 3 x_1+x_2 \\
& x_1+x_2 \geq 0 \\
& x_1-2 x_2 \geq-6 \\
& x_1+x_2 \leq 5 \\
& 5 x_1-x_2 \leq 20 \\
& -3 x_1+x_2 \geq-40 \\
& x_2 \geq 0
\end{aligned}
$$

Si quisieramos formar **cotas inferiores** para la función objetivo, es posible hacer el siguiente razonamiento: 

$$\begin{align}
z_1(x_1+x_2)&\geq0\cdot z_1\;\;\;z_1\geq 0\\  \\
z_2(x_1-2_x2)&\geq z_2\cdot(-6)\;\;\;z_2\geq 0\\  \\
z_3(x_1+x_2)&\geq z_3(5)\;\;\;z_3\leq 0\\  \\
z_4(5x_1-x_2)&\geq z_4(20)\;\;\; z_4\leq 0\\  \\
z_5(-3x_1+x_2)&\geq z_5(-40)\;\;\; z_5\geq 0
 \end{align}$$

Por lo tanto, para **construir una cota inferior a la función objetivo**, podemos sumar cada restricción: 

$$\begin{align}
0z_1-6z_2+5x_3+20z_4-40z_4&\leq\\  \\
z_1(x_1+x_2)+z_2(x_1-2x_2)+z_3(x_1+x_2)+z_4(5x_1-x_1)+z_5(-3x_1+x_2)&=\\  \\
x_1(z_1+z_2+z_3+5z_4-3z_5)+x_2(z_1-2z_2+z_3-z_4+z_5)\end{align}$$

Nos gustaría que todo eso sea $\leq$ a la función objetivo, vale decir, $\leq -3x_1+x_2$. Para garantizar eso, hay que garantizar que la suma de los coeficientes de $x_1$ sea igual a $-3$ y que la suma de los $x_2$ sea mayor o igual a $0$ y que sea menor o igual a $1$: 

$$\begin{align}
z_1+z_2+z_3+5z_4-3z_5&=-3\\  \\
0\leq z_1-2z_2+3z_3-z_4+z_5&\leq 1
\end{align}$$

Notar que lo anterior es **lo mismo que el problema dual** 


>[!quote] Teorema Dualidad Debil 
>Si $x$ es una solución factible para el problema primal e $y$ es una solución factible para el problema dual, entonces: 
>
>