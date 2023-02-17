Python tiene estructuras condicionales que siguen el argumento booleano, su estructura es la siguiente: 

```Python

if expresion_booleana1: 
	accion1 

elif expresion_booleana2: 
	accion2 

elif expresion_booleana3: 
	accion3

else:
	ultimoCaso

```

Lo que dice el siguiente código es: ejecuta la *accion 1* si se cumple la primera proposición, si no es así, ejecuta la segunda y asi sucesivamente. Si no se cumple ninguna se recurre al *else*  donde se ejecuta el ultimo caso. 

Si se quiere considerar un caso particular pero no se quiere hacer nada al respecto se ocupa el indicador *pass*, que basicamente indica acción nula o no hacer nada. 