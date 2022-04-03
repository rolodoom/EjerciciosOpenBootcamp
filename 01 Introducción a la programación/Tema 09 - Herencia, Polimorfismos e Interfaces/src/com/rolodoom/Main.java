package com.rolodoom;

public class Main {

    public static void main(String[] args) {

        Cliente cliente = new Cliente();
        cliente.setEdad(29);
        cliente.setTelefono(4536989);
        cliente.setNombre("Joao Pinto");
        cliente.setCredito(125.25);

        System.out.println(
                "Soy " + cliente.getNombre() +
                        ", tengo " + cliente.getEdad() +
                        " años y me puedes contactar al teléfono " + cliente.getTelefono() +
                        ". Mi crédito es de " + cliente.getCredito() + "€"
        );

        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(35);
        trabajador.setTelefono(5859632);
        trabajador.setNombre("Jorge Galindo");
        trabajador.setSalario(3000.55);

        System.out.println(
                "Soy " + trabajador.getNombre() +
                        ", tengo " + trabajador.getEdad() +
                        " años y me puedes contactar al teléfono " + trabajador.getTelefono() +
                        ". Mi salario es de " + trabajador.getSalario() + "€"
        );

    }
}


class Persona{
    private int edad;
    private String nombre;
    private int telefono;

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }
}

class Cliente extends Persona{
    private double credito;


    public double getCredito() {
        return credito;
    }

    public void setCredito(double credito) {
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    private double salario;

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }
}



















