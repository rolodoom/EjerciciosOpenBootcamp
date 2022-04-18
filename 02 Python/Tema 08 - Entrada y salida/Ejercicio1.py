# Programa Principal
def main():
    escribirArchivo("archivo.txt", "¡Hola a todos! Primera escritura.", "w")
    escribirArchivo("archivo.txt", "Esta es la seguna escritura")
    leerArchivo("archivo.txt")


# Funciones secundarias
def escribirArchivo(archivo, contenido, metodo="a"):
    f = open(archivo, metodo)
    f.write(contenido + "\n")
    f.close()


def leerArchivo(archivo):
    f = open(archivo, "r")
    print(f.read())
    f.close()


# Llamando a la función main
if __name__ == "__main__":
    main()
