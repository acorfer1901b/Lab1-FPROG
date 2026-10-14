numero = int(input("Introduce un número entero positivo: "))
if numero > 0:
    suma = numero * (numero + 1) // 2
    print(f"La suma de los enteros de 1 a {numero} es: {suma}")
else:
    print("Por favor, introduce un número entero mayor que 0.")
    