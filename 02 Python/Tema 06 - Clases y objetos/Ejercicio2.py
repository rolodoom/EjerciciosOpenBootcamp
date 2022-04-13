class Alumno:

    # Inicialización del los atributos
    def inicializacion(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: {}, Nota: {}".format(self.nombre, self.nota))

    def resultado(self):
        if self.nota > 5:
            print("{} ha aprobado con {}".format(self.nombre, self.nota))
        else:
            print("{} ha reprobado con {}".format(self.nombre, self.nota))


alumno1 = Alumno()
alumno1.inicializacion("Jorge", 3)
alumno1.imprimir()
alumno1.resultado()

alumno2 = Alumno()
alumno2.inicializacion("Ana", 6)
alumno2.imprimir()
alumno2.resultado()

alumno3 = Alumno()
alumno3.inicializacion("Pedro", 7)
alumno3.imprimir()
alumno3.resultado()
