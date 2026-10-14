dinero = float(input("Introduce la cantidad de dinero inicial: "))

interes = 0.04

año1 = dinero * (1 + interes)
año2 = año1 * (1 + interes)
año3 = año2 * (1 + interes)

print(f"Saldo después del primer año: {año1:.2f} €")
print(f"Saldo después del segundo año: {año2:.2f} €")
print(f"Saldo después del tercer año: {año3:.2f} €")