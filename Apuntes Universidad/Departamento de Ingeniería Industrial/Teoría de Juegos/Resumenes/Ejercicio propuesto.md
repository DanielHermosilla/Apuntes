
Considere el mercado de las hamburguesas de origen vegetal. Existen diversas empresas que producen el mismo bien, sin embargo, NotCo es la tiene mayor poder de mercado y, por lo tanto, asume un rol de liderazgo (esto puede deberse a que la optimización de sus procesos a generado reducciones de costos, que su publicidad sea más efectiva, etc). Dada esta característica, las empresas juegan un Juego de Stackelberg:

*¿Qué ocurre si, en el segundo periodo, en vez haber solo una firma hay $n$ firmas?* 

### Respuesta 

Dado que tenemos $n$ firmas, me definiré un conjunto $D$ con la cantidad producida por cada firma. Consideremos una demanda inversa $P(Q)=a-Q$ con $Q=\sum^{n}_{i}q_i\in D$. Además, establecemos que $q_1$ corresponde a la demanda de la empresa NotCo. Por último, asumimos que cada firma tiene costos marginales $c$

Por lo tanto, en el segundo período, es posible asegurar un $q_1$ fijo. La utilidad de cualquier firma $i$ se ve por la siguiente función (asumiendo que las firmas son idénticas, producen a cantidades idénticas). 

$$\begin{align}
\Pi_{n\geq i>1}&=P(Q)\cdot q_i-q_i\cdot c\\  \\
&=(a-q_1-nq_i)q_i-q_i\cdot c\\  \\
&=aq_i-q_iq_1-nq_{i}^{2}-q_ic
\end{align}$$

Aplicando condición de primer orden: 

$$\begin{align}
\max_{q_{i}\geq 0}&=a-q_1-2nq_i-c=0\\  \\
\implies q_i&=-\frac{1}{2n}\left(q_1+c-a\right)\tag{1} \\

\end{align}$$

Esto quiere decir que una firma cualquiera producirá $(1)$ unidades dada la producción $q_1$ de NotCo. 

Ahora, como NotCo sabe como reaccionará cada firma ante su jugada, establecemos su función utilidad: 

$$\begin{align}
\Pi_1&=P(Q)\cdot q_1-q_1\cdot c\\  \\
&=(a-\sum^{}_{q_k\in D\backslash\lbrace q_1\rbrace}q_k-q_1)q_1-q_1\cdot c\\  \\
&=aq_1-q_1\sum^{}_{q_k\in D\backslash\lbrace q_1\rbrace}q_k-q_{1}^{2}-q_1c\\  \\
&=aq_1+q_1\cdot\frac{1}{2}(q_1+c-a)-q_{1}^{2}-q_1c\\  \\
&=\frac{1}{2}aq_1-\frac{1}{2}q_{1}^{2}-\frac{1}{2}q_1c\\  \\
\end{align}$$

Nuevamente aplicando condición de primer orden: 

$$\begin{align}\max_{q_1>0}&=\frac{1}{2}a-q_1-\frac{1}{2}c\stackrel{!}{=}0\\  \\
q_1&=\frac{1}{2}(a-c)\tag{2}\end{align}$$

Entonces, NotCo terminaría produciendo $(2)$ y sus **utilidades** llegarían a ser: 

$$\begin{align}
\Pi_1&=\frac{a-c}{2}\left(P(Q)-c\right)\\  \\
&=\frac{a-c}{2}\left(a-q_1+\frac{1}{2n}\left(q_1+c-a\right) -c\right)\tag{2}\\  \\
&=\frac{a-c}{2}\left(a-\frac{a-c}{2}+\frac{1}{2n}(\frac{a-c}{2}+c-a)-c\right) \\  \\
&=\frac{\left(a-c\right)\left(c-a-2nc+2na\right)}{8n}
\end{align}$$


Por el otro lado, la cantidad producida por cada firma sería: 

$$\begin{align}
q_i&=-\frac{1}{2n}\left(\frac{a-c}{2}+c-a\right)\tag{1}\\  \\
q_i&=\frac{a-c}{4n}
\end{align}$$

Notemos que llegamos al mismo resultado que el juego anterior, donde la cantidad de firmas en el segundo período eran $n=1$. 

Por lo tanto, se llegaría al siguiente gráfico: 

![[propuesto2.png|center]]

Dado que el porcentaje de utilidades del mercado están asociado únicamente a la cantidad producida, se puede decir que **NotCo tendría el $66\%$ de la producción y utilidades del mercado**. 

NotCo seguiría teniendo la misma participación en el mercado, pero las otras firmas se dividirían el $33\%$ de forma equitativa entre ellas. Si $n\to\infty$ la utilidad y cantidad producida de cada firma individual tendería a cero, esto se puede ver también por la ecuación $(1)$. 