
producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio por unidad: "))
cantidad = int(input("Introduce la cantidad: "))

total = precio * cantidad

print(f"Producto: {producto}")
print(f"Precio: {precio:09.2f} €")
print(f"Cantidad: {cantidad:03d}")
print(f"Total: {total:011.2f} €")