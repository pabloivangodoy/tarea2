numero = int(input("Ingrese un numero: "))

if 1 <= numero <=20:
    factorial = 1
    i = 1
    
    while i <= numero:
        factorial *= i
        i += 1
        
    print(f"El factorial de {numero} es {factorial}.")
else:
    print("El numero debe estar entre 1 y 20.")