/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 6 - Listas
| |_____  | |___| |    
|_______| |_______|    

Crea un archivo JS que contenga las siguientes líneas
- Una variable que contenga la lista de la compra (mínimo 5 elementos)
- Modifica la lista de la compra y añádele "Aceite de Girasol"
- Vuelve a modificar la lista de la compra eliminando "Aceite de Girasol"
- Una lista de tus 3 películas favoritas (objetos con propiedades: titulo, director, fecha)
- Una nueva lista que contenga las películas posteriores al 1 de enero de 2010 (utilizando filter)
- Una nueva lista que contenga los directores de la lista de películas original (utilizando map)
- Una nueva lista que contenga los títulos de la lista de películas original (utilizando map)
- Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando concat)
- Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando el factor de propagación)

*/
"use strict"

const lista_compra = ["Pasta", "Lechuga", "Tomate", "Aceitunas", "Queso"]
lista_compra.splice(lista_compra.length, 0, "Aceite de Girasol")
lista_compra.pop()

const peliculas_favoritas = [
	{
		titulo: "Aliens",
		director: "James Cameron",
		fecha: new Date(1986, 6, 18),
	},
	{
		titulo: "Predator",
		director: "John McTiernan",
		fecha: new Date(1987, 6, 12),
	},
	{
		titulo: "El Conjuro",
		director: "James Wan",
		fecha: new Date(2013, 6, 19),
	},
]

const peliculas_nuevas = peliculas_favoritas.filter(
	(pelicula) => pelicula.fecha > new Date(2010, 0, 1)
)

const directores = peliculas_favoritas.map((pelicula) => {
	return pelicula.director
})

const titulos = peliculas_favoritas.map((pelicula) => {
	return pelicula.titulo
})

const directores_titulos = directores.concat(titulos)

const directores_titulos_propagacion = [...directores, ...titulos]
