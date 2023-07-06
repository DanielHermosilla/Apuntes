
Sean $X$ e $Y$ dos [[Variable aleatoria continua|variables aleatorias conjuntamente continuas]]  con [[Función de Densidad Conjunta|PDF conjunta]] $f_{xy}(x,y)$. La **función de densidad probabilidad marginal** (PDF marginal) de $X$ se define como: 

$$f_x(x)=\int_{-\infty}^{\infty}f_{xy}(x,y)dy$$ 
### Ejemplo 

En el caso de la flecha en blanco, ¿cómo son las densidades marginales? 

![[Captura de pantalla 2023-05-22 a la(s) 08.48.00.png|center]]

Notemos que, como $x\in[-1,1]$. Entonces: 

$$f_x(x)=\int_{-\infty}^{\infty}f_{xy}(x,y)dy$$ 
$$\iff\int_{-\infty}^{\infty}\frac{1}{\pi}\mathbb{1}_{\lbrace x^2 + y^2\leq 1\rbrace}dy$$ 
Notemos que $-\sqrt{1-x^2}\leq y\leq\sqrt{1-x^2}$, entonces, para sacar la indicatriz, imponemos eso en los límites de integración: 

$$\frac{1}{\pi}\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}dy$$ $$\iff\frac{2}{\pi}\sqrt{1-x^2}$$ 
Entonces, 

$$f_x(x)=\iff\frac{2}{\pi}\sqrt{1-x^2}\mathbb{1}_{\lbrace x\in[-1,1]\rbrace}$$ 