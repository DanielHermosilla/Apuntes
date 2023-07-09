
Consiste en el análisis de la solución partícular del siguiente armónico: 

$$m\ddot{x} + c\dot{x} + kx = F_0\cos(\omega t)$$ 
Esto se puede llegar a traves de [[Fuerzas de restitución|fuerzas de restitución]] donde se tiene una oscilación con una viscocidad $c$ de un fluido a traves de una [[Fuerza roce|fuerza roce]]. Sabemos que la solución particular es: 

$$X_p(t) = A\cos(\omega t - \phi)$$ 
Por lo tanto, para encontrar estas condiciones, se vuelve a derivar $X_p$ para llegar a la solución particular, donde: 

$$\dot{X_p} = -A\omega\sin(\omega t-\phi)$$ $$\ddot{X_p}=-Aw^2\cos(wt - \phi)$$ 
Entonces, reemplazando en la solución particular del armónico: 

$$-Am\omega^2\cos(wt - \phi) -Ac\omega\sin(\omega - \phi) + A\cos(\omega t - \phi) = F_0\cos(\omega t)$$ 
Si se simplifica las amplitudes para poder hacer el análisis trigonométrico: 

$$M\cos(\omega t - \phi) + N(\sin(\omega t - \phi)) = F_0\cos(\omega t)$$ 
Se podría ocupar suma de ángulos para poder dejar otras constantes en función de $\omega t$. 

$$M'\cos(\omega t) + N'\sin(\omega t) = F_0\cos(\omega t)$$

Por lo tanto, para que se cumpla la igualdad, $N'$ **debe ser $0$** y $M'$ **debe ser $F_0$. 

Entonces, volviendo a la ecuación original para encontrar las constantes, al expandir, juntar términos  y ocupando suma de ángulos: 

$$A\left[ (K-m\omega^2)(\cos(\omega t)\cos(\phi)+\sin(\omega t)\sin(\phi))-c\omega(\sin(\omega t)\cos(\phi)-\cos(\omega t)\sin(\phi) \right] = F_0\cos(\omega t)$$ 
Entonces: 

$$\sin(\omega): A\left[(K-m\omega^2)\sin(\phi)-c\omega\cos(\phi)\right] = 0$$ $$\implies \tan(\phi)=\frac{c\omega}{K-m\omega^2}$$ 
Y viendo, el caso de $\cos(\omega t)$: 

$$cos(wt): A\left[ K-m\omega^2\cos(\phi) + c\omega\sin(\phi)\right] = F_0$$ 
Dado que tenemos $\tan(\phi)  = \frac{c\omega}{K-m\omega^2}$ entonces se puede obtener la hipotenusa de un triángulo rectángulo y obtener $\cos(\phi)$ y $\sin(\phi)$ donde cada uno vale $\frac{K-m\omega^2}{\sqrt{(K-m\omega^2)^2 + (c\omega)^2}}$ y $\frac{c\omega}{\sqrt{(K-m\omega^2)^2 + (c\omega)^2}}$ respectivamente. 

Entonces, volviendo a reemplazar: 

$$A\left[\frac{(K-m\omega^2)(k-m\omega^2) + (c\omega)^2}{\sqrt{(K-m\omega^2)^2 + (c\omega)^2}}\right] = F_0$$

Y por lo tanto, como el numerador es el cuadrado de lo de abajo: 

$$A = \frac{F_0}{\sqrt{\left[(K-m\omega^2)^2 + (c\omega)^2\right]}}$$

Si se impone que $c=0$, es decir, no hay roce viscoso.

$$A=\frac{F_0}{m(\frac{K}{m}-\omega^2)}$$ 
Por lo tanto,  *¿Qué pasa si el sistema va a la misma frecuencia que la frecuencia de un resorte?* Sabiendo que $\frac{K}{m} = \omega_{0}^2$, entonces se tiene una indeterminación en $\omega_0 = \omega$ . 


```functionplot
---
title: Resonancia
xLabel: Amplitud
yLabel: Frecuencia angular de respuesta
bounds: [-10,10,0,100]
disableZoom: false
grid: true
---
y =  1500/(x^2-4)

```