
precio = input("Introduce el precio del producto (euros.céntimos): ")

partes = precio.split(".")

euros = partes[0]
centimos = partes[1]

print(f"Euros: {euros}")
print(f"Céntimos: {centimos}")