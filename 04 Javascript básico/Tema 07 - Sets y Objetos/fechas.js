/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 7 - Sets y Objetos
| |_____  | |___| |    Ejercicio 3 - fechas.js
|_______| |_______|    

Crea un archivo llamado fechas.js que contenga las siguientes líneas
- La fecha de hoy
- La fecha de tu nacimiento
- Un variable que indique si hoy es más tarde (>) que la fecha de tu nacimiento
- Una variable que contenga el día de tu nacimiento
- Una variable que contenga el mes de tu nacimiento (recuerda que Enero es mes 0)
- Una variable que contenga el año de tu nacimiento (con 4 dígitos)

*/
"use strict"

const fechaHoy = new Date()
console.log(fechaHoy)

const fechaNacimiento = new Date(1984, 05, 17)
console.log(fechaNacimiento)

const comparar = fechaHoy > fechaNacimiento
console.log(comparar)

const diaNacimiento = fechaNacimiento.getDate()
console.log(diaNacimiento)
const mesNacimiento = fechaNacimiento.getMonth() + 1
console.log(mesNacimiento)
const anyoNacimiento = fechaNacimiento.getFullYear()
console.log(anyoNacimiento)
