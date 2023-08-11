
Anteriormente se definió que se denota por $\mathbb{R}^n$ como el espacio *n*-dimensional dotado de la [[Norma en varias variables|norma euclidiana]]. 

Por lo tanto, sea $\Omega$ un [[Conjuntos|conjunto]] abierto no vacio de $\mathbb{R}^3$. Se denominará **campo escalar** sobre $\Omega$ a toda función a valores reales $f:\Omega\to\mathbb{R}$, es decir, el conjunto de [[Funciones escalares|funciones escalares]]. Por el otro lado se denominará ***grafo** de $f$* al conjunto $G(f)=\lbrace \vec{x},f(\vec{x})\;\vert\;\vec{x}\in\Omega\rbrace$. Por último, dado $\alpha\in\mathbb{R}$, se define el **conjunto de nivel** $\alpha$ de la función $f$ como $N_\alpha(f)=\lbrace\vec{x}\in\Omega\;\vert\;f(\vec{x})=\alpha\rbrace\subset\mathbb{R}^3$, el cual puede ser vacio. 


## Campo vectorial 

Además, el **campo vectorial** sobre $\Omega$ a toda función $\vec{F}:\Omega\subseteq\mathbb{R}^3\to\mathbb{R}^3$ en coordenadas cartesianas se escribirá como: 

$$\vec{F}(x,y,z)=F_1(x,y,z)\hat{i}+F_2(x,y,z)\hat{j}+F_3(x,y,z)\hat{k} $$ 
Donde para cada función $F_{1,}F_2,F_3$ corresponde a un campo escalar sobre $\Omega$. Un campo vectorial se puede representar gráficamente para un punto $(x_0,y_0,z_0)$ el [[vectores|vector]] correspondiente $\vec{F}(x_0,y_0,z_0)$, y repetirlo para una cantidad finita de puntos: 

![[Pasted image 20230807151604.png|center|400]]


### Ejemplo 

Los puntos de un disco plano que gira en sentido anti-horario con velocidad angular constante $\omega>0$, tiene como campo de velocidades a $\vec{v}(x,y,0)=-\omega y\hat{i}+\omega x\hat{j}$

![[Pasted image 20230807152045.png|center|400]]



### Ejemplo 

Si consideramos un fluido moviéndose en una región $\Omega\subset\mathbb{R}^3$. Si a cada punto $(x,y,z)\in\Omega$ se le asocia una velocidad instantánea de las partículas que pasan por dicho punto, se obtiene un campo de velocidades del fluido: 

$$\vec{v}(x,y,z)=v_1(x,y,z)\hat{i}+v_2(x,y,z)\hat{j}+v_3(x,y,z)\hat{k} $$


![[Pasted image 20230807152553.png|center|400]]


Por último, consideraremos $\vec{F}:\Omega\subseteq\mathbb{R}^3\to\mathbb{R}^3$ un campo [[vectores|vectorial]], el cual se supondra suficientemente diferenciable. Se define como **línea de flujo** a la curva tangente en cada punto que proporciona la dirección del campo en dicho punto: 

![[Pasted image 20230807152801.png|center|400]]


Esto se obtiene matemáticamente al resolver el [[Sistema de ecuaciones|sistema de ecuaciones]] diferenciales: 

$$\frac{d\vec{r}}{dt}(t)=\vec{F}(\vec{r(t))}$$

