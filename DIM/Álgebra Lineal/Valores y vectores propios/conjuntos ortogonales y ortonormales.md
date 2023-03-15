
Recordemos que la proyección de un [[vectores|vector]] $u$ sobre $v \neq 0$ está definida por $w = \frac{\langle u,v \rangle}{\langle v,v \rangle} v$. Este vector $w$ sería el que está *más cerca* de $u$ en el espacio de $\langle \lbrace v \rbrace \rangle$.  Se puede verificar facilmente al hacer el [[producto escalar]] y verificar que estamos haciendo una proyección geométrica. 

### Conjunto ortogonal 

Decimos que tenemos un conjunto **ortogonal** cuando el [[producto escalar]] es 0. Es decir, sea un conjunto $\lbrace v_1, \dots, v_n \rbrace$ , entonces tenemos **ortogonalidad** si se cumple que: 

$$\langle v_i, v_j \rangle = 0\enspace\text{para}\enspace i\neq j$$ 
### Conjunto ortonormal 

Vamos a decir que tenemos un conjunto **ortonormal** si tenemos un conjunto **ortogonal** y la [[norma]] del vector en cuestión es igual a la raíz de su [[producto escalar]]: 

$$\langle v_i, v_j \rangle = 0\enspace\text{para}\enspace i\neq j\enspace \land \enspace \|v_i \| = \sqrt{\langle v_i, v_i \rangle} = 1$$

#### Propiedades 

1. Sea $\lbrace v_1, \dots, v_k \rbrace \in \mathbb(R)$ un conjunto ortogonal, entonces $\lbrace v_1, \dots, v_k \rbrace$ es linealmente [[dependencia|dependiente]]. Esto se debe a que la ortogonalidad nos dice si los [[vectores]] son **perpendiculares**. 
 
2. Sea $W$ un [[subespacios vectoriales|subespacio vectorial]] de $R^n$ y $\lbrace{u_1, \dots, u_k}\rbrace$ una base **ortonormal** de $W$. Entonces:
Si $x \in W$, 
$$ x = \sum_{i=1}^{k} \langle x, u_i \rangle u_i \in W $$ Y también, si $x \in R^n$ y definimos 

$$  x = \sum_{i=1}^{k} \langle x, u_i \rangle u_i \in W $$ 
Entonces $(x-z)\perp w, \forall w \in W$ 
