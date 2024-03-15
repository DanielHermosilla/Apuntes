
Es cuando hay una acción inobservable, como lo es al comprar un seguro de auto, uno empezaría a estacionar en lugares menos seguro. No hay motivación de ser "bueno". 

#### Ejemplo 1: 

Como motivación, asumamos el juego donde un jefe encarga una labor a un agente. 

El agente puede elegir su nivel de esfuerzo $e\in\lbrace 0,1\rbrace$. El esfuerzo es costoso para el agente y suponemos que $c(0)=0$ y $c(1)=y$.

El jefe puede recibir uno de dos posibles ingresos $X=\lbrace \bar{s},s\rbrace$. El ingreso alto es más probable si el agente hace mayor esfuerzo. 

El jefe paga un salario $w$ al agente que puede depender del resultado $x\in\lbrace\bar{s},s\rbrace$. El pago principal es $U_p=x-w$ y el pago del jefe es $U_a=v(w)-c(e)$. 

Suponemos que $v(w)$ es creciente y cóncava, eso significa que el agente es averso al [[Preferencias de Riesgo|riesgo]]. 

Primero, supongamos que el esfuerzo es verificable y el jefe ofrece un contrato $\lbrace\bar{w},w\rbrace$ 

El agente acepta la oferta si y sólo si: 

$$\pi_ev(\bar{w})+(1-\pi_e)v(w)-c(e)\geq 0$$

Donde $\pi_1$ es la probabilidad de obtener la mayor utilidad ante un esfuerzo $e=1$ y $\pi_0$ es la probabilidad de obtener la menor utilidad ante un esfuerzo $e=0$. 

Dada esa restricción, el jefe resuelve: 

$$\max_{(e,\bar{w},w)}\pi_e(\bar{s}-\bar{w})+(1-\pi_e)(s-w)$$

Sujeto a: 

$$\pi_ev(\bar{w})+(1-\pi_e)v(w)-c(e)\geq 0$$

Esto llegaría a ser una [[Multiplicadores de Lagrange|optimización de Lagrange]]. 

Resolviéndolo, sabiendo que $v$ es creciente y cóncava, se llega que el salario debe ser el mismo para el valor alto y bajo, es decir, $\bar{w}=w=w^*$. Esto es **cuando el jefe puede observar el esfuerzo**. 

Si asumimos que el jefe quiere maximizar sus utilidades, asumimos que la restricción es **activa**, vale decir, la desigualdad pasaría de ser $\geq$ a una igualdad. 

Ahora, si suponemos que el jefe **no puede observar el esfuerzo**, existe un caso trivial cuando le paga $0$, el trabajador hará esfuerzo $0$. Ahora, cuando el jefe quiere que el trabajador haga un esfuerzo $1$, se debería asegurar lo siguiente: 

$$\pi_1v(\bar{w})+(1-\pi_1)v(w)-c(1)\geq\pi_0 v(\bar{w})+(1-\pi_0)v(w)-c(0)$$

Esta restricción se llama **restricción de incentivos**. 

Entonces, se busca una maximización: 

$$\max_{(\bar{w},w)}\pi_1(\bar{s}-\bar{w})+(1-\pi_1)(s-w)$$

Sujeto a: 

$$\pi_1v(\bar{w})+(1-\pi_1)v(w)-c(1)\geq 0$$

Y 

$$\pi_1v(\bar{w})+(1-\pi_1)v(w)-c(1)\geq\pi_0v(\bar{w})+(1-\pi_0)v(w)-c(0)$$

Al solucionarlo, se llega que el salario alto y bajo llegarían a ser respectivamente: 

$$\begin{align}
\bar{w^*}&=v^{-1}(y+(1-\pi_1)\frac{y}{\pi_1-\pi_0})\tag{Salario alto}\\  \\
w^*&=v^{-1}(y-\pi_1\frac{y}{\pi_1-\pi_0})
\end{align}$$

Si existe [[Correlación|correlación]] perfecta entre el esfuerzo y resultado, $\pi_1=1$ y $\pi_0=0$. Por lo tanto, se tiene que $\bar{w^*}=v^{-1}(y)$, $w^*=v^{-1}(0)=0$. 

Como $v$ es cóncava, $v^{-1}$ es convexa y por lo tanto

#### Ejemplo 2: 

Nuevamente, se desea contratar un agente y se puede verificar su esfuerzo $e$. 

El esfuerzo $e$ del agente da un ingreso $\Pi(e)$ al gerente, donde $\Pi'>0,\Pi''<0$

El agente puede ser de dos tipos, $1$ con probabilidad $q$ o $2$ con probabilidad $1-q$. El gerente no conoce al. tipo del agente. 

- Los dos tipos tienen diferentes funciones de utilidad. 

La utilidad de los agentes llegarías a ser: 

$$\begin{align}
U_1(w,e)&=v(w)-c(e)\\  \\
U_2(w,e)&=v(w)-kc(e)\;\;\;k>1
\end{align}$$

La **curva de indiferencia** para los agentes llegaría a ser la siguiente: 

![[Pasted image 20231026103352.png|center|550]]

Y para el gerente sería: 

![[Pasted image 20231026103534.png|center|550]]


Sin [[Falta de información|información asímetrica]], ambos agentes van a recibir una utilidad de $0$: 

![[Pasted image 20231026103759.png|center|550]]


Si no existieran problemas de información, es decir, el gerente puede distinguir el tipo de agente, el problema del gerente sería: 

$$\begin{align}
\max\Pi(e)&-w \\\\
v(w)-c(e)&\geq 0
\end{align}$$

Cuando se trata de tipo $1$ y: 

$$\begin{align}
\max\Pi(e)&-w \\\\
v(w)-kc(e)&\geq 0
\end{align}$$

cuando se trata de tipo $2$. 

Las soluciones del problema se representarán con $(w^1,e^1)$ y $(w^2,e^2)$. 

![[Pasted image 20231026104300.png|center|550]]


Se debe asegurar que cada tipo no sólo acepte, pero además elija el contrato diseñado para su tipo. 

$$\begin{align}
\max q[\Pi(e^1)-w^1]+(1-q)&[\Pi(e^2)-w^2]\\  \\
v(w^1)-c(e^1)&\geq 0\tag{1}\\  \\
v(w^2)-k\cdot c(e^2)&\geq 0\tag{2}\\  \\
v(w^1)-c(e^1)&\geq v(w^2)-c(e^2)\tag{3}\\  \\
v(w^2)-l\cdot c(e^2)&\geq v(w^1)-k\cdot c(e^1)\tag{4}
\end{align}$$

Donde $(1)$ y $(2)$ son las restricciones de participación, iguales al caso sin información asimétrica. Por el otro lado $(3)$ y $(4)$ son las restricciones de incentivos. Son particulares al problema con información asimétrica. 

Notar que restricción $(1)$ y $(4)$ es redundante. 