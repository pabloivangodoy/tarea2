import random

n = int(input("Ingresa cuantos numeros quieres: "))

for i in range(n):
    numero_aleatorio = random.randint(1, 100)
    print(numero_aleatorio)