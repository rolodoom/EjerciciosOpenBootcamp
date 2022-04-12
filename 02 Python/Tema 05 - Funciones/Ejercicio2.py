# Función que dice si un número (número entero) es primo o no.


def numeroPrimo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                # Se buscan los divisores del numero
                print(
                    "El número {} NO ES PRIMO porque se puede dividir en {}".format(
                        numero, i
                    )
                )
                return False

        # EL número es Primo
        print("El número {} ES PRIMO!".format(numero))
        return True

    else:
        # Los números menore o igual a 1 no son PRIMOS
        print(
            "El número {} NO es primo. Los números primos son enteros mayores a 1".format(
                numero
            )
        )
        return False


# Prueba
# Revisar los números de 1 a 100

for cont in range(1, 100):
    numeroPrimo(cont)
