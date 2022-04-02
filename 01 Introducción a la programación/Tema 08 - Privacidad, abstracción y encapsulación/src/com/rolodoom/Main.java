package com.rolodoom;

public class Main {

    public static void main(String[] args) {

        Persona persona = new Persona();
        
        persona.setEdad(25);
        persona.setNombre("Joao Pinto");
        persona.setTelefono(5282415);

        System.out.println("Soy " + persona.getNombre());
        System.out.println("Tengo " + persona.getEdad() + " años de edad");
        System.out.println("Mi número telefónico es " + persona.getTelefono());


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
