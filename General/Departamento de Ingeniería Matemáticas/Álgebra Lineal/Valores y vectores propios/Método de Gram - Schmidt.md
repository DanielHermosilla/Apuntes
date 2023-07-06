Consiste en un algoritmo para poder asociar un conjunto de $R^n$ a una [[Base|base]] [[conjuntos ortogonales y ortonormales|ortonormal]].   

### Algoritmo 

Para poder analizar y escribir el algoritmo, primero voy a partir con un ejemplo: 

##### Ejemplo

Sea la siguiente [[Base|base]] $\beta = \langle \lbrace \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \\ 0 \\ 0 \end{pmatrix} \rbrace \rangle$, entonces, vamos a querer buscar la base 

ortonormal a partir del conjunto con el método de Gram - Schmidt. 

1. Vamos a numerar cada [[vectores|vector]] de nuestro [[Espacios vectoriales|espacio vectorial]], por lo tanto, el primero equivaldría a $e_1$, el segundo a $e_2$ y asi sucesivamente. 

2. Calculamos nuestro primer vector del conjunto nuevo, $u_1$: 

$$ u_1 = \frac{e_1}{\| e_1 \|} = \frac{(1,0,0,1)}{\sqrt{1^2 + 0^2 + 0^2 + 1^2}} = \frac{(1,0,0,1)}{\sqrt{2}} = (\frac{1}{\sqrt{2}}, 0, 0,\frac{1}{\sqrt{2}}) $$

3. Antes de calcular $u_2$, calculamos $w_2$ que sería un [[vectores|vector]] ortogonal:

$$ w_2 = e_2 - \langle e_2,u_1 \rangle u_1 $$ Notemos que: 
$$ \langle e_2, u_1 \rangle = \langle (-1,0,1,0), (\frac{1}{\sqrt{2}} , 0, 0, \frac{1}{\sqrt{2}}) \rangle = -\frac{1}{\sqrt{2}}$$ 
Entonces: 

$$ w_2 = (-1,0,1,0) - -\frac{1}{\sqrt{2}} (\frac{1}{\sqrt{2}}, 0, 0,\frac{1}{\sqrt{2}}) = (-1,0,1,0) + (\frac{1}{2},0,0,\frac{1}{2}) = (-\frac{1}{2},0,1,\frac{1}{2})$$ 
4. Ya que tenemos $w_2$, que sería el vector ortogonal, entonces calculamos $u_2$ que sería su versión ortonormal, es decir, con módulo 1: 

$$ u_2 =\frac{w_2}{\|w_2\|} = \frac{(-\frac{1}{2},0,1,\frac{1}{2})}{\sqrt{(-\frac{1}{2})^2 + 0 + 1 + \frac{1}{2}^2}} = \frac{(-\frac{1}{2}, 0, 1, \frac{1}{2})}{\frac{\sqrt{6}}{2}} = (-\frac{\sqrt{6}}{6}, 0, \frac{2\sqrt{6}}{6}, \frac{\sqrt{6}}{6})$$ 
5. Ahora repetimos el proceso, calculando $w_3$ para luego normalizarlo: 

$$ w_3 = e_3 - \langle e_3,u_1 \rangle u_1 - \langle e_3,u_2 \rangle u_2$$
$$ \langle e_3, u_1 \rangle = \langle (2,1,0,0), (\frac{1}{\sqrt{2}}, 0, 0,\frac{1}{\sqrt{2}}) \rangle = \frac{2}{\sqrt{2}} = \sqrt{2}$$
$$ \langle e_3, u_2 \rangle = \langle (2,1,0,0), (-\frac{\sqrt{6}}{6}, 0, \frac{2\sqrt{6}}{6}, \frac{\sqrt{6}}{6}) \rangle = -\frac{\sqrt{6}}{3}$$ Entonces: 

$$ w_3 = e_3 - (1,0,0,1) - (\frac{6}{18}, 0, \frac{12}{18}, \frac{6}{18}) = (2,1,0,0) - (1,0,0,1) - (\frac{1}{3},0,\frac{2}{3},\frac{1}{3}) = (\frac{2}{3},1,\frac{2}{3},-\frac{2}{3})$$

6. Al tener $w_3$ lo normalizamos: 

$$u_3= \frac{w_3}{\|w_3\|} = \frac{(\frac{2}{3},1,\frac{2}{3},-\frac{2}{3})}{\sqrt{(\frac{2}{3})^2 + 1 + (\frac{2}{3})^2 + (-\frac{2}{3})^2}} = \frac{(\frac{2}{3},1,\frac{2}{3},-\frac{2}{3})}{\frac{\sqrt{21}}{3}} = (\frac{2}{\sqrt{21}}, \frac{3}{\sqrt{21}}, \frac{2}{\sqrt{21}}, -\frac{2}{\sqrt{21}})$$ 
7. Por último, reescribimos para obtener la [[Base|base]] [[conjuntos ortogonales y ortonormales|ortonormal]] de $\beta$:

$$ \beta' = \langle\lbrace (\frac{1}{\sqrt{2}}, 0, 0,\frac{1}{\sqrt{2}}), (-\frac{\sqrt{6}}{6}, 0, \frac{2\sqrt{6}}{6}, \frac{\sqrt{6}}{6}), (\frac{2}{\sqrt{21}}, \frac{3}{\sqrt{21}}, \frac{2}{\sqrt{21}}, -\frac{2}{\sqrt{21}}) \rangle\rbrace $$ 

Entonces, a partir del ejemplo anterior podemos empezar a definir el algoritmo de Gram Schmidt. Sea un conjunto $\beta = \langle \lbrace v_1, \dots, v_n \rbrace \rangle$ 

1. Normalizamos el primer [[vectores|vector]] bajo la siguiente fórmula: 

$$ u_1 = \frac{v_1}{\|v_1\|} $$

Esto nos dará nuestro primer vector de la nueva base ortonormal, ahora calculamos el siguiente vector ortogonal para luego normalizarlo. La normalización siempre se hace bajo la fórmula expresada arriba. 

2. Calculamos $w_2$, el siguiente vector nuevo que será ortogonal: 

$$ w_2 = v_2 - \langle v_2,u_1 \rangle u_1 $$

Con el paso 1 se normaliza $w_2$ para obtener $u_2$ 

3. Llegamos a la fórmula general que consiste en una recursión: 

$$ w_n = v_n - \langle v_n,u_1 \rangle u_1 - \langle v_n,u_2 \rangle u_2 - \dots - \langle v_n,u_{n-1} \rangle u_{n-1} $$ 
Y luego se normaliza: 

$$ u_n = \frac{w_n}{\|w_n\|} $$

La demostración de este método se hace por **inducción**. 


#algoritmo