
Corresponde a una forma del método científico para demostrar por contradicción ciertas cosas. Esto sigue tres pasos: 

1. Obtener los datos: una muestra de $n$ observaciones $x_1,\dots,x_n$
2. Calcular el [[Estadísticos|estadístico]] de interés: por ejemplo, se podría sacar la media muestral: 
$$\bar{X_n}=\frac{1}{n}\sum^{n}_{i=1}X_i$$

3. Obtener una conclusión: Si $\bar{X_n}$ es demasiado grande (e.g $\bar{X_n}>k$ con $k$ constante), entonces rechazamos $H_0$ en favor de $H_1$. En caso contrario, se dice que no se tiene suficiente información para afirmar que $H_0$ es falsa. 

### Tipos de errores 

Cuando se hacen test de hipótesis, es posible cometer dos errores: 

1. **Tipo 1**: Observan que $\bar{X_n}>k$, sin embargo la distribución verdadera del estadístico es $f(\bar{X_n}\vert H_0)$. En consecuencia: 

$$Pr(\bar{X_n}>k\vert H_0)=Pr(\text{Rechazar}\;H_0\;\vert\;H_0\;\text{es verdadera})$$ 
2. **Tipo 2**: No rechazar la hipótesis nula cuando la hipótesis nula es falsa. 

### Conceptos Generales 

- **Significancia estadística**: 

$$Pr(\text{Rechazar}\;H_0\;\vert\;H_0\;\text{Es verdadera})=Pr(\text{Error tipo 1})=\alpha$$

- **Poder:**

$$Pr(\text{No rechazar}\;H_0\;\vert\;H_1\text{Es verdadera})=Pr(\text{Error tipo 2})=1-\beta$$