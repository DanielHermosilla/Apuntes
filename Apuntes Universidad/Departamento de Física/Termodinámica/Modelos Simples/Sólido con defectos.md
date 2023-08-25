
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


