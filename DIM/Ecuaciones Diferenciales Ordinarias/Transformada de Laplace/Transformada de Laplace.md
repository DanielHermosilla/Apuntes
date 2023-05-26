
Sea $f:[0,\infty)\rightarrow\mathbb{R}$, luego su Transformada de Laplace se define como: 

$$L[f](s)=\int^{\infty}_{0}f(t)e^{-st}dt$$ 
Para $s\geq 0$ cuando la [[Integral de Riemann|integral]] converge. 

Si $\exists c\geq 0$ tal que $L[f](s)$ converge $\forall s>c$, se dice asíntota de la Transformada de Laplace. 

### Transformadas conocidas: 

1. Sea $f(t)=A$, con $A\in\mathbb{R}\;\implies L[f](s)=\int_{0}^{\infty}Ae^{-st}dt=A\int_{0}^{\infty}e^{-st}dt=\frac{A}{s}$
Donde $c=0$ es la asíntota. 

2. Sea $f(t)=e^{at},\; a\in\mathbb{C}\implies L[f](s)=\int^{\infty}_{0}e^{at}e^{-st}dt=\frac{1}{s-a}$


## Propiedad 

1. Sean $f,g:[0,\infty)\rightarrow\mathbb{R}$ tal que existe $c\geq 0: L[f](s),L[g](s)$ convergen para $s>c$ y $\lambda\in\mathbb{C}$ , entonces: 

$$L[f+\lambda g](s)=L[f](s)+\lambda L[g](s),\;\;\forall s>c$$ 
Con esto, podemos calcular: 

Sean $\sigma,\omega\in\mathbb{R}$: 

$$f(t)=e^{(\sigma + i\omega)t}$$ $$L[f](s)=\frac{1}{s-(\lambda+i\omega)},\;\forall s>\sigma$$ 
$$\iff\frac{(s-\lambda)+i\omega}{(s-\lambda)^2+\omega^2}$$ 

2. Propiedad de la [[Derivada|derivada]]: Si $f\in C_{\alpha}$  y $f\in C^{-1}(0,+\infty)$, entonces: 

$$L[f'](s)=sL[f](s)-f(0^+)$$ 
Donde $0^+=\lim_{x\rightarrow 0^+}$. Esto se demuestra por integración por partes. 

3. Sea $f\in C_\alpha, f\in C^n(\mathbb{R}_+), n\geq 1$ tal que $f^{(k)}\in C_\alpha, \forall k\in\lbrace 1,\dots,n\rbrace$, entonces: 

$$L[f^{(n)}](s)=s^nL[f](s)-s^{n-1}f(0^+)-s^{n-2}f'(0^+)-\dots-sf^{(n-1)}(0^+)=s^nL[f](s)-\sum^{n-1}_{k=1}s^{n-k}f^{(k)}(0^+)$$ $$\iff s^nL[f](s)-\sum^{n-1}_{k=1}s^{n-k}\lim_{t\rightarrow 0^+}f^{(k)}(t)$$ 
4. Transformación de Laplace de una primitiva: Sea $f\in C_\alpha$ y $f$ localmente [[Integrales impropias|integrable]]. Sea: 

$$F(t)=\int^{t}_{a}f(u)du$$ 
Para $s>\alpha$, se tiene que: 

$$L[f](s)=\frac{1}{s}L[f](s)-\frac{1}{s}\int^{a}_{0}f(u)du$$ 
Esto se puede demostrar por [[Teorema Fundamental del Cálculo|TFC]]. 

5. Traslación: Sea $f\in C^\alpha$, luego: 

$$L[f(t-a)H_a](s)=e^{-sa}L[f](s)$$ 
Esto se llama shift en tiempo. 