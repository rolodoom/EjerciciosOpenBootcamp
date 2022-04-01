package com.rolodoom;

public class Main {

    public static void main(String[] args) {

        // IF
        System.out.println("1. IF");
        int numeroIf = 15;
        if(numeroIf > 0){
            System.out.println("El número es positivo");
        }else if(numeroIf < 0){
            System.out.println("El número es negativo");
        }else{
            System.out.println("El número es cero");
        }

        // WHILE
        System.out.println("2. WHILE");
        int numeroWhile = 0;
        while(numeroWhile<3){
            numeroWhile++;
            System.out.println(numeroWhile);
        }


        // DO WHILE
        System.out.println("3. DO WHILE");
        int numeroDoWhile = 2;
        do{
            numeroDoWhile++;
            System.out.println(numeroDoWhile);
        } while(numeroDoWhile < 3);

        // FOR
        System.out.println("4. FOR");
        for(int numeroFor = 0; numeroFor<= 3; numeroFor++){
            System.out.println(numeroFor);
        }

        // SWITCH
        System.out.println("5. SWITCH");
        String estacion = "VERANO";
        switch(estacion){
            case "INVIERNO":
                System.out.println("La estación es Invierno");
                break;
            case "PRIMAVERA":
                System.out.println("La estación es Primavera");
                break;
            case "VERANO":
                System.out.println("La estación es Verano");
                break;
            case "OTOÑO":
                System.out.println("La estación es Otoño");
                break;
            default:
                System.out.println("El valor de la variable NO es una estación");
        }

    }
}
