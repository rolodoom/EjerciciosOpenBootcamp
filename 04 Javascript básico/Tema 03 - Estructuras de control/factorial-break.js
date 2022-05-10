/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 3 - Estructuras de control
| |_____  | |___| |    Factorial bucle break
|_______| |_______|    

Este archivo debe calcular el factorial de 10 utilizando
un bucle while, una bifurcación if y una sentencia break

*/
"use strict";

let numero = 10;
let factorial = 1;

let i = 1;
while (true) {
	factorial *= i;
	i++;
	if (i === numero) break;
}

console.log(`El factorial de ${numero} es ${factorial}`);
