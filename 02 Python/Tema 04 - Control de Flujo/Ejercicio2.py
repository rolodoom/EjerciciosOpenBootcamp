# Recibe los valores inicial para el rango de números
numeroInicial = int(input("Ingresa el número inicial: "))
numeroFinal = int(input("Ingresa el número final: "))

if 0 <= numeroInicial < numeroFinal:
    # El número inicial es menor que el número final
    # y es mayor o igual a cero
    lista = []
    for numero in range(numeroInicial, numeroFinal):
        if numero % 2 != 0:
            # Se ha detecatado número impar
            lista.append(numero)
            continue
    print(lista)
else:
    # El número inicial es igual o menor a cero
    # o es mayor que el núermo final
    print("El número inicial debe ser mayor a cero y menor que el final.")
