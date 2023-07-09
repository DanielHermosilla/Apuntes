
Si *A* y *B* son [[Departamento de Ingeniería Industrial/Probabilidades/Axiomas y propiedades/Evento|eventos]] de un mismo [[Espacio muestral|espacio muestral]], entonces la **probabilidad condicional** de *A* dado *B* se define como: 

$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$ 
Donde $P(B) > 0$ 

### [[Axiomas]] 

- **No-negatividad**: Para todo [[Departamento de Ingeniería Industrial/Probabilidades/Axiomas y propiedades/Evento|evento]] $P(A|B)\geq 0$ 
- 
- **Normalización**: $P(B|B) = 1$
- 
- **Aditividad**: Si $A_1, A_2, A_3, \dots$ son disjuntos, entonces $$P(A_1\cup A_2\cup\dots |B) = P(A_1|B) + P(A_2|B) + \dots$$  
### Casos especiales 

- **Eventos disjuntos**: Si dos [[Conjuntos|conjuntos]] son disjuntos, entonces su intersección va a ser vacia, por lo tanto $P(A\cap B)=0\implies P(A|B)$ 

- **Subconjuntos**: Si tenemos que $A\subset B$, entonces: 

$$P(A|B)=\frac{P(A\cap B)}{P(B)} = \frac{P(A)}{P(B)}$$ 
Ahora, si fuera el otro caso, entonces se tendría lo siguiente: 

$$P(B|A) = \frac{P(B\cap A)}{P(A)} = \frac{P(A)}{P(A)} = 1$$ 