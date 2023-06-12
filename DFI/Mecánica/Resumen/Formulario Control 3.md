
## Oscilaciones 

- A partir de una fuerza conservativa: 

$$w_0=\sqrt{\frac{V''(x_0)}{m}}$$ 
- A partir de la energía mecánica: 

$$\omega_{0}^{2}=\frac{V''(u_*)}{\alpha}$$ 
## Momento Angular 

Definición: $$\vec{l_0}=m\vec{r}\times\vec{v}$$ 
$$\vec{l_0}=\begin{cases}
m\begin{pmatrix}y\dot{z}-z\dot{y}\\
z\dot{x}-x\dot{z}\\
x\dot{y}-y\dot{x}\end{pmatrix}&\text{Coordenadas cartesianas}(\hat{x},\hat{y},\hat{z})\\\\
m\begin{pmatrix}r^2\dot{\theta}\\z\dot{r}-r\dot{z}\\-zr\dot{\theta}\end{pmatrix}&\text{Coordenadas cilíndricas}\;(\hat{k},\hat{\theta},\hat{r})\\\\ mr^2\dot{\theta}\hat{k}&\text{Coordenadas polares}\end{cases}$$

Donde $h = r^2\dot{\theta}$. 

## Torque 

Definición: 

$$\vec{\tau}=\vec{r}\times\vec{F}$$ 
Además, se cumple que: 

$$\frac{d\vec{l_0}}{dt}=\vec{\tau}$$ 
## Movimiento relativo 

Cinemática: 

$$\begin{align}
\vec{r}(t)&=\vec{R_0}(t) + \vec{r'(t)}\\\\\vec{v}(t)&=\vec{V_0} + \vec{v'} + \vec{\Omega_e}\times\vec{r'}\\\\\vec{a}(t)&=\vec{A_0} + \vec{a'} + 2\vec{\Omega_e}\times\vec{v'}+\vec{\Omega_e}\times\left(\vec{\Omega_e}\times\vec{r'}\right)+\vec{\alpha_e}\times\vec{r'}
\end{align}$$ 
Donde $\Omega$ es la velocidad angular del eje $S'$ y $\vec{\alpha_e}$ aceleración de la velocidad angular. 

- **Fuerza inercial:** $$\vec{F_0}=-m\vec{A_0}$$
- **Fuerza de Coriolis**: $$\vec{F_{co}}=-2m\vec{\Omega_e}\times\vec{v }$$
- **Fuerza Centrífuga**: 
$$\vec{F_{cf}}=-m\vec{\Omega_e}\times(\vec{\Omega_e}\times\vec{r'})$$

- **Fuerza transversal**: $$\vec{F_T}=-m\vec{\alpha_e}\times\vec{r}$$