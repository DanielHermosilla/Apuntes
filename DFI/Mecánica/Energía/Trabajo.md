
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