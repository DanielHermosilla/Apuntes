
Estimado Ale, 

Junto con saludar, me gustaría hacer un reclamo para la pregunta $1$. 

Antes que nada, reconocer que mi desarrollo posee errores, algunos más significativos que otros, y también admitir que no fuí lo más riguroso con el desarrollo de la pauta. 

No obstante, creo poder *"salvar"* algo de puntaje al haber hecho un desarrollo alternativo que no estaba en la pauta. En su momento, lo comenté en cátedra con el profesor y también me acuerdo haberlo conversado contigo (de hecho, me mandaste un desarrollo que encontraste en internet :)) 

Anterior a mandar mi reclamo, me gustaría aclarar algunas cosas:

1. Primero traté de calcular la resistencia entre ambas esferas intentando hacer el desarrollo mediante la ecuación de continuidad, proceso similar al de la pauta. Sin embargo, al no haber llegado a un resultado concluyente, traté de hacer un desarrollo alternativo. 

2. El desarrollo alternativo se encuentra en la última página del PDF, que en realidad, tuvo que haber sido la segunda hoja en la entrega, ya que quería que se corrija ese análisis primero (probablemente entregué las hojas en distinto orden o hubo una confusión). Esto se puede corroborar dado que arriba aparece, entre paréntesis, "*el diferencial de área lo calculé más adelante, donde traté de hacerlo por Ley de Ohm*"

De tal forma, mi forma de ver el ejercicio fue inspirado por el [siguiente desarrollo](http://www.virtualdynamicssoft.com/VD_University/Physics_3/VDU_Physics_3_009.htm):

![[Pasted image 20231211210711.png|center|800]] 

Notar que el ejercicio es muy parecido al anterior, bajo la diferencia que se tenía el pequeño detalle de tener espacios vacios en las zonas concéntricas. 

Notemos que para el primer paso se tenía lo siguiente: 

$$R=\frac{\rho L}{A}$$

(En mi caso, ocupé que $\rho=g$, debo admitir que pudo haber causado confusiones mi forma de nombrar las variables). 

Ahora, en la pauta de este problema se impuso que el área era $4\pi r^2$, sin embargo, no se podía hacer tal cual en el problema del control porque se tenía un espacio vacio. Por lo tanto, hice el siguiente razonamiento: 

$$\begin{align}
R&=\frac{gL}{A}\\  \\
R\;dA&=g\;dL\\  \\
\int R\;dA&=\int g\;dL\tag{1}
\end{align}$$

Aquí es donde había que ocupar mi indicación de arriba, donde dije que el diferencial de área lo calculé más adelante, en específico, hice el siguiente desarrollo bajo el contexto del desarrollo por la via de la Ley de Ohm: 

$$R=V\int J(r)\;dA$$

Como sólo me interesaba conocer el diferencial de área por esta *"nueva vía"*, simplemente reciclé el resultado, ignorando las constantes $J$ y $V$. En específico, hice el siguiente desarrollo: 

$$\begin{align}
R&=VJ\int^{2\pi}_{0}\int^{\alpha/2}_{0}r^2\sin(\theta)\;d\theta\;d\rho\\  \\
&=VJ\;2\pi r^2\cos(\theta)\bigg\vert^{0}_{\alpha/2}\\  \\
&=VJ\;2\pi r^2(1-\cos(\alpha/2))\\  \\
\implies\text{Diferencial de área}&=2\pi r^2(1-\cos(\alpha/2))
\end{align}$$

Así, volviendo a $(1)$, el desarrollo que hice fue el siguiente: 

$$\begin{align}
R\int dA&=g\int dL\\  \\
R\left(2\pi r^2(1-\cos(\alpha/2)\right)&=g(b-a)\\  \\
R&=\frac{g(b-a)}{2\pi r^2(1-\cos(\alpha/2)}
\end{align}$$

Aquí fue donde cométi mi error que me llevo a un resultado un poco diferente. Notemos que $dL=dr$, por lo que el planteamiento correcto tuvo que haber sido el siguiente: 

$$\begin{align}
R&=g\int\frac{1}{A}\;dL\tag{2}\\  \\
&=g\int^{b}_{a}\frac{1}{2\pi r^2(1-\cos(\alpha/2))}\;dr\\  \\
&=g\frac{(b-a)}{2\pi ab(1-\cos(\alpha/2))}
\end{align}$$

Notar que esa era la resistencia equivalente a sólo una porción de resistencia ($1/2$ de la resistencia total) (aquí también cometí un error, ya que dije que era equivalente a $1/4$ de la resistencia cuando en realidad era $1/2$). 

Si se suman las resistencias, se llega al resultado final donde 

$$R_T=g\frac{(b-a)}{4\pi ab(1-\cos(\alpha /2))}$$

### Recapitulando 

Mi desarrollo fue uno hecho de forma distinta a la pauta, pero que se llega al mismo resultado. Se explicó en el reclamo cómo se hubiera llegado al resultado equivalente. 

El planteamiento fue el adecuado, sin embargo, cometí dos errores: 

1. Integré erróneamente (hice el desarrollo de $(1)$ en vez de $(2)$) 

2. Asumí que la resistencia calculada correspondía a $1/4$ de resistencia, cuando en realidad era equivalente a $1/2$. 

A sabiendas que este desarrollo no es de la pauta, creo que se podría descontar menos por cometer estos dos errores que siento que son de baja gravedad. 

También lamento mucho por el desorden en mi desarrollo, entiendo que pudo haber sido poco claro que en realidad la última página de mi desarrollo correspondía a la segunda (y la forma de leer mi desarrollo también era muy dispersa jajaj)

Muchas gracias de antemano 



