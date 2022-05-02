/*
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______  
| |       |  ___  |    Curso: Javascript básico
| |       | |   | |    Sesion 3 - Estructuras de control
| |_____  | |___| |    Ejercicio 2
|_______| |_______|    

En este segundo ejercicio, tendréis que crear un bucle 
que haga 10 iteraciones y en cada una indique el número de esta. 
Las iteraciones 2, 3, 5 y 7 deben imprimir en su lugar "Número primo".

*/
"use strict";

bucleprimo: for (let num = 1; num <= 10; num++) {
  if (num <= 1) {
    console.log(num);
    continue bucleprimo;
  }
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      console.log(num);
      continue bucleprimo;
    }
  }
  console.log(`Número primo ${num}`);
}
