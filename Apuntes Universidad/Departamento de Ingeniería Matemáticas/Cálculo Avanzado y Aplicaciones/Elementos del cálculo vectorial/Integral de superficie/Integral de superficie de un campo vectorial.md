
Esto, haciendo referencia al *flujo vectorial* a través de una superficie. 

Sea $\Sigma$ la [[Superficie|superficie]] de ecuación $\vec{X}=\vec{F}(u,v)$ con $(u,v)\in D$ suave y simple y supongamos que $\Sigma\subset H$, donde $H\subset \mathbb{R}^3$ es un [[Conjuntos abiertos y cerrados|conjunto abierto]]. Sea $\vec{f}:H\subset\mathbb{R}^3\to\mathbb{R}^3$ un [[Campos escalares y vectoriales|campo vectorial]] continuo en $H$. Se llama integral de superficie o flujo del campo vectorial $\vec{f}$ a través de $\Sigma$: 

$$\int\int_\Sigma \vec{f}\cdot\hat{n}\;d\sigma=\int\int_D\vec{f}(\vec{F}(u,v))\cdot\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\;dudv $$

Notemos que esta notación es consistente con la definición, pues: 

$$\hat{n}=\frac{\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)}{\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert}\;\land\;d\sigma=\vert\vert\vec{F^{'}_{u}}(u,v)\times\vec{F^{'}_{v}}(u,v)\vert\vert\;dudv$$ 
El significado físico de esto se puede ver bajo la siguiente imagen, donde se tiene un flujo vectorial $\vec{f}$ y una [[Superficie|superficie]] $\Sigma$, entonces 