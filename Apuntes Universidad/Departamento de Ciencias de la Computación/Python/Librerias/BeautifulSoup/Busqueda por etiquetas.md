---
~
---

Al tener el [[Configuraciones básicas|objeto]] definido, es posible hacer una búsqueda por [[Etiquetas|etiquetas de HTML]]. Esto se logra a través del método ``find``. 

```python 
# Configuraciones iniciales 
from bs4 import BeautifulSoup 
import requests 

url = "www.ejemplo.com"

respuesta = request.get(url)

# Definición del objeto Soup 
soup = BeautifulSoup(respuesta, "html.parser")

# Buscar la etiqueta H5 

tags = soup.find("h5")
```

El método `find` busca por el primer elemento que se encuentra dentro de la página. Para que devuelva todas las etiquetas se ocupa `find_all`. 

## Filtros 

Es posible que al tener un sitio web existan muchas [[Etiquetas|etiquetas]] con distintas clases asociadas a ellas. Es posible filtrar etiquetas con sus clases respectivas al poner la clase como argumento: 

```python 
course_cards = soup.find_all("div", class_="card")
```

Hay que ocupar el `class_`dado que la palabra `class`de por sí es un método nativo de Python. 