
Existen ciertos tipos de EDOS que se pueden reducir a una **integración directa**, [[Ecuación diferencial lineal de primer orden|ecuaciones de primer orden]] o con [[Método de separación de variables|separación de variables]] al hacer [[Cambio de variable|cambio de variables]]

- **Homogénea**: $y' = h(\frac{y}{x})\ \implies\ u=\frac{y}{x}$$
- **Bernoulli**: $y' + a(x)y = q(x)y^n\ \implies\ u = y^{1-n}$ 
- **Ricatti**: $y' = py^2 + qy + r\ \implies\ u_1 = y_1 + \frac{1}{u_2}\ \land\ u_2 = \frac{1}{y-y_1}$

Por último, se tienen las de orden 2: 
$$ 
\text{Orden 2}=\begin{cases} 
       F(x,y',y^{''}) & \text{No aparece}\; y \\
      F(y,y',y^{''}) & \text{No aparece}\; x  
   \end{cases}
$$