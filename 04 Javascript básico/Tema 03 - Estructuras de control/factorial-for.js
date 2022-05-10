/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 3 - Estructuras de control
| |_____  | |___| |    Factorial bucle for
|_______| |_______|    

Este archivo debe calcular el factorial de 10 utilizando un solo bucle for

*/
"use strict";

let numero = 10;
let factorial = 1;

for (let i = 1; i <= numero; i++) {
	factorial *= i;
}
console.log(`El factorial de ${numero} es ${factorial}`);
