/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 7 - Sets y Objetos
| |_____  | |___| |    Ejercicio 2 - objetos.js
|_______| |_______|    

Crea un archivo llamado objetos.js que contenga las siguientes líneas
- Un objeto con tus datos personales (nombre, apellido, edad, altura, eresDesarrollador)
- Una variable que obtenga tu edad a partir del objeto anterior
- Una lista que contenga el objeto con tus datos personales y un nuevo objeto con los datos personales de tus dos mejores amig@s
- Una nueva lista con los objetos de la lista anterior ordenados por edad, de mayor a menor

*/
"use strict"

const persona = {
	nombre: "Pedro",
	apellido: "Coral",
	edad: 30,
	altura: 180,
	eresDesarrollador: true,
}
console.log(persona)

const edad = persona.edad
console.log(edad)

const lista = [
	{ ...persona },
	{
		nombre: "Paula",
		apellido: "Dávila",
		edad: 28,
		altura: 170,
		eresDesarrollador: false,
	},
	{
		nombre: "Enrique",
		apellido: "Bueno",
		edad: 32,
		altura: 170,
		eresDesarrollador: true,
	},
]
console.log(lista)

const listaOrdenada = lista.sort((a, b) => b.edad - a.edad)
console.log(listaOrdenada)
