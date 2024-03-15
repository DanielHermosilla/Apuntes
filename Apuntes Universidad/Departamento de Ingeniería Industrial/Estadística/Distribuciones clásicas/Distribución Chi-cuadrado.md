
Esta se deriva de una [[Departamento de Ingeniería Industrial/Probabilidades/Variable aleatoria continua/Distribuciones/Distribución Normal|distribución Normal]]. Si $z\sim N(0,1)$, entonces $x=z^2\sim\chi^{2}_{[1]}$ vale decir, distribuye *chi-cuadrado* con $1$ grado de libertad. Se tiene en este caso que $E[z^2]=1$ y $Var[z^2]=2$. 

Si $X_1,\dots, X_n$ son $n$ variable aleatorias independientes y distribuidas chi-cuadrado, entonces $W=\sum^{n}_{i=1}z^{2}_{i}\sim\chi^{2}_{[n]}$ con $E[W]=n$ y $Var[W]=2n$. 

- Los grados de libertad corresponden al número de variable aleatorias normales estándar en la suma 

- Siempre es no-negativa 

- No es simétrica 

Más aún, si $X_1$ y $X_2$ son variable aleatorias independientes y distribuidas chi-cuadrado con $n_1$ y $n_2$ grados de libertad respectivamente, entonces $X_1+X_2\sim \chi^{2}_{[n_1+n_2]}$.  

Para computar los valores se ocupa una tabla *df; prob* donde *df* son los grados de libertad. 

El [[Asimetría (Skewness)|skewness]] de una $\chi^2$ decrece cuando aumenta $n$, tendiendo a una distribución normal. 

![[Captura de pantalla 2024-03-14 a la(s) 12.58.11.png|center]]

