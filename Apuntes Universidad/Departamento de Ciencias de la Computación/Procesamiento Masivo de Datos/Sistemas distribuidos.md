
Al tener una cantidad masiva de datos, ya no es posible procesar todo dentro de una sóla máquina. De tal manera, se introducen los **sistemas distribuidos** donde se conectan máquinas independientes. 

![[Pasted image 20240318143614.png|center|400]] 


Existen tres propiedades principales de ésto: 

1. Concurrencia 

2. Fallas independientes 

3. No hay un *"reloj global"*. 

### BitTorrent 

Un ejemplo de sistemas disstribuidos es *"BitTorrent"*, que funciona Peer-to-Peer pero también mediante un servidor. 

Desde un equipo, se manda *"Metadata"* sobre quién posee el archivo. 

![[Pasted image 20240318151941.png|center]]

Cuando existen muchas búsquedas, existe un sistema llamado *"Tracker"*, donde el servidor que posee el archivo deja que un cliente descarge el archivo y el cliente se convierte en host al mandar los archivos. 

## En la vida real 

Por lo general se ocupan máquinas recopiladas en un lugar central, por ejemplo, un servidor LAN local. 

Por el otro lado, está *"Cloud Computing"*, donde se puede contratar servidores de otra región para poder computacional. Es como arrendar poder computacional. 