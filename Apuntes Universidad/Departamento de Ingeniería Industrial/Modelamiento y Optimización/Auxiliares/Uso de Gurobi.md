Para resolver un problema con el solver de Gurobi se ocupará el siguiente ejemplo.

$$\begin{align}
\max \;8x_A+7x_B\\  \\
s.a\;2x_A+3x_B&\leq 18\\  \\
4x_A+3x_B&\leq 24\\  \\
x_A,\;x_B\leq 0\\  \\
x_A,\;x_B\in\mathbb{Z}
\end{align}$$

Primero se importan las librerías, `numpy`y `gurobi`: 

```python 
import gurobipy as gp 
import numpy as np
```
El objeto que va a resolver el problema se llamará Model. 

```python 
modelo1 = gp.Model()
```
Para añadir las **variables**, se ocupa el método `addVar`. Los argumentos más importantes son: 

- `lb`: Límite ínfimo 
- `ub`: Límite superior 
- `vtype`: Tipo de variable (I es entero, C real y B binario) 

```python 
A = modelo1.addVar(lb = 0, vtype = "I", name = "Caja A")
B = modelo1.addVar(lb = 0, vtype = "I", name = "Caja B")
```

Para las **restricciones** se ocupa el método `addConstr`. 

```python 
modelo1.addConstr(2*A+3*B <= 18)
modelo1.addConstr(4*A+3*B <= 24)
```

[La documentación del método se puede ver acá](https://www.gurobi.com/documentation/current/refman/py_model_addconstr.html). 

Como la función objetivo requiere **maximizar**, se ocupa el objeto `GRB.MAXIMIZE`. 

```python 
modelo1.setObjective(8*A+7*B, gp.GRB.MAXIMIZE)
```

Para que empieze a optimizar, simplemente corremos `modelo1.optimize()`. Sin embargo, esto va a dar un output gigantezco. Para poder sacar el output se puede editar los parámetros al imponer `modelo1.Params.LogToConsole = 0` 

```python 
modelo1.optimize()
modelo1.Params.LogToConsole = 0
```

Así, es posible obtener el valor de la función objetivo de la siguiente forma: 

```python 
print("Ganacia:", modelo1.objVal)
>> Ganacia: 52.0
```
Para acceder al valor de las variables, se puede hacer `A.X` o `B.X`. 

En el caso de tener muchas variables y restricciones, es posible ocupar arreglos de `numpy` para no ir añadiendo muchas líneas. 


