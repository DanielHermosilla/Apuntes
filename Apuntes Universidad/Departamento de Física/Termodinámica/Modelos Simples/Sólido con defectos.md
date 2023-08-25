
Un [[Estructura cristalinas|sólido cristalino]] dentro de lo que se conoce el contexto de modelos simplificados, es un arreglo regular de [[Átomo|átomos]] ordenados en el espacio. 

![[Captura de pantalla 2023-08-24 a la(s) 21.17.53.png|center]]

Notemos que estos tipos de sólidos, dado fenómenos como la **agitación térmica** son suceptibles a que algunos átomos abandonen su posición dejando vacantes. Igual, no olvidar que de la [[Entropía|entropía]], el valor $\Omega$ seguiría siendo constante. Aun así, **la existencia de vacantes es aquella que determina las propiedades del material**. 

### Configuraciones accesibles al sólido con defectos

La cantidad de configuraciones posibles del sólido con vacantes se puede calcular combinatorialmente, de hecho, es un [[Muestreo no ordenado sin reemplazo|muestreo ordenado sin reemplazo]]. Esto parte de la siguiente suposición: 

1. Hay $N+m$ objetos, donde $N$ son los átomos y $m$ las vacantes. 
2. Los $N$ átomos son iguales entre sí, por lo que hay $N!$ permutaciones equivalentes. 
3. Las $m$ vacantes son iguales. 

Por lo tanto, se llega que $\Omega$ resulta ser: 

$$\Omega=\frac{(N+m)!}{N!m!}=\binom{N+m}{m}$$


Esto, al ignorar que entre las vacantes no hay interacciones ni efecto superficie. 

### Entropía del sólido con defectos 

Dado el $\Omega$, se tendría una entropía gigantesca y dificil de concluir. A partir de esto se ocupa la aproximación de Stirling, que es una aproximación factorial para números grandes: 

$$\ln(N!)=N\ln(N)-N+\dots\;\;\text{si}\;N>>1\tag{Aproximación Stirling}$$

Por lo tanto, la entropía llegaría a ser: 

$$\begin{align}
S&=k_B\ln(\Omega)\\ \\
&=k_B\left[(N+m)\ln(N+m)-\cancel{(N+m)}-N\ln(N)+\cancel{N}-m\ln(m)+\cancel{m}\right]\\  \\
&=k_b\left[(N+m)\ln(N+m)-N\ln N-m\ln(m)\right]
\end{align}$$

El número de vacantes debe ser muchisimo menor que el de átomos, de lo contrario el sólido se desintegraría. Esto permite simplificar ocupando la expansión del logaritmo en seríe de Taylor, entonces: 

$$\ln(N+m)=\ln(N)+\frac{m}{N}+\dots$$

Si se reemplaza en la ecuación de [[Entropía|entropía]] mencionado más arriba, se llega que: 

$$S\approx mk_B\ln(\frac{N}{m})$$

### Otro caso 

El caso del sodio ($NaCl$) es interesante pues está constituido por dos iones. En este caso, las vacantes de los iones de cloro no pueden quedar vacias por la condición de nuetralidad de la materia. Cuando el átomo abandona la vacante deja un electrón en su lugar. 

En tal caso, se llega que $\Omega=\frac{N!}{m!(N-m)!}$. 