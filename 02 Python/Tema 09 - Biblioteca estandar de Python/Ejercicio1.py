# Ejercicio1:
# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

# Programa Principal
def main():
    inputdata = input("Ingrese una lista de paises separados por coma:\n")
    paises = list(set(inputdata.split(",")))
    print(",".join(sorted(paises)))


# Llamando a la función main
if __name__ == "__main__":
    main()
