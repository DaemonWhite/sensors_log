# sensors_log


Récupère les informations du sense hat et les répertorie dans un csv

## Configuration

le fichier de configuration ce crée à la racince du programe
il respecte le format .ini

### Environement


| parametre			| Def										|
| ------------  	| ----- 									|
| term = true		| Active le mode réglage par terminale		|
| path = path		| Absolute path to output					|
| log_file = true	| Active L'enregistrement des logs 			|
| log_view = false	| Active le retour en temps reeles des logs	|
| event_file = true	| Logs accel only impact move				|
| event_log = false	|

### Time 

| parametre			| Def										|
| ------------  	| ----- 									|
| log_time = 300.0  | Temps de céation d'un nouveau fichier		|
| log_step = 0.5	| Cycle de capture des logs					|
| event_step = 0.1 `| Cycle verfie change logs 					|

### SENSORS
| parametre			| Def										|
| ------------  	| ----- 									|
| humid = true		| 	Enable hmude logs 						|
| presure = true	|	Enable Pressure logs					|
| temp = true		|	Enable sensors logs						|
| orientation = true|	Enable orientations logs				|
| accel = false		|	Enable senosrs logs						|

### VERSION
version = x.x.x

