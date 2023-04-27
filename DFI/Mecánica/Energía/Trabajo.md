
De la segunda Ley de Newton, se puede hacer lo siguiente: 

$$\vec{F} = m\vec{a}$$

Si se hace el producto punto por la velocidad a ambos lados: 

$$m\vec{a}·\vec{v} = \vec{F}·\vec{v}$$ 
Donde: 

$$\frac{d}{dt}(m\vec{v}·\vec{v}) = \frac{d}{dt} (\frac{1}{2}mv^2)$$ $$\implies \frac{d}{dt}(\frac{1}{2}mv^2) = \vec{F}·\frac{ds}{dt}\hat{t}$$ 
Notemos que aparece la energía cinética y se sabe lo siguiente: 

$$\frac{ds}{dt} = \lim_{\Delta t\rightarrow 0}\frac{\Delta s}{\Delta t}$$ 
Y si llamamos $K$ a la energía cinética: 

$$\frac{dK}{dt}=\frac{\vec{F}ds\hat{t}}{dt}$$ $$\implies dK = \vec{F}·ds\hat{t}$$ 
Y si lo integramos: 

$$\int dK = \int \vec{F}·ds\ \hat{t}$$ 
$$\iff \Delta K = \int \vec{F}·ds\ \hat{t}$$ 
Para el lado derecho, si se ocupan coordenadas intrínsecas: 

$$\vec{F} = F_t\hat{t} + F_n\hat{n}$$ 
Donde: 

$$\int\vec{F}ds\hat{t} = \int(F_s\hat{t}+F_n\hat{n})·ds\ \hat{t}$$ 
Que se llega que: 

$$\int_{S_1}^{S_2}F_s\ ds$$ 
A ese término se le llama **trabajo**, que es la fuerza neta ejercida a lo largo de la trayectoria.

Si para una [[Partícula|partícula]] cualquiera se le define su vector de fuerza conservativa, se puede llegar a lo siguiente: 

$$F_c · d\vec{r} = -dV$$ 
Por lo tanto, 

$$\int dV = \int mgdz$$ $$\implies V(z) = mgz + C$$ 
Y por el otro lado, se tiene que la variación de la energía cinética es la siguiente: 

$$dK = \vec{F}·d\vec{r} = -dV$$

Y como $dK + dV = 0$, entonces $d(K+V)=0$. Por ende, 

$$K + V(x,y,z) = E_0$$ 
Por lo tanto, para saber el cambio de $V$ en función de sus variables: 

$$V(x,y,z) = \frac{\partial V}{\partial x}dx + \frac{\partial V}{\partial y}dy + \frac{\partial V}{\partial z}dz$$ 
Dado que $V:\mathbb{R}^3\rightarrow\mathbb{R}$, es decir, es escalar .

Ahora notemos que: 

$$\vec{F}·d\vec{r} = f_xdx + f_ydy + f_zdz$$ 
Entonces, volviendo a la igualdad anterior, se llega que: 

$$f_xdx + f_ydy + f_zdz = -\left[\frac{\partial V}{\partial x}dx + \frac{\partial V}{\partial y}dy + \frac{\partial V}{\partial z}dz\right]$$

$$\implies\begin{cases} 
f_x = \frac{-\partial V}{\partial x} \\ 
\\
f_y = \frac{-\partial V}{\partial y} \\ 
\\
f_z = \frac{-\partial V}{\partial z}
\end{cases}$$ 

Además, se define lo siguiente $\nabla\times\vec{F_c} = 0$, el **rotor de $\vec{F_c}$.**  Por definición, el rotor de una fuerza conservativa es 0. 