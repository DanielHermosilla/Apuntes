## Pregunta 1 

```SQL 
/* 
No se ocupó SERIAL para los ID's porque se insertaron 
manualmente desde Python
*/ 

--CHARACTER
CREATE TABLE superheroes.characterDS (
    id INT PRIMARY KEY, 
    nombre VARCHAR(250)
)


--SUPERHEROE
CREATE TABLE superheroes.superheroeDS (
    nombre VARCHAR(150),
    intelligence BIGINT,
    strength BIGINT,
    speed BIGINT,
    ch_id INT PRIMARY KEY,
    FOREIGN KEY (ch_id) REFERENCES superheroes.characterDS(id)
)


--RELATION
CREATE TABLE superheroes.relationDS(
    id INT PRIMARY KEY,
    nombre VARCHAR(150)
)


-- RELACION, CHARACTER, SUPERHEROE Y RELATION 
CREATE TABLE superheroes.characterDS_superheroeDS_relationDS( 
	id INT PRIMARY KEY,
	idSeRelaciona INT, 
	idRelacionado INT, 
	idTipoRelacion INT,
	
	FOREIGN KEY(idSeRelaciona) REFERENCES superheroes.characterDS(id),
	FOREIGN KEY(idRelacionado) REFERENCES superheroes.characterDS(id),
	FOREIGN KEY (idTipoRelacion) REFERENCES superheroes.relationDS(id)
	
)


--WORK OCUPATION
CREATE TABLE superheroes.workOcupationDS(
    id BIGINT PRIMARY KEY,
    nombre VARCHAR(150)
)


--RELACION DE SUPERHEROE Y WORK OCUPATION
CREATE TABLE superheroes.superheroeDS_workOcupationDS(
    sup_id SERIAL,
    wo_id SERIAL,
    PRIMARY KEY (sup_id, wo_id),
    FOREIGN KEY (sup_id) REFERENCES superheroes.superheroeDS(ch_id),
    FOREIGN KEY (wo_id) REFERENCES superheroes.workOcupationDS(id)
)


--ALTER EGO
CREATE TABLE superheroes.alterEgoDS(
    id INT PRIMARY KEY,
    nombre VARCHAR(150)
)


--RELACION SUPERHEROE ALTER EGO
CREATE TABLE superheroes.superheroeDS_alterEgoDS(
    sup_id INT,
    ae_id INT,
    PRIMARY KEY (sup_id, ae_id),
    FOREIGN KEY (sup_id) REFERENCES superheroes.superheroeDS(ch_id),
    FOREIGN KEY (ae_id) REFERENCES superheroes.alterEgoDS(id)
);
```

```sql 
CREATE TABLE jugadoresFutbol.appearances (
appearance_id text,
date text,
player_name text,
competition_id text,
game_id integer,
player_id integer,
player_club_id integer,
player_current_club_id integer,
yellow_cards integer,
red_cards integer,
goals integer,
assists integer,
minutes_played integer);
```
```SQL 
CREATE TABLE jugadoresFutbol.club_games (
game_id integer,
club_id integer,
own_goals integer,
own_position integer,
own_manager_name text,
opponent_id integer,
opponent_goals integer,
opponent_position integer,
opponent_manager_name text,
hosting text,
is_win integer
);
```
```SQL 
CREATE TABLE jugadoresFutbol.clubs (
club_id integer,
club_code text,
name text,
domestic_competition_id text,
total_market_value text,
squad_size integer,
average_age numeric,
foreigners_number integer,
foreigners_percentage numeric,
national_team_players integer,
stadium_name text,
stadium_seats integer,
net_transfer_record text,
coach_name text,
last_season integer,
url text
);
```
```SQL 
CREATE TABLE jugadoresFutbol.competitions (
competition_id text,
competition_code text,
name text,
sub_type text,
type text,
country_id integer,
country_name text,
domestic_league_code text,
confederation text,
url text
);
```
```SQL 
CREATE TABLE jugadoresFutbol.game_events (
game_event_id text,
date text,
game_id integer,
minute integer,
type text,
club_id integer,
player_id integer,
description text,
player_in_id integer,
player_assist_id integer
);
```

```SQL 
CREATE TABLE jugadoresFutbol.games ( 
game_id integer,  
competition_id text,  
season integer,  
round text,  
date text,  
home_club_id integer,  
away_club_id integer,  
home_club_goals integer,  
away_club_goals integer,  
home_club_position integer,  
away_club_position integer,  
home_club_manager_name text,  
away_club_manager_name text,  
stadium text,  
attendance integer,  
referee text,  
url text,  
home_club_name text,  
away_club_name text,  
aggregate text,  
competition_type text
```

```SQL 
CREATE TABLE jugadoresFutbol.player_valuations (
player_id integer,  
last_season integer,  
datetime text,  
date text,  
dateweek text,  
market_value_in_eur integer,  
n integer,  
current_club_id integer,  
player_club_domestic_competition_id text
);
```
```SQL 
CREATE TABLE jugadoresFutbol.players (
player_id integer,  
first_name text,  
last_name text,  
name text,  
last_season integer,  
current_club_id integer,  
player_code text,  
country_of_birth text,  
city_of_birth text,  
country_of_citizenship text,  
date_of_birth text,  
sub_position text,  
position text,  
foot text,  
height_in_cm integer,  
market_value_in_eur integer,  
highest_market_value_in_eur integer,  
contract_expiration_date text,  
agent_name text,  
image_url text,  
url text,  
current_club_domestic_competition_id text,  
current_club_name text);
## Pregunta 3 

```SQL 
SELECT nombre FROM superheroes.superheroeDS 
WHERE ch_id IN (
	SELECT idSeRelaciona as conteo FROM superheroes.characterDS_superheroeDS_relationDS
	GROUP BY idSeRelaciona 
	ORDER BY COUNT(idSeRelaciona) DESC 
	LIMIT 3
); 
```

```SQL 
SELECT p.nombre AS nombre_persona
FROM superheroes.characterDS p
LEFT JOIN superheroes.superheroeDS s ON p.nombre = s.nombre
WHERE s.nombre IS NULL
AND p.id IN
    (SELECT idSeRelaciona AS Persona
    FROM superheroes.characterDS_superheroeDS_relationDS
    GROUP BY idSeRelaciona
    ORDER BY COUNT(*) DESC
    LIMIT 3);
```

```SQL 
SELECT s.nombre AS Superheroe
FROM superheroes.characterDS_superheroeDS_relationDS AS r
LEFT JOIN superheroes.superheroeDS AS s ON r.idSeRelaciona = s.ch_id
GROUP BY s.nombre
ORDER BY COUNT(*) DESC
LIMIT 5;
```

```SQL 
SELECT nombre FROM superheroes.relationDS 
WHERE relationDS.id IN (
	SELECT idTipoRelacion FROM superheroes.characterDS_superheroeDS_relationDS 
	GROUP BY idTipoRelacion 
	ORDER BY COUNT(*) DESC 
	LIMIT 1
);
```

```SQL 
SELECT s.nombre FROM superheroes.workOcupationDS AS s
WHERE s.id IN
    (SELECT swo.wo_id FROM superheroes.superheroeDS_workOcupationDS AS swo
    GROUP BY  swo.wo_id
    ORDER BY COUNT(*) DESC
    LIMIT 3);
```




