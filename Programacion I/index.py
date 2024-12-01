"""
#TIPOS DE DATOS
es_primo = True
numero = 32
decimal = 32.85
cadena_texto = "Hola perdida"
char = "H"

#PALABRAS RESERVADAS
print()


# EJERCICIO

anio = int(input("Ingrese el año de su vehículo: "))
peso = float(input("Ingrese el peso de su vehiculo: "))

if (anio <= 1970):
    if peso < 2700:
        clase = 1
        valor = 16.50
    elif peso >= 2700 and peso <= 3800:
        clase = 2
        valor = 25.50
    else:
        clase = 3
        valor = 46.50
elif (anio >= 1971 and anio <= 1979):
    if peso < 2700:
        clase = 1
        valor = 27
    elif peso >= 2700 and peso <= 3800:
        clase = 2
        valor = 30.50
    else:
        clase = 3
        valor = 52.50
else:
    if peso < 3500:
        clase = 7
        valor = 19.50
    else:
        clase = 8
        valor = 52.50

print(f"La clase es: {clase}")
print(f"El valor es: {valor}")

"""


#CALCULADORA

print("Bienvenido a su calculadora")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese una opción: ")

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

match opcion: 
    case "1":
        resultado = a + b
        print(f"El resultado de la suma es: {resultado}")
    case "2":
        resultado = a - b
        print(f"El resultado de la resta es: {resultado}")
    case "3":
        resultado = a * b
        print(f"El resultado de la multiplicación es: {resultado}")
    case "4":
        if b == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = a / b
            print(f"El resultado de la división es: {resultado}")
    case _:
        print("Opción incorrecta.")


