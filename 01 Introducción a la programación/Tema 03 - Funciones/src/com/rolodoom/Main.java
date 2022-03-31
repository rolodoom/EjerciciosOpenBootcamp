package com.rolodoom;

public class Main {

    public static void main(String[] args) {

        // Llamar la función de suma
        suma(2, 5, 15);


        // Coche
        Coche miCoche = new Coche();
        miCoche.AgregarPuerta();
        System.out.println(miCoche.puertas);

    }

    // Función que recibe tres parámetros que se suman entre sí.
    public static void suma (int a, int b, int c){
        int resultado = a+b+c;
        System.out.println(resultado);
    }
}


class Coche {
    public int puertas = 4;

    public void AgregarPuerta(){
        this.puertas++;
    }
}




