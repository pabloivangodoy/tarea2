numeros = input("Ingresa una lista de números separados por espacios: ")

lista_numeros = [float(num) for num in numeros.split()]

suma_total = 0

for num in lista_numeros:
    suma_total += num

print(f"La suma de todos los números es: {suma_total}")
