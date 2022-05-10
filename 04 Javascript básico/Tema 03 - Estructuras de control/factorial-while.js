/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 3 - Estructuras de control
| |_____  | |___| |    Factorial bucle While
|_______| |_______|    

Este archivo debe calcular el factorial de 10 utilizando un bucle while

*/
"use strict";

let numero = 10;
let factorial = 1;

let i = 1;
while (i <= numero) {
	factorial *= i;
	i++;
}

console.log(`El factorial de ${numero} es ${factorial}`);
