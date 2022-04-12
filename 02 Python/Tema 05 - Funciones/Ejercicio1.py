import math

# Función pára calcular el área de un triangulo
# A = (b * h) / 2
def triangulo(b, h):
    return (b * h) / 2


# Función pára calcular el área de un círculo
# A = π * r**2
def circulo(r):
    return math.pi * r**2


# Imprimir Resultados
areaTriangulo = triangulo(3, 4)
print("El área del triángulo es:", round(areaTriangulo, 3))

areaCirculo = circulo(2.5)
print("El área del Círculo es:", round(areaCirculo, 3))
