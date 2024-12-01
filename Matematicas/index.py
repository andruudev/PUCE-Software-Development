# Bienvenida al usuario

print("Bienvenido a la tienda de especialidad")



# Solicitar valores al usuario

cantidad1 = int(input("Ingrese la cantidad del primer artículo: "))

precio1 = float(input("Ingrese el precio unitario del primer artículo: "))

cantidad2 = int(input("Ingrese la cantidad del segundo artículo: "))

precio2 = float(input("Ingrese el precio unitario del segundo artículo: "))

iva = float(input("Ingrese el porcentaje de IVA (ejemplo: 21 para 21%): "))

descuento = float(input("Ingrese el porcentaje de descuento (ejemplo: 10 para 10%): "))



# Calcular el subtotal

subtotal = (cantidad1 * precio1) + (cantidad2 * precio2)



# Calcular el descuento

total_descuento = subtotal * (descuento / 100)

subtotal_con_descuento = subtotal - total_descuento



# Calcular el IVA

total_iva = subtotal_con_descuento * (iva / 100)



# Calcular el precio final

precio_final = subtotal_con_descuento + total_iva



# Imprimir los resultados

print("\nResultados de la compra:")

print(f"Subtotal categoría 1: ${round(cantidad1 * precio1, 2)}")

print(f"Subtotal categoría 2: ${round(cantidad2 * precio2, 2)}")

print(f"Total sin descuento ni IVA: ${round(subtotal, 2)}")

print(f"Descuento aplicado: ${round(total_descuento, 2)}")

print(f"Total con descuento: ${round(subtotal_con_descuento, 2)}")

print(f"IVA aplicado: ${round(total_iva, 2)}")

print(f"\nEl precio total a pagar es: ${round(precio_final, 2)}")