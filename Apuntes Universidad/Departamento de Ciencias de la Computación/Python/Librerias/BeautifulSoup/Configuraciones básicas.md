
Antes de trabajar con BeautifulSoup se necesitará también una librería que pueda llamar el archivo HTML. Por lo general se ocupa ``requests`` para poder hacer busquedas por la web. 

Así, la importación de BeautifulSoup se hace mediante la siguiente sintaxis: 

```python 
from bs4 import BeautifulSoup 
```

Obviamente también habría que importar la librería ``requests`` si se está ocupando para llamar a los sitios. 

Por lo general, al tener un sitio dentro de un objeto, se hace define el objeto `soup`: 

```python 
pagina = "www.ejemplo.com"
p = requests.get(pagina) 
soup = BeautifulSoup(p, "html.parser")
```

A partir del objeto `soup` se pueden hacer todas las operaciones que ofrece la librería. 