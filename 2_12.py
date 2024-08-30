numeros = input("Ingresa una lista de numeros separados por espacios: ")

lista_numeros = [float(num) for num in numeros.split()]

lista_numeros.sort()

print("La lista ordenada de menor a mayor es:", lista_numeros)