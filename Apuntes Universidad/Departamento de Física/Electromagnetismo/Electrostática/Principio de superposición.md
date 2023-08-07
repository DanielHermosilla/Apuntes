
Al tener varias cargas fuertes en un medio, se cumple que la suma [[vectores|vectorial]] entre todas las [[Partícula|partículas]] es la suma total del [[Departamento de Física/Electromagnetismo/Electrostática/Campo eléctrico|campo eléctrico]]. 

$$\vec{E_T}(\vec{r})=\vec{E_1}(\vec{r})+\vec{E_2}(\vec{r})+\dots+\vec{E_N}(\vec{r})$$

Por lo tanto, simplificando, se cumple lo siguiente: 

$$\vec{E_T}(\vec{r})=\frac{1}{4\pi\epsilon_0}\sum^{N}_{i=0}\frac{q_i}{\vert\vert r-\vec{r'_i}\vert\vert^2}\cdot\frac{(\vec{r}-\vec{r_i'})}{\vert\vert \vec{r}-\vec{r_i}'\vert\vert}$$

Al analizar cuerpos macroscópicos no veo cargas individuales, si no más bien la densidad de [[Ley de Coulomb|carga]]. Esto es análogo a lo que se hace en mecánica, que al tener una gran cantidad de cargas puntuales y discretas, se busca una distribución continua. Por lo tanto, se transforma en una [[Integral de Riemann|integral]]. 

$$\vec{E_T}(\vec{r})=\frac{1}{4\pi\epsilon}\int\frac{\vec{r}-\vec{r'}}{\vert\vert\vec{r}-\vec{r'}\vert\vert^3}\rho(\vec{r})dv$$

O análogamente: 

$$\vec{E_T}(\vec{r})=\frac{1}{4\pi\epsilon}\int\frac{\vec{r}-\vec{r'}}{\vert\vert\vec{r}-\vec{r'}\vert\vert^3}dq'$$

