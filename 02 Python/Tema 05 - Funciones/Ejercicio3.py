# Función que dice si un año (número entero) es bisiesto o no.
# Un año es bisiesto en el calendario Gregoriano,


def annioBiciesto():
    annio = int(input("Introduce un año para saber si es bisiesto: "))

    if (annio % 400 == 0) or (annio % 4 == 0 and annio % 100 > 0):
        print("¡El año {} es bisisesto!".format(annio))
    else:
        print("El año {} NO bisisesto!".format(annio))


annioBiciesto()
