/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 7 - Sets y Objetos
| |_____  | |___| |    Ejercicio 1 -  Conjuntos
|_______| |_______|    

Crea un archivo llamado conjuntos.js que contenga las siguientes líneas
- Un nuevo Set con los nombres de tu familia
- Modifica el Set original añadiendo tu nombre (duplicado) (debería darte lo mismo)
- Modifica el Set original añadiendo el nombre "Javascript" (ya que empieza a formar parte de tu vida ;)

*/
"use strict"

/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 7 - Sets y Objetos
| |_____  | |___| |    Ejercicio 2 - conjuntos.js
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
