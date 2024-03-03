import math

a = int(input("Ingrese cateto a: "))
b = int(input("Ingrese cateto b: "))

hipotenusa = math.sqrt((a**2) + (b**2)) #raiz cuadrada es math.sqrt

print(f"La hipotenusa es {hipotenusa}")