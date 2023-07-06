
Sean Sea $V$ y $U$ [[espacios vectoriales]] sobre el mismo cuerpo, donde $dimU = p$ y $dimV = q$. Por el otro lado, sea $\beta_U = \lbrace u_1, \dots, u_p \rbrace$ y $\beta_V = \lbrace v_1, \dots, v_q \rbrace$ la [[base]] de $U$ y $V$ respectivamente. Por último, consideremos la [[transformaciones lineales|transformación lineal]] $T:U \rightarrow V$. 

Sabemos que T queda completamente determinada por la [[base]] $\beta_U$, pues es la que nos genera los valores del dominio. Por lo tanto, si definimos los [[vectores]] de nuestra base en la [[transformaciones lineales|transformación lineal]] llegamos a lo siguiente: 
$$ T(u_{j}) = \sum_{i=1}^{q} \alpha_{ij} v_i$$
Donde la sumatoria corresponde a [[vectores]] que pueden ser generados por la base $\beta_V$. Es importante notar los valores de $\alpha_{ij}$, pues las denominaremos las [[coordenadas]]. 

Esto sería equivalente a escribir: 
$$ T(u_1) = \alpha_{11} v_1 + \alpha_{21} v_2 + \dots + \alpha_{q1}v_{q} $$$$ T(u_2) = \alpha_{12} v_1 + \alpha_{22} v_2 + \dots + \alpha_{q2}v_{q} $$$$ \vdots $$$$T(u_p) = \alpha_{1p}v_1 + \alpha_{2p}v_2 + \dots + \alpha_{qp}v_q$$
Las [[coordenadas]] son importante, pues nos ayudan a representar el comportamiento de [[transformaciones lineales]]. Esto se puede modelar mediante una [[matriz]] y la denominaremos **matriz representante**, donde **las columnas vienen dadas por las coordenadas generadas por los [[vectores]] $u_j$** y **las filas por los [[vectores]] $v_q$** . 

$$ M_{\beta_U \beta_V} (T) = \begin{bmatrix}
			\alpha_{11} & \alpha_{12} & \dots & \alpha_{1p} \\ 
			\alpha_{21} & \alpha_{22} & \dots & \alpha_{2p} \\ 
			\vdots & \vdots & \vdots & \vdots \\ 
			\alpha_{q1} & \alpha_{q2}& \dots & \alpha_{qp}
		\end{bmatrix} \in M_{qp}( \kappa )$$
Donde q = $dimU$ y p = $dimV$.

### Conjunto de transformaciones lineales 

A partir de esto, definimos lo que son el conjunto de todas las transformaciones lineales: 
$$ \ell_K (U,V) = \lbrace T:U \rightarrow V \space | \space T \text{ es transformación lineal }\rbrace $$ Podemos notar que va a heredar las propiedades de las [[transformaciones lineales]] y por ende tenemos un [[isomorfismo]] con la **matriz representante** 
$$ \ell_K (U,V) \cong M_{qp} (K) $$ Otra propiedad que podemos extraer es que **la dimensión es el producto de la dimensión de la imagen con el dominio:**
$$dim \space \ell_K (U,V) = dim \space M_{qp} (K) = p*q = dim \space U * dim \space V $$ Y también, a partir de esto también se puede concluir que **la matriz representante de la composición de dos [[transformaciones lineales]] es el producto de matrices representantes**. 

### Teorema 

Para toda [[matriz representante]] cuadrada "$A \in M_{nn}(K)$" se tiene lo siguiente: 

1. $A$  es invertible
2. $T_a : K^n \rightarrow K^n, v \rightarrow T_A (v) = Av \text{ es un isomorfismo}$ 
3. El conjunto $\lbrace A_{\dot j}\rbrace ^{n}_{j=1}$ es base de $K^n$ 