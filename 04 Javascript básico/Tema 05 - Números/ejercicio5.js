/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 5 - Números
| |_____  | |___| |    
|_______| |_______|    

Crea un archivo JS que contenga las siguientes líneas
- Una variable que contenga tu altura en centímetros (entero)
- Una variable que contenga tu altura en metros (número de coma flotante)
- Una variable que contenga tu peso en kilogramos (número de coma flotante)
- Una variable que contenga tu altura en metros redondeada hacia arriba
- Una variable que contenga tu peso en kilogramos redondeado hacia abajo
- Una variable que contenga si "el máximo valor que se puede obtener en Javascript + 1" es igual al máximo valor que se puede obtener en Javascript

*/
"use strict";

let altura_cm = 170;
let altura_m = altura_cm / 100;
let peso_kg = 111.5;
let altura_m_round = Math.ceil(altura_m);
let peso_kg_round = Math.floor(peso_kg);
const igual_max_value = Number.MAX_VALUE + 1 === Number.MAX_VALUE;
