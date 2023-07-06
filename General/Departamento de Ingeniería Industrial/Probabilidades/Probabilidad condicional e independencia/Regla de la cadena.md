 
Sabemos que la [[Probabilidad Condicional|probabilidad condicional]] nos dice que: 

$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$ 
Entonces, a partir de esto se puede llegar a la siguiente equivalencia: 

$$\iff P(A\cap B)= P(A|B)P(B)$$
$$\iff P(B\cap A)= P(B|A)P(A)$$ 
### Regla de la cadena con 3 [[Conjuntos|conjuntos]]

Sean los tres [[Departamento de Ingeniería Industrial/Probabilidades/Axiomas y propiedades/Evento|eventos]] los siguientes: 

$$P(A\cap B\cap C) = P(A\cap(B\cap C))$$
$$ = P(B\cap C|A)P(A)$$ $$=\frac{P(A\cap B\cap C)}{P(A)}$$ $$=\frac{P(C|A\cap B)P(A\cap B)}{P(A)}$$ $$=P(C|A\cap B)P(B|A)P(A)$$ 
### Regla de la cadena con *n* eventos 

$$P(A_1\cap\dots\cap A_n) = P(A_n|A_{n-1}\cap\dots) = P(A_n|A_{n-1}\cap A_{n-2}\cap\dots)·P(A_{n-1}|A_{n-2}\cap A_{n-3}\cap\dots)\dots$$ 