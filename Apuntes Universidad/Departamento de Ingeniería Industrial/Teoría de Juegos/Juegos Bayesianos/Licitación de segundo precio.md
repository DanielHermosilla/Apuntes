
Se vende un sólo objeto y hay $n$ oferentes con un [[vectores|vector]] de valores no-negativos $v=(v_1,v_2,\dots, v_n)$. 

Es un [[Juegos Bayesianos|juego Bayesiano]] donde el tipo de oferente $i$ es su valor $v_i$ que viene de una distribución sobre algun [[Conjuntos|conjunto]] de números no-negativos. 

Cuando los valores son privados, las distribuciones de valores de los oferentes son independientes. El valor de un jugador no nos dice nada sobre el valor de otros jugadores. 

Aunque sean [[Departamento de Ingeniería Industrial/Probabilidades/Probabilidad conjunta/Probabilidad conjunta continua/Independencia|independientes]], existe una especie de [[Correlación|correlación]] positiva. Si un oferente tiene un valor alto, lo más probable es que otro también lo tenga. 

Poe lo tanto, se tienen varios casos, donde se define la oferta de un jugador como una función de su valor $b_i(v_i)$. El oferente no conoce las ofertas del resto porque es sobre cerrado. 

- Caso 1: Suponemos que la máxima oferta del resto es encima de mi valor, vale decir: 

$$v_i<\max_{j\neq i}\lbrace b_j\rbrace$$

Si el oferente hace una oferta $v_i<b_i=\max_{j\neq i}\lbrace b_j\rbrace$, puede ganar el objeto con probabilidad positiva pero deberá pagar $\max_{j\neq i}\lbrace b_j\rbrace>v_i$ y su pago será negativo.  

Por último, si hace una oferta $v_i<\max_{j\neq i}\lbrace b_j\rbrace<b_i$, gana el objeto y paga $\max_{j\neq i}\lbrace b_j\rbrace>v_i$. Su pago será negativo. 

- Caso 2: $v_i=\max_{j\neq i}\lbrace b_j\rbrace$. 

Si el oferenta hace una oferta $b_i<v_i$ no va a ganar el objeto y su pago será $0$. 

Si hace una oferta $v_i=b_i=\max_{j\neq i}\lbrace b_j\rbrace$ puede ganar el objeto con probabilidad positiva, pero cuando gane deberá pagar $\max_{j\neq i}\lbrace b_j\rbrace=v_i$ y su pago será zero. 


