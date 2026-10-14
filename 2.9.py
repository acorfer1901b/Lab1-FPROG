
fecha = input("Introduce una fecha (dd/mm/yyyy): ")

primera_barra = fecha.find("/")
segunda_barra = fecha.find("/", primera_barra + 1)

dia = fecha[:primera_barra]
mes = fecha[primera_barra + 1:segunda_barra]
año = fecha[segunda_barra + 1:]

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")