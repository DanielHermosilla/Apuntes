
La memoización es una técnica utilizada en algoritmos para evitar el recálculo repetitivo de resultados ya conocidos y mejorar la eficiencia de un programa.

### Ejemplo 

Para entenderlo de manera más sencilla, imaginemos que tenemos una función que se llama *fibonacci(n)* que calcula el $n$-ésimo número de la secuencia de Fibonacci. La secuencia de Fibonacci comienza con los números 0 y 1, y cada número posterior es la suma de los dos números anteriores. Por ejemplo, la secuencia empieza así: $0, 1, 1, 2, 3, 5, 8, 13, 21, \ldots$

Si queremos calcular $fibonacci(5)$, la función debe calcularlo de la siguiente manera:
$$fibonacci(5)=fibonacci(4)+fibonacci(3)$$$$fibonacci(4)=fibonacci(3)+fibonacci(2)$$ $$fibonacci(3)=fibonacci(2)+fibonacci(1)$$$$fibonacci(2)=fibonacci(1)+fibonacci(0)$$
En este proceso, vemos que algunos valores, como *fibonacci(3)*, *fibonacci(2)* y *fibonacci(1)*, se están calculando múltiples veces, incluso cuando ya conocemos sus valores.

La memoización resuelve este problema al almacenar los resultados de los cálculos anteriores en una tabla o estructura de datos especial. Entonces, cuando necesitamos calcular $fibonacci(3)$ nuevamente, en lugar de calcularlo desde cero, simplemente consultamos la tabla para obtener el resultado ya calculado. Esto evita el recálculo innecesario y hace que la función sea mucho más eficiente.

En resumen, la memoización es una técnica que guarda los resultados previamente calculados para evitar el recálculo repetitivo, lo que acelera la ejecución de una función o algoritmo. Es como tener una memoria inteligente que nos ayuda a recordar y reutilizar resultados para evitar trabajo extra.

#chatGPT