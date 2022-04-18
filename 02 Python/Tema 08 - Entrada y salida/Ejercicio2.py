# Importar librerías
import pickle

# Clases
class Vehiculo:
    color = ""
    puertas = 0
    motor = 0

    def __init__(self, color, motor, puertas):
        self.color = color
        self.motor = motor
        self.puertas = puertas

    def __str__(self):
        return f"Vehiculo({self.color}, {self.motor} cc, {self.puertas} puertas)"


# Funciones secundarias
def guardarVehiculo(archivo, contenido):
    f = open(archivo, "wb")
    pickle.dump(contenido, f)
    f.close()


def cargarVehiculo(archivo):
    f = open(archivo, "rb")
    obj = pickle.load(f)
    f.close()
    return obj


# Programa Principal
def main():
    coche = Vehiculo("Rojo", 900, 4)
    guardarVehiculo("datos.bin", coche)

    cocheCargado = cargarVehiculo("datos.bin")
    print(cocheCargado)


# Llamando a la función main
if __name__ == "__main__":
    main()
