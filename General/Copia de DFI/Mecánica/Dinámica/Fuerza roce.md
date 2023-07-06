
## Fuerza de roce estático

Fuerza de magnitud variable, donde lo único que se puede caracterizar es su valor máximo. Se forman dado que las moléculas entre cuerpos ejercen enlaces que no son rotos todavía. 

$$\max|\vec{F}_{\text{Roce estático}}| = \mu_e |\vec{N}|$$ 
Si se considera un cuerpo en un plano inclinado sometido a únicamente la fuerza Normal y [[Atracción gravitacional|atracción gravitacional]] se puede llegar que: 

$$mg\sin\alpha = \mu_e mg\cos\alpha$$$$\tan\alpha = \mu_e$$ 
Y llegar a una dependencia en función del ángulo. 

## Fuerza de roce cinético 

Ocurre cuando hay un [[Cinemática|movimiento]] entre dos cuerpos.  Equivale a una igualdad parecida al roce estático pero con un distinto coeficiente de roce, donde $\mu_c\leq\mu_e$: 

$$\vec{F}_{\text{Roce cinético}} = \mu_c |\vec{N}|$$ 
## Fuerza de roce viscoso 

Se define como el roce ante fluidos, es una aproximación pues empíricamente se debe calcular con simulaciones experimentales. 

$$\vec{F}_{\text{Roce viscoso}} = -Kv^n$$ 
Donde $K$ equivale a una constante de proporcionalidad que se obtiene experimentalmente. También $n$ es un número arbitrario que se va modificando a partir de la magnitud de la velocidad. Se podría llegar a omitir y definir como: 

$$\vec{F}_{\text{Roce viscoso}} = -K\vec{v}$$ 
### Ejemplo

Supongamos una lluvia que ocurre a 300 metros sobre el suelo. *¿A qué velocidad caen las gotas?*. 

En un mundo sin roce viscoso, aplicando las leyes de Newton y ecuaciones de movimiento, una gota de agua en una lluvia promedio, caería en el orden de **300km/h**. Pero en realidad, cuando llueve, se pueden observar las gotas cayendo por el orden de los **10m/s**. 

![[IMG_1E7AF8D69B9B-1.jpeg|center]]


## Ecuación de Stokes 

Es la única ecuación teórica para medir el roce viscoso que sirve únicamente para esferas de radio $R$. Se postula lo siguiente: 

$$\vec{F}_{\text{Roce viscoso}} = 6\pi\mu Rv$$
$$ \mu = 1.8\times 10^{-3}$$ 