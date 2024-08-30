caracter = input("Ingrese el caracter a rastrear: ")
cadena = input("Ingrese la cadena de texto a analizar: ")

contador = 0
for letra in cadena:
    if letra == caracter:
        contador += 1

print(contador)