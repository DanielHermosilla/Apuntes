
Asi como en la mecánica clásica un sistema se podía describir por la *segunda Ley de Newton*, podemos describir la **evolución de un sistema mecánico cúantico**, conocida como la *ecuación de Schrödinger* que es independiente del tiempo.

```ad-info
color: 200, 200, 200

Notar que demostramos la independencia del tiempo en la parte de [[probabilidad]]

````

Vamos a considerar una partícula que se mueve con una **fuerza conservativa** y que solo tiene un componente en x, por lo tanto, hay presencia de una **energía potencial**. Por lo tanto, la *ecuación de Schrödinger* para una energía $E$ definida seria: 
$$ - \frac{\hbar^{2}}{2m} \frac{d^2 \psi (\vec{x})}{d \vec{x}^2} + U(\vec{x}) \psi (\vec{x}) = E \psi (\vec{x})$$$$ \hbar = \frac{h}{2 \pi} $$ $$ \psi (\vec{x}) \enspace \text{función de onda estacionaria tridimensional} $$$$ U(\vec{x}) \text{ función potencial} $$
$$ \text{E}\psi(x) = \text{Energía} $$ 
### Ecuación de Schrödinger unidimensional 

Si consideramos a $\vec{x}$ como $x$, podemos llegar a la siguiente ecuación: 

$$ - \frac{\hbar^{2}}{2m} \frac{d^2 \psi (x)}{d x^2} + U(x) \psi (x) = E \psi (x) $$

Al hacer tal cambio, estariamos analizando la partícula en **una dimensión.** 
 
### Ecuación de Schrödinger unidimensional: [[partícula libre]] 

Una partícula libre es aquella donde no se somete ninguna fuerza, por lo tanto, eligiremos $U(x) = 0$.

$$ - \frac{\hbar^{2}}{2m} \frac{d^2 \psi (x)}{d x^2} = E \psi (x) $$

Reescribiendo llegamos a lo siguiente: 

$$ \frac{d^2 \psi (x)}{dx^2} + \frac{2mE}{\hbar^2}\psi(x) = 0
$$

La **solución general** también se obtiene al resolver una ecuación diferencial ordinaria, donde se combinan dos funciones linealmente independientes. Por consecuencia, se llega que la solución es: 
$$ \psi(x) = A_{+} e^{ikx} + A_{-} e^{-ikx} $$ $$ A_{-} \enspace \text{y} \enspace A_+ \enspace \text{constantes arbitrarias} $$ $$ k^2 = \frac{2mE}{\hbar ^2} $$
Y por conclusión, llegamos a la función de [[onda]] dada por el [[estado estacionario]]:

$$ \psi(x,t) = A_{+} e^{i(kx - wt)} + A_{-} e^{-i(kx + wt)} $$
$$ w = \frac{E}{\hbar} = \frac{\hbar k^2}{2m} $$ 
Para ver si es realmente una solución de la ecuación de Schrödinger sustituímos $\psi(x,t)$  en la ecuación de Schrödinger para la [[partícula libre]]. 

Sustituyendo cuando $U(x) = 0$ :

$$  - \frac{\hbar^{2}}{2m} \frac{d^2 \psi (x)}{d x^2}  = - \frac{\hbar^{2}}{2m} \frac{d^2 (A_{+} e^{i(kx - wt)} + A_{-} e^{-i(kx + wt)}}{dx^2} $$ $$ - \frac{\hbar^{2}}{2m} [(ik)^2 A_+ e^{ikx} + (-ik)^2 A_{-} e^{-ikx}] $$ $$ - \frac{\hbar^{2} k^2}{2m} [A_+ e^{ikx} + A_{-}e^{ikx}] $$ $$ - \frac{\hbar^{2}k^2}{2m} \psi(x) $$$$ E\psi (x) $$
Llegamos a la solución general de Schrödinger, entonces podemos asegurar que la ecuación de [[partícula libre]] es solución de la ecuación. 

A partir de esto, podemos concluir que la energía es independiente de $\textit{k}$. Si consideramos a $k = \frac{p}{\hbar}$ , entonces: 
$$ E = \frac{p^2}{2m} $$ La función de onda de partícula libre tiene una cantidad de movimiento definida $p$, pero para tal estado **no hay incertidumbre de la [[cantidad de movimiento]]**, es decir $\Delta p = 0$. Por lo tanto, viendo el [[principio de incertidumbre de Heisemberg]]: 

$$ \Delta p \Delta x \geq \frac{\hbar}{2} $$
$$ \implies \Delta x \rightarrow \infty $$

Por lo tanto, **no tenemos idea donde está la partícula**. 

Ahora, si vemos lo que ocurre con la  [[probabilidad]], si la integramos en todo el espacio llegamos que: 

$$ \int^{\infty}_{- \infty} \Psi(x,t) |^2 \space dx = \int^{\infty}_{- \infty} |A|^2 \space dx \rightarrow \infty $$ 
Como no se puede normalizar la función de onda, se define el [[paquete de ondas]]

### Ecuación de Schrödinger unidimensional: partícula en una caja (pozo infinito)

Si nos imaginamos una partícula que está dentro de un pozo infinito: 

![[Pozoinfinito.jpeg]]

Tenemos que: 
1. Si x < 0, $U(x) = \infty$ 

2. $0 \leq x \leq L$,  $U(x) = 0$ 

Debido a que el electrón se está moviendo *libremente*, entonces podemos imponer las **condiciones de borde**: 

Condiciones: 
- $\psi(x=0) = 0$ 
- $\psi(x = L) = 0$ 

$$ \psi(0) = A_{+} + A_{-} = 0 \implies A_{+} = A_{-}$$
Y también, 

$$\psi(x = L) = A_+ e^{ikL} + A_{-}e^{-ikL} = 0 $$ Ocupando la **fórmula de Euler** y simplificando:

$$ \psi(x = L) = (A_{+} + A_{-})\cos(kL) + i(A_{+} - A_{-})\sin(kL) $$

De la condición de borde anterior se llega que 

$$ \psi(x) = 2iA_{+} \sin(kx) $$

Entonces, para que la función $\sin(kx)$ se anule en $x = L$ se debe cumplir que $kL = n\pi$. Y a partir de esto llegamos a la condición que determina la energía E: 

$$ E_n = \frac{\hbar \pi^2}{2mL^2} n^2 $$

Es decir **la energía esta cuantizada, solo hay ciertos valores permitidos**. 

Si redefinimos la constante podemos reescribir: 

$$ \psi (x) = A \sin (\frac{n \pi}{L} x) $$ Y, por lo tanto, para encontrar el valor de la constante A, se normaliza la función de onda  (valor absoluto de $\psi(x) ^2$ ) y se integra: 

Normalización: 

$$ \int^{\infty}_{\infty} |\psi(x)|^2 dx = \int^{\infty}_{\infty} \psi*(x)\psi(x) $$

Y ahora, integrando en los bordes en cuestión

$$ \int^{L}_{0} A^2 \sin^2 (\frac{n \pi}{L}x) \space dx \implies A = \sqrt{\frac{2}{L}} $$

Por conclusión la **ecuación de Schrödinger unidimensional de una partícula en una caja** se define de la siguiente forma: 

$$ \psi_n (x) = \sqrt{\frac{2}{L}} \sin(\frac{n \pi}{L}x) $$ 
Y la energía (que está cuantizada): 
$$ E_n = \frac{ \hbar^2 \pi^2}{2mL^2}n^2 $$ ![[SchrodingerCaja.png|center]]

3.  Si x > L, $U(x) = \infty$ 


#concepto 
