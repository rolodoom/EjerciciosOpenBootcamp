# Ejercicio2:
# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá
# los elementos impares de una lista pasada por parámetro con filter y
# realizará una suma de todos estos elementos obtenidos mediante reduce.

# Importar modulos
from functools import reduce

# Funciones secundarias
def mifuncion(lista):
    resultado = list(filter(lambda x: x % 2 != 0, lista))
    resultado = reduce(lambda a, b: a + b, resultado)
    print(resultado)


# Programa Principal
def main():
    numeros = list(range(1, 50))
    mifuncion(numeros)


# Llamando a la función main
if __name__ == "__main__":
    main()
