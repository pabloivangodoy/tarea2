n = int(input("Ingrese un numero: "))
if 1 <= n <= 50:
    a, b = 0, 1
    
    fibonacci = []
    
    for i in range(n):
        fibonacci.append(a)
        a, b = b, a + b
        
    print(f"Los primeros {n} numeros de la secuencia de Fibonacci son: ")
    print(fibonacci)
else:
    print("El valor de n debe estar entre 1 y 50.")