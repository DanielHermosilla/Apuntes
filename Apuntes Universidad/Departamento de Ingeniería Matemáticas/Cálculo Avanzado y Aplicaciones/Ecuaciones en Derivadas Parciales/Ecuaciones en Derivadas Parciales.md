
Una ecuación en derivadas parciales corresponde a una **ecuación diferencial** que involucra más de una variable. Un ejemplo clásico es la ecuación del calor, donde se tiene una función $u=u(t,x)$ y se cumple que: 

$$\frac{\partial u}{\partial t}-c^2\frac{\partial^2u}{\partial x^2}=0$$

Como forma de motivación, consideremos el siguiente problema: 

$$\frac{\partial u}{\partial t}-\frac{\partial^2 u}{\partial x^2}=0\;\;\,\;\;x\in(0,1)\\ 
$$

Como [[Condición inicial|condiciones iniciales]] se tiene que: 

$$\text{Condiciones iniciales}=\begin{cases}\frac{\partial u}{\partial x}(t,0)=0&t>0\\  \\
\frac{\partial}{\partial x}(t,1)=0&t>0\\  \\
u(0,x)=x^2&x\in (0,1)\end{cases}$$

Notemos que se deben tener **la misma cantidad de condiciónes iniciales** que de [[Derivadas parciales|derivadas parciales]]. 
