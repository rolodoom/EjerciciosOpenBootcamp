/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 2 - Sintáxis, variables y
| |_____  | |___| |               palabras reservadas JS
|_______| |_______|    Ejercicio 2

Crea un nuevo archivo JS que contenga una lista con los siguientes elementos:

- Tu nombre (string)
- Tu edad (number)
- ¿Eres desarrollador? (boolean)
- Tu fecha de nacimiento (Date)
- Tu libro favorito (Objeto con propiedades: titulo, autor, fecha, url)

*/
"use strict";

const lista = [
	"Rolando",
	43,
	true,
	new Date(1978, 10, 13),
	{
		titulo: "Africanus. El hijo del cónsul",
		autor: "Santiago Posteguillo",
		fecha: new Date(2015, 5, 1),
		url: "https://www.amazon.es/dp/B00699MBS0/",
	},
];

console.log(lista);
