
#### Integrantes 

- Sebastián Jana 
- Daniel Hermosilla 

#### Preguntas

a)  $\pi_{\text{nombre}}(\text{Jugador})$

b) $\pi_{\text{descripción}}(\sigma_{\text{nombre=Nave espacial}}(\text{Mapa}))$

c) $\sigma_{nick= {Lxopato}}(Mensaje)\;\cup\;\sigma_{\text{nick}=\text{ Rauwul}}(Mensaje)$  

d) $\pi_{nick}(\sigma_{\text{color=azul}}(Partida)\cup\sigma_{\text{color=rojo}}(Partida))$

e) $\pi_{\text{nick\_jugador}}(\sigma_{\text{mapa=Nave espacial}}\;((Juego)\Join_{\text{codigo\_juego}=\text{codigo\_partida}\;\land\;\text{fecha\_juego}=\text{fecha\_partida}}(Partida))\Join_{\text{nick\_juego\_partida}=\text{nick\_jugador}}(\text{Jugador}))$ 
f) $\pi_{\text{nick}}(Jugador) - \pi_{\text{nick\_creador}}(\text{Sala})$

g) (($\pi_{\text{nick\_creador}}(\text{Sala})\;\cup\;\pi_{\text{nick}}(Pertenece))\cap(\pi_{\text{nick}}\left(\sigma_{\text{jugador\_steam}=\text{True}} (JugadorPc)\right))$ 

>[!summary] Observación 
>Notar que $\pi_{\text{nick}}(JugadorPc)\supseteq(\pi_{\text{nick\_creador}}(Sala)\cup\pi_{\text{nick}}(\text{Pertenece}))$

h) $\pi_{\text{nick}}(\text{Partida})-(\pi_{\text{nick}}(\pi_{\text{nick}}(\text{Partida})\;\times\;\pi_{\text{color}}(\text{Partida})-\pi_{\text{nick,color}}(\text{Partida}))$

i) screenshot Disc
