
Dado el gran alcance que ha tenido Python en el ámbito científico y de la investigación se han creado diversas librerías que incluyen funciones de Algebra Lineal, Cálculo, Optimización, etc. 

### Método de importación 

Para importar una librería se ocupa la palabra clave *import*  y luego se menciona el nombre de la librería a importar. 

#### Ejemplo 

```Python

import math 

# Método de llamado 

math.funcion(params)

```

Al importarlo de la manera mencionada anteriormente se tendría que llamar el nombre de la libreria y **luego** la función. Esto es extremadamente útil si se tiene un programa con varias variables asignadas, pues podría ser que una función de una libreria tenga el mismo nombre que una variable local y genere problemas de llamado. 

Otro método es importándolo con un alias, que es el más ocupado. Simplemente se sigue la siguiente sintaxis: 

#### Ejemplo 

```Python 

import math as matematica

# Método de llamado 

matematica.funcion(params)

```

La otra forma menos común es importar todas las funciones sin tener que nombrar la librería anteriormente. Esto podría causar el error previamente mencionado: 

#### Ejemplo 

```Python 

from math import * 

factorial(2)

```

Por último, en caso de solo querer importar una función se puede hacer lo siguiente: 

#### Ejemplo 

```Python 

from math import factorial 

factorial(2)

```

## Librerías populares 

Entre las librerías más populares se destacan las siguientes: 

- *NumPy*:  Contiene, principalmente, funciones de Algebra Lineal, transformadas de Fourier, manejo avanzado de números aleatorios, herramientas para integrarse con lenguajes de bajo o medio nivel. 

- *SciPy*: Está construido por encima de *NumPy*  y contiene módulos de alto nivel relacionado a la ciencia e ingeniería. 

- *Scikit Learn*: Está construido por encima de *NumPy*, contiene un conjunto de herramientas eficientes para el aprendizaje de máquinas y el modelo estadístico, lo que incluye clasificación, regresión y *clustering*. 
