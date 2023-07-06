Solo es aplicable a circuitos con **[[Corriente alterna|forzamiento sinusoidal]]** y en **estado estacionario**. Se define como: 

$$Z = \frac{V}{I}$$ 
Es decir, la impedancia de una resistencia llegaría a ser: 

$$Z_R = \frac{V_R}{I_R} = R$$ 
Y por ende, la impedancia de un [[Condensador|condensador]] se define como: 

$$Z_C = \frac{1}{i\omega C}$$ 
Y la de una [[Inductancia|inductancia]] llegaría a ser: 

$$Z=\frac{V_L}{I}=i\omega L$$ 
Por lo tanto, en un [[Circuito RC|circuito RC]] podemos ocupar la impedancia para poder operar con [[Corriente alterna|corriente alterna]]: 

![[Captura de Pantalla 2023-01-09 a la(s) 19.25.13.png|center]]

Ocupando la [[Segunda ley de Kirchhoff|segunda Ley de Kirchhoff]], se llega que: 

$$\epsilon_t = V_R + V_C = I(Z_R + Z_C)$$ $$\iff I=\frac{\epsilon_t}{Z_R + Z_C}$$ 
Por lo tanto, el voltaje del [[Condensador|condensador]] llegaría a ser: 

$$V_c=\epsilon_t(\frac{1/i\omega C}{R + 1/\omega C}) = \epsilon_t(\frac{1}{1+i\omega RC})$$ 
Se puede notar que a partir de cierta frecuencia $w$ la [[Diferencia de potencial|diferencia de potencial]] se asimila al del [[Condensador|condensador]], casi como si el resistor no existiera. 

Esta ecuación varía según el orden de conexión de los circuitos: 

![[Captura de Pantalla 2023-01-09 a la(s) 19.31.43.png|center]]

Cuando se tiene la conexión de la izquierda, el comportamiento no funciona para resistencias altas, por lo expresado anteriormente. Análogamente al revez para el circuito al revez. 

Por lo tanto, podemos definir la siguiente función, donde el "1" y "0" nos determina si es filtro alto o bajo: 

$$T(\omega) = |V_{\text{out}}/ V_{\text{in}}|$$

En resumen, un circuito de **filtros bajos** es cuando no detecta un voltaje por el condensador debido a bajas frecuencias. Análogo es para los **filtros altos**.

A partir de $\omega = \frac{1}{RC}$ se considera el *punto medio* entre frecuncias altas o frecuencias bajas. 