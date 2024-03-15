
Representaciones idealizadas de la realidad. Existen los siguientes tipos de modelos en el contexto de la optimización: 

- **Optimización lineal**: Ocupa variables continuas, va de $\mathbb{R}^n\to\mathbb{R}^n$, todas las funciones son lineales, de la forma $\alpha_1x_1+\alpha_2x_2+\dots+\alpha_nx_n$, como una [[combinación lineal]]. 

- **Optimización entera (lineal)**: Las variables van en $\mathbb{Z}^n$ y la restricción es lineal. Vale decir, son variables discretas.

- **Optimización no lineal**: Son variables continuas y la función es **no lineal**. 

Cada modelo tiene varios algoritmos para resolver, aunque el uso de esos depende del algoritmo que se ocupa. La complejidad de los algoritmos son determinadas con **complejidad computacional**. 

#### Ejemplo: Problema de producción 

Se tiene el siguiente problema de producción para hacer pizza y lasagna. 

|         | ** Pizza** | **Lasagna** | **En Stock** |
|:-------:|:----------:|-------------|--------------|
|  Tomate |      2     | 3           | 18           |
|  Queso  |      4     | 3           | 24           |
| Ingreso | 8000       | 7000        |              |

Por lo tanto, *¿Cuantas pizzas y lasagnas se producen para maximizar el ingreso? ¿Cuánto es el mayor número de pizzas y lasagnas que se pueden producir?* Notar que se tiene la principal restricción del stock. 

Antes de modelar hay que identificar las **decisiones**: sea $p$ el número de pizzas y $l$ el de lasagnas. 

Por el otro lado, las restricciones llegaría a ser la siguiente: 

$$\begin{align}
2p+3l&\leq 18\\  \\
4p + 3l&\leq 24\\  \\
p,\;l&>0
\end{align}$$

Por último, la **función objetivo** llegaría a ser 

$$8000p+7000l=f(x)$$

Así, el problema quedaría como: 

$$\begin{align}
8000p+7000l\\ \\
2p+3l&\leq 18\\  \\
4p+3l&\leq 24\\  \\
p,l&\geq 0
\end{align}$$

#### Ejemplo: Problema de Staffing 

Se tienen que organizar turnos semanales para enfermeros en una unidad hospitalaria. Existen $d_j$ enfermero/as durante el dia $j$. Cada persona trabaja por $5$ días seguidos. *¿Cual es el menor número de personal necesario para cumplir con los requerimientos?*. 

Se tienen los siguientes requerimientos: 

- Lunes: 7 enfermeros 
- Martes: 10 enfermeros 
- Miercoles: 5 enfermeros 
- Jueves: 6 enfermeros 
- Viernes: 6 enfermeros 
- Sábado: 3 enfermeros 
- Domingo: 5 enfermeros 

Las variables de decisión llegaría a ser el número de personas que **empiezan a trabajar** el dia $i$. Se podría modelar mediante la siguiente matriz: 

$$\begin{pmatrix}
X_L & + X_J & + X_V & + X_S & + X_D & \geq d_L=7 \\
X_L & + X_M & + X_V & + X_S & + X_D & \geq d_m=10 \\
X_L & \dots & \dots & \dots & \dots & \vdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
 &  &  &  &  & \geq d_D
\end{pmatrix}$$

