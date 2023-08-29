
Sea $\Sigma$ la [[Superficie|superficie]] de ecuación $\vec{X}=\vec{F}(u,v)$ con $(u,v)\in D$ suave y simple, supongamos que $\Sigma\subset H$, donde $H\subset \mathbb{R}^3$ es un [[Conjuntos abiertos y cerrados|conjunto abierto]]. Sea $f:H\subset\mathbb{R}^3\to\mathbb{R}$ una [[Continuidad en varias variables|función continua]] en $H$. Se llama integral de superficie de $f$ sobre $\Sigma$, denotado: 

$$\int\int_\Sigma fd\sigma=\int\int_D f(\vec{F}(u,v))\;\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert\;dudv$$ 

![[Captura de pantalla 2023-08-27 a la(s) 20.28.40.png|center|450]]

Esto sería similar al *costo del [[Área de una superficie|área de una superficie]]*. 

- Observemos que si $f(\vec{X})=1$, entonces, $\forall\vec{X}\in\Sigma$ se tendría que $\int\int_\Sigma d\sigma=\text{Área}(\Sigma)$. 

- Si $\delta>0$ representa la densidad superficial de masa, entonces: 

$$\int\int_\Sigma \delta d\sigma=\int\int_D \delta(\vec{F}(u,v))\;\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert\;dudv=\text{Masa}(\Sigma)$$

- El valor medio de $f$ sobre $\Sigma$ se define como: 

$$f_{med}=\frac{1}{\text{Área}(\Sigma)}\int\int_\Sigma fd\sigma$$ 

