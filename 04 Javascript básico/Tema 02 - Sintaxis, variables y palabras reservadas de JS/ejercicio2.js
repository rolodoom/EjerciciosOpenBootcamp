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

En este ejercicio tienes que crear un archivo JavaScript 
donde crees una variable la cual contenga una cadena 
de texto.

Después crearás una función, dentro de ella crearas una 
variable que se llame igual que la primera que has creado 
y le asignaras una cadena de texto diferente a la primera 
y mostrarás la variable por consola.

Por último, fuera de la función tendrás que realizar 
la llamada a la función y mostrarás por consola la 
primera variable que has creado.

*/
"use strict";

let texto = "Primera cadena de texto";

function mifuncion() {
  let texto = "Segunda cadena de texto";
  console.log(texto);
}

mifuncion();
console.log(texto);
