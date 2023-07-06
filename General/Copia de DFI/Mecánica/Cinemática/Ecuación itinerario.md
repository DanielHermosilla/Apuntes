
A partir de la ecuación de [[Aceleración|aceleración]] de la dinámica se tiene lo siguiente: 

$$(\frac{dv_x}{dt}) = a_x $$
$$\implies dv_x = a_x dt$$ 
Entonces se tiene una EDO, y resolviéndola: 
$$\int_{v_{x_0}}^{v_x} dv_x = \int^{t}_{0}a_x(t)dt$$ $$\iff V_x\big\vert_{v_{x_0}}^{v_x}=\int^{t}_{0}a_x(t)dt$$ $$\iff V_x(t) = V_{x_0} + \int^{t}_{0}a_x(t)dt$$ 
Análogo para el eje y. 

También, despejando, se puede obtener lo siguiente: 

$$\vec{v}(t) - \vec{v_0} = \int^{t}_{0}\vec{a}\ dt$$ 
Técnicamente, integrar un vector equivale a integrar a cada uno de sus componentes.

Ahora, si se hace el proceso análogo con la [[Posición|posición]]: 

$$\frac{d\vec{r}}{dt} = \vec{v}\implies\int^{\vec{r}}_{\vec{r_0}} = \int^{t}_{0}\vec{v}(t)dt$$ 
$$\iff\vec{r}(t) - \vec{r_0} = \int^{t}_{0}v(t)dt$$ $$\implies \vec{r}(t) = \int^{t}_{0}v(t) + \vec{r_0}$$ 
### Ejemplo 

[[Partícula]] con [[Aceleración|aceleración]] constante.  Entonces: 

$$\frac{d\vec{v}}{dt} = \vec{a_0}\rightarrow\int_{\vec{v_0}}^{\vec{v}} d\vec{v} = \int_{0}^{t}\vec{a_0}\ dt$$ 
Pero $\vec{a_0}$ es constante, es decir, cada componente de la aceleración es constante. Por lo tanto: 

$$\vec{v} = \vec{v_0} + t\vec{a_0}$$ 
Integrando de nuevo para encontrar la [[Posición|posición]]: 

$$\frac{d\vec{r}}{dt}=\vec{v} = \vec{v_0} + t\vec{a_0}$$ 
$$\int^{\vec{r(t)}}_{\vec{r}}d\vec{r} = \int^{t}_{0}\vec{v_0}\ dt + \int^{t}_{0}\vec{a_0}t\ dt$$ 
Se sabe que $a_0$ es constante y que $v_0$ también, entonces: 

$$\int^{\vec{r(t)}}_{\vec{r}}d\vec{r} = \vec{v_0}t + \frac{1}{2}t^2\vec{a_0}$$ 
$$\vec{r}(t) = \vec{r_0} + t\vec{v_0} + \frac{1}{2}t^2\vec{a_0}$$ 
