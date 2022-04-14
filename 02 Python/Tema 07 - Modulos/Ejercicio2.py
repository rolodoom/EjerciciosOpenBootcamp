# Improtar modulo Time
from datetime import datetime

# Funcion Main
def main():

    # Se inicializan las variables
    horaSalida = 19
    hora = int(datetime.now().strftime("%H"))
    minutos = int(datetime.now().strftime("%M"))

    # Se compara si la hora actual es mayor a la hora de salida
    # True:     Imprime mensaje
    # False:    Se realiza operación para calcular el timepo que falta
    #           para salir y se impriume en pantalla
    if hora >= horaSalida:
        print("Ya es hora de ir a casa!")
    else:
        print(
            f"Te falta {horaSalida-hora-1} horas y {60-minutos} minutos para irte a casa!"
        )


# Llamado a la funcion Main
if __name__ == "__main__":
    main()
