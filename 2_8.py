numeros = input("Ingresa una lista de números separados por espacios: ")

lista_numeros = [float(num) for num in numeros.split()]

valor_maximo = max(lista_numeros)
print(f"El valor maximo es: {valor_maximo}")

valor_minimo = min(lista_numeros)
print(f"El valor minimo es: {valor_minimo}")
