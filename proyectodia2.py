
nombre = input("¿Cuál es tu nombre? ")
ventas = int(input("¿Cuántas ventas tuviste en el mes? "))

comision_por_venta = 13 
comision_total = ventas * comision_por_venta

print(f"¡Hola {nombre}! Tu comisión total es: ${comision_total} pesos mexicanos")
