Notemos que la derivada se define como la **pendiente instantánea en un punto de la función**. Por eso mismo, normalmente se va a requerir que para una función sea derivable también sea [[Función continua|continua]], aunque no necesariamente todas las funciones continuas son derivables. 

Como queremos buscar la pendiente instantánea en un punto, vamos a definir la derivada como un límite: 

Sea una función $f(a,b)\rightarrow\mathbb{R}$. Diremos que es derivable en un punto $\bar{x} \in (a,b)$, si existe el siguiente límite: 

$$\lim_{x\rightarrow\bar{x}} \frac{f(x)-f(\bar{x})}{x-\bar{x}}$$ 
Y por ende, el límite nos estaría representando la **recta tangente** de una función en cierto punto $\bar{x}$, de tal forma se puede evidenciar en la siguiente imagen:

![[Captura de Pantalla 2022-12-06 a la(s) 21.25.07.png|center]]

Si nos apegamos a la fórmula anterior, nos percataríamos que $q(x)$ va cambiando a medida que $\bar{x}\rightarrow x$, por lo tanto, nos estaríamos quedando con una recta tangente que toca únicamente el punto $x$. 

Notemos que la definición se define en el intervalo abierto $(a,b)$, esto se debe a que las funciones son derivables siempre en el **interior del dominio**. 

#definición 