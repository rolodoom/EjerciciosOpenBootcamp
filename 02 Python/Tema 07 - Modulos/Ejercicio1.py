# Importar modulo
import operaciones as op

# Funcion Main
def main():
    # Datos de prueba
    num1, num2 = (10, 5)

    # Imprimir operaciones
    print(f"{num1} + {num2} = {op.sumar(num1,num2)}")
    print(f"{num1} - {num2} = {op.restar(num1,num2)}")
    print(f"{num1} * {num2} = {op.multiplicar(num1,num2)}")
    print(f"{num1} / {num2} = {op.dividir(num1,num2)}")


# Llamado a la funcion Main
if __name__ == "__main__":
    main()
