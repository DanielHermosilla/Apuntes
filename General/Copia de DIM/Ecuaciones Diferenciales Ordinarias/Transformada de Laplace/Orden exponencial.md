
Sea $f:[0,\infty)\rightarrow\mathbb{R}$ se dice de orden exponencial $\alpha\in\mathbb{R}$, si existe $M>0$ tal que: 

$$\vert f(t)\vert\leq Me^{\alpha t},\;\forall t\geq0$$ 
Se define: 

$$C_\alpha=\lbrace f:[0,\infty)\rightarrow\mathbb{R}\;\bigg\vert\;\exists M>0;\;\vert f(t)\vert\leq Me^{\lambda t},\;\forall t>0\rbrace$$ 
## Propiedad 

Si $f\in C_\alpha$, entonces $\forall L[f](s)$ [[Convergencia absoluta|converge]] $\forall s>\alpha$.

### Demostración 

Sea $M>0$, tal que $\vert f(t)\vert\leq Me^{\alpha t}$, luego: 

$$\int^{\infty}_{0}\vert f(t)e^{-st}\vert dt = \int^{\infty}_{0}\vert f(t)\vert e^{-st} dt$$ 
Entonces, 

$$\vert\int f\vert\leq\int\vert f\vert\leq\int^{\infty}_{0}Me^{\alpha t}e^{-st} = M\int^{\int}_{0}e^{\alpha-s)t} dt=M\frac{1}{(s-\alpha)}\;\forall s>\alpha.$$

Luego, $\forall s>\alpha: \int^{\infty}_{0}\vert f(t)e^{-st}\vert dt<+\infty$, luego $L[f](s)$ converge, $\forall s>\alpha$. 