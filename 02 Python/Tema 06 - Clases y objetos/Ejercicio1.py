class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Vehículo de color {}, {} ruedas y {} puertas.".format(
            self.color, self.ruedas, self.puertas
        )


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindraje):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return "Coche de color {}, {} ruedas, {} puertas, {} km/h y {} cc.".format(
            self.color, self.ruedas, self.puertas, self.velocidad, self.cilindraje
        )


vehiculo = Vehiculo("azul", 4, 5)
print(vehiculo)

coche = Coche("azul", 4, 5, 120, 900)
print(coche)
