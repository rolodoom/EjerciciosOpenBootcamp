# Programa para calcular el IMC
print("***************************")
print("  Índice de Masa Corporal  ")
print("***************************")
peso = input( "Ingresar peso en kg: " ) # Solicitar peso
estatura = input( "Ingresar estatura en metros: " ) # Solicitar estatura
imc = round( ( float(peso) / float(estatura) ) , 2) ## Calculamos IMC
print( "El IMC es " + str(imc) )
